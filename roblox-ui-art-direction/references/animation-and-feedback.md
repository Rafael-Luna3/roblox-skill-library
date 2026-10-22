# Animation & Feedback (Game Feel)

Movimento reforça o tema e comunica estado. Não decora por decorar.

## 1. Personalidade de motion por tema (escolha no profile)

| Personalidade | Easing típico | Durações | Combina com |
|---|---|---|---|
| Elástica / brincalhona | `Back` Out, `Elastic` raro | 0.12–0.3s | cartoon, arcade, infantil |
| Pesada / física | `Quad`/`Cubic` Out, pequeno overshoot | 0.18–0.35s | medieval, fantasia, tycoon industrial |
| Mecânica / precisa | `Linear`/`Quint` Out, steps | 0.08–0.2s | sci-fi, tático, minimalista |
| Flutuante / suave | `Sine` InOut | 0.25–0.5s | calmo, social, mágico |
| Seca / tensa | cortes rápidos, flicker raro | 0.05–0.15s | horror, competitivo |

Não use efeitos futuristas (scanlines, glitch) num jogo medieval, nem bounce em horror,
sem justificativa estética registrada.

## 2. Catálogo de interações (adaptar ao tema)

| Evento | Padrão | Notas |
|---|---|---|
| Hover | cor/brilho leve, escala 1.0→1.03 | só em dispositivos com ponteiro |
| Press | escala 0.94–0.97, escurecer | imediato (≤ 0.08s) |
| Release | volta ao hover | ação dispara em `Activated` |
| Entrada de painel | fade + deslocamento 8–24px ou escala 0.95→1 | um tween no root (CanvasGroup) |
| Saída de painel | mais rápida que a entrada (~70%) | esconder após terminar |
| Notificação | entra pelo lado/topo, permanece, sai | fila; não empilhar infinitamente |
| Recompensa | anticipação → revelação → contagem numérica → ícones voam ao contador | pular com toque; respeitar reduced motion |
| Seleção | moldura/realce de seleção do tema | também para gamepad |
| Mudança de aba | indicador desliza; conteúdo cross-fade curto | sem animar cada célula |
| Equipar item | pulso no slot + check | confirmação do servidor antes do estado final |
| Erro | shake curto (≤ 3 ciclos, ≤ 6px) + cor de perigo + mensagem | nunca só cor |
| Sucesso | pulso + cor de sucesso + som | breve |

## 3. Regras

- Uma animação por limite de estado; não animar cada descendente separadamente.
- Interrompível: cancele o tween anterior antes de iniciar outro no mesmo alvo.
- Sem loops perpétuos chamativos; brilhos contínuos só em elementos realmente raros/CTA,
  e pausados quando fora de tela.
- Feedback imediato para input; estado definitivo só após resposta do servidor
  (mostre *pending*: spinner temático, botão desabilitado).
- Som de UI coerente com o tema (madeira, metal, bip, papel) — se o projeto tiver áudio.

## 4. Movimento reduzido

```lua
local GuiService = game:GetService("GuiService")
local function play(target: Instance, info: TweenInfo, goal: {[string]: any})
    if GuiService.ReducedMotionEnabled then
        for k, v in goal do (target :: any)[k] = v end
        return nil
    end
    local t = game:GetService("TweenService"):Create(target, info, goal)
    t:Play()
    return t
end
```

Com reduced motion: trocas instantâneas ou fades curtos; sem shake, parallax, zoom grande.
