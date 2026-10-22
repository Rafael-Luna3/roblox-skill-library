# Accessibility & Usability

Arte forte não pode custar legibilidade ou usabilidade.

## 1. Legibilidade e contraste

- Texto sobre arte: garanta contraste ≥ 4.5:1 (corpo) e ≥ 3:1 (títulos grandes / ícones
  essenciais) contra a **área real** atrás do texto. Se a arte for ruidosa, use placa de
  fundo, `UIStroke` no texto (`ApplyStrokeMode.Contextual`) ou sombra.
- Fonte decorativa só para títulos curtos; corpo e números em fonte legível.
- Tamanhos mínimos (referência, ajustar ao público): corpo ~14px desktop / ~16px mobile
  efetivos; números de moeda no HUD maiores que o corpo.
- Nunca codifique informação só por cor (raridade, erro, disponível/indisponível): some
  ícone, rótulo, forma ou padrão.

## 2. Toque, mouse e gamepad

- Alvos de toque ≥ 44px (ideal ~48px), com espaçamento entre alvos.
- Use `Activated` (unifica mouse, toque, gamepad).
- Gamepad: seleção inicial ao abrir, vizinhos (`NextSelection*`) definidos em grades,
  modal prende o foco, `SelectionImageObject` com arte do tema **visível** (não remover o
  foco), dicas de botão só quando o gamepad é a entrada ativa.
- Teclado em desktop: atalhos para fechar (Esc/B) e alternar abas quando fizer sentido.

## 3. Estados de tela (todos desenhados no tema)

Vazio (com instrução do próximo passo), loading (skeleton/spinner temático), erro
(mensagem clara + ação de tentar de novo), confirmação para ações destrutivas ou caras,
sucesso, desabilitado (com motivo: "Nível 10 necessário").

## 4. Localização

- Todo texto em `TextLabel` nativo; sem texto em imagens.
- Layouts acomodam +30–40% de comprimento (alemão/português); use `AutomaticSize` e
  `TextWrapped` onde couber.
- `AutoLocalize` considerado; números/moedas formatados por função única.
- Ícones e cores sem conotação cultural problemática para o público-alvo.

## 5. Conforto e segurança

- Respeitar `GuiService.ReducedMotionEnabled`; evitar flashes rápidos de alto contraste.
- Não cobrir o centro da tela de jogo com UI persistente em jogos de ação.
- Botões de compra com Robux: fluxo nativo de compra do Roblox; nada que induza clique
  acidental (ex.: botão de compra onde antes havia "fechar").
- Público infantil: linguagem simples, ícones claros, sem padrões manipulativos (timers
  falsos, escassez falsa).

## 6. Ver também (v1.1.0)

Regras detalhadas de foco (XAG 112/113), gamepad, touch e prompts por input:
`references/hud-layout-intelligence/input-and-focus.md`. Fontes e status de verificação:
`references/hud-layout-intelligence/benchmark-register.md`.
