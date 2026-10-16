# Resumo para leigos (explicado como para alguém de 17 anos)

A versão técnica completa está em `RELATORIO.md`. Aqui vai o mesmo conteúdo, só que sem fórmulas.

---

## 1. A situação

Uma eleição teve dois turnos. No 2º turno sobraram dois candidatos, **A** e **B**.

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
7. **Tempo:** quanto a opinião das pessoas pode mudar nos **10 dias** que faltam até a eleição.

Usamos três fontes de informação:
- o resultado oficial do 1º turno;
- pesquisas que perguntam *"em quem você votou antes e em quem vai votar agora"*;
- **oito pesquisas nacionais** de 2º turno, de sete institutos diferentes.

Uma dessas pesquisas, a do instituto pd, trazia números que não batiam entre si. Por isso ela recebeu **meio peso**, como num trabalho em grupo em que a nota de um colega vale metade porque o trabalho dele tinha umas contas estranhas.

## 3. O resultado

> **A aparece com cerca de 48,4 % dos votos válidos, e B com cerca de 51,6 %.**
>
> Em **2 a 5 de cada 100 simulações**, A termina com mais de 50 %.

Ou seja, uma virada de A não é impossível, mas aparece pouco nas simulações. Para comparar: 5 em 100 é a chance de tirar um número específico num dado de 20 lados, numa jogada só. 2 em 100 é ainda menos que isso.

⚠️ **Isso não é uma previsão.** É o que sai quando juntamos estes dados com estas hipóteses. Se as hipóteses mudarem, o número muda.

## 4. Por que a conta pende para B

- **Fidelidade parecida, mas um pouco maior em B.** Cerca de 94,6 % dos eleitores de B repetem o voto, contra cerca de 92 % dos eleitores de A. A diferença no lado de A vai mais para branco/nulo/indeciso do que para B.
- **A troca de lado está empatada.** Cerca de 5 % dos eleitores de cada lado dizem que vão mudar para o outro. Um anula o outro.
- **Os eleitores dos eliminados pendem um pouco para B**, mas são poucos e pesam pouco no total.
- **As oito pesquisas nacionais dizem praticamente a mesma coisa:** B entre 50,5 % e 52,8 % dos válidos.

## 5. O que A precisaria para virar?

Para fechar a diferença, faltam cerca de **3,8 milhões de votos**. Testamos duas formas de conseguir isso.

### Caminho 1: pessoas mudando de lado (a "virada de voto")

Esta é a ferramenta mais poderosa. Quando alguém sai de B e vai para A, **B perde um voto e A ganha um**. A diferença cai **2 votos** de uma vez, como num jogo em que o gol de um time também tira um ponto do outro.

| Se, de cada 100 eleitores de A, este número for para B… | …então, de cada 100 eleitores de B, este número precisa ir para A |
|---|---|
| 0 | cerca de 4 |
| 2 | cerca de 6 |
| **5 (como está hoje)** | **cerca de 9** |
| 7 | cerca de 11 |

**Regrinha:** para cada eleitor de A que passa para B, A precisa trazer de volta praticamente um eleitor de B a mais.

### Caminho 2: os faltantes indo votar

Aqui o efeito é bem mais fraco. Um faltante que vai votar **não tira voto de ninguém**: ele só soma de um lado. E isso só ajuda A se esse grupo **preferir A bem mais do que B**.

Hoje as pesquisas indicam que os faltantes estão divididos mais ou menos ao meio (entre 45 % e 53 % para A).

| Se os novos eleitores votarem A:B assim… | …quantos dos 33,5 milhões de faltantes precisariam ir votar além do esperado |
|---|---|
| 55 para A, 45 para B | **mais do que existem** (impossível) |
| 60:40 | cerca de 2 em cada 3 (22 milhões) |
| 2 para A, 1 para B | cerca de 4 em cada 10 (13 milhões) |
| 75:25 | cerca de 1 em cada 4 (9 milhões) |
| 100 % em A | cerca de 1 em cada 8 (4,4 milhões), **todos** votando em A |

### Juntando os dois caminhos

Dá para misturar: um pouco de gente mudando de lado e um pouco de faltante indo votar. Por exemplo, se 1 em cada 100 eleitores de cada lado trocasse a favor de A, ainda seria preciso que cerca de 30 % dos faltantes fossem votar com divisão 60:40.

Quando o simulador procura **a combinação mais provável** de dar a virada, ele escolhe:

> **Só a troca de votos:** cerca de **7 em cada 100** eleitores de B indo para A, e só cerca de **3 em cada 100** eleitores de A indo para B.

Ele deixa o comparecimento de fora. O motivo: para os faltantes ajudarem, duas coisas precisam acontecer **ao mesmo tempo**. Muito mais gente precisa ir votar **e** essa gente precisa preferir A com folga. Duas surpresas juntas são bem menos prováveis que uma só.

Nas simulações em que A vence:
- cerca de **3/4 da virada** vêm da **troca de votos**;
- cerca de **1/4** vem de as pesquisas terem medido um pouco errado como as pessoas votaram no 1º turno;
- o **comparecimento** contribui de **quase nada** até cerca de 1/5, dependendo de quanto se deixa ele variar.

## 6. Cuidados (as "letras miúdas")

- **Os dados têm contradições.** A pesquisa pd, aplicada ao resultado real, dá A com 47 %, mas a mesma pesquisa diz 49 %. E dois institutos (pd e qu) discordam sobre alguns grupos de eleitores. Mostramos isso em vez de esconder.
- **Não sabemos quantas pessoas de cada grupo foram entrevistadas.** Por isso usamos estimativas.
- **Sobre os faltantes quase não há dados.** O quanto eles podem mudar o jogo é uma suposição nossa.
- **Se todas as pesquisas errarem para o mesmo lado**, o modelo não tem como perceber. Só dá para testar "e se…?".
- **Tudo isso é matemática sobre hipóteses.** Serve para entender **quais peças movem o resultado**, não para apostar nem para dizer quem vai ganhar.

## 7. Resumindo em três frases

1. Pelos dados, A está cerca de 3 pontos atrás nos votos válidos, e a chance de virar fica em torno de **2 a 5 %** neste modelo.
2. O que mais poderia mudar isso é **gente trocando de lado**, porque cada troca vale dois votos.
3. **Levar mais gente para votar** quase não muda a conta, a menos que essas pessoas prefiram A com muita folga, coisa que as pesquisas hoje não mostram.
