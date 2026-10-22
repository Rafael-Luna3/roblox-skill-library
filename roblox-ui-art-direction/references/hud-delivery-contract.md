# HUD Delivery Contract

**"Layout escolhido" não é uma entrega.** Uma entrega de HUD/tela é aceita quando outro
agente ou desenvolvedor consegue implementá-la **sem redescobrir decisões fundamentais**
(o que mostrar, onde, em que ordem, em que estados, com quais componentes, quais assets,
quem valida o quê no servidor e como provar que ficou certo).

Este contrato define o pacote mínimo por tela. Cada item aponta para o template que o
produz; não há regra nova aqui que já exista em outra referência — o contrato só diz
**o que precisa existir e quando**.

## 1. Os 11 artefatos

| # | Artefato | Produzido por | Responde |
|---|---|---|---|
| 1 | Context snapshot | `templates/design-brief.md` (resumo) + `templates/theme-profile.md` (resumo) + memória do projeto | para quem, em que jogo, em que estilo, com que restrições |
| 2 | Layout decision | `templates/layout-decision.md` | qual padrão, por quê, o que foi rejeitado |
| 3 | Screen spec | `templates/hud-screen-spec.md` | objetivo, hierarquia em 3 níveis, zonas, camadas, riscos |
| 4 | Composition por plataforma | seção do screen spec | wireframe + gatilho de reflow por plataforma suportada |
| 5 | Component inventory | `templates/component-contract.md` (1 por componente não trivial) + lista no screen spec | quais peças, com que estados e responsabilidade |
| 6 | State matrix | `templates/state-matrix.md` | o que a tela faz em cada estado e como se recupera |
| 7 | Image/native matrix | tabela por elemento (`references/asset-decision-matrix.md`) | o que é arte, o que é estrutura |
| 8 | Asset manifest | `templates/asset-manifest.json` | quais imagens existem/faltam, com IDs reais ou `null` |
| 9 | Implementation handoff | `templates/implementation-handoff.md` | árvore, módulos, dados, cliente×servidor, ordem, comandos |
| 10 | QA evidence plan | `templates/evidence-board.md` + `templates/layout-review.md` | o que precisa ser capturado e o que é só referência |
| 11 | Manual action queue | seção do handoff | uploads, aprovações, capturas, IDs que só humanos podem fazer |

Versão estruturada mínima: `templates/hud-packet.example.json` validada por
`scripts/validate_hud_packet.py` contra `schemas/hud-spec.schema.json`.

## 2. Obrigatoriedade por fase

Legenda: **R** obrigatório completo · **P** obrigatório, pode ter itens marcados `pendente` com dono ·
**—** não exigido nesta fase · **U** atualizar o que mudou.

| Artefato | Fase A (layout + estático) | Fase B (motion) | Fase C (áudio) | Fase D (polimento/QA) |
|---|---|---|---|---|
| 1 Context snapshot | R | U | U | U |
| 2 Layout decision | R | — (reabrir só voltando à A) | — | — |
| 3 Screen spec | R | U (tokens de motion) | U (eventos sonoros) | R |
| 4 Composition por plataforma | R | — | — | R (verificada) |
| 5 Component inventory | R (estados visuais estáticos) | R (transições por estado) | P (som por estado) | R |
| 6 State matrix | R | U (motion por estado + reduced motion) | U (som por estado) | R |
| 7 Image/native matrix | R | U (spritesheets/flipbooks) | — | R |
| 8 Asset manifest | P (assets podem estar `planned`/`prompt-ready` com fallback) | P | P (áudio fora do manifest de imagem) | R (sem placeholder não aprovado) |
| 9 Implementation handoff | R | U | U | R |
| 10 QA evidence plan | R (plano) | R (plano + capturas de motion) | P | R (**capturas reais** ou veredito `pendente — sem captura`) |
| 11 Manual action queue | R se houver pendência | R se houver | R se houver | R |

## 3. O que pode ficar pendente (e como)

Pode ficar `pendente`, sempre com **dono + próxima ação** na manual action queue:
- assets ainda não gerados/enviados (com fallback nativo descrito);
- AssetIds (sempre `null` até upload real);
- capturas de QA (veredito `pendente — sem captura`);
- decisões marcadas **[aprovação humana]**;
- dados de servidor ainda não existentes (com contrato de dados esperado no handoff).

**Nunca** pode ficar pendente na fase A: padrão escolhido, hierarquia, zonas protegidas
(se gameplay), composição de cada plataforma declarada como suportada, foco inicial e
rota de volta (se gamepad), estados mínimos, recovery de risco alto.

## 4. Critérios de rejeição do pacote

Rejeite (e complete) se qualquer um for verdadeiro:
- só existe o nome do padrão ("usar grid-detail") sem screen spec e state matrix;
- plataforma declarada como suportada sem wireframe/gatilho de reflow;
- gamepad suportado sem foco inicial e rota de retorno;
- HUD de gameplay sem zonas protegidas;
- risco alto/crítico sem cancelamento, recovery e erro;
- componente "genérico" sem função visual clara;
- asset referenciado inexistente sem fallback, ou AssetId fictício;
- QA declarado como feito sem caminho real de captura;
- escolha estética subjetiva apresentada como fato técnico.

## 5. Validação

1. `python ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py <packet.json>` — consistência do pacote.
2. `python ${CLAUDE_SKILL_DIR}/scripts/validate_asset_manifest.py <manifest.json>` — assets.
3. Captura real (Studio/cliente) para aprovação visual — **nenhum validador substitui isso**.

Fora do Claude Code, troque `${CLAUDE_SKILL_DIR}` pelo caminho da pasta da skill.
