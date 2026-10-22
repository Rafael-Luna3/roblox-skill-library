# Asset Decision Matrix — Image vs Native vs Hybrid vs 3D

Para **cada elemento** de cada tela, escolha uma estratégia e registre o porquê.

## 1. Estratégias

| Código | Estratégia | Implementação típica |
|---|---|---|
| **A** | Native UI | `Frame`/`TextLabel` + `UICorner`, `UIStroke`, `UIGradient`, layouts |
| **B** | Image Asset | `ImageLabel`/`ImageButton` (ícone, ilustração, ornamento, badge) |
| **C** | Hybrid | arte em imagem (geralmente nine-slice) + texto/estrutura/hit area nativos |
| **D** | ViewportFrame / 3D | modelo real do item/personagem, rotacionável ou com iluminação do jogo |
| **E** | Outro | `CanvasGroup` (fade/clip em grupo), `UIGradient` animado, `SurfaceGui`/`BillboardGui` (UI no mundo), `VideoFrame`, partículas 2D via spritesheet |

## 2. Critérios (pontue 0–2 cada, mentalmente ou na tabela)

| Critério | Favorece imagem (B/C) | Favorece nativo (A) |
|---|---|---|
| Complexidade visual | textura, ilustração, ornamento, bevel pintado | formas geométricas, cor chapada |
| Reutilização | muitas instâncias da mesma arte (custo amortizado) | único e simples |
| Animação | sprite/flipbook, brilho pintado | cor, tamanho, transparência tweenáveis |
| Conteúdo dinâmico | — (texto sempre nativo) | texto, números, listas, progresso |
| Responsividade | nine-slice estica bem; ilustração não | layouts e scale nativos |
| Performance | 1 imagem < 20 frames empilhados | poucas instâncias nativas < textura grande |
| Manutenção | arte estável | tokens mudam frequentemente |
| Acessibilidade | — | texto nativo escala, localiza e tem contraste controlável |
| Coerência com direção | tema material/ilustrado | tema flat/minimalista/tecnológico |

Regra prática: **se precisar de mais de ~4 Frames decorativos sobrepostos para imitar uma
arte, vire imagem**. **Se a imagem conteria texto, número ou algo que muda, separe.**

Para D (ViewportFrame): use quando o item é 3D no jogo, quando rotação/preview agrega
decisão de compra/equipamento, ou quando manter centenas de ícones 2D é inviável. Custo:
renderização — limite quantidade visível simultânea (ex.: só no painel de detalhe, ou
ícones pré-renderizados para a grade). Alternativa: gerar ícones 2D a partir dos modelos.

## 3. Exemplos canônicos

| Elemento | Decisão | Por quê |
|---|---|---|
| Botão temático de madeira com rebites | C | arte nine-slice + `TextLabel` nativo + `ImageButton` hit area + variantes hover/press/disabled (imagem ou `ImageColor3`) |
| Painel de configurações minimalista | A | `Frame` + `UICorner` + `UIStroke` bastam; imagem não agrega |
| Preview rotacionável de espada | D | modelo existe no jogo, rotação ajuda decisão |
| Barra de progresso | A (ou C) | fill nativo `Size` tweenável; trilha/moldura em imagem só se o tema exigir |
| Ícone de moeda | B | identidade + reconhecimento instantâneo |
| Valor da moeda | A | dinâmico |
| Moldura de raridade | C | nine-slice da moldura; cor/brilho por `ImageColor3`/`UIGradient` se a arte for tintável |
| Fundo decorativo de tela cheia | B (com cuidado) | uma imagem com `ScaleType.Crop`, sem conteúdo essencial nas bordas |
| Header ilustrado com título | C | faixa/ornamento em imagem; título em `TextLabel` (localizável) |
| Divisor simples | A | `Frame` de 1–2px |
| Divisor ornamentado | B | imagem fina, `ScaleType.Fit` ou nine-slice horizontal |
| Tooltip | A | conteúdo dinâmico, deve ser leve |
| Badge/medalha de conquista | B | arte única |
| Cursor de seleção (gamepad) | C/E | `SelectionImageObject` com arte do tema |

## 4. Formato de registro (por tela)

```markdown
| Elemento | Estratégia | Asset(s) do manifest | Justificativa | Fallback se asset pendente |
|---|---|---|---|---|
| Painel raiz | C | panel.frame.default | moldura ornamentada; nine-slice | Frame + UIStroke na cor surface.border |
| Título | A | — | texto localizável | — |
| Ícone moeda | B | icon.currency.soft | identidade | círculo nativo + letra, marcado PLACEHOLDER |
```

## 5. Anti-padrões

- **Tudo nativo** num jogo ilustrado → parece protótipo.
- **Tudo imagem** → tela inteira num PNG; sem responsividade, sem localização, sem estados.
- Texto "COMPRAR" pintado no botão → impossível localizar/alterar.
- Ícones diferentes para hover/press quando `ImageColor3`/escala resolveriam.
- ViewportFrame em cada célula de uma grade de 200 itens.

## 6. Relação com HUD Layout Intelligence (v1.1.0)

As fichas em `references/hud-layout-intelligence/patterns/` indicam a estratégia típica de
cada padrão; a decisão por elemento continua sendo feita **aqui**, depois do
`layout-decision` da tela.
