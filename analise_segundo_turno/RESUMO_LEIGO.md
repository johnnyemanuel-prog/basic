# Resumo para leigos (explicado como para alguém de 17 anos)

**Atualizado em 23/10** com as pesquisas feitas até 22/10.

A versão técnica completa está em `ATUALIZACAO_2310.md` (dados mais recentes). As versões anteriores ficaram em `ATUALIZACAO_2110.md` e `RELATORIO.md`. Aqui vai o mesmo conteúdo, só que sem fórmulas.

---

## 1. A situação

Uma eleição teve dois turnos. No 2º turno sobraram dois candidatos, **A** e **B**. A votação é em **25/10**, daqui a poucos dias.

No 1º turno:
- B teve **56,1 milhões** de votos e A teve **53,9 milhões**. B ficou cerca de 2,2 milhões à frente.
- Outros candidatos (C, D, E…) somaram 9,3 milhões de votos. Eles saíram da disputa, e os eleitores deles agora precisam escolher entre A e B, votar branco/nulo ou não ir votar.
- Cerca de **6 milhões** votaram branco ou nulo.
- Cerca de **33,5 milhões não foram votar**. Vamos chamar esse grupo de **"faltantes"**.

A pergunta é: **com o que se sabe hoje, qual a chance de A terminar com mais da metade dos votos válidos?** Votos válidos são os votos dados a A ou a B, sem contar branco e nulo.

## 2. Como a gente calculou

Pense num simulador de jogo de futebol que roda a partida **1 milhão de vezes**. Em cada rodada, ele muda um pouco as coisas que não sabemos com certeza: um jogador pode estar mais cansado, o juiz pode errar, chover ou não. No fim, você conta em quantas rodadas cada time ganhou.

Aqui fizemos o mesmo com a eleição. As "peças" que variam são:

1. **Fidelidade:** quantos eleitores de A no 1º turno votam em A de novo, e o mesmo para B.
2. **Troca de lado:** quantos eleitores de A passam para B, e quantos de B passam para A.
3. **Eleitores dos eliminados:** para onde vão os votos de C, D, E…
4. **Comparecimento:** quem vai votar e quem fica em casa.
5. **Indecisos:** para onde eles vão.
6. **Erro das pesquisas:** quanto elas podem estar erradas.
7. **Tempo:** quanto a opinião das pessoas pode mudar nos **3 dias** entre a última pesquisa (22/10) e a eleição.

Usamos três fontes de informação:
- o resultado oficial do 1º turno;
- pesquisas que perguntam *"em quem você votou antes e em quem vai votar agora"*. Agora temos **duas** dessas tabelas do instituto pd, uma de 11/10 e outra de 20/10;
- **18 pesquisas nacionais** de 2º turno, de **10 institutos**. As duas mais novas são de df e pd, feitas entre 19 e 22/10.

### As regras do jogo (para não se enganar com os números)

- **Pesquisa velha pesa menos.** Uma pesquisa de 11/10 vale menos que uma de 21/10, como a previsão do tempo de ontem vale mais que a da semana passada.
- **Nada é contado duas vezes.** Uma pesquisa divulga "votos totais" e "votos válidos", mas é a mesma pesquisa escrita de dois jeitos. Ela entra uma vez só.
- **Grupo pequeno, erro grande.** Quando a pesquisa olha só os eleitores de C, por exemplo, ela tem poucas pessoas daquele grupo. Por isso esses números ganham uma margem de erro extra.
- **"Vou votar no mesmo" não é o mesmo que "meu voto é firme".** Quando 95 em cada 100 eleitores de A no 1º turno dizem que vão votar em A de novo, isso mede **fidelidade**. Quando alguém diz "nada me faria mudar", isso mede **firmeza**. São perguntas diferentes, e não misturamos.
- **Dizer que vai votar não é votar.** Na pesquisa pd, 95 em cada 100 dizem que vão votar com certeza, mas no 1º turno só 79 em cada 100 votaram. Por isso a intenção de comparecer fica separada da intenção de voto.
- **Mudança entre duas pesquisas não prova que alguém mudou de ideia.** Entre os que votaram branco/nulo no 1º turno, a pd achou 18 % indo para A em 11/10 e 46 % em 20/10. Só que são pessoas **diferentes**, num grupo pequeno. Tratamos como duas medições imprecisas, não como "28 % mudaram de ideia".

