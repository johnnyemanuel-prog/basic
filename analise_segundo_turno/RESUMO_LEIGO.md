# Resumo para leigos (explicado como para alguém de 17 anos)

**Atualizado em 21/10** com as pesquisas divulgadas até 20/10.

A versão técnica completa está em `ATUALIZACAO_2110.md` (dados novos) e `RELATORIO.md` (versão anterior). Aqui vai o mesmo conteúdo, só que sem fórmulas.

---

## 1. A situação

Uma eleição teve dois turnos. No 2º turno sobraram dois candidatos, **A** e **B**. A votação é em **25/10**.

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
7. **Tempo:** quanto a opinião das pessoas pode mudar nos **5 dias** entre a última pesquisa (20/10) e a eleição.

Usamos três fontes de informação:
- o resultado oficial do 1º turno;
- pesquisas que perguntam *"em quem você votou antes e em quem vai votar agora"*: agora são quatro institutos, alguns com duas rodadas;
- **16 pesquisas nacionais** de 2º turno, de **10 institutos diferentes**. Oito delas são novas, feitas entre 13 e 20/10.

### O que mudou no jeito de calcular

- **Pesquisa velha pesa menos.** Uma pesquisa de 11/10 sobre "para onde vão os eleitores de C" vale menos que uma de 20/10. Não jogamos a velha fora; só damos mais peso à mais recente, como uma previsão do tempo, em que a de ontem vale mais que a da semana passada.
- **Nada é contado duas vezes.** Quando uma mesma pesquisa traz o resultado geral **e** a tabela de "quem votou em quem", as duas partes vêm das mesmas pessoas. Por isso cada parte entra com metade do peso, como num trabalho em grupo em que a mesma pessoa não pode assinar duas vezes.
- **Mudança entre duas pesquisas não prova que alguém mudou de voto.** O instituto qu, por exemplo, achou que os eleitores de C iam 34 % para A em 13/10 e 48 % em 20/10. Mas foram pessoas **diferentes** entrevistadas em cada rodada, e o grupo é pequeno (margem de ±17 pontos). Tratamos isso como duas medições imprecisas, não como "14 % mudaram de ideia".

## 3. O resultado

> **A aparece com cerca de 48,7 % dos votos válidos, e B com cerca de 51,3 %.**
>
> Em **cerca de 3 de cada 100 simulações**, A termina com mais de 50 %. A faixa vai de **2 a 8 em 100**, dependendo de quanto a opinião pode mudar até domingo.

Antes, com os dados até 14/10, A aparecia com 48,4 %. A diferença diminuiu um pouco: B agora está cerca de **3,0 milhões** de votos à frente, contra 3,8 milhões antes.

Para comparar: 5 em 100 é a chance de tirar um número específico num dado de 20 lados, numa jogada só. 3 em 100 é um pouco menos que isso.

⚠️ **Isso não é uma previsão.** É o que sai quando juntamos estes dados com estas hipóteses. Se as hipóteses mudarem, o número muda.

## 4. Por que a conta ainda pende para B

- **Fidelidade parecida, mas um pouco maior em B.** Cerca de 94 % dos eleitores de B repetem o voto, contra cerca de 92 % dos eleitores de A.
- **A troca de lado está empatada.** Cerca de 5 % dos eleitores de cada lado dizem que vão mudar para o outro. Um anula o outro.
- **Os eleitores dos eliminados ainda pendem para B, mas menos que antes.** Juntando C, D, E e F: cerca de 44 % vão para B e 32 % para A (antes era 46 contra 27).
- **Os faltantes e quem votou branco/nulo no 1º turno estão divididos ao meio**, cerca de 37 % para cada lado entre os entrevistados.
- **As pesquisas novas dizem praticamente a mesma coisa:** B entre 50,3 % e 51,6 % dos válidos. Elas mostram B um pouco abaixo das pesquisas da semana anterior, mas a diferença é pequena e cabe no erro normal das pesquisas.

## 5. O que A precisaria para virar?

Para fechar a diferença, faltam cerca de **3,0 milhões de votos**.

### Caminho 1: pessoas mudando de lado (a "virada de voto")

Esta continua sendo a ferramenta mais poderosa. Quando alguém sai de B e vai para A, **B perde um voto e A ganha um**. A diferença cai **2 votos** de uma vez, como num jogo em que o gol de um time também tira um ponto do outro.

| Se, de cada 100 eleitores de A, este número for para B… | …então, de cada 100 eleitores de B, este número precisa ir para A |
|---|---|
| 0 | cerca de 3 |
| 2 | cerca de 5 |
| **5 (como está hoje)** | **cerca de 8** (hoje são cerca de 5) |
| 7 | cerca de 10 |

