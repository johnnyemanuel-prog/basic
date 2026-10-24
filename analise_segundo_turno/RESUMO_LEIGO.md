# Resumo para leigos (explicado como para alguém de 17 anos)

**Atualizado em 24/10**, véspera da eleição, com as quatro pesquisas finais.

A versão técnica completa está em `ATUALIZACAO_2410.md` (dados finais). As versões anteriores ficaram em `ATUALIZACAO_2310.md`, `ATUALIZACAO_2110.md` e `RELATORIO.md`. Aqui vai o mesmo conteúdo, só que sem fórmulas.

---

## 1. A situação

Uma eleição teve dois turnos. No 2º turno sobraram dois candidatos, **A** e **B**. A votação é **amanhã, 25/10**.

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
5. **Indecisos:** para onde eles vão (agora são só 1 a 2 em cada 100).
6. **Erro das pesquisas:** quanto elas podem estar erradas.
7. **Tempo:** quanto a opinião ainda pode mudar no **1 dia** que falta.

Usamos três fontes de informação:
- o resultado oficial do 1º turno;
- duas tabelas do instituto pd que perguntam *"em quem você votou antes e em quem vai votar agora"* (de 11/10 e 20/10), mais outras de df, qu e pv;
- **22 pesquisas nacionais** de 2º turno, de 10 institutos. As **quatro mais recentes** (df, qu, nx e pv) foram feitas entre 22 e 24/10.

### As regras do jogo (para não se enganar com os números)

- **Pesquisa velha pesa menos**, como a previsão do tempo de ontem vale mais que a da semana passada.
- **Nada é contado duas vezes.** "Votos totais" e "votos válidos" são a mesma pesquisa escrita de dois jeitos, e entram uma vez só.
- **Arredondamento importa.** Quando a pesquisa diz "A 49 %, B 50 %", os números reais podem ser 49,4 e 49,6. Com números redondos, a conta dos válidos fica com uma incerteza de cerca de meio ponto, e o modelo leva isso em conta.
- **Voto firme não é fidelidade.** "Meu voto é definitivo" (cerca de 95 em cada 100 dizem isso) mede **firmeza**. Não é a mesma coisa que "votei em A e vou votar em A de novo". Não misturamos.
- **Rejeição não é voto.** "Não voto nele de jeito nenhum" é outra pergunta. Fica só como contexto.
- **Uma conta feita com as mesmas entrevistas não é pesquisa nova.** O instituto nx refez a conta só com quem tem mais chance de votar (o "LVM"). Usamos isso só como "e se…?", não como uma quinta pesquisa.

## 3. O resultado

> **A aparece com cerca de 49,1 % dos votos válidos, e B com cerca de 50,9 %.**
>
> Em **cerca de 3 de cada 100 simulações**, A termina com mais de 50 %. A faixa vai de **2 a 7 em 100**, conforme o quanto a opinião ainda pode mudar e o quanto as pesquisas podem errar.

**Como isso mudou ao longo das atualizações:**

| Dados até | A nos votos válidos | Vantagem de B | Chance de A passar de 50 % |
|---|---|---|---|
| 14/10 | 48,4 % | 3,8 milhões | cerca de 2 em 100 |
| 20/10 | 48,7 % | 3,0 milhões | cerca de 3 em 100 |
| 22/10 | 48,9 % | 2,7 milhões | cerca de 3 em 100 |
| **24/10** | **49,1 %** | **2,2 milhões** | **cerca de 3 em 100** |

A diferença vem caindo devagar e sem parar. A chance, porém, quase não se mexe, porque **a cada atualização a gente tem mais certeza dos números** e sobra menos espaço para surpresas. Com a eleição amanhã, quase não há tempo para mudanças.

Para comparar: 3 em 100 é um pouco menos que a chance de tirar um número específico num dado de 20 lados, numa jogada só.

⚠️ **Isso não é uma previsão.** É o que sai quando juntamos estes dados com estas hipóteses. Se as hipóteses mudarem, o número muda.

## 4. As quatro pesquisas finais: iguais demais?

As quatro pesquisas finais deram **praticamente o mesmo número**: B entre 50,5 % e 50,6 % dos válidos. Se fossem quatro sorteios independentes, o normal seria variarem cerca de 1 ponto para cima ou para baixo. Elas variaram 0,04 ponto.

Pense em quatro amigos chutando o peso de uma melancia sem combinar nada, e todos chutando exatamente 8,05 kg. Pode ser coincidência, mas desconfia-se que eles se olharam, ou que usaram o mesmo método.

Parte disso é arredondamento: nas quatro, B tem 1 ponto a mais que A. Mesmo assim, por precaução, **não tratamos as quatro como quatro confirmações independentes**. E testamos o que aconteceria se todas errassem juntas para o mesmo lado:

| Se todas as pesquisas estiverem erradas, juntas, em… | Chance de A passar de 50 % |
|---|---|
| 1 ponto contra A | cerca de 34 em 100 |
| meio ponto contra A | cerca de 12 em 100 |
| nada (hipótese principal) | cerca de 3 em 100 |
| meio ponto contra B | menos de 1 em 100 |

Olhando **só** as quatro pesquisas finais, sem histórico nem tabelas de troca de voto, A estaria com 49,5 % e a chance subiria para **17 a 29 em 100**. Esse é um **teto**, porque joga fora tudo o que se aprendeu nas semanas anteriores e trata as quatro como independentes.

## 5. Por que a conta ainda pende para B

