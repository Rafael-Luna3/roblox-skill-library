# Responsive Layout (UI com arte)

Uma tela bonita em 1920×1080 não está pronta. Responsividade não é "diminuir tudo".

## 1. Matriz de viewports obrigatória

| Perfil | Resolução de teste (Device Emulator) | Observar |
|---|---|---|
| Desktop | 1920×1080 e 1366×768 | densidade, espaços vazios |
| Celular paisagem | ~ 844×390 (iPhone 14) / 800×360 | thumbstick/jump, notch, altura |
| Celular retrato (se suportado) | ~ 390×844 | composição empilhada |
| Tablet | ~ 1024×768 / 1180×820 | proporção 4:3 |
| Console/TV | 1920×1080 com overscan e gamepad | distância, foco, safe area |

## 2. Estratégia

1. **Composições explícitas**, não escala única: defina 2–3 arranjos (ex.: narrow / wide)
   por tela e troque com base em `AbsoluteSize` do root (ver `roblox-ui` se disponível).
2. **Scale para posição/região, Offset limitado para detalhes**; `UISizeConstraint` para
   travar mínimos/máximos de painéis; `UIAspectRatioConstraint` para cards e arte que não
   pode deformar.
3. **Arte acompanha a densidade**: `SliceScale` menor em telas pequenas para molduras não
   comerem espaço; ícones com tamanho mínimo; ornamentos opcionais podem sumir em narrow.
4. **Texto**: tamanhos da escala do tema com mínimos por dispositivo; evite `TextScaled`
   global (gera tamanhos inconsistentes) — se usar, sempre com `UITextSizeConstraint`.
5. **Safe areas**: interativos dentro de `ScreenInsets = CoreUISafeInsets`; fundos
   decorativos podem sangrar (`None`/`DeviceSafeInsets` + `IgnoreGuiInset`) sem conteúdo
   essencial nas bordas.
6. **Zonas reservadas no mobile**: thumbstick (inferior esquerdo) e pulo (inferior
   direito), topbar do Roblox, chat. HUD deve recompor, não sobrepor.
7. **Scroll** em vez de encolher: listas longas usam `ScrollingFrame` com
   `AutomaticCanvasSize`.

## 3. `UIScale` com critério

`UIScale` global pode ser útil para normalizar entre 720p e 4K, mas **com limites** e
**depois** de existirem composições. Nunca use para fazer um painel de desktop caber num
celular.

```lua
local function clampScale(viewport: Vector2): number
    local s = math.min(viewport.X / 1280, viewport.Y / 720)
    return math.clamp(s, 0.85, 1.25) -- limites decididos por QA, não universais
end
```

## 4. Arte que não pode esticar

Ilustrações, ícones e personagens: `ScaleType.Fit` ou `UIAspectRatioConstraint`. Somente
molduras nine-slice e texturas `Tile` esticam. Fundos: `Crop`.

## 5. Checklist rápido por viewport

Sem clipping; sem sobreposição com controles do sistema; alvos de toque ≥ 44px
(recomendado ~48px); texto ≥ mínimo do tema; hierarquia ainda clara; painel não ocupa
100% sem motivo; scroll alcança o fim; ornamentos não competem com conteúdo.

## 6. Ver também (v1.1.0)

Reflow por padrão de tela, camadas de ScreenGui, style queries (`@ViewportDisplaySize*`,
`@PreferredInput*`, `@ReducedMotionEnabled*`), ultrawide e condições de breakpoint:
`references/hud-layout-intelligence/responsive-composition.md`. Rotas de foco e zonas de
polegar: `references/hud-layout-intelligence/input-and-focus.md`.
