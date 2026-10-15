# Resumo para leigos

Este texto resume, em linguagem simples, a análise estatística de um segundo turno hipotético entre os candidatos **A** e **B**. A versão técnica completa está em `RELATORIO.md`.

## O que foi feito

Juntamos três tipos de informação:

1. **O resultado do 1º turno.** B teve cerca de 2,2 milhões de votos a mais que A (47,0 % contra 45,2 % dos votos dados a candidatos). Os outros candidatos somaram 9,3 milhões de votos. Houve ainda 6 milhões de brancos e nulos e 33,5 milhões de abstenções.
2. **Pesquisas que perguntam "em quem você votou no 1º turno e em quem vai votar agora".** Elas mostram para onde vão os eleitores de cada candidato.
3. **Oito pesquisas nacionais de 2º turno**, feitas por sete institutos entre 3 e 14 de outubro.

Com isso, simulamos a eleição **1 milhão de vezes**. Em cada simulação, variamos tudo o que não se sabe com certeza: quantos eleitores de cada lado mudam de voto, quem vai ou não votar, para onde vão os indecisos, o quanto as pesquisas podem errar e o quanto a opinião pode mudar até o dia da eleição.

## O resultado, em uma frase

**Considerando a eleição em 10 dias, A aparece com cerca de 48,4 % dos votos válidos e B com cerca de 51,6 %.** Na maioria das simulações, a diferença fica entre 0,6 e 5,6 pontos.

Em quantas simulações A termina à frente?

- **Cerca de 2 a 5 em cada 100** no cenário principal.
- O número sobe para algo entre **7 e 25 em cada 100** se confiarmos só nas pesquisas nacionais e admitirmos que a opinião pode mudar bastante em 10 dias.

Isso **não é uma previsão**. É o que resulta das hipóteses do modelo. Se as hipóteses mudarem, o número muda.

## Por que a vantagem de B aparece em quase tudo

- **Os eleitores de B estão um pouco mais fiéis.** Cerca de 94,6 % devem repetir o voto em B, contra cerca de 92 % dos eleitores de A que devem repetir o voto em A. A diferença no lado de A vai principalmente para branco, nulo e indeciso, não para B.
- **As trocas entre os lados se anulam.** Cerca de 5 % dos eleitores de cada candidato dizem que vão mudar para o outro.
- **Os eleitores dos candidatos eliminados se dividem.** Entre eles, cerca de 46 % tendem a B e 27 % a A. Mas são poucos (cerca de 7 % do eleitorado), então isso pesa pouco.
- **Todas as oito pesquisas nacionais mostram B entre 50,5 % e 52,8 % dos votos válidos.** Nenhuma delas destoa das demais além do que o acaso explicaria.

## O que poderia mudar o quadro

Para A chegar a 50 % dos válidos, mantendo tudo o mais igual, seria preciso, por exemplo, que:

- cerca de 9 % dos eleitores de B no 1º turno passassem para A (hoje são cerca de 5 %); **ou**
- 45 % dos votos que os eliminados dariam a B fossem para A; **ou**
- cerca de 14 milhões de pessoas que não votaram no 1º turno fossem votar e escolhessem A na proporção de 2 para 1; **ou**
- todas as pesquisas estivessem erradas na mesma direção, em cerca de 1,5 a 2 pontos.

Dois fatores pesam **pouco**:

- **Aumento do comparecimento em geral.** Mais gente votando só faz diferença se os novos eleitores preferirem muito um dos lados.
- **A forma de distribuir os indecisos.** Eles são só cerca de 2 % dos eleitores, e os quatro métodos testados mudam o resultado em menos de meio ponto.

O fator que pesa **muito** é **quem efetivamente vai votar de cada lado**. Se 1 ponto percentual a mais dos eleitores de A comparecer do que dos eleitores de B, o resultado muda cerca de 0,4 ponto.

## Ressalvas importantes

- **Os dados têm inconsistências.**
  - A tabela de "para onde vai cada eleitor" do instituto pd, aplicada aos votos reais do 1º turno, dá A com 47,1 %. Mas a pesquisa geral do mesmo instituto dá A com 48,9 %.
  - Os institutos pd e qu discordam sobre os eleitores do candidato C e sobre quem não votou no 1º turno.
  - O modelo não esconde essas diferenças: ele as combina e mostra o quanto cada uma influencia o resultado.
- **Por isso, a tabela do instituto pd recebeu peso intermediário.** Ela vale como metade de uma pesquisa, e admitimos um pequeno erro de lembrança do voto no 1º turno. Como o 1º turno foi há pouco tempo, esse erro deve ser pequeno.
- **Não sabemos o tamanho real** de cada subgrupo entrevistado nas pesquisas; usamos estimativas.
- **Um erro de todas as pesquisas na mesma direção não pode ser medido** com estes dados. Só podemos testar o que aconteceria se ele existisse.
- **As probabilidades dependem das hipóteses.** Elas servem para entender a estrutura dos números, não para apostar nem para afirmar quem vai ganhar.
