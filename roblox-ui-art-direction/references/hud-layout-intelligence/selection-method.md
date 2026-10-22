# Selection Method — `layout-decision` obrigatório

Antes de construir qualquer HUD/tela, preencha `templates/layout-decision.md` (salvo no
repositório do jogo, ex.: `docs/ui/layout-decisions/<tela>.md`). Sem decisão registrada,
não passe para assets ou implementação.

## 0. Entradas

Leia primeiro: design brief, theme profile e a **memória do projeto**
(`memory-governance.md`) — decisões anteriores e lições locais podem já responder parte
das perguntas. Lições de outros projetos não são regra; servem de hipótese.

## 1. As 12 perguntas

| # | Pergunta | Por que muda o layout |
|---|---|---|
| 1 | Qual é a **tarefa principal**? (agir · comparar · descobrir · configurar · acompanhar · confirmar · negociar) | define o arquétipo |
| 2 | **Contexto**: combate, exploração, lobby/pré-partida, loja segura, menu seguro? | define quanto pode cobrir o mundo |
| 3 | A informação precisa ficar **sempre visível**? | persistente (HUD) vs sob demanda (menu) |
| 4 | **Urgência e frequência** da ação? | segundos+recorrente → periférico; minutos+opcional → menu/modal |
| 5 | **Quantos itens** agora e quanto podem **crescer**? | ver escala abaixo |
| 6 | Precisa de **busca, filtro, ordenação, paginação ou scroll**? | estrutura do catálogo |
| 7 | Há **seleção + detalhe + comparação** de atributos? | split pane / detalhe sob demanda |
| 8 | Há **risco econômico, social ou irreversível**? | resumo, estado, cancelar, confirmação proporcional, servidor autoritativo |
| 9 | **Dispositivos e inputs** suportados (desktop, phone portrait/landscape, tablet, ultrawide, console/TV; mouse, teclado, touch, gamepad)? | composições e rotas de foco |
| 10 | O que **pode e não pode** cobrir o gameplay? (centro/visada, joystick, jump, topbar, chat) | zonas proibidas |
| 11 | Qual **fase** (A/B/C/D) está autorizada? | limita escopo |
| 12 | Quais **estados** precisam ser testados? (empty, loading, error, disabled, overflow, full + específicos) | plano de prova |

### Escala de itens (heurística)

| Quantidade/crescimento | Default |
|---|---|
| 1–8, fixo | lista/linha de cards ou hotbar; sem busca |
| 9–30 | grid/lista com categorias ou tabs; busca opcional |
| 31–200 | grid + filtros + ordenação; busca recomendada |
| ilimitado / coleção | grid + busca + filtros + ordenação + scroll virtualizado/paginado + gestão de duplicatas |

## 2. Regra de seleção rápida (ponto de partida, não veredito)

| Situação | Candidato inicial |
|---|---|
| ação em < 2 s durante gameplay | `match.overlay` / `collection.hotbar` (periférico, compacto) |
| comparar muitos itens | `collection.grid-detail` ou `commerce.catalog-detail` |
| comparar atributos com slots limitados | `loadout.slot-catalog` |
| troca entre duas partes | `trade.bilateral-confirm` |
| progressão/recompensa | `reward.track-reveal` |
| relação espacial (mapa, árvore) | ver `patterns/pattern-catalog.md` (mapa, skill tree) + alternativa navegável em lista |
| muitas preferências | `settings.hierarchy` |
| objetivo durante o loop | `quest.tracker-expand` |
| tensão/atmosfera | `survival.contextual` |
| mobile não sustenta dois painéis | conteúdo principal + detalhe sob demanda (sheet/modal) |

## 3. Comparar no máximo três alternativas viáveis

Para cada candidata registre: **por que é candidata · trade-offs · impacto mobile ·
impacto gamepad · impacto no QA · escolhida/rejeitada e por quê**.

- Não liste alternativas de enfeite. Se só uma é viável, escreva por que as outras
  famílias não servem (ex.: "hotbar inviável: 140 pets e crescimento ilimitado").
- Compare composições, não estilos visuais. Estética vem do theme profile.

## 4. Decidir e justificar

- A justificativa cita as respostas 1–12 (ex.: "tarefa = comparar; 200+ itens; risco baixo;
  mobile 70% → grid-detail com detalhe em sheet").
- Marque com **[aprovação humana]** toda escolha subjetiva (ex.: sidebar vs tabs quando
  ambas funcionam, densidade preferida, posição estética de um elemento não crítico).
  Não apresente preferência como fato técnico.
- Use os rótulos `official | observed | heuristic | hypothesis` nos argumentos.

## 5. Planejar responsividade e input **antes** do desktop

Escreva os wireframes textuais de **mobile** e **gamepad** primeiro (ou junto), depois o
desktop. Defina as condições de reflow (ver `responsive-composition.md`) e a rota de foco
(ver `input-and-focus.md`).

## 6. Gerar o plano de prova

Lista verificável: viewports × estados × inputs que precisam de captura real
(`templates/layout-review.md`). Sem esse plano, a decisão não está completa.

## 7. Depois da decisão

Siga o workflow existente: matriz imagem/nativo por elemento → manifest de assets →
implementação → QA visual → **registro de memória** (`templates/layout-memory-record.md`).
