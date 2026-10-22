# Visual QA & Iteration

"Compilou" ≠ "está bonito". A aprovação visual exige ver a UI real.

## 1. Como capturar

- Com Roblox Studio MCP: `screen_capture` (modo edição ou play), `start_stop_play`,
  `inspect_instance` para conferir propriedades; repetir por viewport do Device Emulator.
- Com computer use: screenshot da janela do Studio após configurar o emulador.
- Sem captura disponível: escreva **"Revisão visual pendente — sem captura"** no relatório
  e liste o que o humano deve verificar. Não declare aprovado.

Capture no mínimo: desktop 1080p, celular paisagem, (retrato se suportado), tablet, e
gamepad com foco visível. Inclua estados: vazio, cheio, loading, erro, hover/press/selected.

## 2. Checklist (marque ✅ / ⚠️ / ❌ com nota)

**Identidade**
- [ ] Reconhecível como *este* jogo (passaria no teste "trocar logo por outro jogo"? não deveria)
- [ ] Coerente com brief, pilares e lista "não é"
- [ ] Consistência entre telas (mesma moldura, botões, ícones, motion)

**Assets**
- [ ] Qualidade: sem halos de alpha, sem blur por upscale, sem artefatos de geração
- [ ] Estilo de ícones uniforme (perspectiva, luz, contorno)
- [ ] Nine-slice sem distorção nos cantos em todos os tamanhos
- [ ] Nenhum `PLACEHOLDER_*`/`Placeholder=true` não aprovado; nenhum AssetId falso
- [ ] Uso apropriado: nada de tela-inteira-em-PNG; nada de texto em imagem

**Composição**
- [ ] Alinhamento a um grid / escala de espaçamento
- [ ] Hierarquia clara (primário > secundário > terciário) em 3s de olhada
- [ ] Densidade adequada; sem painéis vazios gigantes ou apertados
- [ ] Legibilidade e contraste (ver accessibility)

**Interação**
- [ ] Estados hover/press/selected/disabled visíveis e no estilo
- [ ] Foco de gamepad visível e navegável
- [ ] Feedback de ação e estados pending/erro/sucesso

**Responsividade**
- [ ] Matriz de viewports sem clipping/sobreposição; safe areas; zonas de controles livres

**Performance**
- [ ] Contagem de texturas e tamanho razoáveis; sem ViewportFrame por célula
- [ ] Sem tweens/conexões vazando ao abrir/fechar repetidamente

## 3. Iteração

1. Liste problemas por severidade (bloqueante / alto / polimento).
2. Corrija bloqueantes primeiro; uma categoria por rodada (ex.: espaçamento, depois cor).
3. Recapture os mesmos viewports e compare lado a lado.
4. Pare quando não houver bloqueantes/altos e o checklist estiver ✅ ou ⚠️ justificado.

## 4. Registro

Preencha `templates/visual-review.md`: data, build/branch, viewports capturados (caminhos
das imagens), resultado do checklist, problemas e correções, pendências e veredito
(`aprovado`, `aprovado com ressalvas`, `reprovado`, `pendente — sem captura`).

## 5. Composição (v1.1.0)

Além deste checklist estético, verifique a composição escolhida no `layout-decision` com
`templates/layout-review.md` (matriz viewport × input × estado). Os validadores em `scripts/`
checam apenas estrutura e dados — nunca substituem captura real.
