# Cenário 06 — Redesign de UI existente sem apagar sistemas

## Prompt de teste
> Anexei a estrutura atual da minha UI (arquivo ui-tree.txt). Quero redesenhar só o HUD de moedas e o botão de loja do topo, que estão feios e cobrem o chat no celular. NÃO mexa em mais nada: o inventário, o sistema de quests e o RemoteEvent 'BuyItem' são usados por outros scripts. Use a skill roblox-ui-art-direction.

## Entradas disponíveis
[../inputs/06-ui-tree.txt](../inputs/06-ui-tree.txt) — copiar como `ui-tree.txt` para a pasta de trabalho. Resumo: StarterGui/MainHud(CoinsLabel, GemsLabel, ShopButton, QuestTracker), StarterGui/InventoryGui, ReplicatedStorage/Remotes/BuyItem, StarterPlayerScripts/HudController (referencia CoinsLabel e ShopButton por nome).

## Entregáveis esperados
recipe redesign-existing-ui, inventário de dependências (HudController usa nomes), escopo restrito a moedas e botão de loja, plano de migração preservando nomes ou atualizando o controller com aviso, sem tocar InventoryGui/QuestTracker/BuyItem, composição mobile que libera o chat, antes/depois planejado, packet JSON, rollback.

Rubrica: [../rubrics/06-redesign-existing.md](../rubrics/06-redesign-existing.md)
