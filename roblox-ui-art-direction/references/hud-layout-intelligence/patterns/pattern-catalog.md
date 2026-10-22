# Catálogo de padrões complementares (fichas compactas)

Fichas resumidas das demais famílias. Todas têm os mesmos campos das fichas completas,
em forma condensada. Ao usar uma delas num projeto, expanda-a com
`templates/layout-pattern.md` e registre a decisão. Evidência: salvo indicação, a
disposição é `heuristic`; nenhuma tem benchmark visual verificado nesta versão.

Legenda de campos: **Fam** família/arquétipo · **Prob** problema/tarefa ·
**Ctx** contexto, frequência, urgência, risco, itens/crescimento, densidade ·
**Usar/Evitar** · **Alt** alternativas · **±** vantagens/desvantagens ·
**D/M/G** wireframes desktop/mobile/gamepad · **Reflow** · **Input** ·
**Estados** empty/loading/error/disabled/overflow/full · **Img** imagem/nativo/híbrido ·
**Anti** anti-padrões · **QA** · **Bench** benchmarks/confiança.

---

### `progression.upgrade-craft-tree`
- **Fam:** progressão — árvore/lista de upgrades, crafting e skill tree com painel de detalhe.
- **Prob:** entender pré-requisitos, custo e efeito antes de investir. Tarefa: comparar → confirmar.
- **Ctx:** menu seguro · média · baixa · médio–alto (gasto irreversível) · 10–100 nós · alta.
- **Usar:** dependências reais entre nós; receitas com ingredientes. **Evitar:** upgrades lineares simples (lista basta).
- **Alt:** lista linear de upgrades; grade de receitas + detalhe; árvore em canvas.
- **±:** visualiza dependência / canvas arrastável é hostil a gamepad e mobile.
- **D:** `[árvore em canvas] | [detalhe: efeito, custo, requisitos, Desbloquear]` · **M:** `lista por tier → toque → sheet` · **G:** D-pad salta entre nós vizinhos; A desbloqueia; B volta.
- **Reflow:** canvas no desktop; no mobile, lista agrupada por tier mantendo os requisitos em texto.
- **Input:** sempre há rota navegável sem drag (lista ou nós focáveis); zoom é extra.
- **Estados:** empty (sem receitas) · loading · error (falha ao craftar, itens preservados) · disabled (requisito/ingrediente faltando, com o que falta) · overflow (scroll/filtro por tier) · full (inventário cheio para o resultado).
- **Img:** ícones de nó/ingredientes em imagem; linhas, custos e textos nativos.
- **Anti:** mapa arrastável sem alternativa; custo só no hover; consumir ingredientes no cliente.
- **QA:** desbloquear via 3 inputs; requisitos legíveis; confirmação proporcional ao custo.
- **Bench:** nenhum verificado; AC-02 (alternativa não rolável a mapas/árvores) `heuristic`.

### `nav.global-rail`
- **Fam:** navegação — rail/sidebar global persistente + tabs/filtros locais.
- **Prob:** chegar rápido a seções principais (loja, inventário, teleporte, eventos) sem menus profundos.
- **Ctx:** hub/lobby/mundo social · alta · baixa · baixo · 4–8 destinos · baixa.
- **Usar:** muitos destinos globais acessados com frequência. **Evitar:** jogo com 1–2 menus; partidas de combate.
- **Alt:** botão de menu único → grade de destinos; barra inferior (mobile); hub físico no mundo.
- **±:** reduz profundidade / ocupa borda permanente; pode virar "parede de botões".
- **D:** `rail vertical à esquerda com ícone + rótulo curto` · **M:** `rail compacto só ícones + rótulo no toque longo, ou barra inferior se não colidir com controles` · **G:** botão dedicado foca o rail; ↑/↓ navega; A abre; B devolve ao jogo.
- **Reflow:** rail com rótulos → só ícones (com rótulo acessível) → menu "⋯" em telas pequenas.
- **Input:** rail global ≠ tabs locais: tabs/filtros ficam dentro da tela aberta (`observed` BM-11, baixa).
- **Estados:** empty n/a · loading (badges) · error (destino indisponível) · disabled (destino bloqueado com motivo) · overflow (agrupar em "⋯") · full n/a.
- **Img:** ícones em imagem com rótulos nativos; badges nativos.
- **Anti:** rail com 15 ícones sem rótulo; mesma função em rail e tab com nomes diferentes.
- **QA:** rótulos traduzidos; não colide com chat/topbar; acessível por gamepad.
- **Bench:** BM-11 (Royale High) `observed`, baixa, fetch_failed.

