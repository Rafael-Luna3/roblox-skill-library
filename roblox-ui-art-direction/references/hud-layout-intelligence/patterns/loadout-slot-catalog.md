# Padrão `loadout.slot-catalog`

## Metadados

| Campo | Valor |
|---|---|
| ID | `loadout.slot-catalog` |
| Família | loadout / equipamento |
| Arquétipo | slots equipados + catálogo + detalhe com comparação |
| Problema resolvido | escolher o que ocupa um número limitado de slots e entender o impacto |
| Tarefa principal | comparar → equipar/trocar |
| Contexto | pré-partida, lobby ou menu seguro |
| Frequência | média |
| Urgência | baixa–média (pode haver timer de pré-partida) |
| Risco de erro | baixo (reversível), médio se houver custo de troca |
| Itens e crescimento | 2–8 slots; catálogo 10–200 |
| Densidade de informação | média–alta (stats, deltas) |

## Quando usar

- "Ter" ≠ "estar equipado" (torres, armas, habilidades, equipamento RPG por slot). `observed` (BM-08)
- Stats decidem a escolha e precisam de comparação com o equipado.

## Quando evitar

- Coleção sem slots → `collection.grid-detail`.
- Troca durante a ação → `collection.hotbar`.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Boneco/paper-doll + catálogo | RPG com slots por parte do corpo |
| Lista de slots → catálogo filtrado pelo slot | mobile e gamepad (fluxo linear) |
| Presets de loadout | jogadores alternam builds com frequência |

## Vantagens e desvantagens

- ➕ deixa o limite claro; comparação direta; troca reversível.
- ➖ três regiões competem por espaço; requer reflow cuidadoso.

## Wireframes

### Desktop

```text
[Slots equipados: [1■][2■][3■][4□]]     [Detalhe do selecionado]
[Catálogo filtrado (grid)       ]       ATQ 42 → 50 ▲ +8 (verde + seta)
                                        [Equipar no slot 4] [Trocar com…]
```

### Mobile

```text
[Tabs: Slots | Catálogo]
Slots: [1■][2■][3■][4□]  toque no slot → catálogo filtrado para esse slot
Catálogo: grid 2–3 col → sheet com deltas + [Equipar]
```

### Gamepad

```text
Foco inicial: primeiro slot. A no slot → catálogo filtrado; A no item → equipar; B volta ao slot.
LB/RB alterna Slots/Catálogo. Y: comparar.
```

## Reflow responsivo

- Desktop: três regiões; mobile: duas abas + sheet. Condição: detalhe deixa o catálogo com < mínimo de colunas.
- Slots sempre visíveis no topo/rodapé em telas médias (contexto do limite).

## Input e foco

- Fluxo "slot primeiro" funciona bem em gamepad/touch (sem drag). Drag-and-drop só como atalho no mouse.
- `NextSelection*` explícito entre slots e catálogo.

## Estados

| Estado | Comportamento |
|---|---|
| empty | slot vazio com convite "Escolha uma torre" |
| loading | catálogo skeleton; slots mantêm último estado confirmado |
| error | troca recusada → slot volta ao anterior com mensagem |
| disabled | item incompatível com o slot/nível — motivo visível |
| overflow | catálogo com filtros/scroll |
| full | todos os slots ocupados → "Trocar com qual?" |

## Image vs Native vs Hybrid

Slot: moldura imagem + ícone; deltas e stats nativos; preview 3D em `ViewportFrame` só no detalhe.

## Anti-padrões

- Selecionar item sem saber o slot de destino.
- Comparação só por cor (sem sinal/seta).
- Drag obrigatório para equipar.
- Equipar no cliente sem confirmação do servidor.

## Checklist de QA

- [ ] Equipar/trocar/remover por mouse, toque e gamepad
- [ ] Limite de slots e item incompatível comunicados
- [ ] Deltas legíveis com sinal e cor
- [ ] Portrait em abas sem perder o contexto dos slots
- [ ] Erro de servidor restaura estado anterior

## Benchmarks e confiança

BM-08 (Tower Defense Simulator) — `observed`, confiança baixa (imagem não inspecionada).
