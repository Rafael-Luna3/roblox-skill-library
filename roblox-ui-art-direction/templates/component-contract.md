# Component Contract — <ComponentName>

> Use para componentes não triviais ou específicos do jogo. Tipo base em
> `references/component-system.md`. Componente sem função visual clara não entra.

| Campo | Valor |
|---|---|
| ID | <cmp.id> |
| Tipo base | <Panel/Button/IconButton/Tab/ItemCard/CurrencyPill/ProgressBar/Modal/Sheet/Tooltip/Toast/FocusRing/EmptyState/LoadingSkeleton/ErrorState/ConfirmationFooter/Custom> |
| Responsabilidade | <uma frase> |
| Limites (não faz) | <...> |
| Telas que usam | <...> |

## Estrutura Roblox (DataModel)
```text
<Nome> (<ClassName>)
├── <Filho> (<ClassName>)  — <papel>
└── ...
```

## Propriedades e tokens consumidos
| Propriedade | Token do theme profile | Observação |
|---|---|---|
| BackgroundColor3/ImageColor3 | <surface.raised> | |
| FontFace | <Theme.Font.Body> | |
| Padding | <Theme.Space.md> | |

## Estados
| Estado | Visual (via tokens) | Texto/ícone | Interação | Aplica? |
|---|---|---|---|---|
| idle | | | | |
| hover | | | só ponteiro | |
| press | | | | |
| selected | | | | |
| disabled | | motivo visível | não ativa | |
| pending | | | bloqueia repetição | |
| success | | | | |
| error | | mensagem | recovery | |
| focus | FocusRing | | gamepad/teclado | |

## Comportamento por input
| Input | Comportamento |
|---|---|
| Mouse | |
| Touch | |
| Teclado | |
| Gamepad | |

## Fallback de asset
<o que aparece se o asset do manifest estiver `null`/pendente; atributo `Placeholder`>

## Acessibilidade
<contraste, informação não só por cor, tamanho mínimo, reduced motion, localização>

## Desempenho
<nº de instâncias, pool, CanvasGroup/ViewportFrame?, conexões a limpar>

## Critérios de aceite
- [ ] todos os estados aplicáveis implementados e capturados
- [ ] funciona com os inputs suportados
- [ ] usa só tokens do theme profile
- [ ] fallback visível quando asset ausente
- [ ] sem vazamento de conexões ao destruir
