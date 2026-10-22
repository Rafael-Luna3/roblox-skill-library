# Teste de generalização B — Fantasy RPG

> Brief **simulado** ("Ashen Crown", jogo fictício). Nenhum asset gerado; nenhum AssetId.
> Manifest correspondente: `fantasy-rpg.asset-manifest.json`.

## 1. Design brief (resumo)
- **Identidade:** "Um diário de cartógrafo encadernado em couro e ferro, num reino em cinzas."
- **Gênero/loop:** RPG de exploração cooperativo; masmorras, loot, equipamento, mapa-mundi.
- **Público:** 13+; 50% desktop / 40% mobile / 10% console. **Tom:** épico, melancólico, místico.
- **Mundo 3D:** pedra escura, madeira queimada, brasas laranja, névoa azulada.
- **Pilares:** (1) *Artesanal* → pergaminho, couro, ferro forjado, sem formas perfeitas;
  (2) *Peso* → bordas grossas chanfradas, sombras duras, movimento pesado;
  (3) *Luz de brasa* → o único brilho permitido é laranja-quente (magia, foco, raro);
  (4) *Leitura confortável* → corpo em serifa legível sobre pergaminho claro.
- **Não é:** cartoon saturado, neon, glassmorphism, sci-fi, pílulas arredondadas.

## 2. Theme profile (essencial)
| Token | Valor |
|---|---|
| surface.base | `#14110F` (fuligem) |
| surface.panel | arte (couro `#3A2618` com moldura de ferro) |
| surface.raised | arte (pergaminho `#E8D9B5`) |
| text.onParchment / onLeather | `#2A1D12` / `#EAD9B8` |
| action.primary | `#C8641E` brasa · action.secondary ferro `#6B6F73` |
| focus.ring | brilho de brasa `#FF9A3C` |
| Fontes | Display `Enum.Font.GrenzeGotisch` (títulos curtos) · Body `Enum.Font.Merriweather` · Numeric `Enum.Font.SourceSansSemibold` |
| Forma | cantos chanfrados/irregulares **na arte**; `UICorner` proibido em painéis |
| Motion | pesada: `Quad Out` 0.22s painéis (desliza 16px + fade), press 0.06s; sem bounce |
| Raridades (decisão do jogo) | 5: Comum, Incomum, Raro, Épico, Relíquia — moldura muda de **material** (madeira → ferro → prata → ouro → ouro com runas), não só de cor |
| Style anchor | "pintura digital estilo ilustração de livro de fantasia, texturas de couro, ferro forjado e pergaminho envelhecido, luz quente de vela vinda de cima, paleta terrosa dessaturada com acentos laranja-brasa, vista frontal ortográfica, sem texto, sem letras, fundo transparente" |

## 3. Decisões Image vs Native (tela: Inventário + Equipamento)
| Elemento | Estratégia | Asset | Justificativa |
|---|---|---|---|
| Painel raiz (livro aberto) | C | `panel.tome.frame` | couro + cantoneiras de ferro em nine-slice |
| Página de pergaminho | C | `surface.parchment.tile` | `ScaleType.Tile` 256 + bordas queimadas nine-slice |
| Header com título | C | `header.banner.iron` | faixa de ferro em imagem; título nativo localizável |
| Slots de equipamento (boneco) | C | `frame.slot.empty` + silhueta | moldura imagem; ícone de silhueta do slot |
| Molduras de raridade | B (5 variantes) | `frame.rarity.common`…`relic` | material diferente por raridade — não tingível |
| Ícones de itens | B (atlas) | `atlas.items.weapons` etc. | pintados, mesma luz |
| Divisores | B | `ornament.divider.vine` | ornamento fino |
| Botões | C | `button.iron.base` + `button.iron.pressed` | forma muda ao pressionar (afundado) → 2 texturas |
| Tooltip de atributos | A + C | `panel.tooltip.parchment` | conteúdo 100% nativo (números comparativos verde/vermelho + setas) |
| Preview do personagem equipado | D | — | `ViewportFrame` com luz quente do tema |
| Barras HP/Mana no HUD | C | `bar.frame.iron` | trilha em imagem; fill nativo |
| Mapa-mundi | B + A | `map.world.base` (1024²) | ilustração; marcadores e rótulos nativos por cima |

## 4. Lista de assets (~16 texturas)
Mais imagens que os outros cenários porque a identidade é material. Mitigação: atlas de
ícones, pergaminho em `Tile`, molduras de raridade reaproveitadas no inventário, loja e loot.

## 5. Especificação da tela — "Inventário + Equipamento"
- Wide: livro aberto — página esquerda = boneco com 8 slots + `ViewportFrame`; página
  direita = grade de itens (5 colunas) + filtros por categoria (abas como marcadores de
  fita na lateral do livro).
- Narrow: uma página por vez; abas na parte superior; toque em item abre detalhe como
  "página" sobreposta. SliceScale da moldura 0.5 → 0.3.
- Comparação ao selecionar item: tooltip pergaminho com diferenças (+12 ATQ em verde **e**
  seta ▲). Equipar → servidor valida posse e requisitos → slot pulsa com brilho de brasa.
- Gamepad: LB/RB trocam páginas/abas; foco = moldura de brasa (`SelectionImageObject`).

## 6. Estratégia de implementação
Shell autoral em `StarterGui/InventoryGui` (livro, páginas, slots nomeados por tipo:
`Slot_Head`, `Slot_MainHand`...). Células da grade de template + pool. `Theme.Image` com
tabela `RarityFrame[rarity]`. Equipar via remote validado; UI mostra *pending* (slot com
ampulheta) até resposta. Fonte gótica apenas em títulos ≤ 3 palavras.

## 7. QA (específico deste tema)
- Texto Merriweather legível sobre pergaminho no celular (contraste ≥ 4.5:1)?
- Raridades distinguíveis sem cor (material + ícone de gema)?
- Tile do pergaminho sem costura visível; nine-slice do livro sem cantos esticados?
- Nenhum efeito sci-fi/neon infiltrado; brilho só laranja.
- Veredito do teste documental: **pendente — sem captura** (brief simulado).
