# Padrão `reward.track-reveal`

## Metadados

| Campo | Valor |
|---|---|
| ID | `reward.track-reveal` |
| Família | progressão / recompensa |
| Arquétipo | trilha de progresso + reveal + resultado legível |
| Problema resolvido | mostrar progresso e resultado (daily reward, battle pass, conquistas, gacha, roleta) |
| Tarefa principal | acompanhar → resgatar → entender o que ganhou |
| Contexto | menu seguro ou pós-partida |
| Frequência | diária/por sessão |
| Urgência | baixa |
| Risco de erro | médio (gacha envolve gasto; perder recompensa por não resgatar) |
| Itens e crescimento | 7 (daily) a 100+ níveis (pass) |
| Densidade de informação | média |

## Quando usar

- Recompensas sequenciais ou com marcos; reveal com valor emocional.

## Quando evitar

- Recompensa instantânea de baixo valor → toast/notificação.
- Resultado que precisa ser imediato durante combate.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Trilha horizontal com marcos | daily/pass curtos |
| Lista vertical rolável com marcos | pass longo, mobile portrait |
| Grade de conquistas + filtro | conquistas (não sequenciais) |

## Vantagens e desvantagens

- ➕ progresso visível motiva retorno; reveal gera celebração.
- ➖ animações longas atrasam o jogador; risco de padrões manipulativos em gacha.

## Wireframes

### Desktop

```text
[Passe Temporada 3 — nível 14/50 ▓▓▓▓░░░]
[◆1][◆2]…[◆14 RESGATAR][◇15]…   ← rola    | Detalhe do nível: recompensa grátis / premium
```

### Mobile

```text
[Passe  14/50]
lista vertical: [nível ◆ recompensa | estado]  (resgatáveis no topo ou com atalho "Ir para resgatável")
reveal em tela cheia → card de resultado com texto: "Você recebeu: Espada Rara ×1" [OK] [Ver no inventário]
```

### Gamepad

```text
D-pad navega níveis; A resgata; X pula animação; B volta. Foco inicial: primeiro resgatável.
```

## Reflow responsivo

- Horizontal no desktop/landscape; vertical no portrait; sempre com "ir para resgatável".
- Reveal: modal em `CriticalOverlay`/`Modal`, card de resultado com `UISizeConstraint`.

## Input e foco

- **Skip seguro** sempre disponível (toque/A/X/clique), sem perder o resultado.
- **A animação não é a única prova**: resultado final em texto + item no inventário + histórico. `heuristic`
- Reduced motion: resultado direto com fade.

## Estados

| Estado | Comportamento |
|---|---|
| empty | sem temporada ativa → próxima data |
| loading | trilha skeleton; resgatar em *pending* |
| error | falha de resgate → recompensa continua resgatável; mensagem |
| disabled | nível bloqueado com requisito; premium sem passe |
| overflow | trilha longa com rolagem e salto para resgatável |
| full | inventário cheio → recompensa vai para "caixa de correio" ou aviso antes de resgatar |
| específicos | já resgatado; expira em; reveal pulado |

## Image vs Native vs Hybrid

Imagem: arte de recompensa, baú, burst (spritesheet), molduras. Nativo: níveis, barras,
textos, timers, estados. Detalhes de motion na fase B (`references/animation-and-feedback.md`).

## Anti-padrões

- Resultado comunicado só por animação/roleta.
- Animação que não pode ser pulada.
- Gacha sem odds/custo claros; timers falsos.
- Recompensa resgatada no cliente antes do servidor.

## Checklist de QA

- [ ] Skip em todos os inputs mantém resultado
- [ ] Resultado legível em texto e refletido no inventário
- [ ] Reduced motion
- [ ] Já resgatado / bloqueado / inventário cheio / erro
- [ ] Trilha longa no portrait com atalho para resgatável

## Benchmarks e confiança

Sem benchmark visual verificado nesta versão; disposição é `heuristic`/`hypothesis`. AC-01 (precisão de timing não essencial; skip) — `heuristic`.
