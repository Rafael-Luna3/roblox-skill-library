# Caso documental 2 — HUD de partida

> Jogo **fictício** "Signal Breach" (PvP 5v5 de captura de pontos, sci-fi minimalista).
> Nenhuma captura, asset ou AssetId existe. QA visual: **pendente — sem captura**.

## Contexto
Rodadas de 4 min, 3 pontos de captura, 2 habilidades + arma, vida/escudo, munição.
45% desktop, 40% mobile, 15% console.

## 12 perguntas (resumo)

| # | Resposta | Evidência |
|---|---|---|
| 1 | agir + acompanhar | — |
| 2 | combate ativo | — |
| 3 | sim: vida, escudo, munição, cooldowns, timer, placar, objetivo | — |
| 4 | segundos, contínuo | — |
| 5 | ~10 elementos fixos; feed de eliminações cresce (limitar) | — |
| 6 | não | — |
| 7 | não | — |
| 8 | alto: informação oculta custa a partida | — |
| 9 | desktop, ultrawide, phone landscape, tablet, console; mouse/teclado, touch, gamepad | — |
| 10 | centro/visada livre; joystick (esq.), jump e tiro (dir.), topbar | official (OF-06, OF-01) |
| 11 | fase A | — |
| 12 | pré-rodada, cooldown, sem munição, capturando, perdendo ponto, eliminado/espectador, fim de rodada, fundo claro/escuro | — |

## Alternativas

| Alternativa | Candidata porque | Trade-offs | Mobile | Gamepad | QA | Resultado |
|---|---|---|---|---|---|---|
| `match.overlay` (cantos + topo) | ação em segundos, centro livre | cantos disputados no mobile | reagrupar ações perto do jump | glifos, sem foco de GUI | matriz de fundos e estados | **escolhida** |
| Barra superior única + ações inferiores | simples para casual | objetivos de 3 pontos não cabem bem numa barra única com placar e timer em phone | ok | ok | simples | rejeitada: densidade do objetivo |
| HUD mínimo/diegético | imersão | jogo competitivo precisa de estado explícito | — | — | difícil | rejeitada: risco (8) |

## Decisão
`match.overlay`. Objetivo/placar/timer no **topo-centro** (decisivos para vencer — `official` OF-13);
status do jogador inferior-esquerdo (desktop) / superior-esquerdo (mobile, acima do joystick);
ações inferior-direito. **[aprovação humana]**: feed de eliminações à direita vs esquerda.

## Plano por plataforma

### Phone landscape (primeiro)
```text
[❤ 80 ▓▓▓ 🛡 40]        [⏱1:42 · A● B○ C◐ · 2×1]         [≡]
                     (centro: só retícula)
(joystick)                                   [Hab1 ◔4s][Hab2]
                                                [Tiro][Jump]
```
Ações posicionadas relativas ao jump (`official` OF-06); nenhum elemento sob joystick/jump.

### Gamepad/TV
Glifos RB/LB/Y nas habilidades; sem `SelectedObject` durante a partida; Start abre menu (camada Modal).
Texto do topo dimensionado para 8–10 ft (`official` OF-10); TV-safe.

### Desktop / ultrawide
Cantos da área 16:9 central limitados por `UISizeConstraint`/container central em ultrawide.
Teclas Q/E/F exibidas só com `PreferredInput = KeyboardAndMouse`.

**Camadas:** `GameplayHUD` (medidores em DeviceSafeInsets se só leitura; ações em CoreUISafeInsets),
`CriticalOverlay` para eliminado/fim de rodada.

## Estados
pré-rodada (overlay mínimo + "Aguardando 7/10") · cooldown (número + radial) · sem munição (texto + ícone) ·
capturando (barra no topo, não no centro) · eliminado (OutState + timer de respawn + espectador) ·
fim de rodada (`match.results-spectate-respawn`) · error (perda de sync: indicador discreto) ·
overflow (feed limitado a 4 linhas).

## Visual (módulos existentes)
Maioria nativa (barras, números, timers); ícones de habilidade em atlas tintável; colchetes de canto
como imagem (como em `examples/sci-fi-hud.md`). Contraste com placa translúcida contra fundo claro.

## Checklist de QA (plano)
- [ ] Centro livre em todas as resoluções
- [ ] Phone landscape: nada sob joystick/jump/notch
- [ ] Ultrawide: HUD não vai para os extremos
- [ ] Contraste sobre céu claro, interior escuro e explosões
- [ ] Todos os estados acima capturados nos 3 inputs — **pendentes**

## Memória (registro simulado)
LM-signal-20261022-01 · nível 1 · `match.overlay` · rejeitadas: barra única, diegético ·
confiança `official` (posições do objetivo) + `heuristic` (resto) · decisão humana: pendente (feed).
