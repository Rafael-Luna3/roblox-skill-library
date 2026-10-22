# Rubrica 04 — Trade social de alto risco

Prompt: [../prompts/04-social-trade.md](../prompts/04-social-trade.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- aceitar oferta alterada após Pronto
- lista única misturando ofertas
- lados diferenciados só por cor
- lógica de troca no cliente
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: sem decisão; 1: padrão sem alternativas; 2: alternativas portrait reais comparadas | |
| 2 | Responsividade (reflow real) | 0: lado a lado espremido; 1: abas sem resumo; 2: os dois lados sempre legíveis/resumidos no portrait | |
| 3 | Gamepad/touch | 0: sem gamepad; 1: genérico; 2: LB/RB ou ↑/↓ entre lados, Confirmar nunca foco inicial | |
| 4 | Identidade visual | 0: genérico; 1: tema raso; 2: identidade sem sacrificar clareza dos lados | |
| 5 | Estados | 0: poucos; 1: faltam offer-changed/countdown; 2: matriz completa | |
| 6 | Implementabilidade | 0: vago; 1: sem versão/atomicidade; 2: intenções versionadas e responsabilidades do servidor | |
| 7 | Asset safety | 0: inventa; 1: incompleto; 2: IDs nulos + fallback | |
| 8 | QA honesto | 0: aprova; 1: omite; 2: pendente + teste multi-client | |
| 9 | Ausência de invenções | 0: inventa; 1: imprecisões; 2: nenhuma | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
