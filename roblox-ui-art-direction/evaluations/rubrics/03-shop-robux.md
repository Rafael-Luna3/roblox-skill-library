# Rubrica 03 — Loja com Robux/moeda e confirmação

Prompt: [../prompts/03-shop-robux.md](../prompts/03-shop-robux.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- preço de Robux desenhado em imagem ou modal próprio substituindo o prompt nativo
- debitar saldo no cliente
- inventar IDs de game pass/developer product
- timer/escassez falsa
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: sem decisão; 1: sem alternativas; 2: alternativas e justificativa ligada ao risco | |
| 2 | Responsividade (reflow real) | 0: só desktop; 1: mobile sem gatilho; 2: reflow com botão de compra acessível no polegar | |
| 3 | Gamepad/touch | 0: ignora gamepad; 1: cita; 2: foco inicial, Confirmar nunca em B, rota completa | |
| 4 | Identidade visual | 0: genérico; 1: cores cozy sem forma; 2: identidade cozy em cards/moldura sem prejudicar preço legível | |
| 5 | Estados | 0: poucos; 1: faltam prompt cancelado/possuído; 2: matriz completa | |
| 6 | Implementabilidade | 0: vago; 1: sem fluxo de compra; 2: intenções, servidor, ProcessReceipt e ordem | |
| 7 | Asset safety | 0: IDs inventados; 1: incompleto; 2: IDs nulos + fallback + queue de produtos | |
| 8 | QA honesto | 0: aprova; 1: omite; 2: pendente + plano incluindo prompt nativo em conta de teste | |
| 9 | Ausência de invenções | 0: inventa; 1: imprecisões; 2: nenhuma | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
