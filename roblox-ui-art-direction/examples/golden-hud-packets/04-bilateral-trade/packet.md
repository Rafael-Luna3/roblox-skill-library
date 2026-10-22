# Golden packet 04 — Trade bilateral com confirmação

> **FICTÍCIO · documentação sem captura · veredito visual: pendente — sem captura.**
> Jogo inventado ("Saltmarsh Harbor"). Sem assets, AssetIds, regras reais ou playtest.
> JSON: [packet.json](packet.json).

## Brief resumido
- **Jogo:** pesca cooperativa e vila costeira aconchegante; jogadores trocam peixes raros, iscas e enfeites de barco.
- **Público:** 9–15 e famílias; **70% mobile portrait**, 25% desktop, 5% console. Alvo de golpes → risco crítico.
- **Pilares:** *aquarela de vila de pescadores*, *calma sem pressa* (sem timers agressivos), *clareza de quem dá o quê*.
- **Não é:** mercado frenético, neon, ornamentação medieval, sci-fi.

## Theme profile resumido
| Token | Valor (fictício) |
|---|---|
| surface.panel | papel aquarelado `#F7F1E3` com borda de corda (9-slice) |
| side.you / side.them | `#4E8FA8` + ícone de barco do jogador / `#C9845B` + ícone de chapéu; **rótulos com nome** sempre |
| state.changed | `#E0A526` + ícone ↻ + texto "Oferta alterada" |
| Fontes | Display `Enum.Font.Kalam` (títulos curtos) · Body `Enum.Font.Nunito` (verificar disponibilidade) |
| Motion | suave (`Sine` 0.2 s); countdown sem pulsação agressiva |
| Style anchor | "ilustração em aquarela de itens de pesca e peixes, contorno sépia fino, luz de manhã, vista lateral, fundo transparente, sem texto" |

## Layout decision
| # | Resposta |
|---|---|
| 1 | negociar → comparar → confirmar |
| 2 | social, menu seguro (personagens parados no cais) |
| 3 | as duas ofertas e os status, durante o trade |
| 4 | baixa frequência; pressão social média |
| 5 | até 6 slots por lado (regra fictícia); inventário próprio de centenas |
| 6 | busca/filtro no seletor de inventário |
| 7 | ver detalhe do item do outro (raridade, peso do peixe) |
| 8 | **crítico**: irreversível, alvo de golpes |
| 9 | phone portrait (primário), phone landscape, tablet, desktop, console |
| 10 | tela cheia |
| 11 | A |
| 12 | vazio, pronto/não pronto, oferta alterada, countdown, outro saiu, item intransferível, inventário cheio, erro, bloqueio por idade de conta (regra fictícia) |

**Escolhido:** `trade.bilateral-confirm` **portrait-first**: mesa empilhada "Você em cima / Outro embaixo" com resumo fixo — diferente da versão lado a lado com abas usada no caso documental da v1.1.0; aqui os dois lados ficam visíveis ao mesmo tempo mesmo no phone, com 6 slots compactos.
**[aprovação humana]:** mostrar "peso/raridade" do peixe do outro em destaque (pode incentivar pressão de valor).

## Screen spec
**Hierarquia:** (1) o que cada lado oferece + status de cada lado; (2) aviso de alteração, countdown; (3) detalhe de um item.
```text
PHONE PORTRAIT (primário)
[Troca com @Marina                         ✕]
┌ VOCÊ OFERECE (2/6)           status: ✔ Pronto ┐
│ [🐟][🎣][  ][  ][  ][  ]   [+ Adicionar]       │
└──────────────────────────────────────────────┘
┌ @MARINA OFERECE (1/6)        status: … pensando ┐
│ [🐠][  ][  ][  ][  ][  ]                          │
└──────────────────────────────────────────────┘
↻ Oferta alterada — os dois "Pronto" foram desfeitos     (só quando acontece)
[Recusar]                              [Pronto]
→ ambos prontos → [Confirmar troca] + "3…2…1" (cancela se algo mudar)

DESKTOP / TABLET / LANDSCAPE
[Você | @Marina] lado a lado, mesmos 6 slots, rodapé comum com status e ações

GAMEPAD
↑/↓ alterna mesas; ←/→ slots; A abre seletor/remove; Y detalhe do item do outro;
X Pronto; B fecha seletor; fechar a troca pede confirmação; Confirmar nunca é foco inicial
```
**Gatilhos:** R1 largura < 2× largura mínima de uma mesa de 6 slots → mesas empilhadas; R2 altura útil < duas mesas + rodapé → slots em 1 linha rolável horizontal com contador "2/6".
**Camadas:** `TradeGui` Modal DO 40 · `TradeInventoryGui` Modal DO 45 (seletor, reaproveita `collection.grid-detail`).