**Regrinha:** para cada eleitor de A que passa para B, A precisa trazer de volta praticamente um eleitor de B a mais.

### Caminho 2: os faltantes indo votar

Aqui o efeito é bem mais fraco. Um faltante que vai votar **não tira voto de ninguém**: ele só soma de um lado. E isso só ajuda A se esse grupo **preferir A bem mais do que B**. Hoje esse grupo está dividido mais ou menos ao meio.

| Se os novos eleitores votarem A:B assim… | …quantos dos 33,5 milhões de faltantes precisariam ir votar além do esperado |
|---|---|
| 55 para A, 45 para B | **mais do que existem** (impossível) |
| 60:40 | mais da metade (18 milhões) |
| 2 para A, 1 para B | cerca de 1 em cada 3 (11 milhões) |
| 75:25 | cerca de 1 em cada 5 (7 milhões) |
| 100 % em A | cerca de 1 em cada 9 (3,7 milhões), **todos** votando em A |

### Caminho 3 (novo): quem de fato vai votar

Uma pesquisa nova perguntou se as pessoas vão mesmo votar. Entre os eleitores bem decididos, **95 em cada 100 de A** disseram que vão com certeza. **De B, 92 em cada 100.**

Se essa diferença virasse diferença real nas urnas, mudaria bastante a conta, porque não é só um grupo pequeno: são **todos** os eleitores de cada lado comparecendo um pouco mais ou um pouco menos.

| Quanto dessa diferença vira realidade | Chance de A passar de 50 % |
|---|---|
| nada (hipótese principal) | cerca de 3 em 100 |
| um quarto | cerca de 6 em 100 |
| metade | cerca de 11 em 100 |
| tudo | cerca de 29 em 100 |

Mas tem um porém grande: **dizer que vai votar não é o mesmo que votar**. Pela pesquisa, 93 % do eleitorado diz que vai votar com certeza ou provavelmente, mas no 1º turno só 79 % votaram. Então não sabemos quanto dessa diferença é real. É por isso que ela fica como "e se…?", e não no cálculo principal.

### Juntando tudo

Se 1 em cada 100 eleitores de cada lado trocasse a favor de A, ainda seria preciso que cerca de **1 em cada 6 faltantes** fosse votar com divisão 60:40.

Quando o simulador procura **a combinação mais provável** de dar a virada, ele escolhe de novo:

> **Só a troca de votos:** cerca de **7 em cada 100** eleitores de B indo para A, e cerca de **4 em cada 100** eleitores de A indo para B.

Essa combinação ficou **mais perto** do que o modelo considera normal do que na conta anterior, por dois motivos:
- a diferença a fechar diminuiu;
- a tabela de troca entre A e B é de 11/10 e ninguém publicou uma nova, então hoje temos **menos certeza** sobre ela.

O gráfico interativo `fronteira_virada.html` mostra isso: a linha separa as combinações em que A vira das em que B mantém a maioria.

## 6. Cuidados (as "letras miúdas")

- **A troca direta entre A e B é a peça mais importante e a menos medida.** Só existe uma tabela, de 11/10.
- **Os grupos de eleitores dos eliminados são pequenos nas pesquisas.** Por isso os números deles têm margem enorme (±17 a ±24 pontos).
- **Os institutos discordam um pouco**, mas nenhum se afasta dos outros mais do que o erro normal. Não descartamos nenhum.
- **Se todas as pesquisas errarem para o mesmo lado**, o modelo não tem como perceber. Só dá para testar "e se…?".
- **Comparecimento declarado não é comparecimento real.** Ele entrou só como cenário.
- **Rejeição, voto espontâneo e "posso mudar de voto"** são perguntas diferentes da intenção de voto. Ficaram só como contexto.
- **Tudo isso é matemática sobre hipóteses.** Serve para entender **quais peças movem o resultado**, não para apostar nem para dizer quem vai ganhar.

## 7. Resumindo em quatro frases

1. Com as pesquisas até 20/10, A está cerca de **2,6 pontos atrás** nos votos válidos, um pouco menos que antes. A chance de virar fica em torno de **3 em 100** no cenário principal, entre **2 e 8 em 100** conforme o quanto a opinião ainda pode mudar.
2. O que mais poderia mudar isso continua sendo **gente trocando de lado**, porque cada troca vale dois votos.
3. **A novidade é o comparecimento real.** Se os eleitores de A forem mesmo votar mais que os de B, como eles dizem, a chance pode subir para 6 a 11 em 100, mas ninguém sabe quanto do "eu vou votar" vira voto de verdade.
4. **Levar mais faltantes para votar** quase não muda a conta, porque eles estão divididos ao meio.