### `nav.main-menu`
- **Fam:** navegação — menu principal/título com CTA dominante.
- **Prob:** entrar no jogo rapidamente e achar opções secundárias. Tarefa: decidir/iniciar.
- **Ctx:** pré-jogo · 1×/sessão · baixa · baixo · 3–7 opções · baixa.
- **Usar:** jogos com modos/seleção antes de jogar. **Evitar:** jogos que devem começar instantaneamente (spawn direto é melhor).
- **Alt:** spawn direto + menu de pausa; lobby físico.
- **±:** clareza / atrito extra antes de jogar.
- **D:** `logo · [JOGAR] grande · Modos · Loja · Config` · **M:** `mesma ordem, botões largos, CTA ao alcance do polegar` · **G:** foco inicial em JOGAR; ↑/↓; A; B sem efeito ou sair com confirmação.
- **Reflow:** coluna central com `UISizeConstraint`; arte de fundo `Crop`.
- **Input:** foco inicial obrigatório no gamepad.
- **Estados:** loading (dados do jogador) · error (offline/servidor) · disabled (modo bloqueado com motivo) · empty/overflow/full n/a.
- **Img:** logo/arte de fundo em imagem; botões híbridos; texto nativo.
- **Anti:** menu que esconde o CTA; vídeo/animação longa sem skip.
- **QA:** tempo até jogar; foco; reduced motion.
- **Bench:** nenhum.

### `lobby.party-matchmaking`
- **Fam:** social — estado da party + CTA primário + requisitos/contador.
- **Prob:** preparar grupo e iniciar partida sabendo o que bloqueia. Tarefa: coordenar → iniciar.
- **Ctx:** pré-partida · média · média · médio · 1–N membros · média.
- **Usar:** modos com grupos/fila. **Evitar:** jogo solo sem fila.
- **Alt:** lobby físico no mundo; bottom sheet em mobile.
- **±:** transparência de estado / mais estados de rede.
- **D:** `[membros com status Pronto] | [modo, mapa] | [Procurar partida · ⏱ 0:42]` · **M:** `lista de membros compacta + CTA fixo no rodapé (fora dos controles)` · **G:** A pronto/cancelar; X convidar; B sair da fila com confirmação.
- **Reflow:** membros em lista vertical; CTA sempre visível.
- **Input:** quem está pronto e o que bloqueia o início sempre explícitos.
- **Estados:** empty (sozinho → convidar) · loading (procurando) · error (fila falhou) · disabled (requisito de nível) · overflow (party cheia) · full (lobby cheio).
- **Img:** avatares (thumbnails), molduras; status nativos.
- **Anti:** esconder quem não está pronto; CTA que muda de lugar.
- **QA:** entrar/sair da fila; membro desconecta; timer.
- **Bench:** BM-10 (DOORS lobby) `observed`, baixa.

### `map.minimap-fullmap`
- **Fam:** navegação espacial — minimapa no HUD + mapa completo com alternativa em lista.
- **Prob:** orientar-se e escolher destino. Tarefa: acompanhar/navegar.
- **Ctx:** exploração · contínua (mini) / ocasional (full) · média · baixo · 5–100 pontos · média.
- **Usar:** mundo grande, ilhas, teleportes. **Evitar:** mapas pequenos/lineares (obby).
- **Alt:** bússola no topo; waypoints no mundo; lista de teleportes.
- **±:** orientação / custo de render e espaço.
- **D:** `minimapa canto superior; mapa full em menu com legenda + lista de POIs` · **M:** `minimapa menor ou bússola; mapa full em tela cheia com lista` · **G:** lista de POIs focável que move o mapa; A teleporta/marca; B volta.
- **Reflow:** minimapa com `UIAspectRatioConstraint` 1:1 e `UISizeConstraint`.
- **Input:** alternativa não rolável (lista de POIs) ao mapa arrastável. `heuristic` (AC-02)
- **Estados:** loading (tiles) · error · disabled (área bloqueada) · overflow (filtros de POI) · empty/full n/a.
- **Img:** arte do mapa em imagem (sem rótulos embutidos); marcadores e rótulos nativos.
- **Anti:** nomes de locais pintados na imagem; mapa só por drag/zoom.
- **QA:** localização dos nomes; navegação por controle via lista.
- **Bench:** BM-14 (Fisch, ilhas) só loop, unverified_visual_reference.

