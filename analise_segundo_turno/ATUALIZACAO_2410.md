# Atualização incremental de 24/10 — rodadas finais (v4)

Esta versão acrescenta **quatro pesquisas**: df-r4, qu-r3, nx-r3 e pv-r3.

- **O que foi preservado:** todas as rodadas anteriores, seus parâmetros e as versões v1, v2 e v3 (arquivos `modelo*.py`, `resultados*.md` e `ATUALIZACAO_*.md`).
- **O que não entrou:** nenhum instituto novo e nenhuma taxa nova de migração direta.
- **Onde está a versão nova:** o código em `modelo_v4.py`, as tabelas completas em `resultados_v4.md` e os números principais em `resultados_v4.json` (semente 20261024, 1.000.000 de sorteios).
- **Datas:** eleição em 25/10 e último dia de campo em 24/10, o que dá um horizonte de 1 dia.

Todas as probabilidades são **condicionais às hipóteses**. Não são previsões.

---

## 1. Conferência dos novos inputs

| id | Campo | Modo | n | Σ totais | B/(A+B) dos totais | B válido publicado | Diferença | Margem publicada / margem de amostragem aleatória simples (AAS) | DEFF implícito |
|---|---|---|---:|---|---:|---:|---:|---|---:|
| df-r4 | 23–24/10 | presencial | 4.050 | 100 % | 50,53 % | 51 % | −0,47 | 2,0 / 1,54 | 1,69 |
| qu-r3 | 23–24/10 | presencial | 3.702 | 100 % | 50,55 % | 51 % | −0,45 | 2,0 / 1,61 | 1,54 |
| nx-r3 | 23–24/10 | telefone | 2.000 | 100 % | 50,54 % | 50,5 % | +0,04 | 2,2 / 2,19 | 1,01 |
| pv-r3 | 22–24/10 | não informado | 5.000 | 100 % | 50,51 % | **não publicado** | — | 2,2 / 1,39 | 2,52 |

- **Sem duplicação de totais e válidos (instrução 3).** Cada levantamento entra uma vez, pela fração B/(A+B) calculada dos totais.
  - Os válidos publicados servem só de checagem. As diferenças (até 0,47 p.p.) são compatíveis com arredondamento para inteiro (df, qu) ou para meio ponto (nx).
  - **pv:** como não publicou válidos, a conversão 50/99 = 50,51 % foi feita a partir dos totais arredondados. **Limitação:** com A e B arredondados para inteiro, a fração tem incerteza de cerca de ±0,4 p.p. só por arredondamento. Isso entra em σ_j (instrução 9).
- **Datas de campo** entram na modelagem temporal (instrução 2). Todas as quatro foram informadas.
- **Margens:** df e qu mantiveram ±2,0 com amostras maiores, o que implica DEFF de 1,5–1,7, compatível com amostragem presencial por conglomerados. Usei a regra de sempre: max(margem publicada, margem AAS).
- **Modo de coleta:** o modelo não tem parâmetro de modo. Diferenças entre presencial e telefone ficam no efeito do instituto (h_j) e em σ_extra.
- **Variáveis auxiliares** ficam na camada descritiva, fora da likelihood:
  - df voto decidido 95 %;
  - nx definitivo 94,3 / pode mudar 4,7 / NS 1,1 (soma 100,1 por arredondamento); entre eleitores de A 95,7 % e de B 97,4 %;
  - pv rejeição A 49 / B 47.
  - **Voto definitivo não foi usado como probabilidade de retenção (instrução 5).** Rejeição não foi tratada como voto.
- **LVM de nx:** A 47,6 / B 52,4 nos válidos, excluindo 21 % da amostra. Vem da mesma amostra, então entra **só** na sensibilidade de comparecimento (instrução 6).
- **Matrizes de transferência:** nenhuma nova. pd-r1 (~11/10) e pd-r3 (19–21/10) seguem com suas datas e desconto temporal (instruções 7–8). Rodadas sem cruzamentos de transferência não exigem tempera de dependência.

