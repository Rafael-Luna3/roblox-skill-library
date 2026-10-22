# Golden packet 03 — Loja com compra de risco

> **FICTÍCIO · documentação sem captura · veredito visual: pendente — sem captura.**
> Jogo inventado ("Pit Lane Garage"). Sem assets, AssetIds, produtos reais ou playtest.
> JSON: [packet.json](packet.json).

## Brief resumido
- **Jogo:** corrida arcade de rua; garagem com carros, pinturas e um passe de temporada. Duas moedas: **Fichas** (ganhas em corrida) e compras com **Robux** (game passes / developer products).
- **Público:** 13+; 50% mobile, 40% desktop, 10% console. **Tom:** noturno, veloz, confiante.
- **Pilares:** *vitrine de garagem* (o carro é o herói), *preço sempre explícito*, *nenhuma compra acidental*.
- **Não é:** cassino (sem roleta, sem timer falso), cartoon, medieval.

## Theme profile resumido
| Token | Valor (fictício) |
|---|---|
| surface.base | asfalto `#121418`; surface.panel `#1C2026` |
| accent.brand | magenta `#FF3D8B` (destaque de produto) |
| currency.tokens | amarelo-placa `#FFC83D` + ícone de ficha |
| currency.robux | **ícone oficial de Robux do sistema de compra** (não redesenhado) + rótulo "Robux" |
| action.destructive/cancel | cinza neutro (Cancelar nunca em magenta) |
| Fontes | Display `Enum.Font.Michroma` · Body/Numeric `Enum.Font.GothamSSm` (verificar disponibilidade; alternativa `Enum.Font.Gotham`) |
| Motion | seca e rápida (`Quint Out` 0.12 s); carro gira lentamente no preview |
| Style anchor | "renders de carro estilizado low-poly com luz de neon de garagem, vista 3/4, fundo transparente, sem texto, sem marcas reais" |

## Layout decision
| # | Resposta |
|---|---|
| 1 | descobrir → avaliar → confirmar compra |
| 2 | loja segura (garagem fora da corrida) |
| 3 | saldo sempre visível no header |
| 4 | ocasional; sem urgência (não há ofertas-relâmpago) |
| 5 | ~60 produtos em 5 categorias; rotação semanal de pinturas |
| 6 | categorias + filtro "possuídos"; sem busca (60 itens) |
| 7 | sim: preview 3D do carro, stats, o que se recebe |
| 8 | **crítico**: Robux e Fichas; compras irreversíveis |
| 9 | phone portrait/landscape, tablet, desktop, ultrawide, console |
| 10 | tela cheia permitida |
| 11 | A |
| 12 | saldo insuficiente, já possuído, compra pendente, falha, sucesso, categoria vazia, loading, produto indisponível |

**Escolhido:** `commerce.catalog-detail` com **vitrine de destaque** (1 produto herói) acima do catálogo — diferente do grid-detail de coleção: aqui o detalhe é o herói da tela, não um painel lateral secundário.
**[aprovação humana]:** foco inicial em Cancelar na confirmação de compra com Robux.

## Screen spec
**Hierarquia:** (1) produto em destaque + preço + moeda; (2) categorias e cards com preço; (3) stats detalhados, termos do passe.
```text
DESKTOP
[GARAGEM]                                      [🪙 12.400 Fichas] [Robux ⊕]
[ VITRINE: ViewportFrame do carro girando | Nome · o que recebe · stats ]
[                                      | [Comprar  🪙 8.000] ou [Comprar  199 Robux] ]
[Carros][Pinturas][Rodas][Passe][Possuídos]
[card][card][card][card][card] →   (fileira rolável por categoria)

PHONE PORTRAIT
[← Garagem       🪙12.4K]
[vitrine 16:9 com carro]  Nome · preço
[Comprar 🪙 8.000]                     (botão largo, acima da área de gestos)
[tabs roláveis]
[card][card]  (grid 2 col)

CONFIRMAÇÃO (Modal, todas as plataformas)
"Comprar Neon Viper por 8.000 Fichas?"  Saldo após: 4.400
[Cancelar]  [Confirmar]
Robux → prompt nativo do Roblox (MarketplaceService), sem modal próprio intermediário de preço diferente.

GAMEPAD
LB/RB categorias · D-pad cards · A seleciona → vitrine · A em Comprar → confirmação (foco em Cancelar) · B volta
```
**Gatilhos:** R1 largura < limite para vitrine + stats lado a lado → stats abaixo da vitrine; R2 `ViewportDisplaySize == Small` → saldo abreviado (valor completo ao tocar); R3 ultrawide → root com `UISizeConstraint`.
**Camadas:** `GarageShopGui` Menu DO 20 · `PurchaseConfirmGui` Modal DO 40.

