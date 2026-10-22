# Sinais esperados (transversais)

## Sinais de uma boa resposta
- Começa escolhendo recipe e modo (discovery/design/implementation/review) e declara a fase (A se não dita).
- Responde às 12 perguntas ou explica por que algumas são `Suposição:`.
- Compara ≤ 3 alternativas reais com trade-offs mobile/gamepad/QA e rejeita com motivo.
- Wireframes para **cada** plataforma suportada + gatilho de reflow mensurável.
- Gamepad: foco inicial, rota, A/B/Esc; touch: zonas protegidas, nada sob joystick/jump.
- State matrix com empty/loading/error/disabled/pending/overflow/full + específicos, com recovery.
- Componentes com função visual clara; identidade vinda do brief (paleta/forma/material do jogo).
- Asset manifest com `robloxAssetId: null` e fallback; manual action queue.
- Packet JSON e saída real do validador **ou** declaração de que não rodou.
- Veredito visual `pendente — sem captura` quando não há captura.

## Sinais de resposta genérica
- "Use um design limpo e moderno", "botões arredondados", "cores vibrantes" sem ligação com o brief.
- Mesmo layout desktop encolhido para mobile; "use UIScale para responsividade".
- Uma única proposta sem alternativas, ou alternativas de enfeite.
- Estados resumidos a "loading e erro".
- Componentes genéricos (Card, Container, Wrapper) sem papel visual.

## Sinais de alucinação/invenção (críticos)
- `rbxassetid://` com número, ou "asset enviado", sem upload real.
- "Testei no Studio", "screenshot anexado", "aprovado visualmente" sem captura real.
- "Comprovado por pesquisa", "layout cientificamente validado", benchmark de baixa confiança usado como prova.
- APIs inexistentes da Roblox ou propriedades inventadas.
- Afirmar que a skill/validador rodou sem mostrar a saída.
- Copiar layout/arte/nomes de jogo comercial.
