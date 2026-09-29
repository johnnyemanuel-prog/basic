# Lumínia — Bíblia de Som da Temporada 1

Este documento lista tudo o que a T1 precisa de som. Cada recurso tem um **código** (M = música, V = voz, U = interface do Lume, A = ambiente, F = efeito, T = transição). Os roteiros vão usar só esses códigos, por exemplo "U02 + A01", sem descrever o som de novo. Assim os recursos são reaproveitados de um episódio para outro, o que economiza produção e tokens.

---

## 0. Ordem de produção e duração do episódio

A ideia de "áudio primeiro" está certa, mas **quem define a duração é a faixa de vozes, não a música**. A música é cortada e ajustada depois, por isso ela é feita em partes separadas (stems) e em loops.

1. **Roteiro de áudio**: falas, pausas e os códigos de som de cada cena.
2. **Gravar ou gerar as vozes.**
3. **Montar a faixa de vozes com as pausas.** Aqui o episódio ganha a duração real. Referência: 1 página de roteiro dá cerca de 1 minuto.
4. **Animatic**: as imagens paradas colocadas em cima dessa faixa.
5. **Música e efeitos**: música ajustada ao corte, ambientes e efeitos.
6. **Animar só os momentos-chave** (lista na seção 7).
7. **Mixagem final** para o YouTube: −14 LUFS integrado, pico máximo de −1 dBTP, e a voz sempre na frente.

**Exceção:** as montagens sem fala (T1E8, com a véspera de todos os personagens, e a meia-noite do T1E10) são **cortadas no ritmo da música**. Nesses trechos a música vem primeiro.

---

## 1. Conceito sonoro: digital × analógico

A regra que organiza toda a trilha: **o som diz em que mundo a cena está.**

| | Mundo de cima (o Lume, a elite) | Mundo de baixo (o chão, os apagados) |
|---|---|---|
| Timbre | Sintetizador limpo, vidro, cristal, reverberação longa | Violão de nylon, cello, madeira, voz humana cantarolando |
| Ambiente | Silêncio caro, ar-condicionado, drones | Chuva no zinco, ventoinhas, rádio, goteira |
| Efeitos | Bips perfeitos, portas automáticas | Rangidos, metal, tosse, o carrinho que faz nhec |

Um recurso reforça isso: **as duas primeiras notas do bip de "aprovado" do Lume (U01) são as mesmas duas primeiras notas do tema de abertura (M01).** O sistema literalmente toca a música do país. Quando o Lume nega (U02), a nota é a mesma, só que grave e arrastada.

---

## 2. Música (M)

Cada tema é produzido **uma vez**, em partes separadas (base, melodia, percussão) e em 2 ou 3 versões. É o que dá para reaproveitar a temporada inteira.

| Código | Tema | Instrumentação e clima | Versões | Episódios |
|---|---|---|---|---|
| **M01** | Abertura "Lumínia" (15 s) | Motivo de 4 notas; sintetizador frio que termina num acorde de violão desafinado | Completa · curta de 5 s | Todos |
| **M02** | O Lume | Pads de sintetizador, arpejo de vidro, cerca de 90 BPM, tom maior estéril | a) propaganda, luminosa · b) vigilância, grave e menor · c) solene, com coro (só na meia-noite do E10) | E1, E4, E6, E8, E10 |
| **M03** | Ari | Piano em ostinato sobre um pulso de metrônomo, preciso e "matemático" | a) ambição, subindo · b) solidão, esparsa · c) queda, distorcida | E1, E2, E4, E8, E9, E10 |
| **M04** | Música da elite (diegética) | Quarteto de cordas com peças em domínio público (sugestão: uma valsa de Strauss e Bach) | a) jantar, suave · b) festa, cheia | E2, E9, E10 |
| **M05** | Chão (Alfredo, Mira, George) | Violão de nylon, cello e melodia cantarolada. Quente e latino-americano | a) ternura · b) luto · c) fantasma (lo-fi, chiado de CRT, para George) | E3, E5, E7, E8 |
| **M06** | Tubarões (Dario, Larissa, Arthur) | Pizzicato grave, contrabaixo, pulso sub; gelo no copo usado como percussão | a) elegante · b) predador | E2, E7, E9 |
| **M07** | Ordem (Helena) | Caixa militar contida, metais graves, andamento de marcha | a) dever · b) culpa (mais lenta, trompete solo) | E6, E10 |
| **M08** | Túnel Vermelho | M03 e M02 sobrepostos num crescendo que **para seco** no soco | Uma versão | E9 (final), E10 |
| **M09** | Gancho / cartela final (3–5 s) | Derivado de M01, com o motivo invertido | Uma versão | Fim de todos |
| **M10** | Jingle da LumeTV | Jingle alegre de propaganda | Completa · assinatura curta | E5, E7 e todos os curtas LumeTV |
| **M11** | Marcha nupcial (diegética) | Órgão, peça em domínio público (Mendelssohn ou Wagner) | Um trecho | E2 (flashback) |