---

## 2. Quadro anterior × atual: parâmetros estruturais e resultado

| Parâmetro (média [IC 90 %]) | v3 (até 22/10) | **v4 (até 24/10)** |
|---|---|---|
| R_A = A₁→A | 93,6 [91,8; 95,2] | 93,7 [92,0; 95,3] |
| X_AB = A₁→B | 4,4 [3,1; 5,9] | 4,3 [3,0; 5,8] |
| R_B = B₁→B | 95,3 [93,7; 96,7] | 95,2 [93,6; 96,6] |
| X_BA = B₁→A | 3,9 [2,6; 5,3] | 4,0 [2,7; 5,4] |
| C→A / C→B | 41,0 / 40,8 | 41,1 / 40,7 |
| C:F agregado →A / →B | 32,2 / 45,3 | 32,3 / 45,1 |
| X (BN₁+ABS₁) →A / →B | 41,0 / 37,1 | 41,1 / 37,0 |
| θ_B latente nas pesquisas (25/10) | 51,04 % ± 0,74 | **50,81 % ± 0,57** |
| **θ_A, modelo completo** | 48,89 % [47,93; 49,84] | **49,07 % [48,27; 49,88]** |
| **P(θ_A > 0,5)** | 2,7 % | **2,9 %** |
| Diferença média V_B − V_A | 2,68 mi | **2,23 mi** |
| Fronteira de virada: distância do ponto atual | 2,30 dp | **1,96 dp** |

**Leitura:**
- **Parâmetros estruturais:** praticamente iguais, com mudanças de até 0,2 p.p. Era o esperado, porque não há novas transferências. Pequenas oscilações vêm do erro de Monte Carlo e do ajuste conjunto com as pesquisas.
- **Resultado:** o que muda é o nível medido pelas pesquisas. A média de A sobe 0,2 p.p., a diferença cai cerca de 450 mil votos e a incerteza diminui. A probabilidade fica praticamente igual.
- **Fronteira de virada** (com correlação ρ = 0,16 entre os dois fluxos):
  - Regra: X_BA necessário = 1,88 % + 0,964 × X_AB.
  - No X_AB atual (4,4 %), B→A precisaria chegar a cerca de 6,1 %, contra 4,0 % estimado.
  - O ponto mais provável sobre a fronteira é B→A 5,1 % e A→B 3,3 %.

---

## 3. Comparação das medições entre institutos

**As rodadas finais praticamente coincidem:**

| Rodada | Modo | θ_B | z contra a média ponderada |
|---|---|---:|---:|
| df-r4 | presencial | 50,53 % | −0,00 |
| qu-r3 | presencial | 50,55 % | +0,02 |
| nx-r3 | telefone | 50,54 % | +0,01 |
| pv-r3 | não informado | 50,51 % | −0,02 |

A média ponderada é **θ_B = 50,53 %**, ou θ_A = 49,47 %.

**Concordância maior do que o acaso explica.** O Q de Cochran é 0,001 com 3 graus de liberdade. Se as quatro pesquisas fossem amostras independentes com os erros declarados, uma dispersão tão pequena teria probabilidade da ordem de 10⁻⁶. Parte disso é aritmética: nas quatro, B − A = 1 ponto nos totais arredondados, e isso dá sempre B/(A+B) ≈ 50,5 %. Mesmo assim, a concordância está bem abaixo do esperado. **Não dá para distinguir** entre coincidência de arredondamento, metodologias parecidas ou ajuste das pesquisas umas às outras. Por isso, as quatro não devem ser lidas como quatro confirmações independentes. A seção 5 trata isso como erro comum.

**Rodadas consecutivas do mesmo instituto** (diferença bruta, sem atribuir causa):

