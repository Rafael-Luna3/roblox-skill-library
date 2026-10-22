# HUD Screen Spec — <Tela> — <Jogo>

> Artefato 3–4 do `references/hud-delivery-contract.md`. Um por tela/HUD.
> Ligações obrigatórias: layout decision <LD-...> · state matrix <arquivo> · componentes <lista> · manifest <arquivo> · packet <arquivo.json>

- **ID da tela:** <screen.id> · **Fase:** <A/B/C/D> · **Padrão:** <ID do padrão>
- **Status visual:** <pendente — sem captura | ver evidence board>

## 1. Objetivo e tarefa principal
- Objetivo do jogador nesta tela: <...>
- Tarefa principal (verbo): <agir/comparar/descobrir/configurar/acompanhar/confirmar/negociar>
- Sucesso = <o que o jogador consegue fazer/saber ao sair>

## 2. Hierarquia de informação (3 níveis)
| Nível | Conteúdo | Por que nesse nível |
|---|---|---|
| 1 — leitura imediata (< 1 s) | <...> | |
| 2 — consulta (quando decide) | <...> | |
| 3 — sob demanda (detalhe/expandir) | <...> | |

## 3. Zonas
| Zona | Reservada para / proibida | Plataformas |
|---|---|---|
| centro da tela | <livre para gameplay / conteúdo modal> | |
| joystick / jump / botões touch | proibida | phone, tablet |
| topbar/CoreGui/notch | proibida (CoreUISafeInsets) | todas |
| <...> | | |

## 4. Composição por plataforma
Para cada plataforma **suportada**: wireframe textual + gatilho mensurável de reflow.

### Desktop
```text
<wireframe>
```
### Phone portrait
```text
<wireframe>
```
### Phone landscape
```text
<wireframe>
```
### Tablet / ultrawide
<diferenças e limites (`UISizeConstraint`)>
### Gamepad / TV
```text
<foco inicial · rota · A · B/Esc · LB/RB>
```

### Gatilhos de reflow (mensuráveis)
| Gatilho | Condição medível | Mudança composicional |
|---|---|---|
| R1 | <ex.: grid < 3 colunas com card ≥ 96 px de largura> | <detalhe vira Sheet> |
| R2 | <ex.: `ViewportDisplaySize == Small`> | <tabs viram chips> |

## 5. Camadas (ScreenGui)
| ScreenGui | Camada | DisplayOrder | ScreenInsets | ResetOnSpawn | Conteúdo |
|---|---|---|---|---|---|
| <...Gui> | GameplayHUD / Contextual / Menu / Modal / CriticalOverlay | <n> | CoreUISafeInsets / DeviceSafeInsets | <true/false> | <...> |

## 6. Componentes usados
| ID | Tipo (`references/component-system.md`) | Contrato | Assets |
|---|---|---|---|
| <cmp.id> | <Button/ItemCard/...> | <link ou "trivial"> | <ids do manifest> |

## 7. Estados e riscos
- State matrix: <link>
- Risco: <low/medium/high/critical> — cancelamento: <...> · recovery: <...> · confirmação: <...>
- Server-authoritative: <o que o servidor valida>

## 8. Ligações
Layout decision: <...> · Matriz imagem/nativo: <...> · Handoff: <...> · Evidence board: <...>
