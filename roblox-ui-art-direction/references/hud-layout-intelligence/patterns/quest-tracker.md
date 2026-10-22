# Padrão `quest.tracker-expand`

## Metadados

| Campo | Valor |
|---|---|
| ID | `quest.tracker-expand` |
| Família | progressão / objetivos |
| Arquétipo | tracker compacto expansível + log completo em menu |
| Problema resolvido | manter o objetivo visível sem poluir o gameplay |
| Tarefa principal | acompanhar |
| Contexto | exploração/loop ativo |
| Frequência | contínua (leitura) |
| Urgência | baixa–média |
| Risco de erro | baixo |
| Itens e crescimento | 1–3 rastreadas; log com dezenas |
| Densidade de informação | baixa no tracker; alta no log |

## Quando usar

- Missões, tarefas diárias, objetivos de tutorial, quests temporizadas de evento.

## Quando evitar

- Informação emergencial (ameaça, morte) → overlay/alerta.
- Objetivo único de partida → `match.overlay` (topo).

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Toast ao concluir + log | objetivos raros |
| Marcador no mundo (waypoint) + 1 linha | navegação espacial importa |
| Lista lateral sempre aberta | jogos lentos, desktop, poucos elementos de HUD |

## Vantagens e desvantagens

- ➕ orientação constante com pouco espaço.
- ➖ textos longos/localizados quebram o compacto; compete com outros cantos.

## Wireframes

### Desktop

```text
                                   [▸ Pescar 3 peixes raros  2/3]
                                   [  Fale com o Ferreiro      ]  (expandido: até 3)
```

### Mobile

```text
1 linha recolhida sob o status do topo: [▸ Pescar 2/3]; toque → sheet com lista e recompensas.
```

### Gamepad

```text
Botão dedicado (ex.: D-pad ↑) expande/recolhe; log completo no menu (LB/RB por categoria).
```

## Reflow responsivo

Compacto = 1–2 linhas com truncamento + log completo; `AutomaticSize` Y no expandido com
`UISizeConstraint` de altura máxima.

## Input e foco

- Tracker não captura foco no gameplay; o log, sim (foco inicial na quest ativa).
- Texto do objetivo é sempre texto (não imagem) e localizável.

## Estados

| Estado | Comportamento |
|---|---|
| empty | sem quest → ocultar ou "Novas missões no quadro" |
| loading | ocultar até replicar |
| error | — (mostrar último estado conhecido) |
| disabled | quest bloqueada com requisito (no log) |
| overflow | "+2 outras" no compacto |
| full | limite de quests ativas → aviso no log |
| específicos | progresso atualizado (pulso fase B), concluída (toast + recompensa) |

## Image vs Native vs Hybrid

Nativo (texto, progresso); ícone de tipo de quest em imagem.

## Anti-padrões

- Todos os objetivos abertos sobre o gameplay.
- Objetivo truncado sem forma de ler completo.
- Recompensa de conclusão só por animação.

## Checklist de QA

- [ ] Texto traduzido longo no compacto e expandido
- [ ] Múltiplas quests e troca de quest rastreada
- [ ] Conclusão com toast + reflexo no log
- [ ] Não colide com outros elementos do HUD em portrait/landscape

## Benchmarks e confiança

BM-14 (Fisch: quests e quests temporizadas de evento) — `observed` do loop, **sem** evidência visual
(`unverified_visual_reference`). Disposição é `heuristic`.
