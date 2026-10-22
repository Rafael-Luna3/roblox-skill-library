# Caso documental 1 — Inventário extenso

> Jogo **fictício** "Critter Grove" (simulator de coleção, cartoon). Nenhuma captura,
> asset ou AssetId existe. QA visual: **pendente — sem captura** (caso de papel).

## Contexto
Coleção de criaturas com 300+ espécies, variantes (dourada, arco-íris), duplicatas e
equipe ativa de 6. Público 9–15; ~70% mobile, 25% desktop, 5% console. Inventário com
limite inicial de 250, expansível.

## 12 perguntas (resumo)

| # | Resposta | Evidência |
|---|---|---|
| 1 | comparar → agir (equipar na equipe, fundir duplicatas, deletar) | — |
| 2 | menu seguro (jogador parado/zona segura) | — |
| 3 | não; só a equipe ativa aparece no HUD | heuristic |
| 4 | várias vezes por sessão; sem urgência | hypothesis |
| 5 | 50–250 agora; cresce sem limite prático | observed (BM-02, escala de coleções) |
| 6 | busca + filtros (raridade, variante, equipada) + ordenação + scroll | heuristic (AC-02) |
| 7 | sim: stats, variante, multiplicador; comparar com equipada | — |
| 8 | médio: fundir/deletar irreversíveis | — |
| 9 | phone P/L, tablet, desktop, ultrawide, console; touch, mouse, gamepad | — |
| 10 | tela cheia permitida (menu seguro), mas abrir não pode ocorrer em combate | — |
| 11 | fase A | — |
| 12 | empty, empty-filtro, loading, error, disabled (bloqueada), overflow, full (250/250), nomes longos | — |

## Alternativas

| Alternativa | Candidata porque | Trade-offs | Mobile | Gamepad | QA | Resultado |
|---|---|---|---|---|---|---|
| `collection.grid-detail` | muitos itens + detalhe/comparação | ocupa a tela; exige reflow | grid 3 col + sheet | grid focável + detalhe segue foco | estados + 3 composições | **escolhida** |
| `loadout.slot-catalog` | existe equipe de 6 slots | foco no slot esconde gestão da coleção (fundir/deletar) | abas Slots/Catálogo | bom | menor | rejeitada como tela principal; **reutilizada** como aba "Equipe" |
| Lista com linhas ricas | texto/stats legíveis | arte das criaturas é o atrativo; lista desperdiça | boa | boa | simples | rejeitada: identidade visual é a arte |

## Decisão
`collection.grid-detail` + aba "Equipe" baseada em `loadout.slot-catalog`.
Justificativa: tarefa = comparar/agir (1), crescimento ilimitado (5), filtros necessários (6),
comparação de stats (7), 70% mobile exige detalhe sob demanda (9).
**[aprovação humana]**: categorias em sidebar (desktop) vs tabs — ambas viáveis; proposta: sidebar no desktop, chips no mobile.

## Plano por plataforma

### Mobile portrait (primeiro)
```text
[← Criaturas                 182/250]
[Busca______________] [⇅] [Filtros]
[Todas][Equipadas][Lendárias][Douradas] →
[■][■][■]
[■][■][■]  grid 3 col (2 col se o card cair abaixo do mínimo do brief)
toque → bottom sheet: arte · stats vs equipada (▲/▼ + cor) · [Equipar] [Fundir ×3] [⋯ Deletar]
```
### Phone landscape
`rail de categorias estreito | grid 4–5 col`; detalhe como painel modal à direita.

### Gamepad/TV
Foco inicial no primeiro card (ou último selecionado). LB/RB: categorias. X: filtros. Y: ordenar.
A: abre ações no detalhe. B: fecha detalhe → fecha tela. Detalhe acompanha foco no layout largo.

### Desktop / ultrawide
`sidebar categorias | grid | detalhe` com `UISizeConstraint` no root (ultrawide não estica).

**Reflow:** condição de colunas mínimas → detalhe vira sheet. **Camada:** `Menu` (CoreUISafeInsets).

## Estados
empty ("Choque ovos na Zona 1" + botão ir) · empty-filtro (limpar) · loading (skeleton) ·
error (manter lista anterior + tentar novamente) · disabled (criatura bloqueada por evento, motivo) ·
overflow (contador, scroll virtualizado) · full (banner 250/250 + "Fundir/Expandir" antes de novos ovos).

## Visual (módulos existentes)
Card híbrido: moldura de raridade nine-slice tintável + ícone (atlas) + nome/nível nativos;
raridade com ícone/estrelas além da cor. `ViewportFrame` só no sheet/painel de detalhe.

## Checklist de QA (plano)
- [ ] 0, 1, 50, 250 e 250/250 itens
- [ ] Busca + filtro + ordenação combinados; limpar filtros
- [ ] Sheet abre/fecha com toque, B e Esc; foco volta ao card
- [ ] Fundir/deletar confirmam quantidade e são validados no servidor
- [ ] Nome longo localizado não quebra card
- [ ] Capturas: desktop, ultrawide, phone P/L, tablet, console — **pendentes**

## Memória (registro simulado)
LM-critter-20261022-01 · nível 1 · padrão `collection.grid-detail` · rejeitadas: lista, slot-catalog como principal ·
confiança `heuristic` · decisão humana: pendente (sidebar vs tabs) · licença: n/a (sem capturas).
