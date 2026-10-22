# Evidence Board — <Tela> — <Jogo>

> Separa **evidência de referência** (o que outros fizeram ou documentaram) de
> **evidência de QA do próprio projeto** (o que esta build mostrou). Só a segunda aprova uma tela.
> Fontes da skill: `references/hud-layout-intelligence/benchmark-register.md`.

## A. Evidência de referência (não aprova nada sozinha)
| ID | Tipo | Afirmação | Fonte (URL ou ID do register) | Data | Confiança | Implicação para esta tela | Próxima ação |
|---|---|---|---|---|---|---|---|
| E-01 | official | | | | alta | | |
| E-02 | observed | | | | baixa/média | | revalidar no jogo |
| E-03 | heuristic | | | | média | | testar |
| E-04 | hypothesis | | — | | baixa | | playtest |

## B. Decisões humanas
| ID | Decisão | Quem | Data | Status |
|---|---|---|---|---|
| H-01 | <item marcado [aprovação humana]> | <pendente> | | pendente |

## C. Evidência de QA do projeto
| ID | Viewport/input | Estado | Arquivo da captura (caminho real) | Resultado | Data |
|---|---|---|---|---|---|
| Q-01 | | | <vazio = não capturado> | pendente | |

Regras: uma linha da seção C só existe com **caminho real** de captura; sem isso, o veredito é
`pendente — sem captura`. Benchmark `observed` de baixa confiança nunca é "prova".