**Total:** 9 temas originais e 2 peças em domínio público.

---

## 3. Vozes (V)

**Decidido:** todas as vozes são geradas por IA. A voz do Lume é feminina. O **narrador (V17)** existe, mas só para as frases de narração do livro que não funcionam como legenda nem como fala, **no máximo 1 a 3 por episódio**. O pensamento de um personagem entra na **voz dele** (V.O. próximo ao microfone), usado com moderação.

Os prompts de criação e as frases de teste de cada voz estão em [`vozes-t1.md`](vozes-t1.md).

### Principais
| Código | Personagem | Idade (2034) | Nota de voz |
|---|---|---|---|
| V01 | Ari | ~35 | Tenor médio, dicção precisa e rápida, sem sotaque regional. Quando está sob pressão, a fala acelera e trava |
| V02 | Larissa | ~33 | Contralto suave e pausado, frio, "sorriso na voz" |
| V03 | Dario | ~38 | Barítono charmoso, tom de quem está brindando, ri fácil; o sarcasmo aparece na pausa |
| V04 | Arthur | ~50 | Barítono grave, cadência de professor e orador; **nunca levanta a voz na T1** |
| V05 | Helena | ~48 | Firme, frases curtas, levemente rouca, tom de comando |
| V06 | Alfredo | ~48 | Voz quente de professor, teatral em sala de aula; em 2034 já rouca, com tosse (F14) |
| V07 | Mira | 21 | Grave para a idade, seca, irônica |
| V08 | George | ~24 | Rouco e contido, raiva em volume baixo |

### Secundárias, com dobras (um intérprete faz vários papéis em episódios diferentes)
| Código | Intérprete | Papéis |
|---|---|---|
| V09 | Homem maduro, grave | Roberto (E9) · Reitor Heitor (E3) · chefe da segurança (E5) |
| V10 | Homem comum, 40 anos | O Apagado (E1) · supervisor da usina (E3) · pai de George (E5) |
| V11 | Jovem | Enzo (E1) · Felipe (E4) · analista júnior (E4) · (Beto na T3) |
| V12 | Homem de 60 anos, simples | Jonas (E5) · gerente de TI (E4) · convidado "o técnico fez o seu trabalho" (E9) |
| V13 | Criança (menina, 10 anos) | Mira pequena (E3) |
| V14 | Criança (menino, 13 anos) | George pequeno (E5) |
| V15 | Mulher, voz de apresentadora | Locutora da LumeTV (E5, E7, curtas) |
| V16 | Inglês nativo | Julian: "Fred, mate! Pega uma!" (E7) |
| **V00** | **Voz do Lume** (feminina) | Voz do sistema, calma e simpática, com processamento leve (filtro e reverberação curta). É um personagem recorrente |
| **V17** | Narrador | Mínimo: 1 a 3 frases por episódio |
| W | Walla (vozes de multidão) | Festa, comício, sala de aula, Occupy, cozinha do casamento |

