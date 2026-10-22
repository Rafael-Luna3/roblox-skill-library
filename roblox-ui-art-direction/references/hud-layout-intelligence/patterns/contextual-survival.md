# Padrão `survival.contextual`

## Metadados

| Campo | Valor |
|---|---|
| ID | `survival.contextual` |
| Família | horror / survival |
| Arquétipo | indicadores mínimos + prompts contextuais + inventário limitado |
| Problema resolvido | informar sem romper a atmosfera nem revelar ameaças |
| Tarefa principal | agir + sobreviver |
| Contexto | gameplay tenso |
| Frequência | contínua |
| Urgência | alta |
| Risco de erro | alto (perder a run) |
| Itens e crescimento | poucos slots (inventário limitado) |
| Densidade de informação | mínima |

## Quando usar

- Horror, survival, stealth, exploração atmosférica.

## Quando evitar

- Gestão profunda (crafting extenso, base building) → tela dedicada em contexto seguro.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| HUD totalmente diegético (lanterna com bateria no modelo) | imersão máxima, poucas informações |
| Hotbar mínima persistente | itens usados com frequência (BM-09) |
| HUD que aparece só ao mudar (auto-hide) | informação esporádica |

## Vantagens e desvantagens

- ➕ preserva tensão; centro livre.
- ➖ risco de o jogador não entender o estado; exige QA de legibilidade em escuridão.

## Wireframes

### Desktop

```text
(tela quase limpa)
[prompt contextual perto do objeto: "E  Abrir gaveta"]
[hotbar mínima: [1 🔦 62%] [2 ■] [3 □]]  (pode auto-ocultar)
```

### Mobile

```text
botão contextual grande aparece perto do jump quando há interação; hotbar compacta acima do jump.
```

### Gamepad

```text
prompt com glifo (X); D-pad troca item; nenhuma navegação de GUI durante a ação.
```

## Reflow responsivo

Mínimo de elementos; mesmo layout com reposicionamento perto dos controles no mobile.
Prompts acompanham o objeto (BillboardGui/ProximityPrompt) quando apropriado.

## Input e foco

- Prompts contextuais declaram tecla/botão/toque do input ativo.
- Inventário não bloqueia fuga: abrir não deve prender o personagem sem aviso (decisão do jogo).

## Estados

| Estado | Comportamento |
|---|---|
| empty | slot vazio quase invisível |
| loading | n/a (estado inicial definido) |
| error | ação impossível → feedback curto e diegético quando possível |
| disabled | item sem uso/bateria → ícone + valor, não só cor |
| overflow | n/a (limite rígido) |
| full | inventário cheio → mensagem curta ao tentar pegar |

## Image vs Native vs Hybrid

Ícones e texturas sutis em imagem; números nativos com contraste garantido (stroke/sombra)
sobre cenas escuras.

## Anti-padrões

- Ícones chamativos/cores saturadas que quebram o clima.
- Indicadores que revelam posição do inimigo ou rota sem intenção de design.
- Texto escuro sobre cena escura.

## Checklist de QA

- [ ] Legibilidade em cena escura e com efeitos (névoa, flash)
- [ ] Prompts com glifo correto por input
- [ ] Inventário/hotbar não cobre o centro nem controles
- [ ] Nenhuma informação vazada sobre ameaças

## Benchmarks e confiança

BM-09 (DOORS hotbar), BM-10 (DOORS lobby separa pré-partida) — `observed`, confiança baixa (sites inacessíveis nesta consulta).
