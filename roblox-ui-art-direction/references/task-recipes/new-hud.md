# Recipe: `new-hud` — criar HUD/tela nova

**Modo:** discovery → design (→ implementation se pedido). **Fase padrão:** A.

## Ler
- `references/design-discovery.md` (se não houver brief) · `references/theme-system.md` (se não houver theme profile)
- memória do projeto (`references/hud-layout-intelligence/memory-governance.md`)
- `references/hud-layout-intelligence/selection-method.md` + a ficha do padrão candidato
- `references/hud-delivery-contract.md` · `references/component-system.md`
- sob demanda: `responsive-composition.md`, `input-and-focus.md`, `asset-decision-matrix.md`, `image-production.md`

## Criar/atualizar (no repositório do jogo, ex. `docs/ui/<tela>/`)
design brief e theme profile (se ausentes) · layout-decision · screen spec · state matrix ·
component contracts (só os não triviais) · matriz imagem/nativo · asset manifest ·
implementation handoff · evidence board · `<tela>.packet.json`

## Ordem
1. Context snapshot (brief/theme/memória). 2. Layout decision (≤ 3 alternativas, mobile e gamepad primeiro).
3. Screen spec + composição por plataforma. 4. Componentes + state matrix. 5. Imagem/nativo + manifest.
6. Handoff + evidence board + manual queue. 7. Packet JSON + validadores. 8. Implementar só se pedido.

## Entregáveis
Os 11 artefatos do contrato para a fase pedida; validadores passando; veredito visual
`pendente — sem captura` até haver captura real.

## Parar quando
O pacote passa nos validadores, nenhum item "nunca pendente" do contrato está aberto, e
toda pendência tem dono na manual action queue.

## Perguntar ao usuário quando
- não há como inferir público/dispositivos e a escolha muda a composição (ex.: mobile-first ou não);
- duas direções estéticas opostas são plausíveis e não há referência;
- a tela envolve economia/trade e as regras de negócio (limites, taxas, reembolso) não existem.

## Seguir com hipóteses quando
Escala de espaçamento, easing, nomes de pastas, posição de elementos não críticos, ou
qualquer coisa reversível: registrar como `Suposição:` no brief/evidence board e seguir.