## Component inventory
| ID | Tipo | Função visual |
|---|---|---|
| showcase | Panel + ViewportFrame | vitrine do produto herói |
| balance-tokens | CurrencyPill | saldo de Fichas |
| tabs-category | Tab | categorias |
| card-product | ItemCard | produto com preço, moeda e estado possuído |
| btn-buy | Button | compra com preço no rótulo |
| confirm-modal | Modal | confirmação de Fichas |
| confirm-footer | ConfirmationFooter | Cancelar / Confirmar + saldo após |
| toast-result | Toast | sucesso/falha discreta |
| err-shop | ErrorState | falha de carga |

## State matrix
| Estado | Texto | Ação | Cor/ícone | Foco | Rede | Recovery | Captura |
|---|---|---|---|---|---|---|---|
| empty | "Novas pinturas na segunda-feira" | ver outra categoria | — | tab | — | — | sim |
| loading | skeleton de cards; preço oculto | comprar desabilitado | — | — | catálogo do servidor | timeout → error | sim |
| error | "A loja não carregou." | Tentar de novo | ⚠ + texto | retry | — | refetch | sim |
| disabled | "Faltam 3.600 Fichas" | Ganhar Fichas (vai para corridas) | ícone + texto (não só cinza) | botão continua focável | — | — | sim |
| pending | "Processando compra…" | tudo bloqueado | spinner no botão | footer | aguarda servidor/prompt | erro → error com saldo intacto | sim |
| overflow | fileira > tela | rolar | setas/scroll | D-pad continua | — | — | sim |
| full | "Possuído" / "Equipar" | Equipar | check + texto | botão | — | — | sim |
| success | "Neon Viper é seu!" | Equipar agora / Continuar | toast | foco em Equipar | confirmado pelo servidor | — | sim |
| robux-cancelled | (prompt nativo fechado) | nenhuma | nada muda | volta ao botão | — | — | sim |

## Implementation handoff
```text
StarterGui
├── GarageShopGui (DO 20, CoreUISafeInsets)
│   └── Root → Header(Balance) · Showcase(ViewportFrame + Info + BuyButton) · CategoryTabs · ProductRow(ScrollingFrame)
└── PurchaseConfirmGui (DO 40, Enabled=false) → Panel + ConfirmationFooter
```
- Módulos: `UI/Theme`, `UI/Components/ProductCard`, `UI/Components/ConfirmationFooter`, `GarageShopController`; servidor `ShopService` (preços, saldo, posse), `ProcessReceipt` para developer products.
- Dados: `{balance: number, products: {id: string, category: string, price: number, currency: "tokens"|"robux", owned: boolean, available: boolean}[]}` — preços **sempre do servidor**.
- Intenções: `BuyWithTokens(productId)` → servidor valida saldo/posse/disponibilidade, debita atômico, retorna novo saldo · Robux → `MarketplaceService:PromptProductPurchase`/`PromptGamePassPurchase` com concessão só em `ProcessReceipt`/verificação de passe.
- Ordem: Theme → ProductCard/CurrencyPill → Header + Tabs + Row → Showcase sem 3D → ViewportFrame só na vitrine → confirmação → estados → integração de compra → arte.

## Asset matrix
| Elemento | Estratégia | Asset (status) | Fallback |
|---|---|---|---|
| carro na vitrine | ViewportFrame (modelo do jogo) | — (modelo existente no jogo fictício) | thumbnail 2D |
| thumbnails de produto | Image (atlas por categoria) | atlas.cars.thumbs (prompt-ready) | nome + silhueta nativa |
| ícone de Fichas | Image | icon.currency.tokens (planned) | círculo amarelo + "F" |
| moldura de card | Native (stroke magenta no selecionado) | — | — |
| fundo da garagem | Image `Crop` | bg.garage (planned) | gradiente nativo |

## Packet JSON
[packet.json](packet.json).

## Plano de capturas
Desktop com vitrine e Robux; phone portrait com botão de compra largo e teclado fechado; confirmação de Fichas em todas as plataformas; prompt nativo de Robux (captura real só no cliente com conta de teste — nunca simular o prompt); saldo insuficiente; possuído; falha; sucesso; console com foco em Cancelar.

## Decisões rejeitadas
- **Grade única sem vitrine** — o carro é o herói; preview 3D muda a decisão de compra.
- **Compra de um toque no card** — risco crítico; sempre vitrine/confirmação.
- **Roleta de "carro misterioso"** — fora do escopo e conflita com o pilar "preço sempre explícito".

## Pendências reais
- [aprovação humana] foco inicial em Cancelar.
- Produtos, preços e IDs de game pass/developer product não existem (fictícios).
- Nenhuma captura; assets não produzidos.
- Revisar requisitos atuais da Roblox para compras e transparência de preços antes de publicar (não verificados neste pacote).
