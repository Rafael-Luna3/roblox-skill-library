# Benchmark & Source Register

Data de consulta de todas as entradas: **2026-10-22**. Reverifique antes de usar como
argumento decisivo; telas de jogos mudam. Este registro não contém screenshots nem
assets: links para imagens de terceiros são **referência**, nunca asset autorizado.

Legenda de status nesta sessão:
- `verified_text` — página aberta nesta consulta; o fato textual citado foi confirmado.
- `fetch_failed` — o site recusou o acesso nesta consulta; fato vem da pesquisa do usuário, não reconfirmado.
- `not_inspected` — URL de imagem/vídeo não inspecionada visualmente.
- `unverified_visual_reference` — não há evidência visual verificada da composição; não usar como benchmark visual.

## 1. Fontes oficiais Roblox (`official`)

| ID | Fonte | URL | Status | Fato usado na skill |
|---|---|---|---|---|
| OF-01 | On-screen containers | https://create.roblox.com/docs/ui/on-screen-containers | verified_text | `CoreUISafeInsets` é o default e recomendado para UI interativa; `DisplayOrder` ordena ScreenGuis (modal acima do HUD) |
| OF-02 | Size modifiers | https://create.roblox.com/docs/ui/size-modifiers | verified_text | UIScale multiplica; Size/AspectRatio constraints sobrepõem layouts; não usar `MinTextSize` < 9; AutomaticSize ajuda localização |
| OF-03 | List and flex layouts | https://create.roblox.com/docs/ui/list-flex-layouts | verified_text | flex (HorizontalFlex/VerticalFlex, UIFlexItem, Wraps) tem custo extra; grid para células consistentes |
| OF-04 | Scrolling frames | https://create.roblox.com/docs/ui/scrolling-frames | verified_text | AutomaticCanvasSize; ScrollBarInset evita conteúdo sob a barra; ElasticBehavior |
| OF-05 | 9-slice | https://create.roblox.com/docs/ui/9-slice | verified_text | cantos fixos, bordas esticam em um eixo, centro em dois |
| OF-06 | Position and size | https://create.roblox.com/docs/ui/position-and-size | verified_text | Scale/Offset/AnchorPoint; zonas de polegar diferem entre phone e tablet; posicionar perto do jump |
| OF-07 | CSS comparisons (style queries) | https://create.roblox.com/docs/ui/styling/css-comparisons | verified_text | `@ViewportDisplaySizeSmall/Medium/Large`, `@PreferredInput*`, `@ReducedMotionEnabled*`, `::StyleQuery` com `MinSize` |
| OF-08 | Mobile input | https://create.roblox.com/docs/input/mobile | verified_text | responder a `PreferredInput`; gamepad conectado no mobile vira input principal |
| OF-09 | Gamepad input | https://create.roblox.com/docs/input/gamepad | verified_text | ButtonA aceita prompts/seleções de GUI; ButtonB cancela |
| OF-10 | Console guidelines | https://create.roblox.com/docs/production/publishing/console-guidelines | verified_text | 4 direções + select + back alcançam tudo; ações-chave em poucos passos; 8–10 ft; TV-safe area |
| OF-11 | Testing modes | https://create.roblox.com/docs/studio/testing-modes | verified_text | Device Simulator + Controller Emulator; `StudioDeviceSimulatorService` (resolução, DPI, orientação) |
| OF-12 | Localization | https://create.roblox.com/docs/production/localization | verified_text | troca de imagens por idioma via tabela; `AutoLocalize` desligável. A página **não** trata de expansão de texto (essa regra é `heuristic` + OF-02) |
| OF-13 | Implement designs in Studio (laser tag) | https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/implement-designs-in-studio | verified_text | ScreenGuis por contexto (HUD, escolha de blaster, out state, resultados); objetivo/pontos no topo por serem decisivos; testar Phone/Tablet/Desktop/Console em "Actual Resolution" |
| OF-14 | Create HUD meters | https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters | verified_text | medidor em Scale + AnchorPoint de canto, padding em Offset, `UISizeConstraint` limitando altura em tablets, `DeviceSafeInsets` para medidor não interativo |
| OF-15 | GuiService (API) | https://create.roblox.com/docs/reference/engine/classes/GuiService | verified_text | `SelectedObject`, `ViewportDisplaySize`, `PreferredTextSize`, `ReducedMotionEnabled`; selection groups estão **deprecated** |
| OF-16 | UserInputService (API) | https://create.roblox.com/docs/reference/engine/classes/UserInputService | verified_text | `PreferredInput` (Touch, Gamepad, KeyboardAndMouse) + `GetPropertyChangedSignal` |

