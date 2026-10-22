# Cenário 02 — Inventário com 500+ itens

## Prompt de teste
> Meu simulator de mineração tem 540 tipos de minério e gemas, com variantes brilhantes e duplicatas que podem ser vendidas ou fundidas. O inventário atual é uma grade única sem filtro e todo mundo reclama. Jogadores: 65% celular em pé, 30% PC, 5% console. Usando a skill roblox-ui-art-direction, proponha o novo inventário (fase A) com tudo que um dev precisaria para implementar.

## Entradas disponíveis
Nenhum arquivo. Opcional: o avaliador pode fornecer um print fictício da grade atual — se não houver, a resposta deve tratar a UI atual como desconhecida.

## Entregáveis esperados
layout-decision com escala ilimitada → busca/filtros/ordenação, alternativas (ex.: lista densa vs grade), reflow portrait com Sheet, foco de gamepad no grid, estados (empty, no-results, loading paginado, error, full, venda/fusão pending), ações irreversíveis com confirmação e servidor autoritativo, componentes com pool de células, manifest/atlas, packet JSON.

Rubrica: [../rubrics/02-inventory-500.md](../rubrics/02-inventory-500.md)
