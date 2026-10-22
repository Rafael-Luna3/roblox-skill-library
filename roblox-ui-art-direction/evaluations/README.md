# Avaliações da skill

Objetivo: medir se a skill **melhora o resultado** do Claude (decisão, implementabilidade,
honestidade), não se ele cita arquivos. Seis cenários; cada um tem prompt em `prompts/` e
rubrica em `rubrics/`. Sinais transversais em [expected-signals.md](expected-signals.md).

**Status atual: nenhum cenário foi executado.** Ver [results/README.md](results/README.md).
Nunca registre resultado de um cenário que não rodou.

## Cenários

| # | Cenário | Prompt | Rubrica |
|---|---|---|---|
| 1 | HUD de combate mobile | [prompts/01-mobile-combat-hud.md](prompts/01-mobile-combat-hud.md) | [rubrics/01-mobile-combat-hud.md](rubrics/01-mobile-combat-hud.md) |
| 2 | Inventário com 500+ itens | [prompts/02-inventory-500.md](prompts/02-inventory-500.md) | [rubrics/02-inventory-500.md](rubrics/02-inventory-500.md) |
| 3 | Loja com Robux/moeda e confirmação | [prompts/03-shop-robux.md](prompts/03-shop-robux.md) | [rubrics/03-shop-robux.md](rubrics/03-shop-robux.md) |
| 4 | Trade social de alto risco | [prompts/04-social-trade.md](prompts/04-social-trade.md) | [rubrics/04-social-trade.md](rubrics/04-social-trade.md) |
| 5 | Settings acessível por gamepad | [prompts/05-settings-gamepad.md](prompts/05-settings-gamepad.md) | [rubrics/05-settings-gamepad.md](rubrics/05-settings-gamepad.md) |
| 6 | Redesign de UI existente sem apagar sistemas | [prompts/06-redesign-existing.md](prompts/06-redesign-existing.md) | [rubrics/06-redesign-existing.md](rubrics/06-redesign-existing.md) |

## Critérios (iguais em todas as rubricas, 0–2 cada, total 18)

1. Decisão de layout justificada · 2. Responsividade (reflow real) · 3. Gamepad/touch ·
4. Identidade visual (do brief, não genérica) · 5. Estados · 6. Implementabilidade ·
7. Asset safety · 8. QA honesto · 9. Ausência de invenções.

**Aprova** se: total ≥ 14 **e** nenhum erro crítico **e** nota ≥ 1 nos critérios 7, 8 e 9.
**Reprova** caso contrário. Erros críticos estão em cada rubrica.

## Como executar (Claude Code local)

1. Instale/atualize a skill em `~/.claude/skills/roblox-ui-art-direction` (ver README da biblioteca).
2. Crie uma pasta de trabalho vazia por cenário (ex.: `C:\tmp\eval-01`), copie para ela os
   arquivos listados em "Entradas disponíveis" do prompt (quando houver).
3. **Condição com skill:** abra um terminal novo nessa pasta, rode `claude` (sessão nova),
   cole o prompt do cenário exatamente como está. Não dê dicas extras.
4. **Condição baseline (sem skill):** mova temporariamente a pasta da skill para fora de
   `~/.claude/skills` (ex.: `Documents\skill-off\`), abra outra sessão nova e cole o mesmo prompt.
   Depois, devolva a pasta.
5. Repita com cada modelo disponível que quiser comparar (`claude --model <id>` ou `/model`).
6. Salve a resposta completa e os arquivos gerados em `evaluations/results/<AAAA-MM-DD>-<modelo>-<cenário>-<com|sem>/`.
7. Pontue com a rubrica (idealmente outra pessoa ou outra sessão que **não** viu a geração).
8. Registre em `results/README.md`: data, modelo, condição, nota por critério, erros críticos, aprovado/reprovado.
9. Se rodar `validate_hud_packet.py` sobre o packet gerado, anexe a saída — passar no validador
   **não** aumenta a nota de identidade visual nem prova QA.

Se não for possível executar, registre "não executado" e o motivo.
