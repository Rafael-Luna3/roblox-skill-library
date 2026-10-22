# Image Production Pipeline

Etapas A→E. O artefato central é o **Asset Manifest** (`templates/asset-manifest.json`),
salvo no repositório do jogo (sugestão: `docs/ui/asset-manifest.json`). Valide sempre com:

```bash
python <skill>/scripts/validate_asset_manifest.py docs/ui/asset-manifest.json [--root <repo>]
```

## A — Planejamento

Liste somente imagens que a matriz de decisão marcou como B/C/E. Para cada uma:
`id` lógico (`categoria.nome.variante`, ex. `button.primary.default`), finalidade, tema,
tipo (`icon | frame-9slice | button | background | ornament | badge | illustration |
spritesheet | header`), dimensões, proporção, transparência, nine-slice (`SliceCenter`),
estados, origem/direitos, status, caminho local, `robloxAssetId` (só se real).

Reduza a lista: uma moldura nine-slice tintável pode servir 5 painéis; um atlas pode reunir
30 ícones. Menos texturas = menos memória e downloads.

Status permitidos: `planned → prompt-ready → generated → approved → prepared → uploaded`
(+ `rejected`, `pending`). `uploaded` exige `robloxAssetId` numérico real.

## B — Direção de arte (spec + prompt por asset)

Comece com um **bloco de estilo compartilhado** (style anchor) reaproveitado em todos os
prompts do jogo — é o que garante consistência:

```text
STYLE ANCHOR (jogo X): <técnica> (ex.: ilustração cartoon com contorno escuro de 6px,
cel-shading em 2 tons, luz vinda do canto superior esquerdo), paleta <hexes do profile>,
materiais <...>, perspectiva <frontal | 3/4 isométrica>, sem texto, sem letras, sem
marca d'água, sem logotipo, fundo transparente.
```

Prompt por asset = anchor + objeto + uso na UI + composição + restrições:

```text
<STYLE ANCHOR>
Asset: moldura de painel retangular de madeira escura com cantoneiras de ferro rebitadas.
Uso: nine-slice em UI de jogo; as quatro cantoneiras ficam nos 96px de cada canto; as bordas
entre cantos são repetíveis/esticáveis sem ornamentos únicos; o miolo é liso e uniforme.
Composição: vista frontal ortográfica, centralizada, ocupando o canvas inteiro, 1024x1024.
Evitar: texto, ícones, perspectiva, sombras projetadas fora da moldura, ruído no miolo,
elementos assimétricos nas bordas.
```

Checklist do prompt: estilo do jogo; perspectiva coerente com o conjunto; silhueta legível
a 48px (ícones); **nenhum texto**; transparência quando necessária; espaço/margem
apropriados (ícones com ~8–10% de respiro); para nine-slice, cantos autocontidos e bordas
uniformes; para estados, mesma composição mudando só o necessário.

Ícones em lote: mesmo enquadramento, mesma luz, mesma espessura de contorno; gerar a família
junta ou com o primeiro ícone aprovado como referência.

## C — Produção

Verifique a ferramenta **antes** de prometer geração:
- Codex: skill `imagegen` (built-in `image_gen`) — gera PNG com transparência; mova o
  arquivo final para a pasta do projeto (`assets/ui/...`).
- Roblox Studio MCP: `generate_texture`/`store_image`/`upload_image`, se presentes.
- Arte fornecida pelo usuário/artista.

Sem ferramenta: **não finja**. Entregue prompts prontos (status `prompt-ready`), registre
pendências e use placeholders técnicos:
- Nome `PLACEHOLDER_<id>`; atributo `Placeholder = true`; visual claramente provisório
  (ex.: nativo com `UIStroke` tracejado de cor de debug ou cor neutra + rótulo do id no
  modo Studio).
- O QA reprova build com placeholders não aprovados.

Inspecione cada imagem gerada: estilo, perspectiva, ausência de texto/artefatos, alpha
limpo (sem halo), bordas do nine-slice uniformes. Rejeite e itere com **uma mudança por vez**.

## D — Preparação

- **Formato**: PNG 32-bit com alpha para UI; JPG só para fundos opacos grandes.
- **Resolução**: Roblox limita uploads a 1024×1024 (imagens maiores são reduzidas). Produza
  na resolução do maior uso real em tela × ~1,5–2 (densidade mobile), não maior.
  Referência: ícone de grade 128–256px; ícone de HUD 128px; moldura nine-slice 256–512px;
  fundo 1024px. Dimensões pares; potências de 2 ajudam atlas.
- **Nine-slice**: `ScaleType = Slice`, `SliceCenter = Rect.new(left, top, right, bottom)` em
  pixels da imagem; use `SliceScale` para ajustar a espessura da borda por dispositivo sem
  reexportar. Cantos não podem conter detalhe que precise esticar. Documente o rect no
  manifest.
- **Spritesheet/atlas**: ícones do mesmo tamanho em grade (ex.: 8×8 de 128px numa 1024),
  1–2px de padding transparente entre células para evitar bleeding;
  `ImageRectOffset`/`ImageRectSize` por ícone; registre o mapa `id → célula` no manifest.
  Use atlas quando ≥ ~8 ícones sempre carregados juntos; não force atlas para ícones raros.
- **Estados**: preferir variação por propriedade (`ImageColor3`, `ImageTransparency`,
  `UIScale`, `UIGradient`) a texturas extras. Textura extra só quando a forma muda (ex.:
  botão "afundado").
- **Compressão/memória**: remova metadados; evite fundos 1024 duplicados por tela; um
  fundo de 1024² RGBA ≈ 4 MB de memória de textura.
- **Legibilidade pequena**: teste ícone a 32–48px em fundo claro e escuro antes de aprovar.

## E — Integração

- Upload pelo Asset Manager/Creator Hub/Open Cloud **apenas com autorização**; anote o ID
  retornado no manifest (`robloxAssetId`, `status: uploaded`). Note que upload de Decal gera
  um ID de Image diferente — registre o **Image ID** usado em `Image`.
- O código lê IDs do `Theme.Image` (gerado do manifest ou mantido em sincronia).
- Nunca use IDs de exemplo/fictícios como definitivos; nunca dependa silenciosamente de
  imagem inexistente — fallback visível + aviso no relatório.
- Preload seletivo: `ContentProvider:PreloadAsync` apenas do que aparece na primeira tela
  (HUD, moeda, botão principal). Demais telas carregam sob demanda.
- Moderação: assets podem ficar pendentes de moderação; considere isso no QA.

## Direitos

Registre `source` (`generated:<ferramenta>`, `user-provided`, `creator-store:<id>`,
`commissioned`) e `license`. Não use arte de jogos comerciais, fan art de marcas ou assets
sem licença clara.