## 3. O resultado

> **A aparece com cerca de 48,9 % dos votos válidos, e B com cerca de 51,1 %.**
>
> Em **cerca de 3 de cada 100 simulações**, A termina com mais de 50 %. A faixa vai de **2 a 7 em 100**, dependendo de quanto a opinião ainda pode mudar até domingo.

**Como isso mudou ao longo das atualizações:**

| Dados até | A nos votos válidos | Vantagem de B | Chance de A passar de 50 % |
|---|---|---|---|
| 14/10 | 48,4 % | 3,8 milhões | cerca de 2 em 100 |
| 20/10 | 48,7 % | 3,0 milhões | cerca de 3 em 100 |
| **22/10** | **48,9 %** | **2,7 milhões** | **cerca de 3 em 100** |

A diferença vem diminuindo devagar. Mesmo assim, a chance não subiu, porque **agora a gente tem mais certeza dos números**. Com menos incerteza, sobra menos espaço para surpresas.

Para comparar: 5 em 100 é a chance de tirar um número específico num dado de 20 lados, numa jogada só. 3 em 100 é um pouco menos que isso.

⚠️ **Isso não é uma previsão.** É o que sai quando juntamos estes dados com estas hipóteses. Se as hipóteses mudarem, o número muda.

## 4. Por que a conta ainda pende para B

- **Os dois lados ficaram mais fiéis**, segundo a tabela nova. Cerca de 95 em cada 100 eleitores de B repetem o voto, contra cerca de 94 em cada 100 de A.
- **A troca de lado agora pende um pouco para B.** Cerca de 4,4 % dos eleitores de A vão para B, e cerca de 3,9 % dos de B vão para A. Antes, com uma tabela só, parecia empatado em 5 a 5. Agora são duas medições, e a incerteza caiu pela metade.
- **Os eleitores dos eliminados pendem para B:** juntando C, D, E e F, cerca de 45 % vão para B e 32 % para A.
- **O ponto a favor de A está nos brancos/nulos e nos faltantes do 1º turno.** Nesse grupo, cerca de 41 % dizem que vão votar em A e 37 % em B; o resto vota branco/nulo, não vai ou não sabe. É daí que vem a diminuição da diferença.
- **As 18 pesquisas nacionais concordam entre si.** As duas mais novas mostram B com 50,5 % dos válidos, o valor mais baixo da série, mas dentro do erro normal das pesquisas.

## 5. O que A precisaria para virar?

Para fechar a diferença, faltam cerca de **2,7 milhões de votos**.

### Caminho 1: pessoas mudando de lado (a "virada de voto")

Esta continua sendo a ferramenta mais poderosa. Quando alguém sai de B e vai para A, **B perde um voto e A ganha um**. A diferença cai **2 votos** de uma vez, como num jogo em que o gol de um time também tira um ponto do outro.

| Se, de cada 100 eleitores de A, este número for para B… | …então, de cada 100 eleitores de B, este número precisa ir para A |
|---|---|
| 0 | cerca de 2 |
| 2 | cerca de 4 |
| **4 a 5 (como está hoje)** | **cerca de 6 a 7** (hoje são cerca de 4) |
| 7 | cerca de 9 |

**Regrinha:** para cada eleitor de A que passa para B, A precisa trazer de volta praticamente um eleitor de B a mais.

### Caminho 2: os faltantes indo votar

Aqui o efeito é bem mais fraco. Um faltante que vai votar **não tira voto de ninguém**: ele só soma de um lado. E isso só ajuda A se esse grupo **preferir A bem mais do que B**.

