# Teste de generalização C — Sci-Fi HUD

> Brief **simulado** ("Vector Drift", jogo fictício). Nenhum asset gerado; nenhum AssetId.
> Manifest correspondente: `sci-fi-hud.asset-manifest.json`.

## 1. Design brief (resumo)
- **Identidade:** "Interface projetada no visor do capacete de um piloto de reconhecimento."
- **Gênero/loop:** shooter/exploração espacial em 3ª pessoa; loadout entre missões.
- **Público:** 13+; 55% desktop / 30% mobile / 15% console. **Tom:** frio, preciso, calmo sob pressão.
- **Mundo 3D:** metal escovado, espaço escuro, luzes ciano e âmbar de painel.
- **Pilares:** (1) *Projeção* → elementos parecem luz sobre vidro: linhas finas, sem
  volume, sem textura material; (2) *Precisão* → grid rígido 8px, cantos chanfrados a 45°,
  tipografia monoespaçada para dados; (3) *Silêncio* → poucas cores, muito espaço negativo;
  (4) *Prioridade por cor* → ciano = informação, âmbar = atenção, vermelho = perigo.
- **Não é:** ilustrado, pintado, cartoon, ornamentado, madeira/pergaminho, bounce.

## 2. Theme profile (essencial)
| Token | Valor |
|---|---|
| surface.base | `#05080C` com 25% transparência (vidro escuro) |
| surface.panel | `#0B1520` 15% transparência + `UIStroke` 1px ciano 60% |
| text.primary / secondary | `#DDF6FF` / `#7FA6B8` |
| accent.info / attention / danger | `#3FE0FF` / `#FFB547` / `#FF4D4D` |
| Fontes | Display `Enum.Font.Michroma` · Body `Enum.Font.TitilliumWeb` (alternativa: `Enum.Font.Gotham`) · Numeric `Enum.Font.RobotoMono` |
| Forma | chanfros 45° nos cantos (imagem de canto pequena ou `UIGradient` mask), sem `UICorner` grande |
| Motion | mecânica: `Quint Out` 0.12s; entrada de painel = linha de scan 0.18s + fade; números "contam" com steps; sem overshoot |
| Raridades | **não existem** neste jogo — itens têm "classe" (Mk I–IV) exibida como texto/barras. A skill funciona sem raridade. |
| Style anchor | "ícone de UI holográfica, linhas finas 2px ciano sobre transparente, vetorial plano, sem sombras, sem textura, levemente brilhante, vista frontal, sem texto, fundo transparente" |

## 3. Decisões Image vs Native (tela: Loadout + HUD em voo)
| Elemento | Estratégia | Asset | Justificativa |
|---|---|---|---|
| Painéis | A | — | vidro = `Frame` translúcido + `UIStroke` 1px; imagem não agrega |
| Cantos chanfrados | C | `corner.bracket` (64², 1 asset rotacionado 4×) | colchetes de canto característicos; resto nativo |
| Botões | A | — | retângulo nativo + stroke; hover = preencher 15%; press = 30% |
| Ícones de armas/módulos | B (atlas monocromático) | `atlas.modules` | linhas finas tintáveis via `ImageColor3` (info/attention) |
| Retícula | B | `hud.reticle` | forma precisa; tintável |
| Barras de escudo/energia | A | — | segmentos nativos via `UIListLayout` (10 segmentos) |
| Scanline/ruído do visor | E | `fx.scanline.tile` (64² `Tile`) | 1 textura minúscula, 6% de opacidade, desligada em reduced motion |
| Radar | A + B | `hud.radar.ring` | anel em imagem; blips nativos |
| Preview do módulo | D | — | `ViewportFrame` wireframe-like (Highlight/Material ForceField) |
| Separadores e grid | A | — | `Frame` 1px |

## 4. Lista de assets (5 texturas)
`corner.bracket`, `atlas.modules` (512², 4×4 de 128, tintável), `hud.reticle` (256²),
`hud.radar.ring` (512²), `fx.scanline.tile` (64²). Identidade vem majoritariamente de
tokens nativos — resultado correto da matriz para este tema.

## 5. Especificação da tela — "Loadout"
- Wide: coluna esquerda (lista de slots: Primária, Secundária, Utilitário, Casco) · centro
  `ViewportFrame` da nave girando lentamente · direita painel de estatísticas com barras
  segmentadas e deltas (+/-) em âmbar/ciano com sinal textual.
- Narrow: lista de slots vira carrossel horizontal no topo; stats colapsam em 3 números-chave
  + "Detalhes".
- Selecionar módulo: linha de scan percorre o card (0.18s), números contam até o novo valor.
- Gamepad: D-pad navega slots; A abre lista; foco = colchetes de canto animados (expandem 4px).
- HUD em voo: tudo nas bordas, centro livre; escudo/energia inferior-esquerda **acima** do
  thumbstick no mobile; munição inferior-direita à esquerda do botão de pulo/tiro.

## 6. Estratégia de implementação
Componentes `HoloPanel` (Frame + stroke + 4 `corner.bracket`), `SegmentBar`, `StatDelta`,
`ModuleIcon` (atlas). Tema escuro com transparência: validar contraste contra o pior fundo
(planeta claro) — fallback com `surface.base` mais opaco no mobile. Equipar módulo via remote
validado; HUD só lê estado replicado.

## 7. QA (específico deste tema)
- Linhas de 1px não somem em telas de baixa densidade (usar 2px em mobile)?
- Contraste do texto sobre vidro translúcido contra o fundo mais claro do jogo?
- Informação não depende só de cor (sinais +/−, ícones de alerta)?
- Scanline desligada com reduced motion; nada ornamentado/ilustrado infiltrado.
- Veredito do teste documental: **pendente — sem captura** (brief simulado).
