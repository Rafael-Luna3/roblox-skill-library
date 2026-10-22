# Layout Decision — <Tela/HUD> — <Jogo>

> Obrigatório antes de construir (ver `references/hud-layout-intelligence/selection-method.md`).
> Salvar no repositório do jogo, ex.: `docs/ui/layout-decisions/<tela>.md`.

- **ID:** LD-<jogo>-<tela>-<nn>
- **Data:** <AAAA-MM-DD> · **Versão da skill:** <1.1.0>
- **Entradas lidas:** design brief <caminho> · theme profile <caminho> · memória do projeto <caminho ou "nenhuma">
- **Fase autorizada:** <A | B | C | D>

## 1. Respostas às 12 perguntas

| # | Pergunta | Resposta | Evidência (`official/observed/heuristic/hypothesis`) |
|---|---|---|---|
| 1 | Tarefa principal | <agir/comparar/descobrir/configurar/acompanhar/confirmar/negociar> | |
| 2 | Contexto | <combate/exploração/lobby/loja/menu seguro> | |
| 3 | Precisa ficar sempre visível? | | |
| 4 | Urgência e frequência | | |
| 5 | Itens agora / crescimento | | |
| 6 | Busca/filtro/ordenação/paginação/scroll | | |
| 7 | Seleção, detalhe, comparação | | |
| 8 | Risco econômico/social/irreversível | | |
| 9 | Dispositivos e inputs suportados | <desktop, ultrawide, phone P/L, tablet, console/TV; mouse, teclado, touch, gamepad> | |
| 10 | O que pode/não pode cobrir o gameplay | | |
| 11 | Fase | | |
| 12 | Estados a testar | <empty, loading, error, disabled, overflow, full, + específicos> | |

## 2. Alternativas (máximo 3, só viáveis)

| Alternativa (ID do padrão) | Por que é candidata | Trade-offs | Impacto mobile | Impacto gamepad | Impacto no QA | Resultado |
|---|---|---|---|---|---|---|
| <A> | | | | | | escolhida / rejeitada: <motivo> |
| <B> | | | | | | |
| <C> | | | | | | |

Se só uma é viável: <por que as outras famílias não servem>.

## 3. Decisão

- **Padrão escolhido:** <ID>
- **Justificativa (cita respostas 1–12):** <...>
- **Itens que exigem [aprovação humana]:** <escolhas estéticas/subjetivas> — status: <pendente/aprovado por X em data>

## 4. Plano por plataforma (mobile e gamepad primeiro)

### Mobile portrait / landscape
```text
<wireframe textual>
```
### Gamepad / TV
```text
<foco inicial · rota · A · B/Esc · LB/RB · atalhos>
```
### Tablet / ultrawide
<diferenças>
### Desktop
```text
<wireframe textual>
```

**Condições de reflow:** <ex.: detalhe vira sheet quando o grid cair abaixo de N colunas no card mínimo>
**Camada / ScreenGui / ScreenInsets / DisplayOrder:** <...>
**Zonas proibidas:** <centro, joystick, jump, topbar, chat...>

## 5. Estratégia visual (aponta para os módulos existentes)

- Imagem vs nativo vs híbrido por elemento: <link para a tabela da tela, `references/asset-decision-matrix.md`>
- Assets necessários: <ids do asset manifest; nenhum AssetId inventado>

## 6. Plano de prova (QA)

| Viewport | Input | Estados | Captura exigida |
|---|---|---|---|
| Desktop 16:9 | mouse/teclado | <...> | sim |
| Phone portrait | touch | | sim |
| Phone landscape | touch | | sim |
| Tablet | touch | | sim |
| Ultrawide | mouse | | sim |
| Console/TV | gamepad | | se suportado |

Revisão será registrada em `templates/layout-review.md`.
