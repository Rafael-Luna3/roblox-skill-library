# Recipe: `review-existing-hud` — revisar HUD existente

**Modo:** review. Não altera nada sem pedido.

## Ler
- a UI real e capturas fornecidas/feitas · o pacote da tela, se existir
- `references/visual-qa.md` · `templates/layout-review.md` · `references/hud-delivery-contract.md` (seção 4)
- ficha do padrão usado · `input-and-focus.md` · `responsive-composition.md`

## Criar/atualizar
visual-review + layout-review + evidence board (separando evidência de referência de
evidência de QA do projeto) + lista priorizada de problemas + registro de memória (opcional).

## Ordem
1. Identificar padrão e tarefa da tela. 2. Capturar (ou listar capturas necessárias).
3. Checklist de composição e estética. 4. Classificar problemas (bloqueante/alto/polimento) com evidência.
5. Recomendar correções concretas (componente, estado, plataforma).

## Entregáveis
Relatório com veredito (`aprovado`, `aprovado com ressalvas`, `reprovado`, `pendente — sem captura`),
problemas com localização e correção sugerida, capturas usadas (caminhos reais) ou faltantes.

## Parar quando
Todos os viewports/inputs declarados foram verificados ou registrados como não verificados.

## Perguntar ao usuário quando
Não há acesso à UI nem capturas — pergunte se ele fornece capturas ou se a revisão deve ser só documental.

## Seguir com hipóteses quando
A tarefa principal da tela é óbvia pelo conteúdo; registre a inferência.
