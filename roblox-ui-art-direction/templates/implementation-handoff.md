# Implementation Handoff — <Tela> — <Jogo>

> Artefato 9 do contrato. Objetivo: outro agente/dev implementa sem redescobrir decisões.

## 1. Árvore de ScreenGuis e instâncias
```text
StarterGui
└── <Tela>Gui (ScreenGui; DisplayOrder=<n>; ScreenInsets=<...>; ResetOnSpawn=<...>)
    └── Root
        ├── <Região> ...
```

## 2. Componentes
| ID | Tipo | Módulo | Contrato | Estados |
|---|---|---|---|---|

## 3. Arquivos/módulos
| Caminho (Rojo/DataModel) | Tipo | Responsabilidade |
|---|---|---|
| ReplicatedStorage/UI/Theme | ModuleScript | tokens + Theme.Image |
| ReplicatedStorage/UI/Components/<X> | ModuleScript | |
| StarterPlayerScripts/<Tela>Controller | LocalScript | estado → visual |
| ServerScriptService/<Sistema>Service | Script/Module | validação |

## 4. Dados esperados
```lua
type ViewState = {
    -- campos que a tela consome (fonte: servidor/replicação), com tipos
}
```

## 5. Intenções de interação
| Intenção | Origem (componente/input) | Remote | Validação no servidor | Resposta | Estado da UI |
|---|---|---|---|---|---|

## 6. Responsabilidades cliente × servidor
- Cliente: <render, input, pending, feedback>
- Servidor: <posse, saldo, limites, rate limit, atomicidade>

## 7. Assets pendentes
| Asset ID (manifest) | Status | Fallback em uso |
|---|---|---|

## 8. Ordem de implementação
1. <...>

## 9. Comandos de validação
```bash
python ${CLAUDE_SKILL_DIR}/scripts/validate_hud_packet.py <docs/ui/<tela>/<tela>.packet.json>
python ${CLAUDE_SKILL_DIR}/scripts/validate_asset_manifest.py <docs/ui/asset-manifest.json>
```
(Fora do Claude Code, troque `${CLAUDE_SKILL_DIR}` pelo caminho da pasta da skill.)

## 10. Manual action queue
| # | Ação | Por que só um humano | Dono | Bloqueia |
|---|---|---|---|---|
