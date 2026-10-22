# Padrão `collection.grid-detail`

## Metadados

| Campo | Valor |
|---|---|
| ID | `collection.grid-detail` |
| Família | coleção / inventário |
| Arquétipo | grid filtrável + painel de detalhe |
| Problema resolvido | encontrar, comparar e agir sobre muitos itens (pets, skins, itens, colecionáveis, equipamentos, duplicatas) |
| Tarefa principal | descobrir → comparar → agir (equipar, vender, fundir, favoritar, deletar) |
| Contexto | menu seguro (fora de combate) |
| Frequência | média–alta (várias vezes por sessão) |
| Urgência | baixa |
| Risco de erro | médio (deletar/vender/fundir são irreversíveis) |
| Itens e crescimento | 20+ itens; frequentemente ilimitado |
| Densidade de informação | alta no grid, profunda no detalhe |

## Quando usar

- 20+ itens, ou crescimento contínuo; filtros e detalhes importam. `heuristic`
- Itens com atributos que influenciam a escolha (raridade, nível, stats, variantes).
- Duplicatas existem e precisam de agrupamento (stack "×12") ou ações em lote.

## Quando evitar

- 1–8 itens usados durante gameplay → `collection.hotbar`.
- Itens com slots limitados e comparação contra o equipado → `loadout.slot-catalog`.
- Compra é a tarefa principal → `commerce.catalog-detail`.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Lista com linhas ricas | itens com muito texto e pouca arte |
| Grid sem painel (detalhe em modal) | telas estreitas, detalhe raro |
| Tabs por categoria + grid | poucas categorias estáveis (≤ 6) |

## Vantagens e desvantagens

- ➕ varredura visual rápida; seleção persiste enquanto o detalhe muda; escala com filtros.
- ➖ ocupa muita tela; no mobile exige reflow; foco de gamepad em grids grandes precisa de regras.

## Wireframes

### Desktop

```text
┌ Título ─────────── [Busca____] [Ordenar ▾] [Filtros] ┐
│ Categorias │ Grid rolável (N col)          │ Detalhe   │
│  • Todos   │ [■][■][■][■][■]               │ preview   │
│  • Pets    │ [■][■][■][■][■]               │ stats     │
│  • Itens   │ ...                           │ [Equipar] │
└ Contador 142/500 ── [Seleção múltipla] [Ações em lote]┘
```

### Mobile

```text
[← Título            142/500]
[Busca__________________ ⚙]
[chip][chip][chip][chip] →      (rolagem horizontal)
[■][■][■]
[■][■][■]   (grid 2–3 col, rola)
toque → bottom sheet: preview · stats · [Ação primária] [⋯]
```

### Gamepad

```text
LB/RB: categoria · D-pad: grid · A: abrir ação/equipar · X: filtros · Y: ordenar · B: voltar
Foco inicial: primeiro item (ou o último selecionado). Detalhe acompanha o foco.
```

## Reflow responsivo

- Condição: se o painel de detalhe deixar o grid abaixo do mínimo de colunas/tamanho de card
  do brief → detalhe vira sheet/modal; categorias viram chips.
- Ultrawide: `UISizeConstraint` no root; o grid ganha colunas até um máximo, não células gigantes.
- `UIGridLayout` com `CellSize` calculado por largura; `UIAspectRatioConstraint` no card.
- Scroll: `AutomaticCanvasSize = Y`, `VerticalScrollBarInset = ScrollBar`. `official`
- Coleções muito grandes: paginação ou virtualização (pool de células). `heuristic`

## Input e foco

- Seleção ≠ ação: tocar/clicar seleciona; ação explícita no detalhe (evita equipar sem querer).
- Gamepad: `NextSelection*` entre categorias↔grid↔detalhe; foco não "escapa" do grid ao rolar.
- Busca abre teclado virtual; B/Esc fecha o teclado antes da tela.
- Ações destrutivas em lote: confirmação com contagem e valor.

## Estados

| Estado | Comportamento |
|---|---|
| empty | ilustração + texto do próximo passo ("Abra ovos na Zona 1") |
| empty (filtro) | "Nenhum resultado para X" + limpar filtros |
| loading | skeleton de cards; ações desabilitadas |
| error | mensagem + tentar novamente; inventário anterior não some |
| disabled | item bloqueado/trancado com motivo visível |
| overflow | contador, scroll, paginação; nomes longos com wrap/truncamento + detalhe |
| full | "Inventário cheio 500/500" + caminho (vender, expandir) antes de novas aquisições |

## Image vs Native vs Hybrid

- Nativo: grid, filtros, busca, contadores, textos, seleção, foco.
- Imagem: ícones/arte dos itens (atlas quando sempre carregados juntos), moldura de raridade
  nine-slice tintável. Híbrido: card = moldura imagem + ícone + texto nativo.
- `ViewportFrame` só no detalhe, nunca por célula. Detalhes: `references/asset-decision-matrix.md`.

## Anti-padrões

- Centenas de itens sem busca/filtro/scroll.
- Card gigante por item; scroll infinito sem filtro.
- Painel desktop miniaturizado no celular.
- Raridade só por cor.
- Ação irreversível com um toque no card.

## Checklist de QA

- [ ] Busca, filtros, ordenação e limpar filtros funcionam com 0, 1, 50 e 500+ itens
- [ ] Seleção persiste ao filtrar/rolar (ou é limpa de forma explícita)
- [ ] Card com nome longo/localizado não quebra o grid
- [ ] Detalhe em sheet no portrait; fecha por B/Esc/gesto
- [ ] Foco de gamepad não se perde ao rolar nem ao abrir/fechar detalhe
- [ ] Estados empty/loading/error/disabled/overflow/full capturados
- [ ] Ações irreversíveis confirmadas e validadas no servidor

## Benchmarks e confiança

BM-01, BM-02 (Pet Simulator 99) — `observed`, confiança baixa (imagem não inspecionada).
AC-02 (XAG 112: coleções com filtros/tabs/busca) — `heuristic`. OF-03/OF-04 — `official`.