| Instituto | Rodadas | Δ θ_B (p.p.) | z |
|---|---|---:|---:|
| df | 22/10 → 24/10 | −0,01 | −0,01 |
| qu | 20/10 → 24/10 | −0,01 | −0,01 |
| nx | 18/10 → 24/10 | +0,21 | +0,13 |
| pv | 20/10 → 24/10 | −0,52 | −0,30 |

**House effects:** todos ficam entre −0,13 e +0,18 p.p. (dp ≈ 0,43), e nenhum instituto se destaca. df agora tem 4 rodadas; qu, nx, pv e pd têm 3. fu, mi, rt e ip continuam com uma rodada só, identificadas apenas pelo prior.

**Tendência latente:** θ_B vai de 51,9 % (4/10) para 51,2 % (14/10), 50,9 % (20/10) e **50,8 % (24/10)**. A queda vem sendo contínua e lenta.

---

## 4. Sensibilidade às hipóteses de comparecimento

As duas evidências disponíveis apontam em **direções opostas**, e nenhuma é probabilidade calibrada.

**a) κ — diferencial declarado entre convictos (nx-r2: A 95,0 %, B 91,6 %).** Favorece A. κ é a fração desse diferencial que vira diferença real nas urnas.

| κ | E[θ_A] | P(θ_A > 0,5) |
|---:|---:|---:|
| 0 (caso-base) | 49,07 % | 2,9 % |
| 0,25 | 49,30 % | 7,6 % |
| 0,5 | 49,53 % | 16,7 % |
| 1 | 49,99 % | 48,8 % |

**b) ω — LVM de nx-r3.** Favorece B. Na mesma amostra, restringir a análise aos eleitores mais prováveis muda A de 49,46 % para 47,6 % dos válidos (Δ = −1,86 p.p.). ω é a fração desse efeito aplicada ao modelo.

| ω | E[θ_A] | P(θ_A > 0,5) |
|---:|---:|---:|
| 0 (caso-base) | 49,07 % | 2,9 % |
| 0,25 | 48,61 % | 0,2 % |
| 0,5 | 48,14 % | < 0,1 % |
| 1 | 47,21 % | < 0,1 % |

**Combinações:** com κ = ω = 0,25, E[θ_A] = 48,84 % e P = 0,9 %. Com κ = ω = 0,5, 48,60 % e 0,2 %. Por unidade, o efeito do LVM é maior que o do diferencial dos convictos, porque o LVM é medido diretamente na base de votos válidos.

**c) Comparecimento total × divisão dos faltantes adicionais.** Com o comparecimento igual ao do 1º turno, P = 2,9 %. Com +5 p.p. de comparecimento e divisão 60:40, P = 22 %. Com +5 p.p. e divisão 2:1, P = 50 %. Esses cenários exigem que os faltantes prefiram A muito mais do que indicam as pesquisas, que hoje dão cerca de 52:48 entre os válidos desse grupo.

**Hipótese mantida no caso-base:** κ = ω = 0, ou seja, comparecimento simétrico entre os eleitores de A e B. A diferença entre as duas evidências fica registrada como incerteza não resolvida.

---

## 5. Resíduos e erros comuns

**Resíduos** (nível comum, sem house effects nem σ_extra):
- As 22 pesquisas têm |r_j| < 1,1. Σ r² = 3,6 para 21 graus de liberdade (razão 0,17), ou seja, **sobredispersão nenhuma**. A dispersão está bem abaixo da esperada pelas margens.
- **As quatro rodadas finais têm resíduo negativo semelhante** (−0,20 a −0,26 p.p.). Elas estão abaixo da tendência latente (50,8 %), porque o passeio aleatório com σ_drift = 0,01 suaviza a série junto com o histórico.

**Previsão fora da amostra:** o modelo com dados até 22/10 previu as quatro rodadas finais com z entre −0,28 e −0,34. Isso é coerente com a tendência de queda de B, sem surpresa.

