#!/usr/bin/env python3
"""Validate a roblox-ui-art-direction HUD packet (JSON).

Usage:
    python validate_hud_packet.py <packet.json> [<packet2.json> ...]

Scope (honest): DOCUMENT CONSISTENCY ONLY. It does not evaluate beauty, UX or real
responsiveness — only screen captures from Studio/client can do that.

Checks:
  - required fields / enums (built-in; also JSON Schema if `jsonschema` is installed)
  - unique IDs; references to components, assets and decisions exist
  - layout pattern exists in references/hud-layout-intelligence/patterns
  - valid phase; minimum states present (empty, loading, error, disabled, pending, overflow, full)
  - mobile/gamepad coverage when declared supported
  - gamepad -> initial focus + back route; gameplay HUD -> protected zones
  - high/critical risk -> cancel, recovery, error handling, confirmation, server authority
  - no fictitious AssetIds (same rule as validate_asset_manifest.py)
  - nothing declared as a real capture without an existing file path
  - fictional packets cannot claim captures or a visual approval

Standard library only (jsonschema optional). Exit 0 = valid, 1 = errors, 2 = usage.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # não sujar a pasta da skill com __pycache__
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from validate_asset_manifest import looks_fictitious, normalize_asset_id  # noqa: E402

MIN_STATES = ["empty", "loading", "error", "disabled", "pending", "overflow", "full"]
PHASES = {"A", "B", "C", "D"}
TOUCH_PLATFORMS = {"phone-portrait", "phone-landscape", "tablet"}
ASSET_STATUS = {"planned", "prompt-ready", "generated", "approved", "prepared", "uploaded", "rejected", "pending"}
PROOF_WORDS = re.compile(r"\b(comprovad[oa]|cientificamente|prova que|validado por jogadores)\b", re.I)


def known_patterns() -> set[str]:
    ids: set[str] = set()
    pdir = SKILL_DIR / "references" / "hud-layout-intelligence" / "patterns"
    for f in pdir.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        ids.update(re.findall(r"^\|\s*ID\s*\|\s*`([^`]+)`", text, flags=re.M))
        ids.update(re.findall(r"^### `([^`]+)`", text, flags=re.M))
    return ids


def validate(packet: dict, base: Path) -> list[str]:
    E: list[str] = []

    def req(obj, key, where):
        if not isinstance(obj, dict) or key not in obj:
            E.append(f"{where}: campo obrigatório ausente '{key}'")
            return None
        return obj[key]

    top = ["schemaVersion", "packetId", "status", "game", "screen", "phase", "decisions", "layout",
           "platforms", "inputs", "layers", "components", "states", "assets", "evidence", "manualActions"]
    for k in top:
        req(packet, k, "$")
    if E:
        return E

    status, screen, inputs = packet["status"], packet["screen"], packet["inputs"]
    fictional = bool(req(status, "fictional", "status"))
    verdict = req(status, "visualVerdict", "status")

    if packet["phase"] not in PHASES:
        E.append(f"phase inválida {packet['phase']!r}; use A/B/C/D")

    def unique(items, label):
        seen = set()
        for it in items:
            iid = it.get("id") if isinstance(it, dict) else None
            if not iid:
                E.append(f"{label}: item sem id")
                continue
            if iid in seen:
                E.append(f"{label}: id duplicado {iid!r}")
            seen.add(iid)
        return seen

    comp_ids = unique(packet["components"], "components")
    asset_ids = unique(packet["assets"], "assets")
    dec_ids = unique(packet["decisions"], "decisions")
    state_ids = unique(packet["states"], "states")
    unique(packet["evidence"], "evidence")
    unique(packet["manualActions"], "manualActions")

    # decisions / layout
    layout = packet["layout"]
    if req(layout, "decisionId", "layout") not in dec_ids:
        E.append(f"layout.decisionId {layout.get('decisionId')!r} não existe em decisions")
    pattern = req(layout, "pattern", "layout")
    patterns = known_patterns()
    if pattern and pattern not in patterns:
        E.append(f"layout.pattern {pattern!r} não existe na biblioteca de padrões")
    for r in layout.get("rejected", []):
        if r.get("pattern") not in patterns:
            E.append(f"layout.rejected: padrão {r.get('pattern')!r} não existe na biblioteca")
        if not r.get("reason"):
            E.append("layout.rejected: alternativa sem motivo")
    if len(layout.get("rejected", [])) > 2:
        E.append("layout.rejected: no máximo 3 alternativas no total (escolhida + 2 rejeitadas)")
    for d in packet["decisions"]:
        if d.get("path") and not (base / d["path"]).exists():
            E.append(f"decisions[{d.get('id')}]: path não existe -> {d['path']}")

    # platforms / inputs
    plats = {p.get("id"): p for p in packet["platforms"]}
    supported = {pid for pid, p in plats.items() if p.get("supported")}
    for pid in supported:
        p = plats[pid]
        if not (p.get("composition") or "").strip():
            E.append(f"platforms[{pid}]: suportada sem composition (wireframe/composição)")
        if not (p.get("reflowTrigger") or "").strip():
            E.append(f"platforms[{pid}]: suportada sem reflowTrigger mensurável")
    if supported & TOUCH_PLATFORMS and not inputs.get("touch"):
        E.append("plataforma móvel suportada mas inputs.touch = false")
    if inputs.get("touch") and not supported & TOUCH_PLATFORMS:
        E.append("inputs.touch = true mas nenhuma plataforma phone/tablet suportada com composição")
    if "console-tv" in supported and not inputs.get("gamepad"):
        E.append("console-tv suportado mas inputs.gamepad = false")

    # focus (gamepad)
    if inputs.get("gamepad"):
        focus = packet.get("focus")
        if not focus:
            E.append("gamepad suportado sem focus (foco inicial + rota de retorno)")
        else:
            if focus.get("initial") not in comp_ids:
                E.append(f"focus.initial {focus.get('initial')!r} não é um componente")
            if not (focus.get("back") or "").strip():
                E.append("focus.back vazio (rota B/Esc)")
            for cid in focus.get("route", []):
                if cid not in comp_ids:
                    E.append(f"focus.route: {cid!r} não é um componente")

    # gameplay zones
    if screen.get("gameplay") and not packet.get("protectedZones"):
        E.append("HUD de gameplay sem protectedZones")

    # risk
    if screen.get("risk") in {"high", "critical"}:
        risk = packet.get("risk") or {}
        for k in ("cancel", "recovery", "errorHandling", "confirmation", "serverAuthority"):
            if not (risk.get(k) or "").strip():
                E.append(f"risco {screen.get('risk')}: risk.{k} ausente")

    # states
    for s in MIN_STATES:
        if s not in state_ids:
            E.append(f"states: estado mínimo ausente '{s}'")
    for s in packet["states"]:
        sid = s.get("id")
        if not s.get("applicable", True):
            if not (s.get("reason") or "").strip():
                E.append(f"states[{sid}]: não aplicável sem reason")
            continue
        if sid == "error" and not (s.get("recovery") or "").strip():
            E.append("states[error]: sem recovery")
        cap = s.get("capture")
        if cap:
            if fictional:
                E.append(f"states[{sid}]: pacote fictício não pode declarar captura")
            elif not (base / cap.get("path", "")).is_file():
                E.append(f"states[{sid}]: captura declarada sem arquivo real -> {cap.get('path')}")

    # components
    for c in packet["components"]:
        for a in c.get("assets", []):
            if a not in asset_ids:
                E.append(f"components[{c.get('id')}]: asset {a!r} não existe em assets")
        if c.get("contract") and not (base / c["contract"]).exists():
            E.append(f"components[{c.get('id')}]: contract não existe -> {c['contract']}")
        if c.get("type") == "Custom" and len((c.get("role") or "").split()) < 3:
            E.append(f"components[{c.get('id')}]: componente Custom precisa de função visual clara em 'role'")

    # assets
    for a in packet["assets"]:
        aid = a.get("id")
        if a.get("status") not in ASSET_STATUS:
            E.append(f"assets[{aid}]: status inválido {a.get('status')!r}")
        rid = normalize_asset_id(a.get("robloxAssetId"))
        if rid is not None:
            if not rid.isdigit():
                E.append(f"assets[{aid}]: robloxAssetId não numérico")
            elif looks_fictitious(rid):
                E.append(f"assets[{aid}]: robloxAssetId {rid} parece fictício")
            if fictional:
                E.append(f"assets[{aid}]: pacote fictício não pode ter robloxAssetId")
        elif a.get("status") == "uploaded":
            E.append(f"assets[{aid}]: status uploaded sem robloxAssetId real")
        if a.get("localPath") and not (base / a["localPath"]).exists():
            E.append(f"assets[{aid}]: localPath não existe -> {a['localPath']}")

    # evidence
    captures = 0
    for ev in packet["evidence"]:
        eid = ev.get("id")
        if ev.get("kind") == "qa-capture":
            captures += 1
            if fictional:
                E.append(f"evidence[{eid}]: pacote fictício não pode ter qa-capture")
            elif not ev.get("path") or not (base / ev["path"]).is_file():
                E.append(f"evidence[{eid}]: qa-capture sem arquivo real -> {ev.get('path')}")
        if ev.get("kind") == "observed" and ev.get("confidence") in {"baixa", "nenhuma"} and PROOF_WORDS.search(ev.get("claim", "")):
            E.append(f"evidence[{eid}]: benchmark de baixa confiança apresentado como prova")
        if PROOF_WORDS.search(ev.get("claim", "")) and ev.get("kind") in {"observed", "heuristic", "hypothesis"}:
            E.append(f"evidence[{eid}]: afirmação de prova em evidência {ev.get('kind')}")

    # verdict
    if fictional and verdict != "pendente — sem captura":
        E.append("pacote fictício deve ter visualVerdict 'pendente — sem captura'")
    if verdict in {"aprovado", "aprovado com ressalvas"} and captures == 0:
        E.append(f"visualVerdict {verdict!r} sem nenhuma evidência qa-capture")

    # manual queue
    needs_queue = (verdict == "pendente — sem captura"
                   or any(a.get("status") != "uploaded" for a in packet["assets"])
                   or any(d.get("status") == "pendente" for d in packet["decisions"]))
    if needs_queue and not packet["manualActions"]:
        E.append("há pendências (captura/asset/decisão) mas manualActions está vazio")

    return E


def schema_errors(packet: dict) -> list[str]:
    try:
        import jsonschema  # type: ignore
    except Exception:
        return []
    schema = json.loads((SKILL_DIR / "schemas" / "hud-spec.schema.json").read_text(encoding="utf-8"))
    v = jsonschema.Draft202012Validator(schema)
    return [f"schema: {'/'.join(map(str, e.path)) or '$'}: {e.message}" for e in v.iter_errors(packet)]


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass
    if len(argv) < 2:
        print(__doc__)
        return 2
    total = 0
    for arg in argv[1:]:
        path = Path(arg)
        try:
            packet = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"ERRO: arquivo não encontrado: {path}")
            total += 1
            continue
        except json.JSONDecodeError as exc:
            print(f"ERRO: {path}: JSON inválido: {exc}")
            total += 1
            continue
        errs = schema_errors(packet) + validate(packet, path.resolve().parent)
        for e in errs:
            print(f"ERRO:  {path}: {e}")
        print(f"{path}: {'inválido' if errs else 'válido'} ({len(errs)} erro(s))")
        total += len(errs)
    print("Escopo: consistência documental. Não avalia beleza, UX nem responsividade real.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
