# Component System

Biblioteca **funcional** mínima de componentes de UI. Define papel, estrutura, estados,
foco e custo — **nunca a aparência**, que vem do theme profile do jogo. Receitas de código
(nine-slice, botão híbrido com estados, atlas, fallback) estão em
`references/roblox-ui-implementation.md`; não são repetidas aqui. Para um componente
específico de um jogo, preencha `templates/component-contract.md`.

## Regras comuns (valem para todos)

- Estados canônicos: `idle · hover · press · selected · focus · disabled · pending · success · error`.
  Cada componente declara quais se aplicam; os não aplicáveis são marcados `n/a`.
- `hover` é sempre opcional (só ponteiro); `focus` é obrigatório se o componente for
  interativo e gamepad/teclado forem suportados.
- Ação via `GuiButton.Activated`; nada essencial em hover/drag.
- Texto dinâmico/localizável sempre nativo; tamanho mínimo e contraste vêm do theme profile.
- Asset ausente → fallback nativo visível marcado `Placeholder` (ver implementação).
- Não crie componente "genérico" sem função visual clara: se dois componentes têm o mesmo
  papel e só mudam de cor, é uma **variante**, não um componente novo.

## Catálogo

| Componente | Função | Usar / não usar | Estrutura nativa recomendada | Img/Native/Hybrid | Estados aplicáveis | Responsivo | Foco | Anti-padrão | Custo |
|---|---|---|---|---|---|---|---|---|---|
| **Panel** | agrupar conteúdo de uma região | usar para regiões com título/ação; não para cada linha | `ImageLabel`(Slice) ou `Frame` + `UIPadding` + layout | Hybrid (moldura) ou Native (minimal) | idle, disabled (opcional) | `UISizeConstraint`; `SliceScale` menor em telas pequenas | não focável | painel dentro de painel dentro de painel | baixo |
| **Button** | disparar uma ação nomeada | ações com texto; não para ícone isolado (IconButton) | `ImageButton`/`TextButton` + `TextLabel` + `UIScale` | Hybrid ou Native | idle, hover, press, focus, disabled, pending, success, error | altura mínima de toque em Offset; largura `AutomaticSize` | focável; A ativa | hierarquias iguais para primário e destrutivo | baixo |
| **IconButton** | ação frequente reconhecível por ícone | barras, fechar, filtros; não para ação ambígua | `ImageButton` + ícone + rótulo acessível (tooltip/label curto) | Image (ícone) + Native (hit area) | idle, hover, press, focus, selected, disabled | hit area ≥ mínimo de toque mesmo com ícone menor | focável; rótulo visível no foco | ícone sem rótulo para ação rara | baixo |
| **Tab** | trocar escopo local de uma tela | 2–7 escopos irmãos; não para navegação global (rail) | `TextButton`s em `UIListLayout` + indicador | Native (+ Hybrid opcional) | idle, hover, press, selected, focus, disabled | vira chips roláveis no narrow | LB/RB alterna; foco segue seleção | abas que mudam de lugar entre telas | baixo |
| **ItemCard** | representar um item comparável | grids/listas de itens; não para ações soltas | `ImageButton` (moldura) + ícone + nome + badges + `UIAspectRatioConstraint` | Hybrid | idle, hover, press, selected, focus, disabled (bloqueado), pending | tamanho de célula calculado; nome com wrap/truncamento | focável no grid; `NextSelection*` nas bordas | raridade só por cor; ação ao tocar no card | médio (por instância: use pool) |
| **CurrencyPill** | mostrar saldo de um recurso | HUD/loja; não para preços de itens (use PriceTag dentro do card) | `Frame` + ícone + `TextLabel` (`AutomaticSize` X) | Hybrid | idle, pending (atualizando), success (ganho), error (falha de sync) | abreviação localizada; valor completo no detalhe | não focável (ou focável se abre loja) | saldo atualizado no cliente antes do servidor | baixo |
| **ProgressBar** | mostrar progresso/recurso contínuo | vida, XP, carregamento; não para escolhas discretas | `Frame` trilha + `Frame` fill (`Size` X) + rótulo numérico | Native (+ trilha em imagem se o tema exigir) | idle, pending, success, error, disabled | altura com `UISizeConstraint` | não focável | valor só por cor; animar a cada frame | baixo |
| **Modal** | exigir decisão antes de continuar | confirmação, compra, erro bloqueante; não para info que pode ser toast | ScreenGui própria (`DisplayOrder` alto) + overlay + Panel + ConfirmationFooter | Hybrid | idle, pending, success, error | `UISizeConstraint`; centralizado | **prende o foco**; foco inicial definido; B/Esc = cancelar | modal sem saída; empilhar modais | baixo |
| **Sheet** | mostrar detalhe sob demanda em tela estreita | detalhe de item no portrait; não substitui modal de risco | Frame ancorado na base (`AnchorPoint` (0.5,1)) + alça + conteúdo rolável | Hybrid | idle, pending, error | altura máx. por constraint; vira painel lateral no wide | prende foco enquanto aberto; B fecha | sheet sobre controles de gameplay | baixo |
| **Tooltip** | explicar sem ocupar espaço | detalhes secundários; não para informação essencial | Frame + TextLabel com `AutomaticSize` | Native | idle | reposiciona para não sair da tela | aparece também no foco, não só hover | conteúdo essencial só no hover | baixo |
| **Toast** | avisar sem interromper | conquistas, convites, falhas leves; não para erro que exige ação | Frame em fila (`UIListLayout`) dentro do safe inset | Native (+ ícone) | idle, success, error | 1 por vez no phone, até 3 no desktop | não rouba `SelectedObject` | fila infinita; cobrir CTA | baixo |
| **FocusRing** | indicar o foco de gamepad/teclado | todo interativo focável | `SelectionImageObject` próprio ou realce no componente | Hybrid ou Native | focus | espessura visível na menor resolução e na TV | é o próprio foco: sempre visível, nunca fora da tela | brilho sutil de baixo contraste; desligar o foco | baixo |
| **EmptyState** | dizer por que não há conteúdo e o que fazer | listas vazias, filtro sem resultado | Frame + ilustração opcional + texto + Button de próximo passo | Hybrid | idle | ilustração some em telas pequenas | foco no botão de ação | "Nada aqui" sem próximo passo | baixo |
| **LoadingSkeleton** | reservar espaço enquanto carrega | listas/cards com latência; não para operações < ~200 ms | Frames com a forma do conteúdo final | Native | pending | mesma grade do conteúdo final | ações desabilitadas | spinner de tela cheia bloqueando tudo | baixo (sem animações pesadas) |
| **ErrorState** | explicar falha e oferecer recuperação | falha de carga/ação; não para validação de campo | Frame + texto + Button "Tentar de novo" + detalhe opcional | Native | error, pending (retry) | inline na região afetada | foco no botão de recuperação | erro genérico sem ação; apagar dados já exibidos | baixo |
| **ConfirmationFooter** | concentrar ações finais de decisão de risco | compra, trade, deletar; não para navegação | Frame fixo no rodapé com resumo + Cancelar + Confirmar | Hybrid | idle, pending, success, error, disabled | sempre dentro do safe inset; empilha no narrow | foco inicial em Cancelar quando o risco é alto (decisão do projeto) | Confirmar na posição do antigo Fechar; Confirmar em B | baixo |

## Composição

Telas são composições destes componentes; o `templates/hud-screen-spec.md` lista quais e o
`templates/state-matrix.md` diz o estado de cada um por estado da tela. Componentes
novos só entram quando nenhum acima cumpre a função — registre-os com
`templates/component-contract.md`.
