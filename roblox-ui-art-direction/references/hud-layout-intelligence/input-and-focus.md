# Input & Focus — gamepad, touch, teclado/mouse

Toda tela navegável declara, no `layout-decision`, como cada input completa **a mesma
tarefa**. Complementa `references/accessibility-and-usability.md`.

## 1. Gamepad / console / TV

Requisitos (por padrão de tela):
- **Foco inicial** definido ao abrir (`GuiService.SelectedObject`), só quando o input
  preferido for gamepad (ou teclado sem touch). `official`
- **Foco visual forte**: contorno/preenchimento contrastante e/ou mudança de tamanho/peso;
  visível sobre qualquer fundo; nunca só um brilho sutil. `heuristic` (XAG 113)
- **Rota previsível**: direção pressionada leva ao vizinho visual; em menus lineares de um
  eixo, considerar loop; grids não precisam de loop. `heuristic` (XAG 112)
- `Selectable = true` só no que é interativo; `NextSelectionUp/Down/Left/Right` quando a
  geometria for ambígua (grids com sidebar, painéis lado a lado, modais). `official`
- **A confirma, B cancela/volta**; Esc equivale a B no teclado. `official` (Gamepad doc) + `heuristic`
- **LB/RB** trocam tabs/lados de forma consistente em todo o jogo. `heuristic` (XAG 112)
- **Modal prende o foco** e o devolve ao elemento de origem ao fechar. `heuristic` (XAG 113)
- **Toda ação alcançável** com 4 direções + Select + Back; ações-chave em **poucos passos**;
  atalhos para ações frequentes. `official` (Console guidelines)
- Sem dependência de hover, drag ou precisão de cursor. Drag pode existir como atalho, com
  alternativa por botão. `heuristic` (GAG)
- Layout em TV-safe area; leitura a ~8–10 ft. `official` (Console guidelines)

```lua
-- Abrir tela: foco inicial conforme input preferido; B/Esc fecha via ContextActionService.
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")
local ContextActionService = game:GetService("ContextActionService")

local function open(screen: GuiObject, first: GuiObject, close: () -> ())
    screen.Visible = true
    if UserInputService.PreferredInput == Enum.PreferredInput.Gamepad then
        GuiService.SelectedObject = first
    end
    ContextActionService:BindActionAtPriority("CloseScreen", function(_, state)
        if state == Enum.UserInputState.Begin then close() end
        return Enum.ContextActionResult.Sink
    end, false, Enum.ContextActionPriority.High.Value, Enum.KeyCode.ButtonB, Enum.KeyCode.Escape)
end

local function closeScreen(screen: GuiObject, returnTo: GuiObject?)
    ContextActionService:UnbindAction("CloseScreen")
    screen.Visible = false
    GuiService.SelectedObject = if returnTo and returnTo.Visible then returnTo else nil
end

UserInputService:GetPropertyChangedSignal("PreferredInput"):Connect(function()
    -- atualizar dicas de botão (ícones A/B vs teclas vs nada no touch) sem perder contexto
end)
```

> Esboço: a política exata (ex.: foco automático também com teclado) é do projeto, e
> `close` deve chamar `closeScreen`. Verifique a API atual no Creator Hub antes de copiar.

## 2. Touch (phone/tablet)

- Respeitar notch, topbar/CoreGui e safe areas (`CoreUISafeInsets`). `official`
- Ações recorrentes perto de controles já usados (ex.: relativas ao jump button), não em
  "% da tela" fixo — zonas de polegar diferem entre phone e tablet. `official` (Position and size)
- CTA essencial **nunca** atrás do joystick ou do jump. `heuristic`
- Alvos grandes, **estacionários** e bem espaçados (≥ ~44–48 px efetivos). `heuristic` (GAG)
- Combate: considerar mão dominante e os controles já existentes; ofereça reposicionamento
  se o jogo tiver muitas ações. `heuristic`
- Gestos (swipe/drag/pinça) só como alternativa a botões. `heuristic`
- Phone com gamepad conectado: tratar gamepad como input principal; touch continua como
  fallback. `official` (Mobile input)

## 3. Teclado e mouse

- Hover é **realce extra**, nunca a única forma de descobrir ou executar.
- Atalhos de teclado exibidos no item (ex.: número da hotbar) quando o input é teclado.
- Tooltips também acessíveis por foco/seleção, não só por hover.

## 4. Dicas de input (prompts)

Mostrar apenas o glifo do input ativo (`PreferredInput`); trocar ao alternar input sem
fechar a tela nem perder seleção. Rótulo textual + glifo; não só ícone.

## 5. Checklist de input (copiar para o layout-review)

- [ ] Mesmo fluxo completo com mouse, touch e gamepad
- [ ] Foco inicial e retorno após fechar modal
- [ ] Foco visível em todos os fundos; nunca em elemento invisível/fora da tela
- [ ] B/Esc fecha/volta em toda tela e modal
- [ ] Nada essencial depende de hover/drag
- [ ] Ações recorrentes em ≤ poucos passos no controle
- [ ] Nada sob joystick/jump/notch/topbar
- [ ] Troca de input atualiza prompts sem perder contexto
