# Teste de generalização A — Cartoon Arcade

> Brief **simulado** ("Bloop Brawl", jogo fictício) para validar a skill. Nenhum asset foi
> gerado; nenhum AssetId existe. Manifest correspondente: `cartoon-arcade.asset-manifest.json`.

## 1. Design brief (resumo)
- **Identidade:** "Arena de festa caótica onde tudo parece brinquedo de plástico injetado e adesivo de vinil."
- **Gênero/loop:** party-arcade PvP de rodadas de 2 min; entre rodadas abre baús e equipa chapéus.
- **Público:** 8–14 anos; ~70% mobile. **Tom:** eufórico, bobo, generoso.
- **Mundo 3D:** low-poly arredondado, cores saturadas, luz de dia forte.
- **Pilares:** (1) *Brinquedo* → volumes gordos, bevel pintado, contorno escuro grosso;
  (2) *Adesivo* → ícones com borda branca recortada; (3) *Generoso* → recompensas grandes e
  barulhentas; (4) *Legível de longe* → números enormes com contorno.
- **Não é:** minimalista, escuro, translúcido, neon, realista.

## 2. Theme profile (essencial)
| Token | Valor |
|---|---|
| surface.base | `#2E1A5C` (roxo profundo de fundo de overlay) |
| surface.panel | arte (plástico creme `#FFF4E0`) |
| action.primary | `#FFB800` amarelo-brinquedo · action.secondary `#29C5F6` |
| state.success / danger | `#4CD964` / `#FF4D5E` |
| text.primary / onAction | `#2B1B47` / `#2B1B47` com contorno branco 3px |
| Fontes | Display `Enum.Font.LuckiestGuy` · Body/Numeric `Enum.Font.FredokaOne` |
| Espaçamento | 8 / 12 / 16 / 24 / 32 (mais generoso) |
| Forma | cantos muito arredondados (pintados na arte), contorno 4–6px escuro |
| Motion | elástica: `Back Out` 0.18s (botões), 0.28s (painéis); recompensas com overshoot |
| Raridades (decisão do jogo) | 4: Comum cinza-azul, Raro azul, Épico roxo, Lendário dourado + estrelas 1–4 (indicador não-cromático) |
| Style anchor | "ilustração cartoon de brinquedo de plástico, cel-shading 2 tons, contorno marrom-escuro 6px, luz superior esquerda, highlight branco brilhante, sem texto, fundo transparente" |

## 3. Decisões Image vs Native (tela: Abrir Baú + Inventário de Chapéus)
| Elemento | Estratégia | Asset | Justificativa |
|---|---|---|---|
| Painel do inventário | C | `panel.toy.default` | plástico com bevel pintado — impossível bonito com Frames |
| Botões primário/secundário | C | `button.toy.base` (tintável) | 1 arte branca recolorida via `ImageColor3`; texto nativo |
| Baú fechado/aberto | B | `illus.chest.closed`/`open` | ilustração herói da recompensa |
| Explosão de brilho atrás do baú | E | `fx.burst.sheet` (spritesheet 4×4) | flipbook via `ImageRectOffset` |
| Células de chapéu | C | `frame.card.rarity` (tintável) + ícone | moldura nine-slice tingida pela raridade + estrelas |
| Ícones de chapéu | B (atlas) | `atlas.hats` | 32 ícones carregados juntos |
| Moeda + contador | B + A | `icon.currency.coin` | ícone adesivo; número nativo com UIStroke |
| Abas (Chapéus/Emotes) | A | — | pílulas nativas `UICorner`+`UIStroke` grosso; formas simples |
| Preview do chapéu equipado | D | — | `ViewportFrame` só no painel de detalhe |
| Barra de XP | A | — | fill nativo amarelo + `UIStroke` escuro |

## 4. Lista de assets (8 texturas para a tela inteira)
`panel.toy.default` (512², 9-slice [96,96,416,416]) · `button.toy.base` (256×128, 9-slice) ·
`frame.card.rarity` (256², 9-slice, tintável) · `illus.chest.closed` / `illus.chest.open` (512²) ·
`fx.burst.sheet` (1024², 4×4 células 256) · `atlas.hats` (1024², 8×8 de 128) ·
`icon.currency.coin` (256²). Todos `status: prompt-ready`, `robloxAssetId: null`.

Prompt exemplo (`button.toy.base`): *"<anchor>. Botão retangular de plástico branco-
acinzentado brilhante, cantos muito arredondados, bevel inferior grosso indicando
profundidade, highlight superior. Uso: nine-slice horizontal; cantos autocontidos em 48px;
miolo liso. Vista frontal, 256x128. Evitar: texto, ícones, cor (será tingido)."*

## 5. Especificação da tela — "Baú aberto"
- Overlay `surface.base` 35% transparência; baú centralizado (40% da altura); burst atrás.
- Sequência: baú treme (3×, 0.06s) → abre (troca de imagem + burst 12 fps) → card do chapéu
  escala 0→1.1→1 com cor da raridade → estrelas aparecem uma a uma → botões "Equipar"
  (primário) e "Continuar" (secundário).
- Toque em qualquer ponto pula para o estado final. Reduced motion: aparece direto com fade.
- Narrow (mobile paisagem): card e botões lado a lado; wide: empilhados abaixo do baú.

## 6. Estratégia de implementação
`ReplicatedStorage/UI/Theme` com tokens acima e `Theme.Image` nil até upload; componentes
`ToyButton`, `ToyPanel`, `RarityCard`, `CurrencyPill`; `ChestOpenScreen` controller.
Abrir baú: cliente pede `OpenChest` → servidor sorteia, debita e retorna resultado →
cliente só anima o resultado recebido (nunca sorteia localmente). Flipbook do burst com
`task.wait(1/12)` e cancelamento ao fechar.

## 7. QA (específico deste tema)
- Contornos grossos não serrilham em 0.35 SliceScale no celular?
- Números legíveis sobre o burst (contorno branco + sombra)?
- Raridade distinguível em escala de cinza (estrelas)?
- Burst não roda fora da tela; nenhum `PLACEHOLDER_*` na build.
- Veredito do teste documental: **pendente — sem captura** (brief simulado).