**Deriva diária (σ_drift):** a verossimilhança marginal tem máximo em 0,01, o valor do caso-base, o que confirma essa hipótese. Com só as pesquisas:

| σ_drift | θ_B (25/10) | P(θ_A > 0,5) só pesquisas |
|---:|---:|---:|
| 0,005 | 51,01 % | 0,8 % |
| **0,01** | **50,81 %** | **7,8 %** |
| 0,02 | 50,65 % | 21 % |

**Erro comum a todos os institutos** (sinal não imposto; modelo completo):

| Viés comum em θ_B | E[θ_A] | P(θ_A > 0,5) |
|---|---:|---:|
| −1,0 p.p. | 49,80 % | 34 % |
| −0,5 p.p. | 49,44 % | 12 % |
| 0 | 49,07 % | 2,9 % |
| +0,5 p.p. | 48,71 % | 0,4 % |
| +1,0 p.p. | 48,34 % | < 0,1 % |
| Incerto, dp 0,5 p.p. | 49,02 % | 4,8 % |
| Incerto, dp 1,0 p.p. | 48,93 % | 7,1 % |

**Leitura direta das rodadas finais** (sem o histórico e sem o bloco estrutural): θ_A = 49,47 %. Só com erro amostral, P = 17 %. Somando 0,5 a 0,75 p.p. de erro comum, P fica entre 24 % e 29 %. É uma cota superior: trata as quatro pesquisas como independentes e ignora a tendência e as transferências.

**Resumo das probabilidades:**
- Caso-base (modelo completo): **2,9 %**.
- Com deriva alta e viés de recordação de 1 p.p.: até cerca de 12 %.
- Só pesquisas: 7,8 %.
- Rodadas finais isoladas: 17–29 %.
- Com κ entre 0,25 e 0,5, sobe para 8–17 %. Com o LVM de nx, cai para menos de 1 %.

**Diagnóstico de amostragem por importância:** a variante "sem temperar a dependência" teve ESS de só 205. Esse resultado é pouco confiável e serve apenas como indicação.

---

## 6. Variáveis ainda não observadas adequadamente

| Variável | Situação |
|---|---|
| **Comparecimento efetivo por grupo** | Há duas evidências declaradas em direções opostas (convictos de nx-r2 e LVM de nx-r3), ambas sem calibração. É a maior fonte de incerteza não resolvida no último dia. |
| **Troca direta entre finalistas (X_AB, X_BA)** | Só duas matrizes, ambas do instituto pd. Não é possível separar house effect de mudança real. |
| **Independência entre pesquisas** | A dispersão das rodadas finais é anormalmente baixa. O erro comum não é identificável e foi tratado só por sensibilidade. |
| **Efeito do modo de coleta (presencial × telefone)** | Não há parâmetro próprio no modelo. |
| **Linhas F e G:L; separação entre BN e abstenção** | O prior domina. |
| **Destino dos indecisos (1–2 % nas rodadas finais)** | Não observado; segue a regra de indecisos do modelo. |
| **Viés de recordação do voto do 1º turno** | Não identificável. |
| **Efeito de fu, mi, rt e ip** | Uma rodada cada. |

## 7. Registro de hipóteses

- **Alteradas:**
  - horizonte de 1 dia;
  - quatro rodadas novas no histórico de seus institutos;
  - LVM incluído como cenário ω, sem entrar no caso-base;
  - nova seção de erro comum.
- **Mantidas:**
  - matrizes de transferência com suas datas;
  - peso λ = 0,5 da matriz pd;
  - desconto temporal σ_q = 0,5 p.p./√dia;
  - tempera de dependência entre topline e cruzamentos do mesmo levantamento;
  - viés de recordação σ_r = 0,5 p.p.;
  - indecisos pelo método III;
  - churn simétrico (5 % ± 1,5 %);
  - σ_drift = 0,01, σ_house = 0,02, σ_extra = 0,02;
  - regra max(margem publicada, AAS).
