# Padrão `match.overlay`

## Metadados

| Campo | Valor |
|---|---|
| ID | `match.overlay` |
| Família | HUD de gameplay |
| Arquétipo | overlay periférico e compacto |
| Problema resolvido | informar e permitir agir sob pressão de tempo (vida, stamina, habilidades, cooldowns, hotbar, timer, score, objetivos, eliminações, equipes, recursos) |
| Tarefa principal | agir + acompanhar |
| Contexto | gameplay ativo (combate, corrida, rodada) |
| Frequência | contínua |
| Urgência | muito alta |
| Risco de erro | alto (informação errada ou oculta custa a partida) |
| Itens e crescimento | 4–12 elementos fixos |
| Densidade de informação | baixa por elemento; prioridade estrita |

## Quando usar

- Qualquer partida/rodada com status e ações em tempo real.

## Quando evitar

- Inventário, loja, settings (menu seguro) — não misturar no overlay.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| HUD mínimo + informação diegética | horror/imersão (`survival.contextual`) |
| HUD por equipe (placar lateral) | modos de equipe com muitos jogadores |
| Barra superior única (status) + ações inferiores | jogos casuais/arcade com poucas ações |

## Vantagens e desvantagens

- ➕ centro livre; leitura periférica; ações próximas do polegar.
- ➖ cantos disputados com CoreGui/controles touch/chat; exige prioridade rígida.

## Wireframes

### Desktop

```text
[❤ 82  ⚡ ▓▓▓░]                         [⏱ 1:42 | Azul 3 × 2 Verm. | Objetivo: capture B]
                    (centro livre: retícula apenas)
[feed de eliminações curto]                     [Q ◔ 4s] [E ●] [F Block]
```

### Mobile

```text
landscape: status de leitura compacto no topo (dentro do safe inset);
ações agrupadas em arco ao redor/acima do jump (mão direita), sem cobrir joystick (esquerda);
timer/objetivo no topo-centro estreito.
```

### Gamepad

```text
Glifos de botão nas ações (RB, X, Y); sem foco de GUI (o controle é do personagem);
menus abrem com Start/Select e pausam/ocultam o overlay conforme o jogo.
```

## Reflow responsivo

- Âncoras nos cantos (`AnchorPoint` (0,0), (1,0), (0,1), (1,1)), tamanhos em Scale com
  `UISizeConstraint` (min toque, max ultrawide). `official` (OF-14 faz isso para medidores)
- Mobile: ações reposicionadas relativas ao jump. `official` (OF-06)
- Medidores só de leitura podem usar `DeviceSafeInsets`; ações interativas `CoreUISafeInsets`. `official`
- Ultrawide: manter elementos perto dos cantos da área 16:9 central (limite por constraint),
  não nos extremos da tela. `heuristic`

## Input e foco

- Ações com equivalentes declarados (tecla/botão/toque) e glifo do input ativo. `observed` (BM-07)
- Nenhuma ação de combate depende de hover ou cursor.
- Objetivo e placar no topo: são decisivos para vencer. `official` (OF-13)

## Estados

| Estado | Comportamento |
|---|---|
| empty | antes da rodada: overlay mínimo/"aguardando jogadores" |
| loading | elementos ocultos ou placeholders neutros até replicar estado |
| error | perda de sincronização → indicador discreto |
| disabled | habilidade em cooldown (tempo restante numérico + visual), sem recurso, silenciado |
| overflow | feed de eliminações limitado a N linhas; placar resumido |
| full | — (n/a) recurso/munição cheios mostrados no medidor |
| específicos | pausa, fim de rodada, eliminado/espectador (ver `match.results-spectate-respawn` em pattern-catalog.md) |

## Image vs Native vs Hybrid

Nativo: barras, números, timers, placar, cooldown. Imagem: ícones de habilidade (atlas), molduras
de botão temáticas, retícula. Contraste garantido sobre qualquer fundo (placa/stroke).

## Anti-padrões

- Painéis permanentes no centro; dashboard sobre a visada.
- Botões sob joystick/jump; ações essenciais sem equivalente de gamepad.
- Cooldown só por cor.
- HUD que reage a cada frame com tweens longos.

## Checklist de QA

- [ ] Centro livre em todos os viewports
- [ ] Phone landscape: nada sob controles touch/notch; polegar alcança ações
- [ ] Contraste sobre fundo claro, escuro e com efeitos
- [ ] Estados: pré-rodada, cooldown, sem recurso, pausa, fim de rodada
- [ ] Ultrawide não empurra o HUD para os extremos

## Benchmarks e confiança

OF-13 (laser tag: objetivo no topo, ScreenGuis por contexto) e OF-14 (medidores) — `official`.
BM-07 (Blade Ball, inputs verificados) — `observed`, confiança média.
