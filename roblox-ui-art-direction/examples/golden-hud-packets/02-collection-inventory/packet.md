# Golden packet 02 — Inventário/coleção de grande escala

> **FICTÍCIO · documentação sem captura · veredito visual: pendente — sem captura.**
> Jogo inventado ("Field Atlas"). Sem assets gerados, sem AssetIds, sem playtest.
> JSON: [packet.json](packet.json).

## Brief resumido
- **Jogo:** exploração/coleção naturalista — o jogador captura e cataloga insetos em biomas; 820 espécies × variantes (cor, tamanho, "raro de estação"); duplicatas viram doação ao museu.
- **Público:** 10–16 e adultos casuais; 60% mobile (portrait e landscape), 35% desktop, 5% console.
- **Tom:** calmo, curioso, colecionador. **Pilares:** *caderno de campo* (papel, tinta, etiquetas), *densidade legível* (muitas linhas com dados), *descoberta pelo lugar* (bioma importa).
- **Não é:** cartoon saturado, gamificado com brilhos, glassmorphism.

## Theme profile resumido
| Token | Valor (fictício) |
|---|---|
| surface.page | papel `#F4EEDD`; linhas de caderno em textura `Tile` |
| text.primary | tinta `#2A2620`; secondary `#6B6255` |
| accent.select | marca-texto `#F2D46B` (seleção) + borda tracejada (sinal não cromático) |
| rarity | **não usa cor**: carimbos "comum/incomum/raro/estação" em texto + ícone de lupa 1–4 |
| Fontes | Display `Enum.Font.Merriweather` · Body `Enum.Font.SourceSans` (fonte manuscrita descartada: pouco legível em lista densa) |
| Motion | flutuante e curta (`Sine` 0.15 s); páginas não "viram" |
| Style anchor | "ilustração científica a nanquim com aquarela leve, inseto em vista dorsal, fundo transparente, sem texto" |

## Layout decision
| # | Resposta |
|---|---|
| 1 | comparar → agir (doar duplicata, fixar no diário, ver habitat) |
| 2 | menu seguro (diário aberto pausa a captura) |
| 3 | não |
| 4 | várias vezes por sessão; baixa urgência |
| 5 | 820 espécies; até ~3.000 entradas com variantes; crescimento com eventos |
| 6 | busca por nome, filtros (bioma, raridade, possuído/faltando, estação), ordenação (nº, nome, data) |
| 7 | sim: dados do espécime, onde/quando foi capturado, comparação de 2 variantes |
| 8 | médio: doar duplicatas é irreversível |
| 9 | phone portrait/landscape, tablet, desktop, ultrawide, console |
| 10 | tela cheia permitida |
| 11 | A |
| 12 | empty (diário novo), filtro sem resultado, loading paginado, erro de carga, faltando (silhueta), cheio de duplicatas, doação pendente |

**Escolhido:** `collection.grid-detail` na **variante lista densa** (linhas com miniatura + dados), não grade de cards — o atributo decisivo aqui é dado textual (bioma, data, tamanho), não a arte grande.
**[aprovação humana]:** lista densa como padrão com alternância "grade" opcional.

## Screen spec
**Hierarquia:** (1) miniatura + nome + possuído/faltando; (2) bioma, raridade (carimbo), nº de duplicatas; (3) ficha completa, mapa de ocorrência, comparação.
**Zonas:** nenhuma de gameplay (menu); respeitar topbar/notch.
```text
DESKTOP
[Diário de Campo  412/820] [Busca______] [Bioma ▾][Raridade ▾][Faltando ☐][Ordenar ▾]
| nº | ▣ | Nome            | Bioma    | Carimbo | Dup. |   | FICHA                     |
| 031| ▣ | Besouro-joia    | Floresta | RARO 🔍3| ×4   |   | ilustração · dados        |
| 032| ░ | ??? (faltando)  | Pântano  | —       |  —   |   | [Fixar] [Doar 3 dup.]     |
                                       [Comparar: ▣ ▣  →]   (bandeja de comparação)

PHONE PORTRAIT
[← Diário 412/820] [🔍] [⚙ filtros]
[chips: Todos · Faltando · Floresta · Pântano →]
| ▣ Besouro-joia  RARO ×4 |
| ░ ???  Pântano          |   (linhas de 64 px, scroll virtualizado)
toque → Sheet: ilustração · dados · [Fixar] [Doar]

GAMEPAD/TV
LB/RB bioma · D-pad linhas · A abre ficha · X filtros · Y comparar · B fecha ficha → fecha diário
```
**Gatilhos:** R1 largura útil < 2× largura mínima da ficha → ficha vira Sheet; R2 `ViewportDisplaySize == Small` → colunas Bioma/Dup. somem da linha (vão para a ficha); R3 > 400 linhas filtradas → paginação de 100 + contador.
**Camadas:** `JournalGui` Menu DO 20 · `DonateConfirmGui` Modal DO 30.

