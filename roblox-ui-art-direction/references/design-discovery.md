# Design Discovery → Design Brief

Objetivo: entender **este** jogo antes de desenhar qualquer pixel. Saída: `design-brief.md`
preenchido (ver `templates/design-brief.md`), salvo no repositório do jogo (sugestão:
`docs/ui/design-brief.md`) — nunca dentro da pasta da skill.

## 1. Fontes de evidência (nessa ordem)

1. **Pedido e referências do usuário** — imagens, links, adjetivos, jogos citados.
2. **Documentação do projeto** — README, GDD, AGENTS.md, specs, `docs/`.
3. **DataModel / código** — `StarterGui`, `ReplicatedStorage/UI`, módulos `Theme`/`Style`,
   fontes (`Font`/`FontFace`), cores repetidas, `rbxassetid` em uso, `ImageRect*`,
   `SliceCenter`, tweens existentes. Ferramentas úteis se houver Studio MCP:
   `search_game_tree`, `inspect_instance`, `script_grep "rbxassetid|FontFace|Color3"`.
4. **Mundo 3D** — materiais, paleta do mapa, iluminação, tom dos personagens: a UI deve
   pertencer a esse mundo. Uma captura do jogo vale mais que suposições.
5. **Assets existentes** — pastas de imagens, decals, ícones já enviados (anotar IDs reais).

## 2. Perguntas do brief

| Campo | O que descobrir | Impacto visual |
|---|---|---|
| Gênero / loop | o que o jogador faz 90% do tempo | densidade do HUD, o que é primário |
| Público | idade, plataforma dominante, idioma | tamanho de texto, alvos de toque, legibilidade |
| Temática / mundo | época, materiais, cultura visual | molduras, ornamentos, iconografia |
| Tom emocional | divertido, tenso, épico, calmo, sombrio | saturação, contraste, motion |
| Estilo visual | cartoon, pintado, flat, low-poly, realista, pixel, minimalista | tratamento das imagens |
| Dispositivos | % mobile/desktop/console/VR | composição base (mobile-first?) |
| Sistemas | moedas, inventário, raridades, loja, quests, mapa, social | quais telas e componentes |
| UI existente | o que fica, o que muda, o que é legado | escopo do redesign |
| Restrições | budget de memória, prazo, ferramentas, não pode mudar X | estratégia de assets |
| Assets disponíveis | ícones, fontes, logos, IDs reais | o que precisa ser produzido |
| Convenções | Rojo? Knit? React-lua/Fusion? Instâncias autorais? | estratégia de implementação |

## 3. Quando perguntar e quando seguir

Pergunte **apenas** quando a resposta muda a direção de forma cara de reverter, por exemplo:
- Nenhuma evidência de estilo e dois caminhos opostos plausíveis (ex.: "terror realista" vs
  "terror cartoon").
- Público infantil vs adulto altera conteúdo/legibilidade e não há pista.
- Existe UI e não está claro se é para preservar ou substituir.

Não pergunte sobre o que tem default razoável (escala de espaçamento, easing, nomes de
pastas). Quando houver contexto suficiente: **proponha** a direção no brief, marque
suposições como `Suposição:` e prossiga.

## 4. Anti-vieses

- Não presuma que todo jogo Roblox é "simulator colorido com botões gordos".
- Não transporte a paleta/estilo do último projeto trabalhado.
- Não confunda "popular no Roblox" com "certo para este jogo".
- Gênero não define estilo: um tycoon pode ser minimalista; um horror pode ser fofo.

## 5. Saída mínima aceitável

Brief com: identidade em 1 frase, 3–5 pilares visuais, público/dispositivos, lista de telas
no escopo, assets existentes (com IDs reais ou "nenhum"), restrições, suposições e perguntas
abertas (se houver).