### `onboarding.tutorial-steps`
- **Fam:** onboarding — passos curtos contextuais com destaque do alvo.
- **Prob:** ensinar o loop sem bloquear. Tarefa: aprender fazendo.
- **Ctx:** primeira sessão · 1× · média · baixo · 3–10 passos · baixa.
- **Usar:** mecânicas não óbvias. **Evitar:** paredes de texto antes de jogar.
- **Alt:** tracker de quest de tutorial (`quest.tracker-expand`); dicas contextuais únicas.
- **±:** aprendizado guiado / irritação se não puder pular.
- **D:** `dica curta perto do elemento + seta; [Pular]` · **M:** `dica sem cobrir o alvo nem os controles` · **G:** dicas com glifo do input; A continua; pular acessível.
- **Reflow:** dica ancorada ao elemento-alvo, reposiciona se não couber.
- **Input:** instruções mudam conforme `PreferredInput`.
- **Estados:** loading n/a · error (passo impossível → pular) · disabled · empty/overflow/full n/a.
- **Img:** ilustrações opcionais; texto nativo localizável.
- **Anti:** tutorial que bloqueia sem skip; instrução de teclado para jogador de touch.
- **QA:** três inputs; skip; retomar.
- **Bench:** nenhum.

### `dialog.npc-choices`
- **Fam:** narrativa — caixa de diálogo inferior + escolhas.
- **Prob:** ler falas e escolher respostas. Tarefa: ler/decidir.
- **Ctx:** exploração (pode pausar) · média · baixa · médio (escolhas com consequência) · 1–4 escolhas · média.
- **Usar:** NPCs, quests. **Evitar:** mensagens de sistema (use toast).
- **Alt:** balão no mundo (BillboardGui); diálogo em tela cheia para cenas.
- **±:** leitura confortável / cobre parte inferior (controles touch).
- **D:** `[retrato] [nome · texto]` + `[1. resposta] [2. resposta]` · **M:** caixa acima dos controles touch ou controles ocultos durante o diálogo · **G:** foco na primeira resposta; A escolhe; B avança/fecha conforme regra.
- **Reflow:** caixa com `AutomaticSize` Y e máximo; escolhas empilhadas.
- **Input:** avançar com toque/A/clique; texto completo antes de escolher.
- **Estados:** loading n/a · error n/a · disabled (escolha bloqueada com requisito) · overflow (texto longo pagina) · empty/full n/a.
- **Img:** retrato/moldura em imagem; texto nativo.
- **Anti:** texto em imagem; escolha sem indicar consequência irreversível.
- **QA:** idioma longo; leitura a distância (TV).
- **Bench:** nenhum.

### `rank.leaderboard`
- **Fam:** social — tabela classificada com destaque do próprio jogador.
- **Prob:** comparar posição. Tarefa: acompanhar.
- **Ctx:** lobby/menu ou in-match resumido · média · baixa · baixo · 10–100 linhas · média.
- **Usar:** competição. **Evitar:** in-match permanente grande (use resumo).
- **Alt:** playerlist padrão do Roblox; top-3 + "você".
- **±:** motivação / pode expor jogadores (privacidade/moderação).
- **D:** `tabela com colunas fixas; linha do jogador fixa no rodapé` · **M:** colunas essenciais + detalhe por toque · **G:** foco salta para "você"; ↑/↓ rola.
- **Reflow:** reduzir colunas; nomes truncados com nome completo no detalhe.
- **Input:** ordenar por coluna opcional.
- **Estados:** empty (sem dados) · loading · error · overflow (scroll/paginação) · disabled/full n/a.
- **Img:** medalhas top-3 em imagem; dados nativos.
- **Anti:** números em imagem; tabela que cobre gameplay.
- **QA:** nomes longos; 100+ linhas; foco.
- **Bench:** nenhum verificado.

