# Theme System (Theme Profile)

Cada jogo tem seu **Theme Profile**: documento (`templates/theme-profile.md`) + módulo de
código. A lógica da skill não muda entre jogos; só o profile muda.

## 1. Camadas de tokens

1. **Primitivos** — valores crus: `palette.wood700 = #5A3A22`.
2. **Semânticos** — papéis: `surface.panel`, `text.primary`, `action.primary`,
   `state.danger`, `currency.soft`. Componentes usam **somente** semânticos.
3. **Componente** — variações: `Button.Primary.bg = action.primary`.

Mudar a skin do jogo = trocar primitivos/semânticos, não componentes.

## 2. Conteúdo obrigatório do profile

Nome; descrição estética; paleta + semânticas (incl. success/warning/danger/info, disabled,
foco); tipografia (famílias, pesos, escala de tamanhos, mínimos por dispositivo); espaçamento
(escala, ex.: 4/8/12/16/24/32); raios (ou "chanfro" / "sem canto"); estilo de painel; estilo de
botão por hierarquia (primary/secondary/quiet/destructive); estilo de ícone; tratamento de
imagem (filtros, contorno, sombra embutida ou não); sombras/brilho; motion (durações, easing,
personalidade); estados de interação; raridades **se o jogo tiver**; regras de
responsividade; diretrizes de consistência ("faça / não faça").

Raridades, moedas, facções etc. são **opcionais e definidas pelo jogo** (quantas, nomes,
cores, molduras). Se não existirem, omita a seção.

## 3. Módulo de tema (Luau)

Um único módulo em `ReplicatedStorage` (ou no padrão do projeto). Exemplo de forma — os
valores são ilustrativos e devem vir do profile do jogo:

```lua
--!strict
local Theme = {}

Theme.Color = table.freeze({
    SurfacePanel = Color3.fromHex("#2B2118"),
    TextPrimary = Color3.fromHex("#F4E9D8"),
    ActionPrimary = Color3.fromHex("#C9772B"),
    StateDanger = Color3.fromHex("#B33A2E"),
    Focus = Color3.fromHex("#FFD36A"),
})

Theme.Font = table.freeze({
    Display = Font.new("rbxasset://fonts/families/Merriweather.json", Enum.FontWeight.Bold),
    Body = Font.new("rbxasset://fonts/families/SourceSansPro.json", Enum.FontWeight.Regular),
    Numeric = Font.new("rbxasset://fonts/families/SourceSansPro.json", Enum.FontWeight.Bold),
})

Theme.Space = table.freeze({ xs = 4, sm = 8, md = 12, lg = 16, xl = 24, xxl = 32 })

Theme.Motion = table.freeze({
    Fast = TweenInfo.new(0.08, Enum.EasingStyle.Quad, Enum.EasingDirection.Out),
    Base = TweenInfo.new(0.16, Enum.EasingStyle.Quad, Enum.EasingDirection.Out),
    Panel = TweenInfo.new(0.22, Enum.EasingStyle.Back, Enum.EasingDirection.Out),
})

-- Assets: SÓ ids reais. Pendentes ficam nil e o componente usa fallback nativo visível.
Theme.Image = table.freeze({
    PanelFrame = nil :: string?, -- manifest: panel.frame.default (pending)
})

return table.freeze(Theme)
```

Regras: nada de `Color3.fromRGB` solto em componentes; asset ausente = `nil` + fallback
explícito (não `"rbxassetid://0"`); verifique que fontes usadas existem/estão licenciadas.

## 4. Imagem + tema

- Arte neutra recolorível: desenhe em tons de cinza/branco e aplique `ImageColor3` para
  variar (ex.: botões de cor diferente com a mesma textura). Reduz número de assets.
- Arte pintada (madeira, ouro) não se recolore bem — gere variantes em vez de tingir.
- Registre no profile quais assets são "tintáveis".

## 5. Múltiplos temas no mesmo jogo

Eventos sazonais/skins: mesmo conjunto de semânticos, primitivos alternativos, e tabela
`Theme.Image` alternativa. Troca em runtime só se houver necessidade real; normalmente é
troca em build.