## Component inventory
| ID | Tipo | Função visual |
|---|---|---|
| table-you | Panel | mesa do jogador com nome, contador e status |
| table-them | Panel | mesa do outro com nome, contador e status |
| slot-item | ItemCard | item ofertado com ícone e detalhe |
| btn-add | Button | abre seletor de inventário |
| banner-changed | Toast (persistente) | aviso de oferta alterada |
| trade-footer | ConfirmationFooter | Recusar / Pronto / Confirmar com countdown |
| picker | Sheet | seletor de inventário com busca |
| err-trade | ErrorState | falha/cancelamento com motivo |

## State matrix
| Estado | Texto | Ação | Cor/ícone | Foco | Rede | Recovery | Captura |
|---|---|---|---|---|---|---|---|
| empty | "Adicione itens ou espere a oferta de @Marina" | Adicionar | — | btn-add | — | — | sim |
| loading | itens do outro carregando | Pronto desabilitado | skeleton | btn-add | replicação | timeout → error | sim |
| error | "A troca foi cancelada: @Marina saiu." | OK | ⚠ + texto | botão | servidor encerra | itens voltam intactos | sim |
| disabled | "Este item não pode ser trocado" | — | cadeado + texto | slot focável | — | — | sim |
| pending | "Trocando…" | tudo bloqueado | spinner | footer | troca atômica | erro → error | sim |
| overflow | "6/6 — limite" | remover item | contador | slot | — | — | sim |
| full | "Inventário de @Marina está cheio" | — | ícone + texto | Pronto off | servidor valida | ajustar oferta | sim |
| offer-changed | "↻ Oferta alterada — 'Pronto' desfeito" | revisar | âmbar + ícone + texto | mantém posição | servidor zera ready | Pronto de novo | sim |
| countdown | "Confirmando em 3…" | Cancelar | contador | Cancelar | servidor controla tempo | qualquer mudança cancela | sim |
| account-locked | "Trocas liberadas após 3 dias de conta" | — | texto | — | regra do servidor | — | sim |

## Implementation handoff
```text
StarterGui
├── TradeGui (DO 40, CoreUISafeInsets, Enabled=false)
│   └── Root → Header(nome, fechar) · TableYou · TableThem · ChangedBanner · TradeFooter
└── TradeInventoryGui (DO 45, Enabled=false) → Sheet com busca/filtros + grid
```
- Módulos: `UI/Theme`, `UI/Components/TradeTable`, `UI/Components/ConfirmationFooter`, `TradeController`; servidor `TradeService`.
- Dados: `{tradeId: string, you: {items: string[], ready: boolean}, them: {name: string, items: string[], ready: boolean}, countdown: number?, version: number}`.
- Intenções: `AddItem/RemoveItem(tradeId, itemId, version)` · `SetReady(tradeId, version)` · `Confirm(tradeId, version)` · `Cancel(tradeId)`. O servidor rejeita `version` desatualizada, zera ready em qualquer mudança, trava itens durante o trade e executa a troca atômica.
- Ordem: Theme → TradeTable/ItemCard → layout empilhado e lado a lado (R1/R2) → footer com estados → integração com TradeService → seletor → arte.

## Asset matrix
| Elemento | Estratégia | Asset (status) | Fallback |
|---|---|---|---|
| moldura das mesas | Hybrid (9-slice corda) | panel.rope.frame (planned) | Frame + UIStroke sépia |
| ícones de itens | Image (atlas) | atlas.fish.items (prompt-ready) | nome do item em chip |
| ícones de lado | Image | icon.side.boat / icon.side.hat (planned) | inicial do nome em círculo |
| textos, status, contador | Native | — | — |

## Packet JSON
[packet.json](packet.json).

## Plano de capturas
Phone portrait 390×844 com as duas mesas, aviso de alteração e countdown; phone landscape; tablet; desktop lado a lado; console com foco nas mesas e no seletor. Estados da matriz, incluindo saída do outro jogador durante o countdown (requer 2 clientes de teste).

## Decisões rejeitadas
- **Abas "Você / Outro" no phone** — esconde metade da negociação; com 6 slots compactos, empilhar cabe e mantém os dois lados visíveis.
- **Mercado assíncrono (listagens)** — não atende troca ao vivo entre amigos; outro sistema.
- **Countdown longo (10 s) com pulsação** — conflita com o pilar "calma"; adotado 3 s, cancelável.

## Pendências reais
- [aprovação humana] destaque de peso/raridade do item do outro.
- Regras de negócio (6 slots, 3 dias de conta) são fictícias.
- Nenhuma captura; assets não produzidos.
- Teste com dois clientes reais para desconexão/countdown.
