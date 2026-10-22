# Visual Direction

Transforma o brief num **conceito estético defensável**. A direção não é uma paleta; é um
conjunto de decisões que explicam por que cada tela parece pertencer ao mesmo jogo.

## 1. Estrutura de uma direção

1. **Conceito em uma frase** — metáfora material/espacial.
   Ex.: "Painéis de madeira de taverna presos com ferragens, iluminados por velas";
   "Vidro holográfico projetado por um capacete de piloto"; "Adesivos de papelão recortados
   colados num caderno escolar".
2. **Pilares (3–5)** — adjetivos acionáveis com consequência. "Robusto → bordas grossas,
   cantos chanfrados, sombras duras". Evite pilares vazios ("bonito", "moderno").
3. **Linguagem de forma** — cantos (redondos, chanfrados, irregulares), espessura de
   contorno, proporção dos painéis, silhuetas de botões, densidade.
4. **Materiais e superfícies** — papel, madeira, metal, vidro, plástico, pedra, tecido,
   energia. Define o que vira imagem (textura/ilustração) e o que fica plano.
5. **Luz e profundidade** — sombras projetadas? brilho interno? flat sem sombra? bevel?
6. **Cor (papel, não lista)** — base neutra, cor de marca, acento de ação, semânticas.
   Proporção típica 60/30/10, adaptada ao tema.
7. **Tipografia** — família display (títulos) + família de leitura (corpo/números). Usar
   fontes disponíveis no Roblox (`Font.new("rbxasset://fonts/families/...json")` ou fontes do
   Creator Store com licença). Números de economia sempre legíveis.
8. **Iconografia** — estilo (preenchido, contorno, ilustrado, pixel), perspectiva
   (frontal / 3/4), espessura de contorno, iluminação comum.
9. **Motion** — personalidade do movimento (elástico, mecânico, flutuante, seco).
10. **O que a direção NÃO é** — 3–5 proibições explícitas. Ex.: "sem neon, sem gradiente
    arco-íris, sem glassmorphism" num jogo medieval.

## 2. Gerando e escolhendo

- Considere 2–3 conceitos mentalmente; escolha um e registre por que venceu (tom, público,
  viabilidade de produção de assets, legibilidade mobile). Não entregue três opções ao
  usuário a menos que ele peça.
- Teste o conceito em 3 elementos difíceis antes de seguir: botão primário, card de item,
  número de moeda no HUD. Se o conceito não resolve esses três, ajuste.
- Viabilidade: se o conceito depende de 200 ilustrações únicas sem ferramenta de geração,
  simplifique (ex.: molduras modulares + ícones).

## 3. Coerência com o mundo 3D

Capture o jogo (ou peça captura). A UI deve compartilhar pelo menos dois de: paleta,
material, forma, iluminação. HUD sobre o mundo precisa de contraste garantido (placa de fundo,
contorno de texto ou sombra) — não confie no fundo do cenário.

## 4. Referências externas

Use referências (jogos, ilustrações, UI de outros meios) para extrair **princípios**
(hierarquia, ritmo, materiais). Nunca reproduza layout + arte + iconografia de um jogo
comercial; nunca use assets de terceiros sem direitos.

## 5. Sinais de direção genérica (refazer)

- Poderia ser colada em qualquer outro jogo sem estranheza.
- Todos os painéis são retângulos arredondados cinza-escuro com 70% de transparência.
- Gradiente + glow + sombra em tudo "para parecer premium".
- Ícones de estilos misturados (emoji + flat + 3D).