### `match.results-spectate-respawn`
- **Fam:** fim de rodada — overlay centrado com resultado → causa → próximo passo; spectate lateral.
- **Prob:** entender o desfecho e o que acontece agora. Tarefa: entender/decidir.
- **Ctx:** fim de rodada/morte · por rodada · média · baixo · 1–10 dados · média.
- **Usar:** partidas, mortes com respawn/espectador. **Evitar:** jogos sem rodada.
- **Alt:** painel lateral em spectate; toast de respawn.
- **±:** clareza / interrompe se longo demais.
- **D:** `VITÓRIA · causa/estatísticas · [Jogar de novo] [Lobby]`; spectate: `nome do observado · ◀ ▶ · tempo para respawn` · **M:** mesmo, CTA no polegar · **G:** foco em "Jogar de novo"; LB/RB troca espectado; B mostra opções.
- **Reflow:** overlay com `UISizeConstraint`; estatísticas colapsáveis.
- **Input:** nunca tirar o jogador do jogo sem explicar o retorno (timer/botão).
- **Estados:** loading (resultados) · error · disabled (botão até servidor liberar) · empty/overflow/full n/a.
- **Img:** banner de vitória/derrota sem texto embutido; dados nativos.
- **Anti:** resultado só por animação; timer de respawn invisível.
- **QA:** vitória/derrota/empate; reduced motion.
- **Bench:** OF-13 (RoundResultsGui/OutStateGui como ScreenGuis próprios) `official`.

### `social.notification-stack`
- **Fam:** feedback — pilha de notificações/toasts com prioridade.
- **Prob:** avisar sem interromper. Tarefa: perceber.
- **Ctx:** qualquer · variável · variável · baixo · fila ilimitada · baixa.
- **Usar:** convites, conquistas, eventos. **Evitar:** erros que exigem ação (use modal/inline).
- **Alt:** central de notificações com badge; inline no elemento afetado.
- **±:** não bloqueia / se acumular vira ruído.
- **D:** `pilha no canto superior direito, máx. 3` · **M:** 1 por vez no topo, dentro do safe inset · **G:** toast com ação mostra glifo; não rouba foco.
- **Reflow:** largura com `UISizeConstraint`; texto com wrap.
- **Input:** ação opcional com atalho; nunca roubar `SelectedObject`.
- **Estados:** empty (sem notificações) · overflow (fila + "+N") · loading/error/disabled/full n/a.
- **Img:** ícones de tipo; texto nativo.
- **Anti:** toasts empilhando infinitamente; toast cobrindo CTA.
- **QA:** rajada de 10 notificações; idioma longo.
- **Bench:** nenhum.

### `event.live-hub`
- **Fam:** eventos — hub temporário com timer, tarefas e recompensas.
- **Prob:** entender o evento e o tempo restante. Tarefa: acompanhar/resgatar.
- **Ctx:** menu seguro + tracker · sazonal · baixa · baixo · 3–20 tarefas · média.
- **Usar:** eventos temporários. **Evitar:** pop-up obrigatório a cada entrada.
- **Alt:** aba no menu existente + `quest.tracker-expand`.
- **±:** visibilidade / poluição se competir com o loop principal.
- **D:** `banner + timer · tarefas · trilha de recompensas` · **M:** abas Tarefas/Recompensas · **G:** LB/RB entre abas.
- **Reflow:** reaproveitar `reward.track-reveal` e `quest.tracker-expand`.
- **Input:** fechar sempre disponível.
- **Estados:** empty (evento encerrado) · loading · error · disabled (tarefa bloqueada) · overflow · full n/a.
- **Img:** banner temático sem texto embutido; timer nativo.
- **Anti:** timer falso; texto do evento em imagem.
- **QA:** fim do evento durante a sessão; fuso horário do timer.
- **Bench:** BM-14 (quests temporizadas de evento) `observed`, sem visual.

