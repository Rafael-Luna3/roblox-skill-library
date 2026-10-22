# Responsive Composition — reflow, não miniatura

Complementa `references/responsive-layout.md` (base v1.0.0) com regras por composição.
Fontes: ver `benchmark-register.md` (seção oficial).

## 1. Regras técnicas

| Ferramenta | Use para | Não use para | Evidência |
|---|---|---|---|
| `UDim2` **Scale** | regiões e proporções relativas ao pai | tudo indiscriminadamente ("100% Scale" é dogma errado) | `official` (Position and size) |
| `AnchorPoint` | origem e direção de crescimento (cantos: (1,0), (0,1)…; centro: (0.5,0.5)) | — | `official` |
| **Offset** | padding, gaps, stroke, bordas, mínimos físicos, hit targets, arte pixelada | malha principal do HUD (`fromOffset` em tudo) | `official` + `heuristic` |
| `UIScale` | normalização limitada (ver clamp em responsive-layout) | fazer desktop caber no celular | `official` (multiplica o tamanho do pai) |
| `UIAspectRatioConstraint` | ícones, cards, arte, avatar que não pode deformar | containers de layout fluido | `official` (sobrepõe o layout) |
| `UISizeConstraint` | limitar painel/modal/botão (ex.: não crescer em ultrawide, não encolher abaixo do toque) | aplicar "por hábito" — prevalece sobre layouts | `official` |
| `UITextSizeConstraint` | legibilidade com `TextScaled`; `MinTextSize` **≥ 9** | — | `official` (doc desaconselha < 9) |
| `UIListLayout` (+ flex, `Wraps`, `UIFlexItem`) | linhas/colunas de conteúdo variável, chips que quebram linha | grid de cards comparáveis; flex sem necessidade (custo extra) | `official` |
| `UIGridLayout` | cards com célula estável | conteúdo de altura variável | `official` |
| `AutomaticSize` | texto/containers que crescem com localização | — | `official` |
| `ScrollingFrame` + `AutomaticCanvasSize` | conteúdo que cresce; `VerticalScrollBarInset = ScrollBar/Always` para nada ficar sob a barra; `ElasticBehavior` conforme gosto | esconder overflow por clipping | `official` |
| `ScreenInsets` | `CoreUISafeInsets` (default, recomendado para UI interativa); `DeviceSafeInsets` para HUD não interativo que precisa de mais tela (ex.: medidores) | interativos em `None` | `official` |
| `DisplayOrder` | separar camadas por ScreenGui | pilha de ZIndex sem plano | `official` |
| **Style queries** | `@ViewportDisplaySizeSmall/Medium/Large`, `@PreferredInputKeyboardAndMouse/Touch/Gamepad`, `@ReducedMotionEnabledTrue/False`; queries de container com `::StyleQuery` + `MinSize` | substituir decisão de composição por números copiados | `official` (CSS comparisons) |
| `GuiService.ViewportDisplaySize` / `UserInputService.PreferredInput` | equivalente em script às queries | — | `official` |

## 2. Camadas de ScreenGui (declare no layout-decision)

| Camada | Conteúdo | DisplayOrder (exemplo relativo) | ScreenInsets |
|---|---|---|---|
| `GameplayHUD` | status, timer, hotbar, tracker | baixo | Core (interativo) / Device (só leitura) |
| `Contextual` | prompts, toasts, tooltips | médio | Core |
| `Menu` | inventário, loja, settings | médio-alto | Core |
| `Modal` | confirmação, trade final, compra | alto | Core |
| `CriticalOverlay` | morte, desconexão, resultado | máximo | Core |

Números concretos são do projeto; o que importa é a ordem e não misturar modal com HUD.

## 3. Breakpoint = condição de composição

Não copie "600px" de outro jogo. Defina **condições**:
- "Quando o grid com painel de detalhe não mantém ≥ N colunas no tamanho mínimo de card
  definido no brief, o detalhe vira bottom sheet/modal."
- "Quando a altura útil não comporta hotbar + controles touch sem sobreposição, a hotbar
  vira vertical/compacta junto aos controles."
Use `ViewportDisplaySize` (Small/Medium/Large) como gatilho grosso e `AbsoluteSize` do
container / `::StyleQuery MinSize` como gatilho fino.

## 4. Exemplos de reflow real

**Inventário extenso** (`collection.grid-detail`)
- Desktop: `sidebar categorias | grid | detalhe` (proporção decidida no brief, ex. 18/52/30 — exemplo, não regra).
- Phone portrait: `header + busca` → `chips de filtro horizontais roláveis` → `grid 2–3 colunas` → toque abre **bottom sheet** de detalhe com ação.
- Phone landscape: `rail de categorias estreito | grid`; detalhe em modal lateral.
- Gamepad/TV: tabs com LB/RB; grid focável; detalhe atualiza com o foco; A age; B fecha/volta.

**Trade** (`trade.bilateral-confirm`): desktop lado a lado → portrait em abas
"Você / Outro" com **resumo fixo dos dois lados** e status no rodapé.

**HUD de partida** (`match.overlay`): desktop nos cantos → mobile reagrupa ações perto do
jump/joystick e encolhe status de leitura para o topo, mantendo o centro livre.

## 5. Matriz de viewports e reprovação

| Perfil | Observar | Reprova se |
|---|---|---|
| Desktop 16:9 | hierarquia, densidade, hover só como extra | ação essencial depende de hover |
| Ultrawide (21:9+) | conteúdo não espalha; foco central | painel sem `UISizeConstraint`; linhas longas demais |
| Phone portrait | safe area, polegar, 1–3 colunas, scroll | CTA atrás de notch/joystick; desktop miniaturizado |
| Phone landscape | cantos disputados com controles touch | hotbar/botão sob controles CoreGui |
| Tablet | distâncias maiores para o polegar | posição "% da tela" que só funciona no phone |
| Console/TV | foco, B/Esc, poucas etapas, distância 8–10 ft, TV-safe | sem foco inicial; foco invisível; texto pequeno |
| Texto longo/localizado | wrap, truncamento com alternativa | preço/ação/aviso cortado |
| Reduced motion | estado entendível sem animação | resultado comunicado só por motion |

Ferramentas de teste: Device Simulator/Emulator do Studio (Phone/Tablet/Desktop/Console,
"Actual Resolution") e Controller Emulator; via script, `StudioDeviceSimulatorService`
(resolução, DPI, orientação). `official` — o nome da ferramenta varia entre versões do Studio.

## 6. Anti-padrões de composição

- `UDim2.fromOffset` como malha de um HUD inteiro.
- Diminuir a tela desktop até caber no mobile.
- Constraints espalhadas sem um risco concreto (elas vencem o layout e criam surpresas).
- Grid extenso sem busca/filtro/scroll.
- Painel que cresce sem limite em ultrawide.
- Breakpoints numéricos copiados sem condição de composição.