### Falas do Lume (V00): gerar uma vez e reutilizar
- "Acesso autorizado. Bom dia, Diretor Adjunto Lanes."
- "Transação aprovada."
- "Erro crítico. Destinatário inexistente. Tentativa de transação com usuário deletado."
- "Acesso negado."
- "Status atualizado."
- "Compilação concluída. Lume 3.0 pronto para implantação."
- "Bem-vindo, cidadão." · "Toque de recolher juvenil em vinte minutos."
- (Para T2 e T3, já gravar:) "Usuário não encontrado." · "Você contribuiu para o giro econômico. Parabéns, cidadã."

---

## 4. Interface do Lume (U)

É a família sonora mais importante e a que mais se repete. Todos os sons têm o mesmo timbre de vidro e sintetizador.

| Código | Som | Uso na T1 |
|---|---|---|
| U01 | Bip de aprovado (2 notas subindo, as mesmas de M01) | Catracas, pagamentos, portas |
| U02 | Bip de negado (três bips longos e graves, BEEEEP) | Apagado (E1), Alfredo (E3) |
| U03 | Erro crítico (glitch descendo + alarme curto) | Bracelete do Apagado (E1) |
| U04 | Aproximação NFC (chiado curto + pulso) | Pulso com pulso (E1) |
| U05 | Notificação | Espelho inteligente (E1), avisos |
| U06 | Scanner biométrico (retina, pulso) | Entrada no BC (E3) |
| U07 | Holograma que aparece ou some | Agenda (E1), mapa, logo do Lume (E8) |
| U08 | Teclado holográfico | Ari digitando (E4, E8), cartelas de tempo e lugar |
| U09 | Barra de progresso + "concluído" | Latência caindo (E4), 99% → 100% (E8) |
| U10 | Mudança de status (3 cliques descendo) | ATIVO → SUSPENSO → INDESEJADO (E3) |
| U11 | Bracelete desligando | Alfredo (E3), meia-noite (E10) |
| U12 | Áudio de câmera de segurança (voz metálica, estourada) | Câmera 04 (E9) |

**Contraponto analógico**, no mundo de baixo: teclado mecânico, chiado de CRT e o clique de uma chave de fenda (bunker, E5).

---

## 5. Ambientes (A)

Loops de 1 a 2 minutos. **São 16 ambientes para a temporada inteira**, e vários voltam na T2 e na T3.

| Código | Ambiente | Episódios (T1) | Volta em |
|---|---|---|---|
| A01 | Lucerna à noite: zumbido elétrico, carros elétricos, drones distantes, **nenhuma voz humana** | E1, E8, E10 | T2, T3 |
| A02 | Delegacia morta: vento, painel de propaganda murmurando, drone parado no ar | E1 | T2E8 |
| A03 | Apartamento de Ari e Larissa: silêncio, zumbido do espelho inteligente | E1, E8 | — |
| A04 | Carro blindado por dentro: pneus abafados, silêncio | E1, E6 | T3 |
| A05 | Cobertura de Dario: ar-condicionado, cidade distante atrás do vidro | E1, E2 | — |
| A06 | Saguão do BC: eco de mármore, catracas | E3, E4 | T3 |
| A07 | Núcleo, servidores: ventoinhas e ar-condicionado forte | E4, E8 | T2, T3 |
| A08 | 20º andar: silêncio de luxo, vento contra o vidro | E4 | T3 |
| A09 | Usina: prensas hidráulicas, esteira, apitos | E3 | — |
| A10 | Barraco de Alfredo: chuva no zinco, goteira, rádio distante | E3, E7, E8 | T2 |
| A11 | Bunker dos Offliners: ventoinhas improvisadas, chiado de CRT, fios estalando | E5, E8 | T2, T3 |
| A12 | Salão de Cristal: vozes da elite, taças, drones do lado de fora da cúpula | E9, E10 | — |
| A13 | Gabinete presidencial: silêncio filtrado, **relógio antigo** (tic-tac = a História) | E7 | T3 |
| A14 | Comício de 2028: multidão reverente e silenciosa, alto-falantes | E6 | — |
| A15 | Flashbacks, pacote único: sala de aula de 2023 (canetão, sinal digital) · igreja de 2023 (eco) · rua e cozinha do casamento (chapa de Cartucho, garçons) · Londres 2011 (tambores, "We are the 99%") | E2, E3, E5, E7 | — |
| A16 | Chuva ácida na cidade (camada que se soma a A01) | E5, E8 | T2, T3 |

