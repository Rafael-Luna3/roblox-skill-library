# Rubrica 01 — HUD de combate mobile

Prompt: [../prompts/01-mobile-combat-hud.md](../prompts/01-mobile-combat-hud.md) · Sinais gerais: [../expected-signals.md](../expected-signals.md)

## Erros críticos (qualquer um reprova)
- habilidades ou vida posicionadas sob o joystick/botões de ataque no phone landscape
- centro da tela ocupado por painéis permanentes
- AssetId numérico ou captura alegada
- estética genérica sci-fi/neon ignorando sumi-e
- AssetId numérico, captura, teste ou aprovação visual alegados sem evidência real
- benchmark popular apresentado como prova de eficácia

## Rubrica (0–2 por critério)
| # | Critério | Âncoras | Nota |
|---|---|---|---|
| 1 | Decisão de layout justificada | 0: só descreve elementos; 1: escolhe padrão sem alternativas; 2: ≤3 alternativas com rejeição motivada | |
| 2 | Responsividade (reflow real) | 0: desktop encolhido; 1: menciona mobile sem composição; 2: composição phone landscape própria com gatilho | |
| 3 | Gamepad/touch | 0: ignora touch/gamepad; 1: cita sem detalhar; 2: posições relativas aos controles touch + glifos de gamepad | |
| 4 | Identidade visual | 0: genérica; 1: cores de tinta sem forma/material; 2: pinceladas/papel em molduras e ícones com legibilidade preservada | |
| 5 | Estados | 0: sem matriz; 1: estados parciais; 2: matriz completa com KO/fim de round/cooldown e recovery | |
| 6 | Implementabilidade | 0: vago; 1: estrutura sem dados; 2: ScreenGuis, DisplayOrder, dados replicados e ordem de implementação | |
| 7 | Asset safety | 0: inventa IDs; 1: IDs nulos sem fallback; 2: IDs nulos + fallback + manifest | |
| 8 | QA honesto | 0: aprova sem captura; 1: omite veredito; 2: pendente — sem captura + plano de capturas | |
| 9 | Ausência de invenções | 0: inventa API/teste; 1: pequenas imprecisões; 2: nenhuma invenção | |

## Sinais de resposta genérica ou alucinação
Ver `expected-signals.md`; específicos deste cenário: os erros críticos acima e qualquer
solução que não use os dados do prompt (público, plataformas, tema).

## Aprovar / reprovar
Aprova com total ≥ 14/18, nenhum erro crítico e nota ≥ 1 nos critérios 7, 8 e 9.
Resultado: <não executado | aprovado | reprovado> · Data: <> · Modelo: <> · Condição: <com skill | baseline>