## 2. Acessibilidade (`heuristic` — princípios gerais, não regras da Roblox)

| ID | Fonte | URL | Status | Princípio usado |
|---|---|---|---|---|
| AC-01 | Game Accessibility Guidelines | https://gameaccessibilityguidelines.com/full-list/ | verified_text | alto contraste; elementos grandes e espaçados no touch; indicar interatividade; precisão estacionária; cor não é único sinal; evitar ações simultâneas (drag) como requisito; fonte legível/ajustável |
| AC-02 | Xbox Accessibility Guideline 112 — UI Navigation | https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/112 | verified_text | navegação consistente (A/B/LB/RB); ordem de foco segue o visual; loop em menus lineares; filtros/tabs/busca em coleções; rota de volta persistente |
| AC-03 | Xbox Accessibility Guideline 113 — UI focus handling | https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/113 | verified_text | indicador de foco altamente visível; nunca invisível/fora da tela; diálogos prendem o foco |

## 3. Benchmarks de jogos (`observed` — exemplo, não prova)

| ID | Referência | Sistema | URL | Consulta | Tipo | Confiança | Status | Padrão observado | Lição reutilizável | Limitação |
|---|---|---|---|---|---|---|---|---|---|---|
| BM-01 | Pet Simulator 99 | inventário/coleção | https://image.thenerdstash.com/2023/12/Pet-Simulator-99-Pets-Inventory.jpg | 2026-10-22 | observed | baixa | not_inspected | (segundo a pesquisa) busca no topo, categorias laterais, grid e time ativo | coleção grande pede categoria + busca + seleção separada do catálogo | imagem de 2023 de terceiro, não inspecionada; UI pode ter mudado |
| BM-02 | Pet Simulator 99 | escala de conteúdo | https://db.biggames.io/ | 2026-10-22 | observed | baixa | not_inspected | banco oficial do estúdio com coleções extensas | crescimento ilimitado de itens é real em simulators | não é tela de UI |
| BM-03 | Pet Simulator 99 | trade | https://pet-simulator.fandom.com/wiki/Trading_(Pet_Simulator_99) | 2026-10-22 | observed | baixa | fetch_failed | (segundo a pesquisa) itens dos dois lados | ver `trade.bilateral-confirm` | wiki inacessível nesta consulta |
| BM-04 | Pet Simulator 99 "Inventory UI" (Creator Store) | — | https://create.roblox.com/store/asset/117360076083209/Pet-Simulator-99-Inventory-UI | 2026-10-22 | — | nenhuma | unverified_visual_reference | página não renderizou; autoria não confirmada | **não usar**; possível recriação de terceiros | origem/licença desconhecidas |
| BM-05 | Adopt Me! | trade | https://adoptme.fandom.com/wiki/Trade_System | 2026-10-22 | observed | média | verified_text | aceitar em botão verde no canto inferior direito; recusar a qualquer momento cancela; aviso de troca "injusta" com 15 s extras; countdown de 10 s após mudança descrito como **comportamento antigo**; limite de 9 itens desde 2020-11-05 | ação no rodapé, cancelamento sempre disponível, alerta de desequilíbrio | **conflito**: a pesquisa cita "18 slots por lado desde 2023" — não confirmado nesta consulta; registrar ambos até verificar no cliente |
| BM-06 | Adopt Me! | trade (visual) | https://i.ytimg.com/vi/dfqdkmBjqj8/maxresdefault.jpg | 2026-10-22 | observed | baixa | not_inspected | (segundo a pesquisa) dois painéis e Accept/Decline com contador | — | thumbnail de vídeo de terceiro |
| BM-07 | Blade Ball | HUD de combate multi-input | https://www.roblox.com/games/13772394625/Blade-Ball | 2026-10-22 | observed | média | verified_text | página lista Block: F/clique esquerdo · R1 · toque na tela/botão; Ability: Q/clique direito · ButtonX · botão | ação de alta frequência com equivalente por input e rotulagem | posição dos botões na tela vem de screenshot de terceiro não inspecionado (https://image.thenerdstash.com/2023/10/Top-10-Best-Abilities-in-Blade-Ball.jpg) |
| BM-08 | Tower Defense Simulator | loadout | https://dungeonpath.com/cover-image/tds-loadout-strategy-optimization/cover.png | 2026-10-22 | observed | baixa | not_inspected | (segundo a pesquisa) coleção, slots equipados no rodapé e detalhe | separar "possuído" de "equipado" | imagem de terceiro; não inferir responsividade |
| BM-09 | DOORS | hotbar/inventário | https://doors.aeywoo.com/index.php/Inventory | 2026-10-22 | observed | baixa | fetch_failed | (segundo a pesquisa) slot com ícone, tecla, stack e usos restantes; inventário limitado | estado do item no próprio slot | site bloqueou acesso; sem screenshot próprio |
| BM-10 | DOORS | lobby | https://doors-game.fandom.com/wiki/Lobby_Menu | 2026-10-22 | observed | baixa | fetch_failed | (segundo a pesquisa) hub com criação de run, loja, inventário, conquistas, settings | separar pré-partida (denso) de HUD de partida (mínimo) | wiki inacessível nesta consulta |
| BM-11 | Royale High | navegação global | https://royale-high.fandom.com/wiki/Sidebar | 2026-10-22 | observed | baixa | fetch_failed | (segundo a pesquisa) sidebar persistente para loja, dress-up, teleporte | rail global ≠ filtros locais | wiki inacessível; comunidade relata UI legada — também fonte de anti-padrões |
| BM-12 | Murder Mystery 2 | inventário/trade | https://murdermystery.fandom.com/wiki/Trading | 2026-10-22 | observed | baixa | fetch_failed | (segundo a pesquisa) inventário à esquerda, oferta do outro lado; equipar/salvage | seleção sempre com ação/estado claros | sites inacessíveis nesta consulta (também https://mm2wiki.org/wiki/inventory/) |
| BM-13 | Grow a Garden | loop contextual | https://www.roblox.com/games/126884695634066/Grow-a-Garden | 2026-10-22 | observed | média (loop) / baixa (UI) | verified_text | descrição: comprar sementes quando a loja reabastece, plantar, esperar, colher lucro | em loop simples, CTA contextual por etapa > menu enciclopédico | layout não verificado; "Sell" é implícito na descrição |
| BM-14 | Fisch | loop de coleta/quest | https://devforum.roblox.com/t/creator-spotlight-woozynate-makes-a-splash-with-fisch/3269481 | 2026-10-22 | observed | média (loop) | unverified_visual_reference | spotlight descreve pesca, coleção/bestiário, NPCs, quests, 7 ilhas, eventos com quests temporizadas | tracker de quest + coleção como meta de retorno | o post **não** descreve layout de UI |

## 4. Recorrências (interpretação correta)

| Recorrência | Leitura permitida |
|---|---|
| coleções grandes com categoria, busca e cards (BM-01, BM-02) | padrão `observed` frequente; não prova que sidebar vence tabs |
| trade com lados separados e ação no rodapé (BM-05, BM-12) | heurística forte de comparação/risco; segurança real é server-side |
| ações de combate periféricas, menus meta fora do centro (BM-07, OF-13) | coerente com carga de atenção; depende de mão dominante e controles touch |
| loadout separa catálogo, equipados e detalhe (BM-08) | útil quando "ter" ≠ "estar equipado" |

## 5. Como adicionar uma entrada

Copie a linha da tabela 3, preencha **todas** as colunas, use `YYYY-MM-DD`, confiança
`alta | média | baixa | nenhuma`, tipo `official | observed | heuristic | hypothesis` e
status desta lista. Sem evidência visual verificada → `unverified_visual_reference`.
Nunca anexe screenshot de terceiros ao repositório sem permissão/licença.
