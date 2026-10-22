# State Matrix — <Tela>

> Uma linha por estado da **tela** (não do componente). Estados mínimos obrigatórios:
> empty, loading, error, disabled, pending, overflow, full + estados específicos do sistema.
> Estado não aplicável: manter a linha com "n/a — <motivo>".

| Estado | Gatilho | Texto exibido | Ação disponível | Cor/ícone (token + sinal não cromático) | Foco (gamepad) | Comportamento de rede | Recovery | Captura requerida |
|---|---|---|---|---|---|---|---|---|
| empty | | | | | | | | sim/não |
| loading | | | | | | | | |
| error | | | | | | | | |
| disabled | | | | | | | | |
| pending | | | | | | | | |
| overflow | | | | | | | | |
| full | | | | | | | | |
| <específico 1> | | | | | | | | |
| <específico 2> | | | | | | | | |

Regras: nenhum estado comunicado só por cor ou só por animação; todo estado de erro tem recovery;
estado `pending` bloqueia repetição da ação e só termina com resposta do servidor.
