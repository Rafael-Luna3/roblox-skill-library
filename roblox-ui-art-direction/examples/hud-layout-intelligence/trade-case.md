# Caso documental 3 — Trade bilateral

> Jogo **fictício** "Kingdom Pets" (social/coleção, tema medieval ilustrado).
> Nenhuma captura, asset ou AssetId existe. QA visual: **pendente — sem captura**.

## Contexto
Trade de pets e itens entre dois jogadores; limite de 9 slots por lado (decisão do jogo);
público 10–16; 65% mobile. Alvo frequente de golpes → risco muito alto.

## 12 perguntas (resumo)

| # | Resposta | Evidência |
|---|---|---|
| 1 | negociar → comparar → confirmar | — |
| 2 | menu seguro, interação social | — |
| 3 | sim, durante o trade: as duas ofertas e o status | heuristic |
| 4 | baixa frequência; pressão social média | hypothesis |
| 5 | até 9 por lado; inventário próprio de centenas | — |
| 6 | sim no submodal de inventário (busca/filtro) | heuristic (AC-02) |
| 7 | sim: ver item do outro em detalhe | — |
| 8 | **muito alto**: irreversível, golpes | observed (BM-05) |
| 9 | phone P/L, tablet, desktop, console; touch, mouse, gamepad | — |
| 10 | tela cheia (modal); personagem parado | — |
| 11 | fase A | — |
| 12 | vazio, pronto/não pronto, oferta alterada, countdown, outro saiu, item intransferível, inventário cheio, erro de servidor | — |

## Alternativas

| Alternativa | Candidata porque | Trade-offs | Mobile | Gamepad | QA | Resultado |
|---|---|---|---|---|---|---|
| `trade.bilateral-confirm` lado a lado | comparação simétrica | largura | não cabe no portrait | LB/RB entre lados | muitos estados | **escolhida (desktop/tablet/landscape)** |
| Abas "Você / Outro" + resumo fixo | portrait | uma oferta por vez | **boa** com resumo fixo | LB/RB = abas | igual | **escolhida (phone portrait)** — mesma família, reflow |
| Lista única misturando ofertas | simples | ambígua sobre quem dá o quê | — | — | — | rejeitada: anti-padrão para risco 8 |

## Decisão
`trade.bilateral-confirm` com reflow lado a lado ↔ abas + resumo fixo.
Regras: qualquer alteração zera "Pronto" dos dois lados e mostra aviso; confirmação final com
countdown curto que **cancela** em qualquer alteração; troca atômica validada no servidor.
**[aprovação humana]**: exibir ou não "valor estimado" (pode incentivar comparação de valor — decisão de design do jogo).

## Plano por plataforma

### Phone portrait (primeiro)
```text
[Trade com @Outro                      ✕]
[Você 3 itens ⇄ @Outro 2 itens · você: ✔ · @Outro: …]   (resumo fixo)
[Você] [@Outro]
[■][■][■]
[■][□][□]   (9 slots)
[+ Adicionar]
⚠ Oferta alterada — Pronto reiniciado
[Recusar]                       [Pronto]   (rodapé fixo, safe area)
```
### Gamepad/TV
Foco inicial em "+ Adicionar". LB/RB: lado. A: abre submodal/remove item. Y: detalhe do item do outro.
X: Pronto. B: fecha submodal; fechar trade pede confirmação. Confirmar nunca está em B nem é foco inicial.

### Desktop / tablet / landscape
Dois painéis simétricos rotulados com nome + posição; rodapé com status e ações.

**Camada:** `Modal` (DisplayOrder acima do HUD; CoreUISafeInsets). Submodal de inventário reaproveita `collection.grid-detail`.

## Estados
empty · loading (itens do outro) · pronto/não pronto por lado · oferta alterada (aviso persistente até nova ação) ·
countdown (3…2…1, cancelável) · outro saiu/desconectou (trade cancelado, itens intactos) ·
item intransferível (disabled com motivo) · limite 9/9 (overflow) · inventário cheio do receptor (full, bloqueia confirmação) ·
error de servidor (cancelado com motivo).

## Visual (módulos existentes)
Painéis em nine-slice de pergaminho/madeira (tema), slots com moldura; nomes, contadores, status e
avisos 100% nativos; aviso de alteração com ícone + texto + cor (não só cor).

## Checklist de QA (plano)
- [ ] Alterar oferta em qualquer momento zera Pronto e cancela countdown
- [ ] Desconexão durante countdown
- [ ] Resumo fixo legível no menor phone portrait
- [ ] Fluxo completo só com gamepad; B nunca confirma
- [ ] Nome de jogador longo; idioma longo nos avisos
- [ ] Capturas de todos os estados — **pendentes**

## Memória (registro simulado)
LM-kpets-20261022-01 · nível 1 · `trade.bilateral-confirm` (reflow por abas) · rejeitada: lista única ·
confiança `observed` (BM-05, média) + `heuristic` · decisão humana: pendente (valor estimado) ·
nota: limite de slots é decisão do jogo; benchmark Adopt Me! tem conflito de dados (9 vs 18) registrado.
