# Layout Review — <Tela/HUD> — <AAAA-MM-DD>

> Complementa `templates/visual-review.md` (estética/assets) com a verificação da
> **composição** escolhida no layout-decision. Sem captura real → veredito
> `pendente — sem captura`. Validação estrutural de documentos não conta como QA visual.

- **Layout decision:** <LD-...> · **Padrão:** <ID> · **Fase:** <A/B/C/D>
- **Build/place:** <...> · **Revisor:** <...>
- **Método de captura:** <Studio Device Simulator/Emulator + screen_capture | cliente real | NENHUM>

## 1. Matriz de captura

| Viewport | Input | Estado | Arquivo/URL da captura | Resultado |
|---|---|---|---|---|
| Desktop 16:9 | mouse/teclado | padrão | | ✅/⚠️/❌ |
| Ultrawide 21:9 | mouse | padrão | | |
| Phone portrait | touch | padrão | | |
| Phone landscape | touch (controles visíveis) | padrão | | |
| Tablet | touch | padrão | | |
| Console/TV | gamepad | foco inicial | | |
| <qualquer> | — | empty | | |
| <qualquer> | — | loading | | |
| <qualquer> | — | error | | |
| <qualquer> | — | disabled | | |
| <qualquer> | — | overflow | | |
| <qualquer> | — | full | | |
| <qualquer> | — | texto localizado longo | | |
| <qualquer> | — | reduced motion | | |

## 2. Gate de composição

- [ ] Todas as ações essenciais visíveis e alcançáveis em cada viewport declarado
- [ ] Reflow real ocorreu onde planejado (não é o desktop miniaturizado)
- [ ] Sem overlap, corte, deformação, texto < mínimo, conteúdo sob safe area/CoreGui/joystick/jump
- [ ] Centro da tela respeitado (se gameplay ativo)
- [ ] Mesmo fluxo completo com mouse, touch e gamepad; troca de `PreferredInput` preserva contexto
- [ ] Foco inicial, foco visível em todos os fundos, B/Esc volta/fecha, modal prende o foco
- [ ] Estados empty/loading/error/disabled/overflow/full intencionais
- [ ] Risco (compra/trade/delete): lado, preço, mudança de estado e confirmação proporcionais
- [ ] Nenhuma informação essencial só por cor, hover, drag ou animação
- [ ] Ultrawide limitado por constraint

## 3. Problemas e correções

| # | Severidade | Viewport/input | Problema | Correção | Recaptura |
|---|---|---|---|---|---|

## 4. Veredito

<aprovado | aprovado com ressalvas | reprovado | pendente — sem captura>

## 5. Memória

Registro criado: <LM-...> em <caminho> (ver `templates/layout-memory-record.md`).
