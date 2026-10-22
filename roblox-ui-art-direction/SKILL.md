---
name: roblox-ui-art-direction
description: Direção de arte, escolha de layout e produção visual de UI para qualquer jogo Roblox (qualquer gênero ou tema). Define design brief e theme profile por jogo, seleciona e justifica o layout de cada HUD por tarefa, risco, dispositivo e input (HUD Layout Intelligence), entrega um pacote implementável por tela (spec, componentes, estados, assets, handoff, QA), decide entre arte em imagem e UI nativa (Image-First), implementa no Studio e faz QA visual real com memória por projeto. Use para criar, redesenhar, implementar ou revisar HUDs, menus, inventários, lojas, trades e telas de recompensa; não use para lógica de gameplay, rede ou dados sem componente visual.
allowed-tools:
  - Bash(python ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py *)
  - Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py *)
  - Bash(python ${CLAUDE_SKILL_DIR}/scripts/validate_asset_manifest.py *)
  - Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/validate_asset_manifest.py *)
  - Bash(python ${CLAUDE_SKILL_DIR}/scripts/validate_skill_docs.py)
  - Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/validate_skill_docs.py)
metadata:
  short-description: Direção de arte + layout de HUD + pacote implementável + UI Roblox
  version: "1.2.0"
---

# Roblox UI Art Direction

Objetivo: interfaces Roblox com **identidade visual forte e própria de cada jogo**, sólidas
em qualquer dispositivo e **entregues como pacote implementável**. A skill é independente de
jogo: tudo que é estético (cores, fontes, raridades, molduras) vem do **theme profile do
projeto**, nunca desta skill.

## 1. Primeiro: escolha a recipe e o modo

| Pedido | Recipe | Modo |
|---|---|---|
| criar HUD/tela nova | `references/task-recipes/new-hud.md` | discovery → design (→ implementation se pedido) |
| redesenhar UI existente | `references/task-recipes/redesign-existing-ui.md` | discovery → design → implementation |
| implementar design já aprovado | `references/task-recipes/implement-approved-design.md` | implementation |
| revisar/auditar HUD existente | `references/task-recipes/review-existing-hud.md` | review |
| só produzir/preparar assets | `references/task-recipes/asset-production-only.md` | design (assets) |

Leia **só** a recipe escolhida; ela diz quais referências carregar. Declare no início:
recipe, modo e **fase** (A layout + estático do conjunto · B motion · C áudio · D polimento/QA;
sem fase declarada, assuma A e diga isso).

## 2. Contrato de entrega (obrigatório para criar ou redesenhar)

"Layout escolhido" **não** é entrega. Cada tela entrega os 11 artefatos de
`references/hud-delivery-contract.md`: context snapshot, layout decision, screen spec,
composição por plataforma, component inventory, state matrix, matriz imagem/nativo, asset
manifest, implementation handoff, QA evidence plan e manual action queue — com o que é
obrigatório ou pode ficar pendente em cada fase.

Quando a tarefa cria ou redesenha HUD, gere também o **HUD packet** JSON
(`templates/hud-packet.example.json`, schema `schemas/hud-spec.schema.json`) no repositório
do jogo, ex.: `docs/ui/<tela>/<tela>.packet.json`.

## 3. Princípio central: Image-First Art Direction

> **Imagens carregam a identidade visual. Componentes nativos carregam estrutura,
> responsividade, conteúdo dinâmico e interação.**

- Imagem: molduras ilustradas, botões com acabamento, ornamentos, ícones, badges, headers, arte de item.
- Nativo: layout, clipping, scroll, grids, texto, áreas de clique, foco, barras simples, formas simples.
- Híbrido (o mais comum): arte em `ImageLabel` (nine-slice) + `TextLabel` nativo + hit area + estados.
- Proibido: dezenas de Frames simulando uma moldura; a tela inteira numa imagem; texto dinâmico
  ou localizável em imagem; AssetId inventado.

Decisão por elemento: `references/asset-decision-matrix.md`. Componentes:
`references/component-system.md` (função, estados, foco e custo — nunca a aparência).

## 4. Fluxo

1. **Contexto:** design brief, theme profile e memória do projeto
   (`references/design-discovery.md`, `references/visual-direction.md`,
   `references/theme-system.md`, `references/hud-layout-intelligence/memory-governance.md`).
2. **Layout:** HUD Layout Intelligence — `templates/layout-decision.md` (12 perguntas,
   ≤ 3 alternativas, mobile e gamepad antes do desktop). Comece por
   `references/hud-layout-intelligence/README.md`.
3. **Especificação:** `templates/hud-screen-spec.md`, `templates/state-matrix.md`,
   `templates/component-contract.md` (só componentes não triviais),
   `templates/implementation-handoff.md`, `templates/evidence-board.md`.
4. **Arte e construção:** imagem vs nativo → `references/image-production.md` e
   `templates/asset-manifest.json` → `references/roblox-ui-implementation.md` →
   reflow (`references/responsive-layout.md`,
   `references/hud-layout-intelligence/responsive-composition.md`) → input/foco
   (`references/hud-layout-intelligence/input-and-focus.md`) → motion só na fase B
   (`references/animation-and-feedback.md`).
5. **Validação documental:** rode os validadores (seção 6) e corrija até passarem.
6. **QA visual e memória:** capturas reais (`references/visual-qa.md`,
   `templates/visual-review.md`, `templates/layout-review.md`) e registro em
   `templates/layout-memory-record.md`.

Carregue referências **apenas quando pertinentes** à etapa atual.

