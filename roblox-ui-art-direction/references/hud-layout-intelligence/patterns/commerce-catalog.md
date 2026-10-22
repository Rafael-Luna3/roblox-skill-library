# Padrão `commerce.catalog-detail`

## Metadados

| Campo | Valor |
|---|---|
| ID | `commerce.catalog-detail` |
| Família | comércio / loja |
| Arquétipo | categorias + grid/lista + detalhe + confirmação |
| Problema resolvido | descobrir e comprar com clareza de preço, moeda e resultado |
| Tarefa principal | descobrir → avaliar → confirmar compra |
| Contexto | menu seguro |
| Frequência | média |
| Urgência | baixa |
| Risco de erro | alto (gasto de moeda/Robux) |
| Itens e crescimento | 10–200; rotações/ofertas temporárias |
| Densidade de informação | média |

## Quando usar

- Várias categorias (moedas, Robux, passes, bundles, cosméticos, upgrades).
- Preço, moeda e o que se recebe precisam ser comparados.

## Quando evitar

- Oferta única → card/modal de oferta simples com CTA.
- Upgrades em árvore com pré-requisitos → `progression.upgrade-craft-tree` (pattern-catalog.md).

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Cards horizontais em destaque + "ver tudo" | poucas ofertas curadas |
| Lista com linhas | itens de texto/estatística (upgrades numéricos) |
| Tabs + grid sem painel (detalhe em modal) | mobile-first |

## Vantagens e desvantagens

- ➕ preço e resultado claros; categorias reduzem busca; detalhe evita compra cega.
- ➖ mais passos; requer cuidado para não virar padrão manipulativo.

## Wireframes

### Desktop

```text
[Loja]                         [Saldo: 🪙 12.400] [💎 35]
[Categorias] | [Grid de produtos ■■■■] | [Detalhe: arte, o que recebe, preço, posse]
                                        | [Comprar 🪙 2.500]  (desabilitado se saldo < preço, com motivo)
```

### Mobile

```text
[← Loja       🪙12.400 💎35]
[tab][tab][tab][tab] →
[■][■]  (grid 2 col)
toque → modal/sheet: arte · o que recebe · preço · [Comprar] [Cancelar]
```

### Gamepad

```text
LB/RB categorias · D-pad grid · A abre detalhe · A em [Comprar] abre confirmação · B volta
Foco inicial: primeira categoria ou destaque.
```

## Reflow responsivo

- Sidebar de categorias só se a largura comportar grid legível; senão tabs/chips. `heuristic`
- Saldo sempre visível no header (não some no scroll).
- Confirmação como modal com `UISizeConstraint`, centrado, botões grandes.

## Input e foco

- Compra nunca no primeiro toque do card; sempre detalhe/confirm proporcional ao valor.
- Robux: fluxo nativo (`MarketplaceService`); botão de compra não ocupa a posição de "fechar".
- Confirmação: foco inicial em **Cancelar** para itens caros/irreversíveis (`heuristic`, decisão do projeto).

## Estados

| Estado | Comportamento |
|---|---|
| empty | categoria sem itens → "volta em X" ou ocultar categoria |
| loading | skeleton; botão comprar em *pending* durante a transação |
| error | falha de compra com motivo; saldo não muda no cliente |
| disabled | saldo insuficiente (mostra quanto falta + caminho), requisito de nível |
| overflow | scroll + filtros; preços longos/abreviados com valor completo no detalhe |
| full | já possuído → "Possuído/Equipar" em vez de "Comprar" |

## Image vs Native vs Hybrid

Imagem: arte do produto, ícones de moeda, banners de oferta (sem texto embutido).
Nativo: preço, saldo, tabs, botões, timers de oferta. Híbrido: card com moldura + preço nativo.

## Anti-padrões

- Compra de um toque sem moeda/preço/resultado.
- Timer ou escassez falsos; botão de compra onde antes era "fechar".
- Preço em imagem (impede localização e atualização).
- Cliente debitando saldo antes da resposta do servidor.

## Checklist de QA

- [ ] Preço + moeda + o que recebe visíveis antes da confirmação
- [ ] Saldo insuficiente, item possuído, falha de rede testados
- [ ] Confirmação com A/B, toque e mouse; B/Esc cancela
- [ ] Preço localizado/formatado não corta
- [ ] Saldo atualiza só após confirmação do servidor

## Benchmarks e confiança

Sem benchmark visual verificado nesta versão (`hypothesis` para a disposição exata).
AC-01 (indicar interatividade, contraste) — `heuristic`. OF-01 (DisplayOrder para modal) — `official`.
