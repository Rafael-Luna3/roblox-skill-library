# Rubrica 05 — Settings acessível por gamepad

Prompt: [../prompts/05-settings-gamepad.md](../prompts/05-settings-gamepad.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- informação só em hover
- B fecha tudo em vez de voltar um nível
- foco sutil/invisível
- sem foco inicial
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: sem decisão; 1: sem alternativas; 2: alternativas e justificativa | |
| 2 | Responsividade (reflow real) | 0: só desktop; 1: cita mobile; 2: lista→subpágina com gatilho | |
| 3 | Gamepad/touch | 0: genérico; 1: parcial; 2: rota completa, foco forte, TV-safe, 8–10 ft | |
| 4 | Identidade visual | 0: genérico; 1: raso; 2: coerente com o jogo sem prejudicar legibilidade | |
| 5 | Estados | 0: poucos; 1: parcial; 2: matriz completa | |
| 6 | Implementabilidade | 0: vago; 1: parcial; 2: estrutura, dados de preferência, persistência e ordem | |
| 7 | Asset safety | 0: inventa; 1: incompleto; 2: poucos assets justificados, IDs nulos | |
| 8 | QA honesto | 0: aprova; 1: omite; 2: pendente + plano com Controller Emulator | |
| 9 | Ausência de invenções | 0: inventa; 1: imprecisões; 2: nenhuma | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