| Se os novos eleitores votarem A:B assim… | …quantos dos 33,5 milhões de faltantes precisariam ir votar além do esperado |
|---|---|
| 55 para A, 45 para B | **quase todos** (95 %) |
| 60:40 | cerca de metade (16 milhões) |
| 2 para A, 1 para B | cerca de 3 em cada 10 (10 milhões) |
| 75:25 | cerca de 1 em cada 5 (6 milhões) |
| 100 % em A | cerca de 1 em cada 10 (3,2 milhões), **todos** votando em A |

### Caminho 3: quem de fato vai votar

Uma pesquisa (nx) perguntou se as pessoas vão mesmo votar. Entre os eleitores bem decididos, **95 em cada 100 de A** disseram que vão com certeza, contra **92 em cada 100 de B**.

Se essa diferença virasse diferença real nas urnas, mudaria bastante a conta:

| Quanto dessa diferença vira realidade | Chance de A passar de 50 % |
|---|---|
| nada (hipótese principal) | cerca de 3 em 100 |
| um quarto | cerca de 6 em 100 |
| metade | cerca de 13 em 100 |
| tudo | cerca de 36 em 100 |

Mas, como já vimos, **dizer que vai votar não é o mesmo que votar**. Ninguém sabe quanto dessa diferença é real. Por isso ela fica como "e se…?", e não no cálculo principal.

### Juntando tudo

Se 1 em cada 100 eleitores de cada lado trocasse a favor de A, ainda seria preciso que cerca de **1 em cada 10 faltantes** fosse votar com divisão 60:40.

Quando o simulador procura **a combinação mais provável** de dar a virada, ele escolhe de novo:

> **Só a troca de votos:** cerca de **5 em cada 100** eleitores de B indo para A, e só cerca de **3 em cada 100** eleitores de A indo para B.

Repare numa coisa curiosa: **a diferença diminuiu, mas essa combinação ficou mais longe do que o modelo considera normal.** Na conta de 21/10, ela estava "um pouco fora do comum"; agora está "bem fora do comum". O motivo é que a tabela nova de troca de lado mediu esse número com mais precisão, e ele saiu um pouco a favor de B. Quando a gente tem mais certeza sobre uma peça, fica mais difícil ela "surpreender".

O gráfico interativo `fronteira_virada.html` mostra isso: a linha azul separa as combinações em que A vira das em que B mantém a maioria, e o ponto preto mostra onde estamos hoje.

## 6. Cuidados (as "letras miúdas")

- **As duas tabelas de troca de lado são do mesmo instituto (pd).** Não dá para saber se uma diferença entre elas é real ou um jeito particular daquele instituto medir.
- **Os grupos de eleitores dos eliminados são pequenos nas pesquisas.** Por isso os números deles têm margem enorme.
- **Os institutos discordam pouco.** Nenhum se afasta dos outros mais do que o erro normal, e nenhum foi descartado.
- **Três institutos citados (vx, ve e al) não entraram**, porque nenhum número deles foi enviado. Não inventamos dados.
- **Se todas as pesquisas errarem para o mesmo lado**, o modelo não tem como perceber. Só dá para testar "e se…?".
- **Tudo isso é matemática sobre hipóteses.** Serve para entender **quais peças movem o resultado**, não para apostar nem para dizer quem vai ganhar.

## 7. Resumindo em quatro frases

1. Com as pesquisas até 22/10, A está cerca de **2,2 pontos atrás** nos votos válidos, um pouco menos que nas contas anteriores. A chance de virar fica em torno de **3 em 100**, entre **2 e 7 em 100** conforme o quanto a opinião ainda pode mudar.
2. A diferença diminuiu porque **brancos/nulos e faltantes do 1º turno** que vão votar pendem um pouco para A. Mas a **troca direta entre eleitores de A e B** agora pende um pouco para B, e foi medida com mais precisão.
3. O que mais poderia mudar o resultado continua sendo **gente trocando de lado**, porque cada troca vale dois votos.
4. **Se os eleitores de A forem mesmo votar mais que os de B**, como dizem, a chance pode chegar a 6 a 13 em 100. Ninguém sabe quanto do "eu vou votar" vira voto de verdade.
