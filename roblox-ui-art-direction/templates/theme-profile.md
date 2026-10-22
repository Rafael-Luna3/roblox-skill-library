# Theme Profile — <nome-do-tema>

> Fonte de verdade estética de UM jogo. Os componentes leem apenas tokens semânticos.
> Espelhe este documento no módulo `Theme` do projeto (ver references/theme-system.md).

## 1. Identidade
- **Nome do tema:** <...>
- **Descrição estética (2–3 frases):** <conceito material/espacial, luz, personalidade>
- **Conceito de motion:** <elástico / pesado / mecânico / flutuante / seco>

## 2. Paleta primitiva
| Token | Hex | Notas |
|---|---|---|
| <ink900> | <#...> | <...> |

## 3. Cores semânticas
| Token semântico | → Primitivo | Uso |
|---|---|---|
| surface.base | <...> | fundo de tela/overlay |
| surface.panel | <...> | painel |
| surface.raised | <...> | card, célula |
| border.default | <...> | contornos |
| text.primary / text.secondary / text.onAction | <...> | |
| action.primary / action.secondary / action.destructive | <...> | botões |
| state.success / warning / danger / info | <...> | feedback |
| state.disabled | <...> | |
| focus.ring | <...> | seleção gamepad/teclado |
| currency.<nome> | <...> | se houver moedas |

## 4. Tipografia
| Papel | Família (FontFace) | Peso | Tamanho desktop / mobile | Uso |
|---|---|---|---|---|
| Display | <...> | <...> | <...> | títulos curtos |
| Heading | <...> | | | |
| Body | <...> | | | |
| Numeric | <...> | | | moedas, timers |
| Caption | <...> | | | |
Regras: <contorno/sombra de texto? caixa alta? tracking?>

## 5. Espaçamento, raios e forma
- Escala de espaçamento: <4 / 8 / 12 / 16 / 24 / 32>
- Raios / cantos: <ex.: 0 (chanfro via imagem) | 8 | 16 | pílula proibida>
- Espessura de contorno: <...>
- Linguagem de forma: <...>

## 6. Componentes
| Componente | Estratégia (A/B/C/D/E) | Assets | Regras visuais |
|---|---|---|---|
| Painel | <...> | <ids do manifest> | <...> |
| Botão primário | | | |
| Botão secundário | | | |
| Botão quieto / ícone | | | |
| Card de item | | | |
| Abas | | | |
| Barra de progresso | | | |
| Tooltip | | | |
| Notificação / toast | | | |
| Modal de confirmação | | | |

## 7. Ícones e imagens
- Estilo de ícone: <preenchido/contorno/ilustrado/pixel>, perspectiva <...>, contorno <...>, luz <...>
- Tratamento de imagens: <cel-shading, pintado, flat...>; tintáveis: <lista>
- Sombras e brilho: <dura / suave / nenhuma / glow apenas em X>
- Style anchor para prompts:
  ```text
  <bloco de estilo compartilhado usado em todos os prompts de geração>
  ```

## 8. Motion
| Token | Duração | Easing | Uso |
|---|---|---|---|
| fast | <...> | <...> | press/hover |
| base | | | trocas de estado |
| panel | | | entrada/saída |
| reward | | | recompensa |
Reduced motion: <comportamento>

## 9. Estados de interação
| Estado | Tratamento |
|---|---|
| idle / hover / press / selected / disabled / pending / error | <...> |

## 10. Raridades (somente se o jogo tiver)
| Nome | Cor/token | Moldura/efeito | Indicador não-cromático |
|---|---|---|---|
| <...> | | | <ícone/rótulo/forma> |

## 11. Responsividade
- Composições: <narrow < Xpx; wide ≥ Xpx>
- SliceScale por perfil: <...>; texto mínimo: <...>
- Elementos que somem/recompõem em narrow: <...>

## 12. Diretrizes de consistência
- **Faça:** <...>
- **Não faça:** <...>
