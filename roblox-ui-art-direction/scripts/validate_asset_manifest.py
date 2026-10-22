#!/usr/bin/env python3
"""Validate a roblox-ui-art-direction asset manifest.

Usage:
    python validate_asset_manifest.py <manifest.json> [--root <project-root>] [--strict]

Checks (errors fail the run; warnings are reported):
  - JSON structure, required fields, unique ids, allowed types/status
  - robloxAssetId: only real-looking numeric ids; required when status == "uploaded";
    flags ids that look fictitious (0, 123456789, repeated digits...)
  - localPath required once an asset exists (generated/approved/prepared/uploaded)
    and, with --root, the file must exist; transparency vs file extension
  - nine-slice rect sanity for frame-9slice assets
  - atlas cell sanity
  - unfilled template placeholders ("<...>")
  - optional (if Pillow is installed): real image size / alpha channel vs manifest

Standard library only (Pillow optional). Exit code 0 = valid, 1 = errors, 2 = usage.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_TYPES = {
    "icon", "frame-9slice", "button", "background", "ornament", "badge",
    "illustration", "spritesheet", "header", "texture", "cursor", "other",
}
ALLOWED_STATUS = [
    "planned", "prompt-ready", "generated", "approved", "prepared", "uploaded",
    "rejected", "pending",
]
EXISTS_STATUS = {"generated", "approved", "prepared", "uploaded"}
REQUIRED = ["id", "purpose", "type", "status", "transparent", "size", "source", "fallback"]
ID_RE = re.compile(r"^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"<[^<>]{1,80}>")
MAX_UPLOAD = 1024


def looks_fictitious(asset_id: str) -> bool:
    if asset_id in {"0", "1"}:
        return True
    if len(set(asset_id)) == 1:  # 11111111
        return True
    seq = "01234567890123456789"
    if len(asset_id) >= 6 and (asset_id in seq or asset_id in seq[::-1]):
        return True
    return len(asset_id) < 5


def normalize_asset_id(value) -> str | None:
    if value is None:
        return None
    s = str(value).strip()
    s = s.removeprefix("rbxassetid://")
    m = re.search(r"[?&]id=(\d+)", s)
    if m:
        s = m.group(1)
    return s


def validate(manifest: dict, root: Path | None, strict: bool):
    errors: list[str] = []
    warnings: list[str] = []

    def walk_placeholders(obj, path="$"):
        if isinstance(obj, str):
            if PLACEHOLDER_RE.search(obj):
                warnings.append(f"{path}: placeholder de template não preenchido: {obj[:60]!r}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                walk_placeholders(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk_placeholders(v, f"{path}[{i}]")

    walk_placeholders({k: v for k, v in manifest.items() if k != "assets"})

    assets = manifest.get("assets")
    if not isinstance(assets, list):
        return ["'assets' deve ser uma lista"], warnings
    if not assets:
        warnings.append("manifest sem assets (ok se a UI for 100% nativa — documente o porquê)")

    seen: set[str] = set()
    for i, a in enumerate(assets):
        where = f"assets[{i}]"
        if not isinstance(a, dict):
            errors.append(f"{where}: deve ser objeto")
            continue
        aid = a.get("id", f"#{i}")
        where = f"{where} ({aid})"
        walk_placeholders(a, where)

        for f in REQUIRED:
            if f not in a:
                errors.append(f"{where}: campo obrigatório ausente: {f}")
        if isinstance(aid, str):
            if not ID_RE.match(aid):
                errors.append(f"{where}: id deve ser minúsculo, ex. 'button.primary.default'")
            if aid in seen:
                errors.append(f"{where}: id duplicado")
            seen.add(aid)

        atype = a.get("type")
        if atype is not None and atype not in ALLOWED_TYPES:
            errors.append(f"{where}: type inválido {atype!r}; use um de {sorted(ALLOWED_TYPES)}")
        status = a.get("status")
        if status is not None and status not in ALLOWED_STATUS:
            errors.append(f"{where}: status inválido {status!r}; use um de {ALLOWED_STATUS}")

        # size
        size = a.get("size") or {}
        w, h = size.get("width"), size.get("height")
        if not (isinstance(w, int) and isinstance(h, int) and w > 0 and h > 0):
            errors.append(f"{where}: size.width/height devem ser inteiros > 0")
            w = h = None
        elif w > MAX_UPLOAD or h > MAX_UPLOAD:
            warnings.append(f"{where}: {w}x{h} excede {MAX_UPLOAD}px; o Roblox reduz uploads maiores")

        # asset id
        rid = normalize_asset_id(a.get("robloxAssetId"))
        if rid is not None:
            if not rid.isdigit():
                errors.append(f"{where}: robloxAssetId deve ser numérico (ou null), recebido {a.get('robloxAssetId')!r}")
            elif looks_fictitious(rid):
                errors.append(f"{where}: robloxAssetId {rid} parece fictício — use null até ter um id real")
            if status != "uploaded":
                warnings.append(f"{where}: tem robloxAssetId mas status={status!r} (esperado 'uploaded')")
        elif status == "uploaded":
            errors.append(f"{where}: status 'uploaded' exige robloxAssetId real")

        # prompt / source
        source = str(a.get("source", ""))
        if status in {"prompt-ready", "generated"} and not a.get("prompt") and not source.startswith("user"):
            errors.append(f"{where}: status {status!r} sem 'prompt'")

        # local file
        lp = a.get("localPath")
        if status in EXISTS_STATUS and not lp:
            errors.append(f"{where}: status {status!r} exige localPath do arquivo real")
        if lp:
            ext = Path(lp).suffix.lower()
            if a.get("transparent") and ext in {".jpg", ".jpeg"}:
                errors.append(f"{where}: transparent=true mas arquivo {ext} não tem alpha (use PNG)")
            if root is not None:
                fp = (root / lp) if not Path(lp).is_absolute() else Path(lp)
                if not fp.exists():
                    errors.append(f"{where}: localPath não existe: {fp}")
                else:
                    _check_image(fp, a, where, errors, warnings)
        elif status in {"planned", "prompt-ready", "pending"} and not a.get("fallback"):
            errors.append(f"{where}: asset inexistente precisa de 'fallback' explícito")

        # nine-slice
        ns = a.get("nineSlice")
        if atype == "frame-9slice" and not ns:
            errors.append(f"{where}: frame-9slice exige nineSlice.sliceCenter")
        if ns:
            sc = ns.get("sliceCenter")
            if not (isinstance(sc, list) and len(sc) == 4 and all(isinstance(v, int) for v in sc)):
                errors.append(f"{where}: nineSlice.sliceCenter deve ser [left, top, right, bottom] inteiros")
            else:
                l, t, r, b = sc
                if not (0 <= l < r and 0 <= t < b):
                    errors.append(f"{where}: sliceCenter inválido (left<right, top<bottom)")
                if w and h and (r > w or b > h):
                    errors.append(f"{where}: sliceCenter fora da imagem {w}x{h}")

        # atlas
        atlas = a.get("atlas")
        if atlas:
            cell, cs = atlas.get("cell"), atlas.get("cellSize")
            if not atlas.get("sheet"):
                errors.append(f"{where}: atlas.sheet deve apontar para o id do spritesheet")
            elif atlas["sheet"] not in {x.get("id") for x in assets if isinstance(x, dict)}:
                errors.append(f"{where}: atlas.sheet {atlas['sheet']!r} não existe no manifest")
            if not (isinstance(cell, list) and len(cell) == 2 and isinstance(cs, int) and cs > 0):
                errors.append(f"{where}: atlas precisa de cell [col,row] e cellSize > 0")

        if a.get("transparent") is not True and atype in {"icon", "badge", "ornament", "frame-9slice"}:
            warnings.append(f"{where}: {atype} normalmente precisa de transparência")

    if strict:
        errors.extend(f"(strict) {w}" for w in warnings)
        warnings = []
    return errors, warnings


def _check_image(fp: Path, a: dict, where: str, errors: list, warnings: list):
    try:
        from PIL import Image  # type: ignore
    except Exception:
        return
    try:
        with Image.open(fp) as im:
            size = a.get("size") or {}
            if (im.width, im.height) != (size.get("width"), size.get("height")):
                warnings.append(f"{where}: arquivo é {im.width}x{im.height}, manifest diz {size.get('width')}x{size.get('height')}")
            if a.get("transparent") and "A" not in im.getbands():
                errors.append(f"{where}: transparent=true mas a imagem não tem canal alpha")
    except Exception as exc:  # pragma: no cover
        warnings.append(f"{where}: não foi possível abrir imagem ({exc})")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("manifest")
    p.add_argument("--root", help="raiz do projeto para resolver localPath")
    p.add_argument("--strict", action="store_true", help="warnings viram erros")
    args = p.parse_args(argv)

    try:
        data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERRO: arquivo não encontrado: {args.manifest}")
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERRO: JSON inválido: {exc}")
        return 1

    errors, warnings = validate(data, Path(args.root) if args.root else None, args.strict)
    for w in warnings:
        print(f"AVISO: {w}")
    for e in errors:
        print(f"ERRO:  {e}")
    n = len(data.get("assets", []) or [])
    if errors:
        print(f"\nInválido: {len(errors)} erro(s), {len(warnings)} aviso(s) em {n} asset(s).")
        return 1
    print(f"\nVálido: {n} asset(s), {len(warnings)} aviso(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
