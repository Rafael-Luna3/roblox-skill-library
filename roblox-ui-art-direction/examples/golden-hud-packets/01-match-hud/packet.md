# Golden packet 01 — HUD competitivo de partida

> **FICTÍCIO · documentação sem captura · veredito visual: pendente — sem captura.**
> Jogo inventado ("Ironclad Skies"). Nenhum asset gerado, nenhum AssetId, nenhum playtest.
> JSON: [packet.json](packet.json).

## Brief resumido
- **Jogo:** batalha de dirigíveis 4v4 por equipes; cada jogador pilota um dirigível com casco, vapor (boost) e 2 armas laterais; partidas de 6 min com objetivo de capturar 3 faróis.
- **Público:** 12+; 45% mobile landscape, 40% desktop, 15% console.
- **Tom:** aventureiro, mecânico, competitivo. **Pilares:** *instrumento de cabine* (medidores físicos), *leitura periférica*, *equipe antes do indivíduo*.
- **Não é:** sci-fi holográfico, cartoon saturado, painéis centrais.

## Theme profile resumido
| Token | Valor (fictício) |
|---|---|
| surface.panel | latão envelhecido em arte nine-slice; fallback `#3B2F22` + stroke `#C9A15B` |
| text.primary / onPanel | `#F3E7CF` / contorno `#1A140E` |
| team.ally / team.enemy | `#3FA7B5` + ícone âncora / `#C8553D` + ícone caveira (sinal não cromático) |
| state.danger | `#E2483B` + pulso de ponteiro (fase B) |
| Fontes | Display `Enum.Font.Oswald` (números de placar) · Body `Enum.Font.SourceSansSemibold` |
| Motion | mecânica com inércia: ponteiros com `Quad Out` 0.18 s; sem bounce |
| Style anchor | "instrumentos de latão de cabine de dirigível, ilustração pintada, vidro de mostrador, luz quente de cima, vista frontal, sem texto, fundo transparente" |

## Layout decision
| # | Resposta |
|---|---|
| 1 Tarefa | agir (pilotar/atirar) + acompanhar (casco, vapor, faróis, placar) |
| 2 Contexto | combate ativo |
| 3 Sempre visível | casco, vapor, recarga das armas, placar, timer, estado dos 3 faróis |
| 4 Urgência | segundos, contínua |
| 5 Itens | ~10 elementos fixos; feed limitado a 4 linhas |
| 6 Busca/filtro | não |
| 7 Detalhe | não |
| 8 Risco | alto para a partida (informação oculta custa rodada), sem risco econômico |
| 9 Plataformas | desktop, ultrawide, phone landscape, tablet, console; mouse/teclado, touch, gamepad |
| 10 Não cobrir | centro (mira), joystick (esq.), botões de disparo/boost (dir.), topbar |
| 11 Fase | A |
| 12 Estados | pré-rodada, carregando, desconexão, morto/respawn, farol em disputa, sem vapor, armas recarregando, fim de rodada |

**Escolhido:** `match.overlay` — tarefa de segundos + centro protegido (`official` OF-13 coloca objetivo/placar no topo; `heuristic` para o resto).
**[aprovação humana]:** medidores como mostradores circulares (identidade) vs barras horizontais (mais compactas).

## Screen spec
**Hierarquia**
1. (≤ 1 s) casco, vapor, recarga das armas.
2. (decisão) estado dos 3 faróis, placar, timer.
3. (sob demanda) feed de abates, lista da equipe (segurar Tab/Select).

**Zonas:** centro livre (só mira) · joystick esquerdo · cluster de disparo/boost direito · topbar.

**Composição**
```text
DESKTOP / TABLET / ULTRAWIDE (ultrawide: overlay limitado à área 16:9 central)
[⚓ 3 ×  2 ☠]   [◐ A ● B ○ C]   [⏱ 4:12]                     topo-centro
                      (mira)
[◔ CASCO 74%] [◑ VAPOR ▓▓░]                 [⟳ L 1.2s] [⟳ R ●]   cantos inferiores

PHONE LANDSCAPE
[⚓3×2☠ ◐A●B○C ⏱4:12]  (faixa única no topo, dentro do inset)
[◔74 ◑▓▓░] acima do joystick         [⟳L][⟳R] em arco acima de [BOOST][FIRE]

CONSOLE/TV
igual ao desktop, números +25% de tamanho; glifos LT/RT nas armas, A no boost
```
**Gatilhos de reflow:** R1 `ViewportDisplaySize == Small` → faixa única de topo; R2 altura útil < 420 px → medidores mostram só número sem rótulo; R3 largura > 21:9 → container central com `UISizeConstraint`.

**Camadas:** `MatchHudGui` GameplayHUD DO 5 (DeviceSafeInsets para medidores só leitura) · `MatchActionsGui` GameplayHUD DO 6 (CoreUISafeInsets) · `RoundEndGui` CriticalOverlay DO 50.

