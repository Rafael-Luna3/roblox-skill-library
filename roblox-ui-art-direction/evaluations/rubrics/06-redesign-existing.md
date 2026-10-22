# Rubrica 06 — Redesign de UI existente sem apagar sistemas

Prompt: [../prompts/06-redesign-existing.md](../prompts/06-redesign-existing.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- alterar ou remover InventoryGui, QuestTracker ou BuyItem
- renomear CoinsLabel/ShopButton sem tratar HudController
- propor reescrever todo o HUD
- inventar conteúdo do ui-tree que não foi fornecido
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: sem decisão; 1: sem considerar manter o atual; 2: alternativas incluindo ajuste mínimo | |
| 2 | Responsividade (reflow real) | 0: ignora chat no mobile; 1: cita; 2: composição que libera chat com gatilho | |
| 3 | Gamepad/touch | 0: ignora; 1: parcial; 2: touch e gamepad para o botão de loja | |
| 4 | Identidade visual | 0: genérico; 1: raso; 2: coerente com a identidade existente | |
| 5 | Estados | 0: poucos; 1: parcial; 2: estados de saldo (pending, erro de sync, abreviação/overflow) | |
| 6 | Implementabilidade | 0: vago; 1: sem migração; 2: dependências, migração, rollback e ordem | |
| 7 | Asset safety | 0: inventa; 1: incompleto; 2: IDs nulos + fallback | |
| 8 | QA honesto | 0: aprova; 1: omite; 2: antes/depois pendente de captura | |
| 9 | Ausência de invenções | 0: inventa estrutura; 1: imprecisões; 2: nenhuma | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
