# Roblox UI Implementation

Foco: transformar direção + assets em UI real, mantendo arte e estrutura separadas.
(Se a skill `roblox-ui` estiver disponível, ela cobre em profundidade lifecycle,
navegação e layout; aqui está o que é específico de UI **com arte**.)

## 1. Antes de construir

- Respeite a arquitetura do projeto: instâncias autorais no Studio/Rojo, React-lua, Fusion,
  Roact, ou módulos próprios. Não troque o paradigma do projeto.
- Prefira **shell autoral persistente** (ScreenGuis em `StarterGui`, `ResetOnSpawn = false`
  quando apropriado) com conteúdo repetido gerado de templates. Evite destruir e recriar
  hierarquias grandes a cada abertura; alterne `Visible`/`Enabled`.
- Não modifique GUIs/scripts existentes fora do escopo pedido.

## 2. Separação de responsabilidades

```text
ReplicatedStorage/UI
├── Theme           (tokens + Theme.Image com IDs reais)
├── Components      (Button, Panel, ItemCard, CurrencyPill, ProgressBar...)
└── Screens         (controllers: estado → visual; escuta eventos)
StarterGui
└── <Tela>Gui (ScreenGui) → Root → regiões nomeadas por papel
```

- **Aparência**: Theme + componentes (só leem tokens).
- **Estado**: tabela de view-state por tela (aberto, aba, seleção, loading, erro).
- **Dados**: vindos de módulos/replicação; UI não é fonte da verdade.
- **Interação**: `Activated`, foco, atalhos — chamam intents.
- **Rede**: intents viram `RemoteFunction/RemoteEvent` validados no servidor. O cliente
  mostra *pending* e só confirma visualmente após resposta. Nunca debite/credite no cliente.

## 3. Receitas de componente com arte

### Painel nine-slice com conteúdo nativo

```text
Panel (ImageLabel)  Image=Theme.Image.PanelFrame, ScaleType=Slice,
│                   SliceCenter=Rect.new(96,96,928,928), SliceScale=0.5,
│                   BackgroundTransparency=1
├── UIPadding       (>= espessura visual da borda * SliceScale)
├── Header (Frame)  → Title (TextLabel, Theme.Font.Display)
└── Body (Frame)    → layouts e conteúdo
```

### Botão híbrido com estados

```text
PrimaryButton (ImageButton)  Image=Theme.Image.ButtonPrimary, ScaleType=Slice,
│                            AutoButtonColor=false (estados controlados pelo componente)
├── UIScale                  (press: 0.96)
├── Icon (ImageLabel)        opcional
└── Label (TextLabel)        texto nativo, TextScaled=false + UITextSizeConstraint/AutomaticSize
```

```lua
local function bindStates(button: ImageButton, palette)
    local scale = button:FindFirstChildOfClass("UIScale") :: UIScale
    local function render(state: "idle" | "hover" | "press" | "disabled")
        button.ImageColor3 = palette[state]
        scale.Scale = if state == "press" then 0.96 else 1
    end
    button.MouseEnter:Connect(function() if button.Active then render("hover") end end)
    button.MouseLeave:Connect(function() if button.Active then render("idle") end end)
    button.MouseButton1Down:Connect(function() if button.Active then render("press") end end)
    button.MouseButton1Up:Connect(function() if button.Active then render("hover") end end)
    button.SelectionGained:Connect(function() render("hover") end)
    button.SelectionLost:Connect(function() render("idle") end)
    render(if button.Active then "idle" else "disabled")
end
-- A ação vai em button.Activated (mouse, toque e gamepad).
```

### Ícones de atlas

```lua
local function setAtlasIcon(img: ImageLabel, atlasId: string, cell: Vector2, cellSize: number)
    img.Image = atlasId
    img.ImageRectOffset = cell * cellSize
    img.ImageRectSize = Vector2.new(cellSize, cellSize)
end
```

### Moldura de raridade (se o jogo tiver)

Uma moldura nine-slice neutra + `ImageColor3` da raridade (tokens do jogo) + `UIGradient`
opcional para brilho. Raridades e cores vêm do profile; nada hardcoded na skill.

### Fallback de asset pendente

```lua
local function applyImageOrFallback(img: ImageLabel, id: string?, fallback: () -> ())
    if id then
        img.Image = id
    else
        img.Image = ""
        img:SetAttribute("Placeholder", true)
        fallback() -- ex.: BackgroundTransparency=0 + UIStroke de debug
        warn(("[UI] asset pendente em %s"):format(img:GetFullName()))
    end
end
```

## 4. Instâncias e propriedades-chave

`ScreenGui` (`IgnoreGuiInset`, `ScreenInsets`, `ZIndexBehavior=Sibling`, `DisplayOrder`),
`Frame`, `ImageLabel`/`ImageButton` (`ScaleType` Stretch/Slice/Tile/Fit/Crop,
`SliceCenter`, `SliceScale`, `TileSize`, `ImageRectOffset/Size`, `ImageColor3`,
`ResampleMode` — `Pixelated` para pixel art), `TextLabel`/`TextButton` (`FontFace`,
`RichText` com moderação, `TextWrapped`, `AutomaticSize`), `ScrollingFrame`
(`AutomaticCanvasSize`, `ScrollingDirection`, `ScrollBarImageColor3` temático),
`ViewportFrame` (+ `WorldModel` se precisar de animação; `Ambient`/`LightColor` do tema),
`CanvasGroup` (fade de grupo; custo de memória — use para painéis, não para cada célula),
`UIListLayout`, `UIGridLayout`, `UIPadding`, `UIScale`, `UIAspectRatioConstraint`,
`UISizeConstraint`, `UITextSizeConstraint`, `UICorner`, `UIStroke`
(`ApplyStrokeMode` Contextual/Border), `UIGradient`, `AnchorPoint`, Scale+Offset, `ZIndex`,
`GuiService` (seleção), `TweenService`, `ContentProvider`.

## 5. Ordem de construção recomendada

1. Theme module + componentes base (Panel, Button, Text styles) com fallbacks.
2. Shell da tela (regiões) com layouts — sem arte, validando responsividade.
3. Aplicar arte (assets aprovados) e estados.
4. Conteúdo dinâmico (templates + dados mock locais; remover mocks antes da entrega).
5. Motion e feedback.
6. QA visual (captura) → iterar.

## 6. Performance de UI com arte

- Reutilize células de lista (pool) em grades grandes; evite `ViewportFrame` por célula.
- Limite `CanvasGroup` simultâneos; evite `UIGradient` animado em dezenas de elementos.
- Não anime propriedades a cada frame sem necessidade; prefira tweens pontuais.
- Desconecte conexões e cancele tweens ao fechar/destruir.