---

## 6. Efeitos (F) e transições (T)

### Foley e efeitos
| Código | Som | Observação |
|---|---|---|
| F01 | Passos: sapato social no mármore · salto alto · bota militar · tênis | Um pacote, 4 variações |
| F02 | **Gelo girando no copo de uísque** | **Assinatura sonora de Dario.** Sempre que ele aparece, antes de falar |
| F03 | **O carrinho de limpeza, com nhec** | **Assinatura sonora de Mira.** Estreia no E4 |
| F04 | Taças: brinde e cristal | E2, E9 |
| F05 | Vidro quebrando / bandeja caindo | E9, E10 |
| F06 | Soco (impacto seco) | **Uma vez só, no E10** |
| F07 | Queda de corpo | Roberto (E10), pai de George (E5) |
| F08 | Porta de metal pesada | Doca de carga (E5), bunker |
| F09 | Porta automática de vidro | BC, cobertura |
| F10 | Tosse de Alfredo (5 a 6 tomadas, da leve à pesada) | E3, E7, E8, e T2/T3 |
| F11 | Drone: passando · descendo e parando no ar | Exteriores; E6 no gancho |
| F12 | **Zumbido no ouvido + mundo abafado** (filtro que corta os agudos) | Humilhação de Ari (E9), túnel vermelho (E10). Volta no 404 da T2 |
| F13 | Batimento cardíaco | Túnel vermelho (E10) |
| F14 | Gerador B ao longe, tossindo | Pista no E4, que paga na T3 |
| F15 | Tecido, gravata e abotoaduras | Ari se arrumando (E1, E8) |
| F16 | Caneta-tinteiro + papel | Ari (E4) |
| F17 | Prensa hidráulica + acidente | E3 |
| F18 | Chapa e Cartucho sendo feito | E5 (rua do casamento) |
| F19 | Elevador de luxo: sino suave + portas | E1, E4 (20º andar); T3 |
| F20 | Vibração curta de celular | E1 (mensagem de "D."); reaproveitável |

### Transições
| Código | Som | Regra |
|---|---|---|
| T01 | **Entrada de memória**: reverberação ao contrário + filtro | Todo flashback entra com T01 e sai com T01 invertido |
| T02 | **Corte seco para o preto (silêncio total)** | Só nos ganchos. O silêncio é o efeito |
| T03 | Troca de mundo: **para cima**, um tilintar de vidro; **para baixo**, um baque grave abafado | Nos cortes entre elite e chão (E3 tem vários) |
| T04 | Cartela de tempo e lugar ("Lucerna, 2034") | Usa U08 |

---

## 7. Mapa por episódio

