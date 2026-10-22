# Recipe: `asset-production-only` — produzir/preparar assets

**Modo:** design (assets). Não altera layout nem código.

## Ler
- theme profile (style anchor) · asset manifest existente · matriz imagem/nativo da tela
- `references/image-production.md` · `references/asset-decision-matrix.md`

## Criar/atualizar
asset manifest (status, prompts, nine-slice, atlas, fallback) · prompts prontos ·
arquivos gerados no repositório (se houver ferramenta real) · manual queue de upload.

## Ordem
1. Confirmar que cada asset pedido é de fato imagem (matriz). 2. Style anchor. 3. Prompt/spec por asset.
4. Gerar com ferramenta disponível **ou** marcar `prompt-ready`. 5. Inspecionar e preparar.
6. `validate_asset_manifest.py`. 7. Fila de upload/IDs.

## Entregáveis
Manifest validado; arquivos reais (se gerados) com caminho; prompts; manual queue.
Nenhum AssetId sem upload real.

## Parar quando
Todo asset pedido está `prompt-ready`, `generated`, `approved`, `prepared` ou `uploaded`
com dados coerentes e o validador passa.

## Perguntar ao usuário quando
- o pedido pede texto embutido em imagem ou cópia de arte de terceiros (recusar e propor alternativa);
- não há theme profile e o estilo não pode ser inferido.

## Seguir com hipóteses quando
Dimensões, padding de atlas, `SliceCenter`: usar defaults de `image-production.md` e registrar.