## Component inventory
| ID | Tipo | Função visual |
|---|---|---|
| row-specimen | ItemCard (variante linha) | linha densa com miniatura, nome, carimbo, duplicatas |
| sheet-detail | Sheet | ficha do espécime no narrow |
| panel-detail | Panel | ficha no wide |
| tabs-biome | Tab | escopo por bioma |
| compare-tray | Custom | bandeja de até 2 espécimes para comparar lado a lado |
| empty-journal | EmptyState | diário vazio com próximo passo |
| skeleton-rows | LoadingSkeleton | linhas reservadas na paginação |
| err-load | ErrorState | falha de carga com tentar de novo |
| donate-footer | ConfirmationFooter | resumo e confirmação de doação |
| focus-ring | FocusRing | foco tracejado de alto contraste |

## State matrix
| Estado | Texto | Ação | Cor/ícone | Foco | Rede | Recovery | Captura |
|---|---|---|---|---|---|---|---|
| empty | "Seu diário está vazio. Capture um inseto no Bosque Inicial." | Ir ao mapa | ilustração de rede | botão | — | — | sim |
| loading | — (skeleton) | ações off | linhas cinza | mantém última posição | página sob demanda | timeout → error | sim |
| error | "Não foi possível abrir esta página do diário." | Tentar de novo | ícone ⚠ + texto | botão retry | — | refetch; linhas já carregadas permanecem | sim |
| disabled | "Doação indisponível: espécime fixado" | — | cadeado + texto | item focável, ação off | — | desafixar | sim |
| pending | "Doando 3…" | bloqueada | ampulheta | footer | aguarda servidor | erro → error | sim |
| overflow | "Mostrando 1–100 de 1.212" | próxima página | contador | foco na última linha | paginação | — | sim |
| full | "Coleção completa neste bioma" | ver outro bioma | carimbo "COMPLETO" | — | — | — | sim |
| no-results | "Nada para 'besoro'. Você quis dizer 'besouro'?" | limpar filtros | — | botão limpar | busca local | — | sim |
| missing | "???" com silhueta + bioma | ver habitat | silhueta | linha focável | — | — | sim |

## Implementation handoff
```text
StarterGui
├── JournalGui (DO 20, CoreUISafeInsets, ResetOnSpawn=false)
│   └── Root → Header(Search, Filters, Counter) · BiomeTabs · List(ScrollingFrame, pool de 30 linhas) · Detail
└── DonateConfirmGui (DO 30, Enabled=false)
```
- Módulos: `UI/Theme`, `UI/Components/SpecimenRow` (pool), `UI/Components/DetailSheet`, `JournalController`, servidor `CollectionService` (doar, fixar).
- Dados: `{entries: {id: string, owned: boolean, biome: string, rarity: "common"|"uncommon"|"rare"|"seasonal", dupes: number, pinned: boolean, caughtAt: number?}[], page: number, total: number}`.
- Intenções: `DonateDuplicates(id, count)` (servidor valida posse, contagem, não fixado; atômico) · `TogglePin(id)`.
- Ordem: Theme → SpecimenRow + pool → List com busca/filtros locais → Detail (Panel/Sheet por R1) → estados → paginação → doação com confirmação → arte.

## Asset matrix
| Elemento | Estratégia | Asset (status) | Fallback |
|---|---|---|---|
| fundo de papel | Image `Tile` | texture.paper.lines (planned) | Frame cor papel |
| miniaturas das espécies | Image (atlas por bioma, 128 px) | atlas.specimens.forest … (planned) | silhueta genérica nativa |
| carimbos de raridade | Native (texto + ícone) | icon.magnifier (planned) | texto apenas |
| ficha (ilustração grande) | Image sob demanda | — gerada por espécie, fora do escopo A | miniatura ampliada |

## Packet JSON
[packet.json](packet.json).

## Plano de capturas
Phone portrait 390×844 (lista, Sheet aberto, sem resultados), phone landscape, tablet, desktop com ficha lateral, ultrawide (root limitado), console com foco em linha e na bandeja. Estados da matriz. Texto localizado longo (alemão) em nomes.

## Decisões rejeitadas
- **Grade de cards grandes** — 820+ itens com dados textuais decisivos; cards escondem bioma/data e exigem mais scroll.
- **Navegação por mapa (`map.minimap-fullmap`) como entrada principal** — bom para descoberta, ruim para gerir duplicatas; vira atalho "ver habitat" dentro da ficha.
- **Slots de exposição (`loadout.slot-catalog`)** — o museu tem só 3 vitrines; tratado como recurso secundário, não como a tela.

## Pendências reais
- [aprovação humana] lista densa como padrão.
- Nenhuma captura; nenhum asset produzido.
- Fonte: confirmar no Studio que `Merriweather` e `SourceSans` estão disponíveis na versão do projeto.
- Regra de negócio da doação (recompensa, limite diário) inexistente — fictícia aqui.