| Ep | Ambientes | Música | Efeitos-chave | Momento para animar |
|---|---|---|---|---|
| 1 Destinatário Inexistente | A01, A02, A03, A04, A05 | M01, M02b, M03a, M06a | U04, U03, V00, U05, U07, F15, F11, F02 (na porta) | **O bracelete: NFC → vermelho** · a agenda holográfica no espelho |
| 2 O Triunvirato | A05, A15 (igreja) | M04a, M06a/b, M11, M03a | F02, F04, T01 | O olhar no altar (movimento lento de câmera) |
| 3 Indesejado | A06, A09, A10, A15 (sala de aula) | M03a × M05a (alternando), M05b | U06, U01, U10, U11, F17, F10, T03, T01 | **A tela ATIVO → INDESEJADO** · o bracelete apagando |
| 4 Economia Cognitiva | A06, A07, A08 | M03a/b, M02a | F03 (estreia), F01, U08, U09, F14, F16 | **A latência caindo de 400 para 12 ms** |
| 5 O Guri da Fronteira | A11, A16, A15 (rua e cozinha) | M05c, M05b, M10 (TV) | F08, F18, F07, F05, T01 | A TV do bunker com a contagem regressiva |
| 6 Formação Diamante | A04, A14 | M07a/b, M02b | F01 (bota), F11 (drone descendo) | **O drone descendo e subindo** |
| 7 Você Não Tinha Wi-Fi, Karl | A10, A15 (Londres), A13 | M05a, M10, M06b, M02b | F10, T01, relógio do A13 | Máscara de Guy Fawkes (trecho curto) |
| 8 99% | A07, A03, A10, A11, A01 | **Montagem cortada na música:** M03a → M02a | U09, U07, F15 | **O holograma do Lume girando + a barra chegando a 100%** |
| 9 O Salão de Cristal | A12 | M04b, M06a/b, M03b, M08 (início) | F04, F12, U12 | **O celular com a câmera 04** |
| 10 Bata | A12, A01 | M08 → T02 → **M02c (montagem da meia-noite)** → M09 | F05, F07, F13, F06 (o único soco), U11, U01 | **O túnel vermelho** · os braceletes de toda a cidade mudando à meia-noite |

---

## 8. Lista de produção (em ordem de prioridade)

1. **V00 + U01–U12**: a família do Lume aparece em quase todas as cenas.
2. **M01, M02, M03 e M05**: sustentam 80% da temporada.
3. **A01, A07, A10 e A11**: os ambientes que mais se repetem.
4. **F02 e F03**: as assinaturas de Dario e Mira.
5. O resto, na ordem em que os episódios forem feitos.

---

## 9. Onde buscar música e efeitos com uso liberado

Canal no YouTube com monetização conta como **uso comercial**. Confira sempre a licença de cada faixa, porque dentro de um mesmo site as licenças variam. Guarde o nome, o link e a licença de tudo numa planilha.

### Música gerada por IA (a sua escolha principal)
- **Verifique o plano antes de gerar.** Em várias ferramentas (por exemplo Suno e Udio), o **plano gratuito não libera uso comercial**, e a música gerada ali não pode ir para um canal monetizado. Gere já no plano pago, porque a licença normalmente vale para o que foi gerado durante a assinatura.
- Peça sempre **instrumental** e, quando a ferramenta permitir, **as partes separadas (stems)** para ajustar ao corte.

### Bibliotecas de música
| Biblioteca | Para quê | Licença |
|---|---|---|
| **YouTube Audio Library** (dentro do YouTube Studio) | Complemento geral e mais seguro contra reclamação de direitos no próprio YouTube | Grátis; algumas faixas pedem crédito na descrição |
| **Musopen** | **M04 e M11**: gravações de clássicos (Strauss, Bach, Mendelssohn) | Muitas gravações em domínio público; confira cada uma |
| **Pixabay Music** | Complemento, trilhas de tensão | Grátis e sem crédito obrigatório, mas algumas faixas geram reclamação automática de direitos no YouTube; teste antes de publicar |
| **Incompetech (Kevin MacLeod)** | Emergências, clima genérico | CC BY: crédito obrigatório na descrição |

### Bibliotecas de efeitos
| Biblioteca | Para quê | Licença |
|---|---|---|
| **Freesound** | Ambientes e foley (chuva no zinco, passos, taças) | Por som: prefira **CC0**; CC BY exige crédito; **evite CC BY-NC** (não comercial) |
| **Pixabay Sound Effects** | Efeitos rápidos | Grátis, sem crédito |
| **Sonniss (pacotes GDC)** | Pacotes profissionais grandes: interface, drones, ambientes urbanos | Livre de royalties, uso comercial liberado |
| **ElevenLabs Sound Effects** | Sons sob medida da família U (interface do Lume) e do gerador | Uso comercial nos planos pagos |

**Evite:** BBC Sound Effects, porque a licença gratuita é só para uso não comercial.
