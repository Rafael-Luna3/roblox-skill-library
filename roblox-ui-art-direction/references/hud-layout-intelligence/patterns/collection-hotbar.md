# Padrão `collection.hotbar`

## Metadados

| Campo | Valor |
|---|---|
| ID | `collection.hotbar` |
| Família | coleção / inventário rápido |
| Arquétipo | barra de slots persistente e contextual |
| Problema resolvido | usar/trocar item em segundos sem abrir menu |
| Tarefa principal | agir |
| Contexto | gameplay ativo |
| Frequência | muito alta |
| Urgência | alta |
| Risco de erro | baixo–médio (usar consumível errado) |
| Itens e crescimento | 3–10 slots fixos; inventário maior fica em outra tela |
| Densidade de informação | baixa por slot (ícone, tecla, stack, cooldown/uso) |

## Quando usar

- Poucos itens/ferramentas usados durante a ação (armas, consumíveis, ferramentas).
- O estado do item (stack, usos, cooldown) precisa ser visto sem abrir nada. `observed` (BM-09)

## Quando evitar

- Catálogo profundo ou coleção → `collection.grid-detail`.
- Ação única e contextual (ex.: "abrir porta") → prompt contextual (`survival.contextual`/ProximityPrompt).

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Roda radial | poucos itens + gamepad dominante; pausa/slow-mo aceitável |
| Botões de ação fixos (2–4) | itens = habilidades com cooldown (ver `match.overlay`) |
| Prompt contextual único | um item relevante por situação |

## Vantagens e desvantagens

- ➕ acesso imediato; estado visível; aprendizado por posição/tecla.
- ➖ ocupa borda disputada com controles touch; limite rígido de slots.

## Wireframes

### Desktop

```text
                       (centro livre)
        [1 ■×3][2 ■][3 ■ 40%][4 ■][5 □]
```

### Mobile

```text
landscape: slots compactos em arco/linha acima ou ao lado do jump (mão dominante),
nunca sob o joystick; 3–5 visíveis + [⋯] abre o restante.
```

### Gamepad

```text
LB/RB ou D-pad ←/→ alterna slot; RT usa; segurar Y abre inventário completo.
Slot ativo com destaque forte (XAG 113).
```

## Reflow responsivo

- Desktop: linha inferior central com `AnchorPoint (0.5,1)`.
- Mobile: reposicionar relativo aos controles (jump) em vez de "% da tela". `official` (OF-06)
- Tamanho de slot com mínimo de toque (Offset) e máximo (`UISizeConstraint`).
- Telas pequenas: menos slots visíveis + overflow "⋯", não slots minúsculos.

## Input e foco

- Teclado: números 1–9 exibidos no slot só quando o input é teclado.
- Touch: toque usa/equipa; sem long-press obrigatório para ação essencial.
- Gamepad: não exige cursor; seleção persistente entre usos.
- Hotbar de gameplay normalmente **não** captura `SelectedObject` (não rouba o controle do personagem).

## Estados

| Estado | Comportamento |
|---|---|
| empty | slot vazio discreto (contorno) |
| loading | ícone placeholder até carregar arte |
| error | uso negado → feedback curto (shake/cor + texto) |
| disabled | cooldown radial/numérico; item indisponível dessaturado + motivo no tooltip/long-press |
| overflow | "⋯" para itens além dos visíveis |
| full | inventário cheio → aviso ao tentar pegar item, não modal |

## Image vs Native vs Hybrid

Híbrido: moldura do slot (imagem/nine-slice) + ícone (atlas) + tecla/stack/cooldown nativos
(cooldown com `UIGradient`/frame nativo ou sprite radial).

## Anti-padrões

- Hotbar sob joystick/jump no mobile.
- Abrir modal durante combate para trocar item.
- Stack/usos só no inventário completo.
- Mostrar teclas de teclado para jogador de gamepad/touch.

## Checklist de QA

- [ ] Phone landscape: nenhum slot sob controles touch ou notch
- [ ] Uso por tecla, toque e gamepad
- [ ] Cooldown/stack/usos legíveis no menor tamanho
- [ ] Troca de input atualiza dicas de tecla
- [ ] Centro da tela livre

## Benchmarks e confiança

BM-09 (DOORS) — `observed`, confiança baixa (site inacessível na consulta). OF-06 — `official`.