## 5. Regras obrigatórias

- **Nunca** invente imagens, caminhos, `rbxassetid://`, capturas, testes, playtests,
  pesquisas ou aprovações humanas. Asset inexistente = `robloxAssetId: null` + fallback
  identificado (`PLACEHOLDER_*`, atributo `Placeholder = true`).
- **Aprovação visual só com captura real** (Studio/cliente) nos viewports e estados do plano.
  Sem captura → veredito `pendente — sem captura`. Validadores não aprovam nada visualmente.
- Não imponha paleta, fonte, raridades ou estilo universais; preferências de um jogo ficam
  na memória **daquele projeto** e só viram regra via revisão humana/PR.
- Texto dinâmico, números, nomes e strings localizáveis são sempre nativos.
- Botão de UI nunca autoriza economia: compra, trade, equipar, recompensas → servidor.
- Não copie UI, screenshots, assets ou logos de jogos de terceiros; benchmarks extraem
  princípios. Popularidade é `observed`, não prova de eficácia.
- Não sobrescreva assets/GUIs existentes nem altere sistemas fora do escopo sem pedido.
- Nenhum HUD sem `layout-decision`; nenhum layout preso a uma resolução; reflow em vez de
  miniatura do desktop; nada essencial só por hover, drag, cor ou animação.
- Rotule evidências (`official | observed | heuristic | hypothesis`); escolhas estéticas
  subjetivas recebem **[aprovação humana]** em vez de virar fato técnico.
- Geração de imagem é opcional: sem ferramenta real, entregue prompts e registre pendências.
- **Manual action queue obrigatória** sempre que houver asset, upload, AssetId, aprovação ou
  captura pendente.

## 6. Validadores (rode antes de declarar a documentação consistente)

```bash
python ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py <docs/ui/<tela>/<tela>.packet.json>
python ${CLAUDE_SKILL_DIR}/scripts/validate_asset_manifest.py <docs/ui/asset-manifest.json>
python ${CLAUDE_SKILL_DIR}/scripts/validate_skill_docs.py   # integridade da própria skill
```

Use `python3` se `python` não existir. Fora do Claude Code, troque `${CLAUDE_SKILL_DIR}` pelo
caminho da pasta da skill. Os validadores checam **consistência documental** (campos, IDs,
referências, AssetIds fictícios, capturas sem arquivo) — não beleza, UX nem responsividade real.
Mostre a saída real; se não puder rodar, diga isso.

## 7. Ferramentas opcionais (use se existirem)

- Geração de imagem: `imagegen` (Codex) ou `generate_texture`/`upload_image`/`store_image`
  do Roblox Studio MCP. Verifique disponibilidade antes de prometer.
- Studio: `screen_capture`, `execute_luau`, `inspect_instance`, `search_game_tree`,
  Device Simulator/Emulator e Controller Emulator para QA.
- Upload: Asset Manager / Open Cloud — só com autorização do usuário.
- Skills Roblox complementares, se instaladas (`roblox-ui`, `roblox-architecture`,
  `roblox-security`, `roblox-performance`, `roblox-luau`, `roblox-testing`): use-as para
  lifecycle, arquitetura, segurança e performance. Esta skill não depende delas.

## 8. Critérios de qualidade

Uma tela está pronta quando: (1) o pacote do contrato está completo para a fase;
(2) o packet passa no validador; (3) a identidade é reconhecível e coerente com o brief;
(4) cada elemento tem decisão imagem/nativo; (5) só tokens do tema; (6) todas as
plataformas e inputs declarados têm composição, foco e reflow; (7) a state matrix cobre
empty/loading/error/disabled/pending/overflow/full + específicos com recovery;
(8) nenhum placeholder esquecido ou AssetId falso; (9) captura real aprovada — ou veredito
`pendente — sem captura` explícito.

## 9. Conclusão da tarefa

Entregue: recipe/modo/fase usados; artefatos criados ou atualizados (caminhos); saída real
dos validadores; o que foi implementado (DataModel/arquivos); veredito visual com capturas
ou `pendente — sem captura`; registro de memória; **manual action queue**.

## 10. Recursos

| Arquivo | Ler quando |
|---|---|
| `references/task-recipes/*.md` | sempre, primeiro — uma recipe por pedido |
| `references/hud-delivery-contract.md` | ao criar/redesenhar: o que entregar por fase |
| `references/component-system.md` | ao montar o inventário de componentes |
| `references/hud-layout-intelligence/README.md` | antes de escolher layout (método, padrões, reflow, input, benchmarks, memória) |
| `references/design-discovery.md` · `references/visual-direction.md` · `references/theme-system.md` | contexto e identidade |
| `references/asset-decision-matrix.md` · `references/image-production.md` | imagem vs nativo e assets |
| `references/roblox-ui-implementation.md` | construção no Studio |
| `references/responsive-layout.md` · `references/accessibility-and-usability.md` | responsividade e acessibilidade |
| `references/animation-and-feedback.md` | fase B |
| `references/visual-qa.md` | revisão e QA |
| `templates/` | artefatos por jogo (brief, theme, layout, screen spec, componentes, estados, evidências, handoff, review, memória, manifest, packet) |
| `schemas/hud-spec.schema.json` | estrutura do HUD packet |
| `examples/golden-hud-packets/` | 4 pacotes completos de referência (fictícios, sem captura) |
| `examples/` (demais) | generalização de temas e casos de layout v1.1.0 |
| `evaluations/` | cenários e rubricas para medir se a skill melhora respostas |
| `scripts/` | validadores (documentais) |