## Component inventory
| ID | Tipo | Função visual |
|---|---|---|
| gauge-hull | ProgressBar (Custom visual radial) | mostrador de casco com ponteiro e número |
| gauge-steam | ProgressBar | barra de vapor segmentada |
| weapon-left / weapon-right | IconButton | arma com recarga radial + glifo |
| beacon-strip | Custom | 3 faróis com dono por cor **e** ícone |
| scoreboard | Panel | placar + timer |
| killfeed | Toast | fila de 4 linhas |
| round-end | Modal | resultado → causa → próximo passo |

## State matrix
| Estado | Texto | Ação | Cor/ícone | Foco | Rede | Recovery | Captura |
|---|---|---|---|---|---|---|---|
| empty | n/a — HUD sempre tem dados na partida | — | — | — | — | — | não |
| loading | "Embarcando…" | nenhuma | medidores neutros | — | aguarda estado replicado | timeout → reconectar | sim |
| error | "Conexão instável" (ícone ⚡) | nenhuma | indicador discreto no topo | — | perda de sync | reconexão automática; HUD mantém último estado | sim |
| disabled | arma sem munição "VAZIO" | — | ícone riscado + texto | — | — | recarregar | sim |
| pending | arma recarregando "1.2s" | — | radial + número | — | — | fim da recarga | sim |
| overflow | feed > 4 abates | — | linhas antigas somem | — | — | — | sim |
| full | vapor cheio "MAX" | boost disponível | anel completo + texto | — | — | — | sim |
| beacon-contested | "B em disputa" | — | farol pisca + ícone ⚔ (fase B) | — | servidor autoritativo | — | sim |
| dead | "Abatido — volta em 5s" | espectar | overlay de borda | — | — | respawn | sim |

## Implementation handoff
```text
StarterGui
├── MatchHudGui (DO 5, DeviceSafeInsets, ResetOnSpawn=false)
│   ├── TopStrip (UIListLayout H): Score, Beacons, Timer
│   └── Gauges (AnchorPoint 0,1): Hull, Steam
├── MatchActionsGui (DO 6, CoreUISafeInsets): WeaponLeft, WeaponRight
└── RoundEndGui (DO 50, Enabled=false)
```
- Módulos: `ReplicatedStorage/UI/Theme`, `UI/Components/Gauge`, `UI/Components/WeaponSlot`, `StarterPlayerScripts/MatchHudController`.
- Dados: `{hull: number, steam: number, weapons: {cooldown: number, ammo: number}[2], beacons: {owner: "ally"|"enemy"|"none", contested: boolean}[3], score: {ally: number, enemy: number}, timeLeft: number}` — tudo replicado do servidor.
- Intenções: disparo/boost são input de gameplay (não GUI); HUD só lê estado.
- Ordem: Theme → Gauge/WeaponSlot com fallback → TopStrip/Gauges com âncoras → reflow R1–R3 → estados → dados → arte aprovada.
- Validação: `python ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py examples/golden-hud-packets/01-match-hud/packet.json`.

## Asset matrix
| Elemento | Estratégia | Asset (status) | Fallback |
|---|---|---|---|
| mostrador do casco | Hybrid | gauge.hull.face (planned) | Frame circular + número |
| moldura do placar | Hybrid (9-slice) | panel.brass.frame (planned) | Frame + UIStroke latão |
| ícones de arma | Image (atlas) | atlas.weapons (planned) | letra L/R em círculo |
| faróis | Native + ícone | icon.beacon (planned) | círculo + letra A/B/C |
| números/timer | Native | — | — |

## Packet JSON
[packet.json](packet.json) — validado por `scripts/validate_hud_packet.py`.

## Plano de capturas
Desktop 1920×1080 · ultrawide 2560×1080 · phone landscape 844×390 com controles touch visíveis · tablet 1024×768 · console 1920×1080 com Controller Emulator. Estados: loading, error, arma vazia, recarga, feed cheio, vapor cheio, farol em disputa, abatido, fim de rodada. Fundo claro (céu) e escuro (tempestade).

## Decisões rejeitadas
- **Barra única de status no topo** — no phone, placar + 3 faróis + timer + casco não cabem legíveis numa faixa.
- **HUD diegético (instrumentos no modelo 3D)** — jogo competitivo precisa de estado explícito e legível em mobile.
- **Medidores no centro inferior** — competem com a mira e com a visada de descida.

## Pendências reais
- Captura de todos os estados/plataformas (nenhuma feita).
- [aprovação humana] mostrador circular vs barra.
- Assets `gauge.hull.face`, `panel.brass.frame`, `atlas.weapons`, `icon.beacon` não produzidos.
- Regras de jogo (tempo de respawn, recarga) são fictícias neste exemplo.
