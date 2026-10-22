#!/usr/bin/env python3
"""Structural validator for the roblox-ui-art-direction skill documentation.

Usage:
    python validate_skill_docs.py [<skill-root>]      (default: parent of this script)

Checks (STRUCTURE ONLY — this does NOT evaluate visual quality, UX or responsiveness):
  1. Relative Markdown links and backticked skill paths resolve to real files.
  2. Every full pattern file in references/hud-layout-intelligence/patterns/ has the
     required sections and an ID row; compact catalog entries have all required labels.
  3. Pattern IDs are unique and the 10 mandatory IDs exist.
  4. Benchmark register rows have URL, date, evidence type, confidence and status.
  5. Benchmark/source IDs cited in patterns and examples exist in the register.
  6. Layout templates contain their mandatory fields.
  7. HUD Layout Intelligence case studies contain alternatives, decision, per-platform
     plan, states and QA checklist.
  8. (v1.2.0) delivery contract, component system, recipes, new templates, schema,
     golden HUD packets (all artefacts + JSON passing validate_hud_packet.py),
     evaluations (6 prompts + 6 rubrics), no capture claims in examples, and
     low-confidence benchmarks never presented as proof.

Standard library only. Exit 0 = ok, 1 = structural errors.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # não sujar a pasta da skill com __pycache__
HLI = Path("references/hud-layout-intelligence")
PATTERN_SECTIONS = [
    "## Metadados", "## Quando usar", "## Quando evitar", "## Alternativas reais",
    "## Vantagens e desvantagens", "## Wireframes", "### Desktop", "### Mobile",
    "### Gamepad", "## Reflow responsivo", "## Input e foco", "## Estados",
    "## Image vs Native vs Hybrid", "## Anti-padrões", "## Checklist de QA",
    "## Benchmarks e confiança",
]
META_FIELDS = [
    "ID", "Família", "Arquétipo", "Problema resolvido", "Tarefa principal", "Contexto",
    "Frequência", "Urgência", "Risco de erro", "Itens e crescimento", "Densidade de informação",
]
STATE_NAMES = ["empty", "loading", "error", "disabled", "overflow", "full"]
CATALOG_LABELS = ["**Fam:**", "**Prob:**", "**Ctx:**", "**Usar:**", "**Evitar:**", "**Alt:**",
                  "**±:**", "**D:**", "**M:**", "**G:**", "**Reflow:**", "**Input:**",
                  "**Estados:**", "**Img:**", "**Anti:**", "**QA:**", "**Bench:**"]
REQUIRED_IDS = {
    "collection.grid-detail", "collection.hotbar", "commerce.catalog-detail",
    "loadout.slot-catalog", "trade.bilateral-confirm", "reward.track-reveal",
    "match.overlay", "settings.hierarchy", "quest.tracker-expand", "survival.contextual",
}
EVIDENCE = {"official", "observed", "heuristic", "hypothesis", "—"}
CONFIDENCE_RE = re.compile(r"^(alta|média|baixa|nenhuma)")
STATUS = {"verified_text", "fetch_failed", "not_inspected", "unverified_visual_reference"}
MEMORY_FIELDS = [
    "ID", "Data", "Versão da skill", "Jogo e estilo", "Família do HUD", "Tarefa",
    "Dispositivo/input", "Padrão escolhido", "Alternativas rejeitadas", "Justificativa",
    "Screenshots autorizados ou URLs", "Resultados de QA", "Problemas", "Soluções",
    "Nível de confiança", "Decisão humana", "Licença/origem do material visual",
]
CASE_SECTIONS = ["## Alternativas", "## Decisão", "## Plano por plataforma", "## Estados",
                 "## Checklist de QA"]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TICK_RE = re.compile(r"`((?:references|templates|examples|scripts|schemas|evaluations)/[^`\s]+)`")
REF_ID_RE = re.compile(r"\b((?:BM|OF|AC)-\d{2})\b")


V12_FILES = [
    "references/hud-delivery-contract.md", "references/component-system.md",
    "templates/hud-screen-spec.md", "templates/component-contract.md", "templates/state-matrix.md",
    "templates/evidence-board.md", "templates/implementation-handoff.md",
    "templates/hud-packet.example.json", "schemas/hud-spec.schema.json",
    "scripts/validate_hud_packet.py", "evaluations/README.md", "evaluations/expected-signals.md",
    "evaluations/results/README.md",
]
RECIPES = ["new-hud", "redesign-existing-ui", "implement-approved-design", "review-existing-hud",
           "asset-production-only"]
RECIPE_SECTIONS = ["## Ler", "## Criar/atualizar", "## Ordem", "## Entregáveis", "## Parar quando",
                   "## Perguntar ao usuário quando", "## Seguir com hipóteses quando"]
GOLDEN_SECTIONS = ["## Brief resumido", "## Theme profile resumido", "## Layout decision",
                   "## Screen spec", "## Component inventory", "## State matrix",
                   "## Implementation handoff", "## Asset matrix", "## Packet JSON",
                   "## Plano de capturas", "## Decisões rejeitadas", "## Pendências reais"]
COMPONENTS = ["Panel", "Button", "IconButton", "Tab", "ItemCard", "CurrencyPill", "ProgressBar",
              "Modal", "Sheet", "Tooltip", "Toast", "FocusRing", "EmptyState", "LoadingSkeleton",
              "ErrorState", "ConfirmationFooter"]
EVAL_PROMPT_SECTIONS = ["## Prompt de teste", "## Entradas disponíveis", "## Entregáveis esperados"]
EVAL_RUBRIC_SECTIONS = ["## Erros críticos", "## Rubrica (0–2 por critério)",
                        "## Sinais de resposta genérica ou alucinação", "## Aprovar / reprovar"]
CAPTURE_CLAIM_RE = re.compile(r"(captura real (anexada|feita)|testado no studio|aprovad[oa] visualmente|screenshot anexad)", re.I)
PROOF_RE = re.compile(r"(comprovad[oa]|cientificamente|prova que|prova de eficácia)", re.I)


def check_v12(root: Path) -> list[str]:
    E: list[str] = []
    for f in V12_FILES:
        if not (root / f).exists():
            E.append(f"arquivo v1.2.0 ausente: {f}")
    for r in RECIPES:
        rp = root / "references" / "task-recipes" / f"{r}.md"
        if not rp.exists():
            E.append(f"recipe ausente: {rp.relative_to(root)}")
            continue
        t = rp.read_text(encoding="utf-8")
        for sec in RECIPE_SECTIONS:
            if sec not in t:
                E.append(f"{rp.relative_to(root)}: seção ausente '{sec}'")
    cs = root / "references" / "component-system.md"
    if cs.exists():
        t = cs.read_text(encoding="utf-8")
        for c in COMPONENTS:
            if f"| **{c}** |" not in t:
                E.append(f"component-system.md: componente ausente {c}")

    # golden packets
    sys.path.insert(0, str(root / "scripts"))
    try:
        import validate_hud_packet as vhp  # type: ignore
    except Exception as exc:  # pragma: no cover
        return E + [f"não foi possível importar validate_hud_packet: {exc}"]
    gdir = root / "examples" / "golden-hud-packets"
    golden = sorted(d for d in gdir.iterdir() if d.is_dir()) if gdir.exists() else []
    if len(golden) < 4:
        E.append(f"esperados ≥ 4 golden HUD packets, encontrados {len(golden)}")
    import json as _json
    styles = set()
    for d in golden:
        md, js = d / "packet.md", d / "packet.json"
        rel = d.relative_to(root)
        if not md.exists() or not js.exists():
            E.append(f"{rel}: precisa de packet.md e packet.json")
            continue
        t = md.read_text(encoding="utf-8")
        for sec in GOLDEN_SECTIONS:
            if sec not in t:
                E.append(f"{rel}/packet.md: seção ausente '{sec}'")
        if "FICTÍCIO" not in t or "pendente — sem captura" not in t:
            E.append(f"{rel}/packet.md: deve declarar FICTÍCIO e 'pendente — sem captura'")
        try:
            packet = _json.loads(js.read_text(encoding="utf-8"))
        except Exception as exc:
            E.append(f"{rel}/packet.json: JSON inválido ({exc})")
            continue
        for e in vhp.validate(packet, js.parent) + vhp.schema_errors(packet):
            E.append(f"{rel}/packet.json: {e}")
        if not packet.get("status", {}).get("fictional"):
            E.append(f"{rel}/packet.json: golden packet deve ser fictional=true")
        styles.add((packet.get("game", {}).get("visualStyle"), packet.get("layout", {}).get("pattern")))
    if golden and len(styles) < len(golden):
        E.append("golden packets repetem a mesma combinação estilo/padrão")
    ex = root / "templates" / "hud-packet.example.json"
    if ex.exists():
        for e in vhp.validate(_json.loads(ex.read_text(encoding="utf-8")), ex.parent):
            E.append(f"templates/hud-packet.example.json: {e}")

    # no capture claims in examples
    for md in (root / "examples").rglob("*.md"):
        for ln, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if CAPTURE_CLAIM_RE.search(line) and not re.search(r"\b(não|nunca|sem|nenhum)\b", line, re.I):
                E.append(f"{md.relative_to(root)}:{ln}: alega captura/aprovação visual")

    # low-confidence benchmarks never as proof
    reg = root / HLI / "benchmark-register.md"
    low: set[str] = set()
    if reg.exists():
        for line in reg.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*(BM-\d{2})\s*\|", line)
            if m:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) == 11 and re.match(r"^(baixa|nenhuma)", cells[6]):
                    low.add(m.group(1))
    for md in root.rglob("*.md"):
        if md == reg:
            continue
        for ln, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            cited = set(re.findall(r"\bBM-\d{2}\b", line)) & low
            if cited and PROOF_RE.search(line) and not re.search(r"\b(não|nunca|proibido)\b", line, re.I):
                E.append(f"{md.relative_to(root)}:{ln}: benchmark de baixa confiança {sorted(cited)} apresentado como prova")

    # evaluations
    ev = root / "evaluations"
    prompts = sorted((ev / "prompts").glob("*.md")) if (ev / "prompts").exists() else []
    rubrics = sorted((ev / "rubrics").glob("*.md")) if (ev / "rubrics").exists() else []
    if len(prompts) < 6 or len(rubrics) < 6:
        E.append(f"avaliações: esperados ≥ 6 prompts e 6 rubricas ({len(prompts)}/{len(rubrics)})")
    for p in prompts:
        t = p.read_text(encoding="utf-8")
        for sec in EVAL_PROMPT_SECTIONS:
            if sec not in t:
                E.append(f"{p.relative_to(root)}: seção ausente '{sec}'")
        if not (ev / "rubrics" / p.name).exists():
            E.append(f"{p.relative_to(root)}: sem rubrica correspondente")
    for r in rubrics:
        t = r.read_text(encoding="utf-8")
        for sec in EVAL_RUBRIC_SECTIONS:
            if sec not in t:
                E.append(f"{r.relative_to(root)}: seção ausente '{sec}'")
        if len(re.findall(r"^\|\s*[1-9]\s*\|", t, flags=re.M)) < 9:
            E.append(f"{r.relative_to(root)}: rubrica precisa dos 9 critérios")
    res = ev / "results" / "README.md"
    if res.exists():
        for ln, line in enumerate(res.read_text(encoding="utf-8").splitlines(), 1):
            if re.search(r"\|\s*\**(aprovado|reprovado)\**\s*\|\s*$", line):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[0]) or cells[1] in {"", "—"}:
                    E.append(f"evaluations/results/README.md:{ln}: resultado sem data/modelo reais")
    return E


def main(argv: list[str]) -> int:
    try:  # Windows consoles/pipes may not be UTF-8
        sys.stdout.reconfigure(errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errors: list[str] = []
    checked_links = 0

    md_files = sorted(p for p in root.rglob("*.md"))
    # 1. links
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        in_fence = False
        for ln, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK_RE.findall(line):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                checked_links += 1
                path = (md.parent / target.split("#")[0]).resolve()
                if not path.exists():
                    errors.append(f"{md.relative_to(root)}:{ln}: link quebrado -> {target}")
            for target in TICK_RE.findall(line):
                if any(c in target for c in "<*{"):
                    continue
                if target.endswith("/"):
                    if not (root / target).is_dir():
                        errors.append(f"{md.relative_to(root)}:{ln}: pasta inexistente -> {target}")
                    continue
                checked_links += 1
                if not (root / target).exists():
                    errors.append(f"{md.relative_to(root)}:{ln}: caminho inexistente -> {target}")

    # 4. register
    reg_path = root / HLI / "benchmark-register.md"
    known_refs: set[str] = set()
    if not reg_path.exists():
        errors.append("benchmark-register.md ausente")
    else:
        for ln, line in enumerate(reg_path.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"^\|\s*((?:BM|OF|AC)-\d{2})\s*\|", line)
            if not m:
                continue
            rid = m.group(1)
            if rid in known_refs:
                errors.append(f"benchmark-register:{ln}: ID duplicado {rid}")
            known_refs.add(rid)
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not any(c.startswith("http") for c in cells):
                errors.append(f"benchmark-register:{ln}: {rid} sem URL")
            if not any(c in STATUS for c in cells):
                errors.append(f"benchmark-register:{ln}: {rid} sem status válido {sorted(STATUS)}")
            if rid.startswith("BM"):
                if len(cells) != 11:
                    errors.append(f"benchmark-register:{ln}: {rid} deve ter 11 colunas (tem {len(cells)})")
                    continue
                _, _, _, _, date, etype, conf, *_ = cells
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                    errors.append(f"benchmark-register:{ln}: {rid} data inválida {date!r}")
                if etype not in EVIDENCE:
                    errors.append(f"benchmark-register:{ln}: {rid} tipo de evidência inválido {etype!r}")
                if not CONFIDENCE_RE.match(conf):
                    errors.append(f"benchmark-register:{ln}: {rid} confiança inválida {conf!r}")

    # 2/3. patterns
    ids: dict[str, str] = {}
    pdir = root / HLI / "patterns"
    for pf in sorted(pdir.glob("*.md")):
        text = pf.read_text(encoding="utf-8")
        rel = pf.relative_to(root)
        if pf.name == "pattern-catalog.md":
            entries = re.split(r"^### `([^`]+)`\s*$", text, flags=re.M)
            for i in range(1, len(entries), 2):
                pid, body = entries[i], entries[i + 1]
                for label in CATALOG_LABELS:
                    if label not in body:
                        errors.append(f"{rel}: entrada {pid} sem campo {label}")
                for st in STATE_NAMES:
                    if st not in body:
                        errors.append(f"{rel}: entrada {pid} não menciona estado '{st}'")
                if pid in ids:
                    errors.append(f"{rel}: ID duplicado {pid} (também em {ids[pid]})")
                ids[pid] = str(rel)
            continue
        for sec in PATTERN_SECTIONS:
            if not re.search(rf"^{re.escape(sec)}\s*$", text, flags=re.M):
                errors.append(f"{rel}: seção ausente '{sec}'")
        for field in META_FIELDS:
            if not re.search(rf"^\|\s*{re.escape(field)}\s*\|", text, flags=re.M):
                errors.append(f"{rel}: campo de metadados ausente '{field}'")
        for st in STATE_NAMES:
            if not re.search(rf"^\|\s*{st}\b", text, flags=re.M):
                errors.append(f"{rel}: estado ausente na tabela '{st}'")
        m = re.search(r"^\|\s*ID\s*\|\s*`([^`]+)`", text, flags=re.M)
        if not m:
            errors.append(f"{rel}: linha de ID inválida")
            continue
        pid = m.group(1)
        if f"`{pid}`" not in text.splitlines()[0]:
            errors.append(f"{rel}: título não corresponde ao ID {pid}")
        if pid in ids:
            errors.append(f"{rel}: ID duplicado {pid} (também em {ids[pid]})")
        ids[pid] = str(rel)
    missing = REQUIRED_IDS - ids.keys()
    if missing:
        errors.append(f"padrões obrigatórios ausentes: {sorted(missing)}")

    # 5. cited refs exist
    for f in list(pdir.glob("*.md")) + list((root / "examples" / "hud-layout-intelligence").glob("*.md")):
        for rid in set(REF_ID_RE.findall(f.read_text(encoding="utf-8"))):
            if rid not in known_refs:
                errors.append(f"{f.relative_to(root)}: cita {rid}, ausente no benchmark-register")

    # 6. templates
    tdir = root / "templates"
    mem = tdir / "layout-memory-record.md"
    if mem.exists():
        t = mem.read_text(encoding="utf-8")
        for field in MEMORY_FIELDS:
            if not re.search(rf"^\|\s*{re.escape(field)}\s*\|", t, flags=re.M):
                errors.append(f"templates/layout-memory-record.md: campo ausente '{field}'")
    else:
        errors.append("templates/layout-memory-record.md ausente")
    dec = tdir / "layout-decision.md"
    if dec.exists():
        rows = re.findall(r"^\|\s*(\d{1,2})\s*\|", dec.read_text(encoding="utf-8"), flags=re.M)
        if sorted(set(int(r) for r in rows)) != list(range(1, 13)):
            errors.append("templates/layout-decision.md: deve conter as 12 perguntas")
    else:
        errors.append("templates/layout-decision.md ausente")
    for name in ("layout-pattern.md", "layout-review.md"):
        if not (tdir / name).exists():
            errors.append(f"templates/{name} ausente")

    # 7. cases
    cases = sorted((root / "examples" / "hud-layout-intelligence").glob("*.md"))
    if len(cases) < 3:
        errors.append(f"esperados ≥ 3 casos documentais, encontrados {len(cases)}")
    for c in cases:
        t = c.read_text(encoding="utf-8")
        for sec in CASE_SECTIONS:
            if sec not in t:
                errors.append(f"{c.relative_to(root)}: seção ausente '{sec}'")
        for word in ("Mobile", "Gamepad", "Desktop"):
            if word.lower() not in t.lower():
                errors.append(f"{c.relative_to(root)}: plano sem '{word}'")
        if not re.search(r"\|\s*`[a-z]+\.[a-z-]+`.*\|\s*\*\*escolhida", t):
            errors.append(f"{c.relative_to(root)}: tabela de alternativas sem opção escolhida")

    errors.extend(check_v12(root))

    for e in errors:
        print(f"ERRO: {e}")
    print(f"\n{len(md_files)} arquivos .md, {checked_links} links/caminhos, {len(ids)} padrões, "
          f"{len(known_refs)} fontes/benchmarks, {len(cases)} casos.")
    print("Escopo: validação ESTRUTURAL. Não avalia beleza, UX nem responsividade real "
          "(isso exige captura em Studio/cliente).")
    if errors:
        print(f"Inválido: {len(errors)} erro(s).")
        return 1
    print("Estrutura válida.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
