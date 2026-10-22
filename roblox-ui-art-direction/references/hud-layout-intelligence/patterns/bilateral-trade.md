# Padrão `trade.bilateral-confirm`

## Metadados

| Campo | Valor |
|---|---|
| ID | `trade.bilateral-confirm` |
| Família | social / economia |
| Arquétipo | ofertas simétricas + estado Ready + confirmação/countdown |
| Problema resolvido | trocar itens sem confundir quem oferece o quê e sem aceitar oferta alterada |
| Tarefa principal | negociar → comparar → confirmar |
| Contexto | menu seguro, com outro jogador |
| Frequência | baixa–média |
| Urgência | média (pressão social) |
| Risco de erro | muito alto (irreversível, alvo de golpes) |
| Itens e crescimento | 1–N slots por lado (limite do jogo) + inventário próprio |
| Densidade de informação | alta |

## Quando usar

- Qualquer troca entre dois jogadores (itens, moedas, pets).

## Quando evitar

- Doação unilateral → fluxo de "enviar presente" com confirmação simples.
- Mercado assíncrono (leilão/listagem) → padrão de comércio com listagens.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Lados lado a lado (simétrico) | desktop/tablet/landscape com largura suficiente |
| Abas "Você / Outro" + resumo fixo | phone portrait |
| Submodal de seleção do inventário | inventário grande; mantém a mesa de trade limpa |

## Vantagens e desvantagens

- ➕ comparação direta; estados explícitos reduzem aceitação acidental.
- ➖ tela densa; mobile exige abas; muitos estados para testar.

## Wireframes

### Desktop

```text
┌ Trade com @Outro ────────────────────────────────┐
│ VOCÊ OFERECE (3/9)        │ @OUTRO OFERECE (2/9)  │
│ [■][■][■][□]...           │ [■][■][□]...          │
│ Valor estimado: 1.2k      │ Valor estimado: 900   │
│ [Adicionar do inventário] │ Status: ✔ Pronto      │
├───────────────────────────┴───────────────────────┤
│ ⚠ Oferta alterada — "Pronto" foi reiniciado      │
│ [Recusar]        [Pronto]   → ambos prontos → [Confirmar (3…2…1)] │
└───────────────────────────────────────────────────┘
```

### Mobile

```text
[Trade com @Outro            ✕]
[Resumo fixo: Você 3 itens ⇄ Outro 2 itens | status]
[Aba: Você] [Aba: @Outro]
grid da aba ativa · [Adicionar]
[Recusar]  [Pronto]   (rodapé fixo, fora de joystick/jump)
```

### Gamepad

```text
LB/RB alterna lado/aba; D-pad nos slots; A abre inventário (submodal) / remove item;
X = Pronto; Y = ver item do outro; B = voltar/fechar submodal; fechar trade pede confirmação.
```

## Reflow responsivo

- Condição: se os dois lados não cabem com cards no mínimo legível → abas + resumo fixo.
- Nomes de jogadores com `AutomaticSize`/truncamento + nome completo no header.
- Rodapé de ações fixo e dentro de `CoreUISafeInsets`.

## Input e foco

- **Toda alteração invalida "Pronto" dos dois lados** e mostra aviso visível. `observed` + `heuristic`
- Confirmação final com countdown curto **após** ambos prontos; countdown cancela se algo mudar.
- Foco inicial em "Adicionar"; nunca em "Confirmar".
- Lados rotulados por texto (nome) e posição; não só por cor.
- Toda a lógica (posse, travamento de itens, troca atômica) é **server-authoritative**.

## Estados

| Estado | Comportamento |
|---|---|
| empty | "Adicione itens ou aguarde a oferta" |
| loading | itens do outro carregando; Pronto desabilitado |
| error | falha → trade cancelado com motivo; itens voltam |
| disabled | item intransferível/bloqueado com motivo; Pronto desabilitado com mesa vazia (regra do jogo) |
| overflow | limite de slots atingido → aviso; inventário com filtros |
| full | inventário do receptor cheio → bloquear confirmação com motivo |
| específicos | Pronto/não pronto por lado; oferta alterada; countdown; outro saiu/reconectou; desequilíbrio (aviso opcional) |

## Image vs Native vs Hybrid

Nativo: estrutura, nomes, contadores, status, botões, avisos. Imagem: ícones de itens, molduras.
Nada de status ou nome rasterizado.

## Anti-padrões

- Uma lista única misturando as duas ofertas.
- Aceitar uma oferta que mudou depois do Pronto.
- Esconder itens da oferta atrás de scroll sem indicador de quantidade.
- Countdown que continua após alteração.
- Confiar no cliente para validar a troca.

## Checklist de QA

- [ ] Alterar oferta zera Pronto dos dois lados e mostra aviso
- [ ] Countdown cancela em qualquer alteração
- [ ] Desconexão/saída do outro cancela com segurança
- [ ] Mobile portrait: resumo fixo mostra os dois lados sempre
- [ ] Gamepad completa trade sem cursor; B nunca confirma
- [ ] Inventário cheio, item intransferível e limite de slots testados

## Benchmarks e confiança

BM-05 (Adopt Me!, texto verificado) — `observed`, confiança média; inclui conflito de limite
de slots. BM-06, BM-03, BM-12 — `observed`, confiança baixa. Segurança: `heuristic` + server-side.
