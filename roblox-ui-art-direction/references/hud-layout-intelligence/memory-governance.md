# Memória evolutiva governada

Objetivo: aprender com decisões de layout sem transformar a preferência de um jogo em
regra universal. É uma **proposta documental**: arquivos markdown versionados, sem
automação de treino.

## 1. Três níveis

```text
<repo-do-jogo>/docs/ui/project-memory/layout-decisions/   # 1. privado do projeto
<repo-do-jogo>/docs/ui/project-memory/shared-candidates/   # 2. candidatos (opt-in)
<skill-library>/roblox-ui-art-direction/curated-library/   # 3. biblioteca curada (só via revisão/PR)
```

| Nível | Quem escreve | Conteúdo permitido | Sai do projeto? |
|---|---|---|---|
| 1. Projeto privado | agente + equipe | contexto completo, capturas internas, nomes de sistemas | não |
| 2. Candidato compartilhável | só com **opt-in explícito** do dono do projeto | lição generalizada; sem PII, sem capturas privadas, sem assets de terceiros ou não licenciados | só quando aprovado |
| 3. Biblioteca curada | mantenedor humano via PR revisado | padrão generalizado, evidência rotulada, origem/licença comprovada | sim (faz parte da skill) |

A pasta `curated-library/` **não existe** na v1.1.0 de propósito: ela só é criada quando o
primeiro candidato for aprovado por um humano.

## 2. Registro

Use `templates/layout-memory-record.md`. Campos obrigatórios: ID, data, versão da skill,
jogo e estilo, família do HUD, tarefa, dispositivo/input, padrão escolhido, alternativas
rejeitadas, justificativa, screenshots autorizados ou URLs, resultados de QA, problemas,
soluções, nível de confiança, decisão humana, licença/origem do material visual.

ID sugerido: `LM-<jogo-curto>-<AAAAMMDD>-<nn>` (ex.: `LM-tbb-20261022-01`).

## 3. Regras obrigatórias

1. Memória local **não altera pesos do modelo** e **não altera regras globais** da skill
   automaticamente. É contexto lido no início do workflow.
2. Não compartilhar capturas privadas, dados de jogadores (PII) ou assets de terceiros.
3. Uma lição de projeto **não vira padrão universal** sem revisão.
4. Promoção nível 1 → 2 exige opt-in do dono; nível 2 → 3 exige revisão humana, curadoria,
   generalização demonstrada (≥ 2 contextos distintos ou justificativa explícita),
   origem/licença comprovada e **PR**.
5. **Conflitos históricos não são apagados**: um registro novo que contradiz um antigo
   referencia o antigo em `supersedes`/`conflicts_with` e explica a mudança.
6. Quando a memória do projeto contradiz esta skill, a decisão do projeto vale **para o
   projeto** e a divergência é registrada; a skill só muda via nível 3.

## 4. Fluxo

```text
decisão (layout-decision) → implementação → QA (layout-review)
   → registro LM no nível 1 (sempre)
   → [opt-in] cópia sanitizada no nível 2
   → [revisão humana + PR] incorporação ao nível 3 / patterns/*.md
```

## 5. Simulação de promoção (exemplo documental)

- LM-demo-20261022-01 (nível 1): "Em portrait, chips de filtro horizontais aumentaram a área
  do grid" — confiança `hypothesis` (sem telemetria), decisão humana: aprovado para o projeto.
- Candidato (nível 2): mesma lição sem nomes nem capturas; opt-in registrado.
- Revisão (nível 3): rejeitada por ora — apenas 1 contexto; mantida como candidato.
  Nenhuma regra global foi alterada.
