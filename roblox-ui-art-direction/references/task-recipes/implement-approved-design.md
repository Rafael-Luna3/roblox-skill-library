# Recipe: `implement-approved-design` — implementar design já aprovado

**Modo:** implementation. **Fase:** a que o pacote aprovado declara.

## Ler
- o pacote aprovado (screen spec, state matrix, component contracts, handoff, manifest, packet JSON)
- `references/roblox-ui-implementation.md` · `references/component-system.md`
- sob demanda: `responsive-composition.md`, `input-and-focus.md`, `animation-and-feedback.md` (só fase B)

## Criar/atualizar
Instâncias/módulos listados no handoff; Theme module; componentes; controllers; remotes
validados no servidor (ou integração com os existentes); atualização do manifest com IDs reais
recebidos; evidence board com as capturas feitas.

## Ordem
Seguir a "ordem de implementação" do handoff. Default: Theme → componentes base com
fallbacks → shell da tela com layouts → reflow por plataforma → estados → dados/rede → arte
aprovada → (fase B) motion → validadores → capturas.

## Entregáveis
Código/instâncias + manifest atualizado + evidence board com capturas reais **ou** veredito
`pendente — sem captura` + manual queue atualizada.

## Parar quando
Todos os itens do handoff estão implementados ou explicitamente pendentes; validadores
passam; nenhum placeholder sem registro.

## Perguntar ao usuário quando
- o pacote contradiz o código/arquitetura existente de forma que exige redesenho;
- um AssetId/asset aprovado não existe ou não carrega;
- a implementação exigiria mudar sistemas fora do escopo.

## Seguir com hipóteses quando
Detalhes de implementação não especificados (nomes internos, ordem de conexões, pequenos
ajustes de offset dentro do token): decidir e registrar no handoff.

**Não** redecida layout aqui; se o design não funciona, volte para `new-hud`/`redesign-existing-ui` (fase A).
