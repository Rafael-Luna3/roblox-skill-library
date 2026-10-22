# Padrão `settings.hierarchy`

## Metadados

| Campo | Valor |
|---|---|
| ID | `settings.hierarchy` |
| Família | configuração / navegação |
| Arquétipo | categorias + conteúdo (master-detail) |
| Problema resolvido | muitas preferências sem sobrecarga |
| Tarefa principal | configurar |
| Contexto | menu seguro (pode pausar) |
| Frequência | baixa |
| Urgência | baixa |
| Risco de erro | baixo–médio (reset, keybinds) |
| Itens e crescimento | 10–60 opções em 3–8 categorias |
| Densidade de informação | média |

## Quando usar

- Mais de ~8 opções ou opções agrupáveis (áudio, gráficos, controles, acessibilidade, social).

## Quando evitar

- 1–3 toggles → painel simples/popover.

## Alternativas reais

| Alternativa | Quando ganha |
|---|---|
| Sidebar/vertical tabs + conteúdo | desktop/tablet/console |
| Lista de categorias → subpágina | phone portrait |
| Página única com seções | poucas opções (≤ 12) |

## Vantagens e desvantagens

- ➕ escaneável; escala; navegação linear no controle.
- ➖ um nível a mais no mobile.

## Wireframes

### Desktop

```text
[Configurações]                                   [Restaurar padrão]
[Áudio      ] | Música     [────●───] 60%
[Gráficos   ] | Efeitos    [──●─────] 30%
[Controles  ] | Silenciar ao perder foco  [✔]
[Acessibil. ] | (descrição curta da opção focada)
```

### Mobile

```text
[← Configurações]
[Áudio        >]
[Gráficos     >]
toque → subpágina com controles grandes; ← volta
```

### Gamepad

```text
Foco inicial na primeira categoria; → entra no conteúdo; B volta um nível; LB/RB troca categoria;
←/→ ajusta sliders; A alterna toggles.
```

## Reflow responsivo

Sidebar quando a largura comporta labels sem truncar; senão lista → subpágina.
Labels com `AutomaticSize`/wrap (localização). Controles com mínimo de toque.

## Input e foco

- Rótulo textual em toda opção (ícone sozinho não basta).
- Descrição da opção focada visível também no controle (não só tooltip de hover).
- Reset pede confirmação; mudanças aplicadas mostram estado salvo.
- Considere opções de acessibilidade: tamanho de texto (`GuiService.PreferredTextSize`), contraste, reduced motion. `official` + `heuristic`

## Estados

| Estado | Comportamento |
|---|---|
| empty | n/a |
| loading | valores carregando → controles desabilitados |
| error | falha ao salvar → valor anterior + aviso |
| disabled | opção indisponível na plataforma com motivo |
| overflow | categoria longa rola; labels longos quebram linha |
| full | n/a |

## Image vs Native vs Hybrid

Quase tudo nativo; moldura do painel temática (nine-slice) se o tema pedir.

## Anti-padrões

- Modal único com todas as opções e scroll profundo.
- Ícones sem rótulo; descrição só em hover.
- B fecha tudo em vez de voltar um nível.

## Checklist de QA

- [ ] Rota de foco contínua; B volta um nível
- [ ] Sliders/toggles por toque, mouse e controle
- [ ] Labels traduzidos longos
- [ ] Reset e erro de salvamento

## Benchmarks e confiança

AC-02 (XAG 112: rota de volta, consistência) e AC-03 (foco) — `heuristic`. Sem benchmark de jogo.