- **Os dois lados estão muito fiéis:** cerca de 95 em cada 100 eleitores de B repetem o voto, contra cerca de 94 em cada 100 de A.
- **A troca de lado pende um pouco para B:** cerca de 4,4 % dos eleitores de A vão para B, e cerca de 4,0 % dos de B vão para A.
- **Os eleitores dos eliminados pendem para B:** juntando C, D, E e F, cerca de 45 % vão para B e 32 % para A.
- **O ponto a favor de A está nos brancos/nulos e nos faltantes do 1º turno.** Nesse grupo, cerca de 41 % dizem que vão votar em A e 37 % em B.
- **Todas as 22 pesquisas nacionais concordam** que B está um pouco à frente nos válidos, e a vantagem vem diminuindo devagar.

## 6. O que A precisaria para virar?

Para fechar a diferença, faltam cerca de **2,2 milhões de votos**.

### Caminho 1: pessoas mudando de lado

Continua sendo a ferramenta mais poderosa. Quando alguém sai de B e vai para A, **B perde um voto e A ganha um**, e a diferença cai **2 votos** de uma vez.

| Se, de cada 100 eleitores de A, este número for para B… | …então, de cada 100 eleitores de B, este número precisa ir para A |
|---|---|
| 0 | cerca de 2 |
| 2 | cerca de 4 |
| **4 (como está hoje)** | **cerca de 6** (hoje são cerca de 4) |
| 7 | cerca de 9 |

### Caminho 2: os faltantes indo votar

O efeito é mais fraco: um faltante que vai votar **não tira voto de ninguém**. E só ajuda A se esse grupo **preferir A bem mais do que B**. Hoje esse grupo está quase dividido ao meio.

| Se os novos eleitores votarem A:B assim… | …quantos dos 33,5 milhões de faltantes precisariam ir votar além do esperado |
|---|---|
| 55 para A, 45 para B | cerca de 4 em cada 5 (26 milhões) |
| 60:40 | cerca de 4 em cada 10 (13 milhões) |
| 2 para A, 1 para B | cerca de 1 em cada 4 (8 milhões) |
| 75:25 | cerca de 1 em cada 6 (5 milhões) |
| 100 % em A | cerca de 1 em cada 13 (2,6 milhões), **todos** votando em A |

### Caminho 3: quem de fato vai votar (duas pistas que se contradizem)

- **Pista a favor de A:** numa pesquisa de 18/10, entre os eleitores bem decididos, 95 em cada 100 de A disseram que vão votar com certeza, contra 92 em cada 100 de B. Se metade dessa diferença virasse realidade, a chance de A subiria para cerca de **17 em 100**.
- **Pista a favor de B:** na pesquisa final do nx, quando se olha só para quem tem **mais chance de votar** (deixando de fora os 21 % menos prováveis), A cai de 49,5 % para **47,6 %**. Se um quarto desse efeito fosse real, a chance de A cairia para **menos de 1 em 100**.

As duas pistas vêm de **perguntas sobre intenção de votar, não do voto real**. Como apontam para lados opostos e nenhuma foi comprovada, o cálculo principal supõe que eleitores de A e de B comparecem por igual. **Essa é a maior dúvida que sobra para amanhã.**

### Juntando tudo

Se 1 em cada 100 eleitores de cada lado trocasse a favor de A, bastaria que cerca de **2 em cada 100 faltantes** fossem votar a mais, com divisão 60:40.

Quando o simulador procura **a combinação mais provável** de dar a virada, ele escolhe de novo:

> **Só a troca de votos:** cerca de **5 em cada 100** eleitores de B indo para A, e cerca de **3 em cada 100** eleitores de A indo para B.

Essa combinação está "bem fora do comum" para o modelo, mas um pouco menos do que na conta de 23/10, porque a diferença diminuiu.

O gráfico interativo `fronteira_virada.html` mostra isso: a linha azul separa as combinações em que A vira das em que B mantém a maioria, e o ponto preto mostra onde estamos hoje.

## 7. Cuidados (as "letras miúdas")

- **As tabelas de troca de lado são só duas, e as duas são do mesmo instituto (pd).** Nenhuma nova saiu nas pesquisas finais.
- **As pesquisas finais concordam demais entre si.** Pode ser coincidência ou método parecido; não dá para saber.
- **Pesquisa por telefone e presencial podem medir diferente.** O modelo não separa isso.
- **Os grupos de eleitores dos eliminados são pequenos nas pesquisas**, então os números deles têm margem grande.
- **Comparecimento declarado não é comparecimento real**, e as duas pistas disponíveis se contradizem.
- **Tudo isso é matemática sobre hipóteses.** Serve para entender **quais peças movem o resultado**, não para apostar nem para dizer quem vai ganhar.

## 8. Resumindo em quatro frases

1. Na véspera, A está cerca de **1,8 ponto atrás** nos votos válidos, a menor diferença de todas as atualizações. A chance de virar fica em torno de **3 em 100** no cenário principal, entre **2 e 7 em 100** nas variações normais.
2. A diferença vem caindo devagar, mas a chance não sobe porque a incerteza também cai: há mais dados e menos tempo para mudanças.
3. **A maior dúvida é quem vai votar de verdade.** Uma pista ajuda A, outra ajuda B, e nenhuma está comprovada.
4. O segundo maior "e se…?" é **todas as pesquisas errarem juntas**: um erro de 1 ponto contra A levaria a chance a cerca de 34 em 100. As pesquisas finais parecem iguais demais, e por isso esse risco merece atenção.
