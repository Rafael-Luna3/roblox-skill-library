# HUD Layout Intelligence

Extensão da `roblox-ui-art-direction` (desde v1.1.0) para **escolher a composição** de um HUD
ou tela antes de aplicar arte, assets e implementação. Ela não substitui os módulos v1.0.0:
decide *qual layout*; os módulos existentes decidem *como ele fica bonito e funciona*.

## Quando ler

- Antes de criar ou redesenhar qualquer HUD, menu, inventário, loja, trade, recompensa,
  settings, tracker, lobby, mapa ou overlay de partida.
- Quando um layout "não funciona no celular/controle" e a correção parece ser só encolher.
- Ao registrar decisões e lições de layout de um projeto.

## Roteamento

| Necessidade | Arquivo |
|---|---|
| Processo obrigatório de decisão (12 perguntas, ≤ 3 alternativas) | [selection-method.md](selection-method.md) |
| Reflow, Scale/Offset, constraints, StyleQuery, camadas, matriz de viewports | [responsive-composition.md](responsive-composition.md) |
| Gamepad, touch, teclado/mouse, foco, B/Esc, zonas de polegar | [input-and-focus.md](input-and-focus.md) |
| Fontes oficiais, acessibilidade e benchmarks datados | [benchmark-register.md](benchmark-register.md) |
| Memória por projeto, candidatos opt-in e biblioteca curada | [memory-governance.md](memory-governance.md) |
| Fichas de padrão | [patterns/](patterns/) — índice abaixo |
| Templates | `templates/layout-decision.md`, `templates/layout-pattern.md`, `templates/layout-review.md`, `templates/layout-memory-record.md` |
| Casos documentais | `examples/hud-layout-intelligence/` |
| Depois de escolher o layout (v1.2.0) | `references/hud-delivery-contract.md` — o layout vira pacote implementável; exemplos completos em `examples/golden-hud-packets/` |

### Índice de padrões

| ID | Arquivo | Uso típico |
|---|---|---|
| `collection.grid-detail` | [patterns/collection-grid-detail.md](patterns/collection-grid-detail.md) | pets, skins, itens, colecionáveis, duplicatas |
| `collection.hotbar` | [patterns/collection-hotbar.md](patterns/collection-hotbar.md) | itens de uso rápido em gameplay |
| `commerce.catalog-detail` | [patterns/commerce-catalog.md](patterns/commerce-catalog.md) | lojas de moeda/Robux, passes, bundles |
| `loadout.slot-catalog` | [patterns/loadout-slot-catalog.md](patterns/loadout-slot-catalog.md) | equipamento RPG, torres, habilidades, comparação de stats |
| `trade.bilateral-confirm` | [patterns/bilateral-trade.md](patterns/bilateral-trade.md) | trade entre jogadores |
| `reward.track-reveal` | [patterns/reward-track-reveal.md](patterns/reward-track-reveal.md) | daily, battle pass, conquistas, gacha, roleta |
| `match.overlay` | [patterns/gameplay-overlay.md](patterns/gameplay-overlay.md) | vida, stamina, cooldowns, timer, score, objetivos, equipes |
| `settings.hierarchy` | [patterns/settings-hierarchy.md](patterns/settings-hierarchy.md) | configurações |
| `quest.tracker-expand` | [patterns/quest-tracker.md](patterns/quest-tracker.md) | missões e objetivos durante o loop |
| `survival.contextual` | [patterns/contextual-survival.md](patterns/contextual-survival.md) | horror e survival |
| 14 fichas compactas | [patterns/pattern-catalog.md](patterns/pattern-catalog.md) | `progression.upgrade-craft-tree`, `nav.global-rail` (sidebar global vs tabs locais), `nav.main-menu`, `lobby.party-matchmaking`, `map.minimap-fullmap`, `onboarding.tutorial-steps`, `dialog.npc-choices`, `rank.leaderboard`, `match.results-spectate-respawn`, `social.notification-stack`, `event.live-hub`, `obby.progress-checkpoint`, `tycoon.build-economy`, `vehicle.drive-customize` |

## Classificação de evidência (obrigatória)

Toda afirmação de padrão é marcada com um rótulo:

| Rótulo | Significa | Pode virar regra? |
|---|---|---|
| `official` | API ou recomendação documentada pela Roblox (Creator Hub) | sim, enquanto a doc não mudar |
| `observed` | Padrão visto em jogo publicado ou fonte verificável (wiki, guia, página do jogo) | não sozinho; é exemplo, não prova |
| `heuristic` | Boa prática de UX/acessibilidade (ex.: Game Accessibility Guidelines, XAG) | default razoável; validar no jogo |
| `hypothesis` | Ideia sem playtest/telemetria própria | só depois de teste |

Proibido: chamar um layout de "cientificamente validado" ou "comprovado" porque aparece em
jogo popular. Popularidade é `observed`, não eficácia.

## Fases de produção

| Fase | Escopo autorizado | Não fazer nesta fase |
|---|---|---|
| **A** | layout, estrutura, responsividade e visual estático consistentes em **todo** o escopo | tweens de produção, áudio, partículas |
| **B** | animação e microinteração (ver `references/animation-and-feedback.md`) | redesenho de layout sem voltar à A |
| **C** | áudio e feedback sonoro | — |
| **D** | polimento e QA final (ver `references/visual-qa.md` + `templates/layout-review.md`) | features novas |

Não polir um HUD com motion e som enquanto o restante do conjunto ainda está
visualmente inconsistente. Se o pedido não diz a fase, assuma **A** e declare isso.

## Ligação com os módulos v1.0.0

| Etapa | Módulo existente que continua sendo a fonte |
|---|---|
| contexto do jogo | `templates/design-brief.md`, `references/design-discovery.md` |
| estética e tokens | `templates/theme-profile.md`, `references/theme-system.md`, `references/visual-direction.md` |
| imagem vs nativo vs híbrido | `references/asset-decision-matrix.md` (os padrões só indicam a estratégia; a matriz decide por elemento) |
| assets | `references/image-production.md`, `templates/asset-manifest.json` |
| implementação | `references/roblox-ui-implementation.md` |
| responsividade base | `references/responsive-layout.md` (esta extensão acrescenta reflow por padrão) |
| motion | `references/animation-and-feedback.md` (fase B) |
| acessibilidade | `references/accessibility-and-usability.md` |
| QA | `references/visual-qa.md` + `templates/visual-review.md` + `templates/layout-review.md` |

## Limites honestos

- Benchmarks são datados (consulta: 2026-10-22) e podem mudar; vários não foram
  verificados visualmente nesta versão — ver status em `benchmark-register.md`.
- Nenhum padrão aqui foi validado por playtest ou A/B; os rótulos dizem o grau de confiança.
- `scripts/validate_skill_docs.py` verifica estrutura (links, campos, IDs). Não avalia
  beleza, UX nem responsividade real — isso exige captura em Studio/cliente.