### `obby.progress-checkpoint`
- **Fam:** obby — progresso de estágio + checkpoint + ações mínimas.
- **Prob:** saber onde está e voltar ao checkpoint. Tarefa: acompanhar/agir.
- **Ctx:** gameplay · contínua · média · baixo · 1 contador + 1–3 ações · mínima.
- **Usar:** obbies/parkour. **Evitar:** menus densos sobre a pista.
- **Alt:** barra de progresso no topo; contador simples.
- **±:** clareza / pouco espaço.
- **D:** `[Estágio 34/100] topo` · `[Pular estágio] [Reset]` lateral · **M:** ações perto do jump sem colidir · **G:** atalhos (Select = reset com confirmação).
- **Reflow:** contador compacto; ações relativas ao jump.
- **Input:** reset com confirmação ou segurar para evitar acidente.
- **Estados:** loading · disabled (pular estágio requer compra/condição) · empty/error/overflow/full n/a.
- **Img:** ícones opcionais; números nativos.
- **Anti:** botão de compra colado ao reset; HUD cobrindo a pista.
- **QA:** phone landscape com controles; reset acidental.
- **Bench:** nenhum.

### `tycoon.build-economy`
- **Fam:** tycoon/simulator — barra de recursos no topo + CTA contextual + menu de construção.
- **Prob:** acompanhar renda e decidir próxima compra. Tarefa: acompanhar → comprar.
- **Ctx:** gameplay de baixa pressão · contínua · baixa · médio · 2–5 moedas, 10–100 compras · média.
- **Usar:** loops de renda/construção. **Evitar:** encher a tela com todos os upgrades.
- **Alt:** botões físicos no mundo (padrão do gênero) + HUD só de recursos; `commerce.catalog-detail` para upgrades.
- **±:** clareza da economia / tentação de poluir o HUD.
- **D:** `[🪙 12.4K +320/s] topo` · `[próxima compra sugerida]` lateral · **M:** recursos compactos (abreviação com valor completo no toque); rail inferior se não colidir · **G:** botão abre menu de construção.
- **Reflow:** números com abreviação localizada; `AutomaticSize` X.
- **Input:** compras no mundo via ProximityPrompt + equivalente na UI.
- **Estados:** loading · disabled (saldo insuficiente com falta) · overflow (números muito grandes → abreviação) · empty/error/full conforme jogo.
- **Img:** ícones de recurso; números nativos.
- **Anti:** números enormes sem abreviação; muito texto num loop simples.
- **QA:** formatação de números 1e3–1e15; localização de separadores.
- **Bench:** BM-13 (Grow a Garden: loop comprar/plantar/colher) `observed`, UI não verificada.

### `vehicle.drive-customize`
- **Fam:** veículos — HUD de condução periférico + tela de customização com preview 3D.
- **Prob:** dirigir com informação mínima; customizar vendo o resultado. Tarefa: agir / comparar.
- **Ctx:** gameplay (HUD) · contínua; menu seguro (custom.) · alta / baixa · baixo–médio · 3–6 medidores; 10–200 peças · baixa / alta.
- **Usar:** jogos com veículos. **Evitar:** customização sobre a pista.
- **Alt:** HUD diegético (painel do carro); customização em garagem física.
- **±:** imersão / preview 3D custa render.
- **D:** HUD `velocímetro canto inferior direito; marcha/nitro` · custom. `categorias | ViewportFrame | peças + preço` · **M:** controles touch de direção têm prioridade; medidores no topo · **G:** gatilhos aceleram; customização com LB/RB por categoria.
- **Reflow:** customização segue `loadout.slot-catalog` (slots = partes do veículo).
- **Input:** controles touch de direção não podem ser cobertos.
- **Estados:** loading (modelo) · disabled (peça bloqueada) · overflow (catálogo) · error · empty/full n/a.
- **Img:** ícones de peça; `ViewportFrame` no preview; medidores nativos ou híbridos.
- **Anti:** `ViewportFrame` por peça no grid; medidores cobrindo a pista.
- **QA:** touch driving + HUD; preview em mobile.
- **Bench:** nenhum.
