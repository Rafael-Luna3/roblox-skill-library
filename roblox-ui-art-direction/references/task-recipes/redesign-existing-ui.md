# Recipe: `redesign-existing-ui` — redesenhar UI existente

**Modo:** discovery → design → implementation. **Fase padrão:** A.

## Ler
- a UI real primeiro (Explorer/Rojo, scripts que a controlam, remotes que ela chama); capturas atuais se houver
- memória do projeto e layout-decisions anteriores
- `references/design-discovery.md` · `references/hud-layout-intelligence/selection-method.md`
- `references/hud-delivery-contract.md` · `references/component-system.md`

## Criar/atualizar
- **inventário do existente**: o que fica, o que muda, o que é legado, quem depende de quê (scripts, nomes de instâncias, atributos, remotes)
- layout-decision (inclua "manter layout atual" como alternativa quando viável) · screen spec · state matrix · handoff · packet JSON
- memória: registro LM com o motivo da mudança (`supersedes` o anterior, sem apagá-lo)

## Ordem
1. Mapear dependências e escopo (o que **não** pode ser tocado). 2. Capturar o estado atual (ou registrar que não há captura).
3. Decidir layout. 4. Especificar. 5. Implementar **ao lado** (nova ScreenGui/versão) ou com migração explícita.
6. Validar. 7. Comparar antes/depois nas mesmas resoluções.

## Entregáveis
Pacote do contrato + lista de migração (instâncias renomeadas/removidas, scripts afetados) + plano de rollback.

## Parar quando
Nenhum sistema fora do escopo foi alterado; dependências mapeadas continuam funcionando;
validadores passam; antes/depois documentado (ou pendente sem captura).

## Perguntar ao usuário quando
- remover/renomear instâncias que scripts fora do escopo usam;
- a UI atual tem comportamento que parece intencional mas contraria a skill (ex.: modal sem B);
- não está claro se a identidade visual atual deve ser preservada ou substituída.

## Seguir com hipóteses quando
Ajustes de espaçamento/tokens dentro do escopo, novos estados que faltavam, correções de foco
e safe area: aplicar e registrar.

**Nunca:** apagar sistemas, scripts ou GUIs fora do escopo; sobrescrever assets existentes.
