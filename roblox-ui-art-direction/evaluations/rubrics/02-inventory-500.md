# Rubrica 02 — Inventário com 500+ itens

Prompt: [../prompts/02-inventory-500.md](../prompts/02-inventory-500.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- grade sem busca/filtro para 540+ itens
- vender/fundir com um toque sem confirmação
- detalhe lateral espremido no portrait sem reflow
- inventar como é a UI atual sem evidência
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: sem decisão; 1: grid-detail sem alternativas; 2: alternativas reais e justificativa com escala/crescimento | |
| 2 | Responsividade (reflow real) | 0: miniatura do desktop; 1: cita Sheet sem gatilho; 2: gatilho mensurável e composição portrait completa | |
| 3 | Gamepad/touch | 0: sem foco; 1: foco genérico; 2: foco inicial, NextSelection nas bordas do grid, B fecha Sheet antes da tela | |
| 4 | Identidade visual | 0: genérico; 1: tema de mineração superficial; 2: identidade aplicada a cards/raridade com sinal não cromático | |
| 5 | Estados | 0: poucos estados; 1: faltam full/no-results; 2: matriz completa com recovery | |
| 6 | Implementabilidade | 0: vago; 1: sem dados/paginação; 2: pool/virtualização, dados, intenções e servidor | |
| 7 | Asset safety | 0: IDs inventados; 1: manifest incompleto; 2: atlas planejado, IDs nulos, fallback | |
| 8 | QA honesto | 0: alega teste; 1: omite; 2: pendente sem captura + plano | |
| 9 | Ausência de invenções | 0: inventa; 1: imprecisões; 2: nenhuma | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
