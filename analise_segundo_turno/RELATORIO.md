# Segundo turno hipotético A × B: modelo estrutural de transição + agregação bayesiana de pesquisas

> Este relatório usa **apenas** os números fornecidos. A, B, C… e aa, bb, … são rótulos abstratos.
> Todas as probabilidades são **condicionais às hipóteses do modelo**. Não são previsões nem recomendações.
> Todos os números vêm de `modelo.py` (numpy, semente 20261015, 1.000.000 de sorteios).
> Todas as tabelas estão em `resultados.md`, e os números principais em `resultados.json`.

---

## 0. Resultado principal (configuração recomendada)

**Hipóteses da configuração recomendada:**
- Eleição em 25/out: 10 dias após 15/out e 11 dias após a última pesquisa (H = 11).
- **Peso intermediário da matriz pd:** λ = 0,5, ou seja, metade do tamanho efetivo das subamostras da pd.
- **Viés de recordação baixo:** σ_r = 0,5 p.p., sem sinal imposto. A justificativa é que o 1º turno foi recente, o que reduz o erro de lembrança do voto.
- Os demais parâmetros seguem o caso-base: Modelo 2, indecisos III, σ_house = 0,02 e σ_extra = 0,02.

| Deriva da intenção até a eleição | E[θ_A] | IC 90 % | P(θ_A > 0,5) |
|---|---:|---|---:|
| σ_drift = 0,01 (base) | 48,4 % | 47,2 – 49,7 % | **1,9 %** |
| σ_drift = 0,02 (alta) | 48,4 % | 46,8 – 50,0 % | **5,3 %** |

**Faixa recomendada: P(θ_A > 0,5) ≈ 2 a 5 %, com E[θ_A] ≈ 48,4 %.** Essa probabilidade depende das hipóteses e não é uma previsão. A seção 12 mostra a sensibilidade completa a λ e σ_r: com λ = 1 e σ_r = 0 a faixa vai de 0,4 a 1,2 %; com λ = 0,25 e σ_r = 1 p.p., de 4,7 a 14,1 %. Usando só as pesquisas nacionais (λ = 0), a faixa é de 7 a 25 %.

---

## 1. Conferência dos dados

### 1.1 Somas (valores exatos)

| Bloco | Votos | % dos votos em candidatos | % do comparecimento | % do eleitorado |
|---|---:|---:|---:|---:|
| A | 53.876.617 | 45,162 % | 43,008 % | 33,940 % |
| B | 56.104.268 | 47,029 % | 44,786 % | 35,343 % |
| **Σ candidatos (A:L)** | **119.297.632** | 100 % | 95,230 % | 75,152 % |
| C:L | 9.316.747 | 7,810 % | 7,437 % | 5,869 % |
| C:F | 9.056.092 | 7,591 % | 7,229 % | 5,705 % |
| G:L | 260.655 | 0,218 % | 0,208 % | 0,164 % |
| Brancos + nulos (2.300.781 + 3.674.149) | 5.974.930 | — | 4,770 % | 3,764 % |
| **Comparecimento** | **125.272.562** | — | 100 % | 78,916 % |
| Abstenção (≈) | 33.470.000 | — | — | 21,084 % |
| **Eleitorado implícito** | **158.742.562** | — | — | 100 % |

- A soma de A até L confere: 119.297.632. A ordem C ≥ D ≥ … ≥ L confere.
- No 1º turno, B − A = 2.227.651 votos (1,867 p.p. dos votos em candidatos). Restrito a A+B, θ_A = 48,987 %.
- **Aproximação:** a abstenção foi informada como "≈ 33,47 milhões" (incerteza de ±5 mil por arredondamento). Por isso o eleitorado é derivado, não observado.

### 1.2 Inconsistências encontradas (mostradas, não corrigidas em silêncio)

| # | Inconsistência | Tratamento |
|---|---|---|
| 1 | Linhas da matriz pd que não somam 100: B = 99, D = 101, E = 99, BN = 101 | Normalizei cada linha: m[g,k] = x/Σx. O resíduo não foi usado como informação. |
| 2 | Totais publicados somando 101 % (pd, ip) | Para a pesquisa, usei B/(A+B) dos totais. A diferença para os válidos publicados é ≤ 0,4 p.p. (nx: 51,61 % calculado contra 52 % publicado). Somei a variância de arredondamento (uniforme ±0,5 p.p. em A e B). |
| 3 | **at: MOE publicada ±1,0 p.p. menor que a de amostragem aleatória simples, ±1,38 p.p. (n = 5.026)**, o que implicaria DEFF = 0,52 | No caso-base usei max(MOE, MOE_AAS). A MOE literal entra como sensibilidade e muda θ_B em +0,03 p.p. |
| 4 | pv: MOE ±2,3 com n = 5.000 implica DEFF ≈ 2,75; pv tem BN = 1 % e NS = 0 %, muito abaixo dos outros institutos | Mantido. O DEFF implícito entra em σ_j. |
| 5 | **Matriz pd × resultado oficial ≠ topline pd**: aplicar a matriz às coortes reais dá θ_A = 47,07 %, mas a topline pd dá 48,94 % | É uma diferença real nos dados. A matriz só reproduz a topline se a coorte A pesar 1,112× o seu tamanho oficial. Possíveis causas: recordação do voto no 1º turno ou ponderação diferente do resultado oficial, ou viés nas linhas. Não corrigi. O conflito é resolvido pela verossimilhança das pesquisas nacionais, e isso explica boa parte da diferença entre o "prior pd" e o posterior. |
| 6 | A linha G:L da pd (A 39, NS 27) vem de uma subamostra de ≈ 5 entrevistas (n_eff ≈ 2,5) | Mantida. O Dirichlet resultante é quase uniforme e o peso eleitoral de G:L é 0,16 %. |

---

## 2. Metodologia

Tudo é calculado ao mesmo tempo:

1. **Bloco de pesquisas:** espaço de estados gaussiano exato (passeio aleatório em logit, com house effects). Como todas as partes são gaussianas, o posterior é analítico (filtro de Kalman / condicionamento gaussiano). Não precisa de MCMC e não tem erro de Monte Carlo.
2. **Bloco estrutural:** Monte Carlo com 1.000.000 de sorteios por conjunto. Sorteio as linhas de transição π_g (Dirichlet), o comparecimento τ_g (Beta) e a divisão dos indecisos. Em seguida calculo V_A, V_B e θ_A.
3. **Observações independentes de transferência (df, qu):** amostragem por importância com proposta conjugada. As observações qu de C, D e E entram **exatamente**, pela propriedade de agregação da Dirichlet: o par (B, A, BN+NS) é Dirichlet, e a divisão BN|NS segue uma Beta independente. As observações agregadas df (C:F) e qu (BN+ABS) entram por pseudo-contagens atenuadas (λ = 0,6) na proposta, depois corrigidas pelo peso exato log w = ℓ_exata − ℓ_pseudo. Tudo em log-likelihood.
4. **Pesquisas nacionais → estrutural:** cada sorteio é ponderado por N(logit θ_B; μ_T, s_T²). Aqui (μ_T, s_T²) é o posterior das 8 pesquisas com house effects e deriva já integrados analiticamente. Isso equivale à verossimilhança conjunta dos institutos marginalizada em h_j e na trajetória.

Escolhi Monte Carlo com amostragem por importância porque não havia biblioteca de NUTS disponível (sem scipy, PyMC ou Stan). ESS efetivo: 1,0 M (só pd), 526 mil (pd + pesquisas), 17,8 mil (pd+df+qu) e **13,7 mil (modelo completo)**.

---

## 3. Equações

**Coortes:** g ∈ {B, A, C, D, E, F, G:L, BN₁, ABS₁}, com tamanhos N_g exatos acima.

**Preferência declarada (pd, normalizada):** q_g = (q_gB, q_gA, q_gBN, q_gNS).

```
q_g ~ Dirichlet(κ_g · m_g + 0,5)
  Modelo 1 (conservador): κ = 0,25/(σ_geral² + σ_add²) − 1,  σ_geral = 1,8/1,96 p.p., σ_add = 5 p.p.  → κ = 95,7
  Modelo 2 (n efetivo):   κ_g = n_eff,g = 3000 · (N_g/Eleitorado) / DEFF,  DEFF ∈ {1,5; 2; 3}
```

Com DEFF = 2, o n_eff de cada coorte é B = 530, A = 509, C = 32,6, D = 25,3, E = 24,6, F = 3,1, G:L = 2,5, BN = 56,5 e ABS = 316. **É uma aproximação**, porque o n real das subamostras não foi informado.

**Indecisos (NS → B, A, BN):**
- I: proporcional aos decididos no agregado, NS·(r_B, 1−r_B) com r_B = Σ N_g q_gB / Σ N_g (q_gA+q_gB).
- II: 50:50.
- III: proporcional a (q_gB, q_gA, q_gBN) da própria coorte.
- IV: Dirichlet(1,1,1) por coorte e por sorteio.

**Comparecimento** (separado da preferência):

```
τ_g = 1 − c_g,   c_g ~ Beta(μ=0,05; dp=0,015), independentes por coorte (g ≠ ABS)
τ_ABS ~ Beta(μ=0,1871; dp=0,03)   (μ escolhido para que E[comparecimento] = 78,916 %, igual ao 1º turno)
π_gA = τ_g p_gA,  π_gB = τ_g p_gB,  π_gBN = τ_g p_gBN,  π_gABS = 1 − τ_g
V_k = Σ_g N_g π_gk,   θ_A = V_A/(V_A+V_B),   θ_B = 1 − θ_A
```

**Pesquisas:**

```
z_t = logit θ_B,t ;  z_3 ~ N(0, 1);  z_t = z_{t−1} + ε_t,  ε_t ~ N(0, σ_drift²)   (t em dias, 3–14/out)
logit y_j ~ N( mean(z_t, t ∈ campo_j) + h_inst(j),  σ_j² + σ_extra² )
h_inst ~ N(0, σ_house²)   (sem sinal; df-1 e df-2 compartilham h_df)
σ_j = [max(MOE_j, MOE_AAS)/1,96]/√(A_j+B_j) ⊕ σ_arredondamento,  convertido para logit por 1/[y(1−y)]
```

**Verossimilhanças de transferência** (n efetivo = n_pesq · participação da coorte no eleitorado / DEFF):

```
df:  n_CF · Σ_k p_obs,k · log( Σ_{g∈C:F} w_g q_gk ),   p_obs = (B .46, A .32, BN .15, NS .07)
qu:  n_g · [b log q_gB + a log q_gA + (1−a−b) log(1−q_gA−q_gB)]  para g = C, D, E
     e a mesma forma para a mistura (BN₁+ABS₁) ponderada por N   (o "restante" não é decomposto)
```

---

## 4–7. Parâmetros estimados, intervalos, transferências e retenção

As colunas abaixo mostram como cada fonte de informação desloca as estimativas. Valores em % como **média [IC 90 %]**. Modelo 2, DEFF = 2. As linhas q são intenção declarada normalizada, antes de indecisos e comparecimento.

| Parâmetro | pd apenas | pd + df | pd + qu | pd + df + qu | pd + pesquisas | **completo** |
|---|---|---|---|---|---|---|
| R_B = P(B₂\|B₁) | 94,7 [93,0; 96,2] | 94,7 | 94,7 | 94,7 [93,0; 96,2] | 94,3 [92,7; 95,8] | **94,6 [93,0; 96,0]** |
| X_BA = P(A₂\|B₁) | 5,1 [3,7; 6,8] | 5,1 | 5,1 | 5,1 [3,6; 6,8] | 5,5 [4,0; 7,0] | **5,2 [3,8; 6,8]** |
| R_A = P(A₂\|A₁) | 91,7 [89,7; 93,6] | 91,8 | 91,7 | 91,7 [89,6; 93,6] | 92,1 [90,3; 93,9] | **91,9 [90,0; 93,7]** |
| X_AB = P(B₂\|A₁) | 5,1 [3,6; 6,8] | 5,1 | 5,1 | 5,1 [3,6; 6,8] | 4,7 [3,4; 6,2] | **4,9 [3,6; 6,4]** |
| T_CB | 54,2 [40,3; 67,8] | 51,1 | 44,5 | 43,9 [34,1; 53,9] | 52,8 | **43,6 [34,0; 53,5]** |
| T_CA | 26,9 [15,4; 39,8] | 30,7 | 29,7 | 32,6 [23,4; 42,3] | 28,2 | **32,9 [23,6; 42,5]** |
| T_DB | 45,9 [30,6; 61,5] | 43,7 | 43,5 | 44,1 | 44,7 | **43,9 [32,5; 55,3]** |
| T_DA | 24,8 [12,5; 39,2] | 28,6 | 20,5 | 22,9 | 25,8 | **23,1 [13,7; 33,6]** |
| T_EB | 55,1 [39,3; 70,5] | 52,7 | 49,9 | 50,0 | 53,9 | **49,8 [38,1; 61,6]** |
| T_EA | 19,6 [8,6; 33,2] | 22,7 | 21,0 | 23,2 | 20,6 | **23,3 [14,0; 34,0]** |
| T_FB | 53,5 [19,5; 85,8] | 52,1 | 53,4 | 53,6 | 52,9 | **53,3 [19,5; 85,6]** |
| T_FA | 15,9 [0,5; 46,5] | 17,1 | 15,9 | 17,5 | 16,4 | **17,6 [0,6; 49,8]** |
| T_G:L,B | 21,7 [1,3; 56,9] | — | — | — | — | **21,5 [1,3; 57,1]** |
| T_G:L,A | 32,7 [5,0; 69,9] | — | — | — | — | **33,0 [5,2; 70,6]** |
| T_G:L,NS | 26,1 [2,5; 62,5] | — | — | — | — | **25,9 [2,3; 62,9]** |
| BN₁ → B / A / BN | 21,9 / 18,1 / 45,8 | = | 23,2 / 22,4 / 41,5 | = | 21,1 / 18,9 / 45,8 | **22,8 / 22,8 / 41,6** |
| ABS₁ → B / A / BN | 41,9 / 33,9 / 19,0 | = | 41,1 / 38,7 / 16,0 | = | 41,6 / 34,2 / 19,0 | **41,0 / 38,7 / 16,0** |
| C:F agregado → B | 52,0 [43,6; 60,3] | 49,4 | 46,0 | 46,0 [40,6; 51,5] | 50,7 | **45,8 [40,5; 51,1]** |
| C:F agregado → A | 23,8 [17,0; 31,2] | 27,3 | 24,0 | 26,5 [21,8; 31,4] | 24,9 | **26,7 [22,1; 31,5]** |
| **θ_A (válidos)** | 47,5 [46,1; 49,0] | 47,8 | 48,0 | 48,1 [46,8; 49,5] | 48,2 [47,4; 49,0] | **48,4 [47,6; 49,2]** |

**Retenção e crossover.** R_A e R_B quase não mudam com df e qu, que não informam sobre essas coortes. O que as move é só a verossimilhança das pesquisas nacionais: R_B cai para 94,3–94,6, X_BA sobe para 5,2–5,5, R_A sobe para 91,9–92,1 e X_AB cai para 4,7–4,9. É por esse canal que o modelo absorve a inconsistência nº 5 (topline pd mais equilibrada que a matriz pd).

O crossover líquido ficou em X_BA − X_AB ≈ +0,3 p.p. A retenção bruta é R_A ≈ 92 % contra R_B ≈ 94,6 %. A diferença vai para BN/NS de A (3 % na pd) e não para B.

**Retenção hipotética (bloco 6) contra pd.** O bloco 6 usa R_A = 0,97 e X_AB = 0,02, contra pd R_A = 0,92 [0,90; 0,94] e X_AB = 0,05. **R_A = 0,97 fica fora do IC 90 % da pd.** Para B, o bloco 6 usa R_B = 0,93 e X_BA = 0,02, contra pd R_B = 0,947 [0,93; 0,96] e X_BA = 0,051 [0,037; 0,068]. **X_BA = 0,02 está abaixo do IC 90 %.**

---

## C. Comparação pd × df × qu

Os valores de z usam n efetivo aproximado (DEFF = 2), porque o n real das subamostras é desconhecido.

| Fluxo | pd normalizada | Observação externa | Δ (p.p.) | z |
|---|---:|---:|---:|---:|
| C:F → B | 54,5 | df 46,0 | −8,5 | −1,07 |
| C:F → A | 23,5 | df 32,0 | +8,5 | +1,19 |
| C:F → BN | 17,6 | df 15,0 | −2,6 | −0,44 |
| C → B | 56,0 | qu 30,0 | **−26,0** | **−2,02** |
| C → A | 27,0 | qu 34,0 | +7,0 | +0,56 |
| D → B | 47,5 | qu 40,0 | −7,5 | −0,50 |
| D → A | 24,8 | qu 14,0 | −10,8 | −0,91 |
| E → B | 57,6 | qu 42,0 | −15,6 | −1,01 |
| E → A | 19,2 | qu 23,0 | +3,8 | +0,30 |
| BN₁+ABS₁ → B | 38,9 | qu 38,0 | −0,9 | −0,24 |
| BN₁+ABS₁ → A | 31,5 | qu 43,0 | **+11,5** | **+2,96** |

- **df contra pd:** as duas concordam na ordenação B > A > BN entre os votos de C:F, mas df mostra margem menor (14 p.p. contra 31 p.p.). A diferença é compatível com erro amostral (|z| ≈ 1,1).
- **qu contra pd:** há duas tensões fortes.
  - Em C, B tem 30 % na qu e 56 % na pd (z ≈ −2,0).
  - No bloco BN+ABS, A tem 43 % na qu e 31,5 % na pd (z ≈ +3,0).
  - No modelo combinado, o posterior fica entre as duas fontes: T_CB = 43,6 %, ABS₁→A = 38,7 %.
  - Como qu não decompõe o "restante", **parte da diferença pode vir de categorias diferentes de resposta** (NS, não resposta, "outro"). Isso não é identificável, e não tentei decompor.
- **Hipótese 2/3 : 1/3 para novos comparecentes:** pd dá A = 44,7 % dos válidos entre abstêmios, e qu (BN+ABS) dá 53,1 %. O valor 66,7 % está fora do alcance das duas fontes, por isso foi tratado só como cenário.

---

## 8. Comparecimento

**Ponto de partida.** Com comparecimento igual ao do 1º turno, cerca de 6,26 mi de eleitores do 1º turno se abstêm e cerca de 6,26 mi de abstêmios do 1º turno comparecem (τ_ABS ≈ 18,7 %).

Abaixo, E[θ_A] e P(θ_A > 0,5) para o modelo estrutural (pd+df+qu). A divisão A:B é aplicada aos votos válidos dos novos comparecentes, como cenário. "pd" significa usar a linha ABS₁ estimada.

| Comparecimento | pd | 50:50 | 55:45 | 60:40 | 2:1 | 40:60 | 45:55 |
|---|---|---|---|---|---|---|---|
| = 1º turno | 48,11 / 1,1 % | 48,18 / 1,3 % | 48,40 / 2,7 % | 48,62 / 5,0 % | 48,91 / 9,7 % | 47,74 / 0,3 % | 47,96 / 0,7 % |
| +1 p.p. | 48,12 / 1,0 % | 48,20 / 1,3 % | 48,48 / 3,1 % | 48,75 / 6,5 % | 49,11 / 14,0 % | 47,66 / 0,2 % | 47,93 / 0,6 % |
| +2 p.p. | 48,12 / 1,0 % | 48,22 / 1,3 % | 48,55 / 3,7 % | 48,87 / 8,2 % | 49,30 / 19,3 % | 47,58 / 0,1 % | 47,90 / 0,5 % |
| +3 p.p. | 48,13 / 1,0 % | 48,24 / 1,3 % | 48,62 / 4,2 % | 48,99 / 10,4 % | 49,49 / 25,5 % | 47,49 / 0,1 % | 47,87 / 0,3 % |
| +5 p.p. | 48,13 / 1,1 % | 48,28 / 1,3 % | 48,75 / 5,5 % | 49,22 / 16,0 % | 49,85 / 41,6 % | 47,34 / 0,0 % | 47,81 / 0,2 % |
| −1 p.p. | 48,11 / 1,1 % | 48,16 / 1,3 % | 48,33 / 2,4 % | 48,49 / 3,8 % | 48,72 / 6,7 % | 47,83 / 0,4 % | 48,00 / 0,8 % |
| −2 p.p. | 48,11 / 1,2 % | 48,14 / 1,3 % | 48,25 / 1,9 % | 48,37 / 2,9 % | 48,51 / 4,5 % | 47,92 / 0,6 % | 48,03 / 0,9 % |

Em cada célula: E[θ_A] em % / P(θ_A > 0,5).

**Comportamento estrutural do comparecimento:**
- Mais comparecimento só muda θ quando os novos comparecentes se dividem de forma diferente do eleitorado que já vota. Com a divisão estimada pela pd (≈ 45:55), +1 p.p. de eleitorado (1,59 mi) muda θ_A em −0,03 p.p. Com a linha ABS posterior (≈ 49:51), a mudança é praticamente 0.
- **Comparecimento diferencial pesa muito mais que comparecimento total.** As derivadas são ∂θ_A/∂τ_A = +0,21 e ∂θ_A/∂τ_B = −0,20 (p.p. por p.p.). Uma diferença de 1 p.p. entre o churn das coortes A e B vale cerca de 0,4 p.p. de θ, o mesmo que +5 p.p. de comparecimento total com divisão 55:45.
- Quando as pesquisas nacionais entram na ponderação, todas as células ficam com P(θ_A > 0,5) ≤ 1,9 %. Isso acontece porque o modelo trata as pesquisas como já incorporando o comparecimento. Se o comparecimento real diferir do declarado nas pesquisas, essa ponderação deixa de valer. Veja Limitações.

---

## 9. Indecisos (NS ≈ 2,05 % dos comparecentes, ≈ 2,57 mi)

| Método | pd apenas: E[θ_A] / P(θ_A>0,5) | pd+df+qu | completo |
|---|---|---|---|
| I proporcional (agregado) | 47,20 / 0,1 % | 47,77 / 0,3 % | 48,26 / 0,0 % |
| II 50:50 | 47,28 / 0,1 % | 47,82 / 0,3 % | 48,27 / 0,0 % |
| III por coorte | 47,55 / 0,2 % | 48,13 / 1,1 % | 48,38 / 0,0 % |
| IV Dirichlet(1,1,1) | 47,26 / 0,1 % | 47,80 / 0,4 % | 48,28 / 0,0 % |

A amplitude entre os métodos é de cerca de 0,35 p.p. em E[θ_A]. Com ponto central fixo, os métodos vão de 46,7 % a 47,5 %. O método III dá o maior θ_A porque A tem mais NS dentro da própria coorte (2 %) que B (0 %). No IV, a variância dos indecisos responde por cerca de 7 % da variância estrutural.

---

## 10. Resíduos por instituto (posterior predictive checks)

Valores previstos pelo nível comum (σ_house = σ_extra = 0, σ_drift = 0,01) e por leave-one-out (LOO) no caso-base.

| Pesquisa | θ_B observado | Previsto | Resíduo (p.p.) | σ_j (p.p.) | r_j | r_j LOO |
|---|---:|---:|---:|---:|---:|---:|
| df-1 (6–7/out) | 52,13 | 52,02 | +0,11 | 1,07 | +0,10 | +0,25 |
| df-2 (13–14/out) | 51,09 | 51,46 | −0,37 | 1,09 | −0,34 | −0,37 |
| qu | 51,11 | 51,55 | −0,44 | 1,16 | −0,38 | −0,35 |
| pd | 51,06 | 51,57 | −0,51 | 0,97 | −0,53 | −0,46 |
| nx | 51,61 | 51,57 | +0,04 | 1,18 | +0,03 | +0,03 |
| at | 52,79 | 52,05 | +0,74 | 0,72 | +1,03 | +1,03 |
| ip | 52,69 | 51,98 | +0,71 | 1,39 | +0,51 | +0,56 |
| pv | 50,51 | 51,55 | −1,04 | 1,20 | −0,87 | −0,80 |

- Σ r_j² = 2,62 com ≈ 7 graus de liberdade (p ≈ 0,92). A razão de dispersão é 0,37, ou seja, **não há sobredispersão**. As pesquisas estão mais próximas entre si do que suas MOEs sugerem, o que é comum quando as MOEs incluem DEFF conservador.
- O máximo do perfil de σ_extra está em 0. Mantive σ_extra = 0,02 logit (≈ 0,5 p.p.) no caso-base para representar o erro não amostral, que a MOE não cobre.
- Nenhuma pesquisa tem |r_j| > 1,1, então não há incompatibilidade estatística. Os extremos são at (+1,0, campo mais antigo, 3–8/out) e pv (−0,9). Retirar at desloca o nowcast em −0,18 p.p., e retirar pv em +0,15 p.p. Nenhum instituto foi descartado.
- **House effects posteriores** (prior N(0; 0,02²), sem sinal): todos com |h_j| < 0,5 dp a priori, entre −0,14 p.p. (pv) e +0,22 p.p. (at). Os dados não identificam house effects.
- **df-1 → df-2** (atualização temporal por Kalman, não média): a variação foi de −1,04 p.p., com z = −0,68 (só amostragem). O ganho da 2ª rodada vai de 0,50 (σ_drift = 0) a 0,71 (σ_drift = 0,02). O valor filtrado do df para 13–14/out fica entre 51,61 % e 51,39 %.
- **Tendência latente:** θ_B vai de 51,97 % (3/out) a 51,48 % (14/out) no caso-base. A verossimilhança marginal favorece levemente σ_drift > 0 (máximo na grade com σ_drift = 0,02).

**Nowcast das pesquisas** (14/out; σ_drift = 0,01, σ_house = 0,02, σ_extra = 0,02): **θ_B = 51,48 % ± 0,60 p.p.**, ou θ_A = 48,52 %.

| σ_drift (logit/√dia) | θ_B, H = 0 | dp H=0 / H=7 / H=14 (p.p.) |
|---|---:|---|
| 0,005 | 51,63 % | 0,50 / 0,60 / 0,69 |
| 0,010 | 51,48 % | 0,60 / 0,90 / 1,11 |
| 0,020 | 51,22 % | 0,82 / 1,55 / 2,04 |

A data da eleição não foi informada, então H (dias após 14/out) é um parâmetro livre.

---

## D. O que separa pesquisas "52:48", "51:49" e "50:50"

Selecionei os sorteios estruturais (pd+df+qu) com θ_B em cada faixa e comparei a média dos parâmetros nessa faixa com a média geral, em desvios-padrão.

| Parâmetro | Média geral | θ_B ≈ 50 | θ_B ≈ 51 | θ_B ≈ 52 |
|---|---:|---|---|---|
| R_B | 94,67 | 93,54 (**−1,18 dp**) | 94,21 (−0,48) | 94,77 (+0,10) |
| X_BA | 5,14 | 6,27 (**+1,19 dp**) | 5,59 (+0,48) | 5,04 (−0,10) |
| X_AB | 5,07 | 4,18 (**−0,92 dp**) | 4,59 (−0,50) | 5,11 (+0,04) |
| R_A | 91,75 | 92,74 (+0,80) | 92,27 (+0,42) | 91,71 (−0,03) |
| τ_B | 95,01 | 93,66 (**−0,90**) | 94,48 (−0,36) | 95,14 (+0,09) |
| τ_A | 94,98 | 95,82 (+0,55) | 95,50 (+0,35) | 94,99 (0,00) |
| BN₁ → A | 22,44 | 25,40 (+0,52) | 23,74 (+0,23) | 22,17 (−0,05) |
| C:F → A | 26,52 | 27,73 (+0,41) | 27,15 (+0,22) | 26,44 (−0,03) |
| ABS₁ → A | 38,63 | 39,07 (+0,20) | 38,76 (+0,06) | 38,60 (−0,01) |

A regressão linear de θ_B sobre os parâmetros tem R² = 0,986. Ela atribui a variância de θ_B assim:
- crossover: X_AB 16,8 % e X_BA 13,8 %;
- comparecimento diferencial: τ_A 14,5 % e τ_B 13,5 %;
- BN₁: cerca de 7 %;
- C:F: cerca de 4 %;
- R_A e R_B "líquidos" de crossover: cerca de 4 %;
- abstêmios: cerca de 1 %.

**Interpretação matemática:**
- Um cenário de 52:48 é o centro do modelo estrutural.
- Para chegar a 51:49, basta deslocar cerca de 0,5 dp ao mesmo tempo no crossover e no comparecimento diferencial.
- Para chegar a 50:50, é preciso cerca de 1 dp nesses mesmos dois canais: X_BA ≈ 6,3 %, X_AB ≈ 4,2 % e τ_B − τ_A ≈ −2 p.p.
- Transferências de C:F e preferência dos abstêmios contribuem pouco, porque as coortes são pequenas (C:F) ou porque os novos comparecentes se dividem de forma parecida com o eleitorado (ABS).

---

## E. Decomposição da variância

**Bloco estrutural.** Cada fonte varia sozinha e as demais ficam na média a priori. A soma das partes é 1,02 × o total, ou seja, as interações são pequenas.

| Fonte | dp de θ (p.p.) | Parcela |
|---|---:|---:|
| Retenção A (linha A, inclui X_AB) | 0,437 | 23,8 % |
| Retenção B (linha B, inclui X_BA) | 0,429 | 23,0 % |
| Comparecimento τ_g | 0,439 | 24,1 % |
| Eliminados C:L | 0,323 | 13,0 % |
| Indecisos (IV) | 0,244 | 7,4 % |
| BN do 1º turno | 0,227 | 6,4 % |
| Abstêmios do 1º turno (preferência) | 0,135 | 2,3 % |
| **Total estrutural** | **0,888** | |

**Bloco de pesquisas** (H = 7 dias; as partes são calculadas por diferença, e a soma é 1,00 × o total):

| Fonte | dp de θ (p.p.) | Parcela |
|---|---:|---:|
| Deriva temporal (inclui os 7 dias de horizonte) | 0,768 | 73,5 % |
| Amostragem (MOE) | 0,368 | 16,9 % |
| House effects | 0,204 | 5,2 % |
| σ_extra | 0,188 | 4,4 % |
| **Total pesquisas** | **0,895** | |

Na combinação gaussiana aproximada, dp_post = 0,63 p.p., com peso de informação de 50,4 % para o bloco estrutural e 49,6 % para as pesquisas.

---

## F/G. Sensibilidade univariada e elasticidades

As derivadas são analíticas: ∂θ_A/∂p = N_g τ_g V_B / S² para um parâmetro que soma votos a A, e −N_g τ_g V_A / S² para um que soma a B, com S = V_A + V_B. "Parcial" significa que a massa vem de fora dos votos válidos. "Troca" significa que a massa vem do adversário (= N_g τ_g / S). As unidades são p.p. de θ_A por p.p. do parâmetro. Base: média posterior completa (θ_A = 48,38 %, V_A = 57,57 mi, V_B = 61,46 mi). ∂θ_B = −∂θ_A.

| Parâmetro | Valor | ∂θ_A parcial | ∂θ_A troca | Elasticidade (θ do favorecido) |
|---|---:|---:|---:|---:|
| R_A | 93,9 % | +0,222 | +0,431 | 0,43 |
| X_AB | 5,0 % | −0,208 | −0,431 | 0,02 |
| R_B | 94,6 % | −0,216 | −0,447 | 0,40 |
| X_BA | 5,3 % | +0,231 | +0,447 | 0,03 |
| T_CA / T_CB | 36,4 / 48,4 % | +0,014 / −0,013 | ±0,028 | 0,011 / 0,013 |
| T_DA / T_DB | 24,0 / 45,2 % | +0,011 / −0,010 | ±0,021 | 0,006 / 0,009 |
| T_EA / T_EB | 25,6 / 54,4 % | +0,011 / −0,010 | ±0,021 | 0,006 / 0,011 |
| T_FA / T_FB | 20,0 / 60,9 % | ±0,001 | ±0,003 | < 0,002 |
| BN₁→A / B | 26,2 / 26,3 % | +0,025 / −0,023 | ±0,048 | 0,013 / 0,012 |
| ABS₁→A / B | 40,4 / 42,9 % | +0,027 / −0,026 | ±0,053 | 0,023 / 0,021 |
| τ_A | — | +0,208 | — | — |
| τ_B | — | −0,203 | — | — |
| τ C:F | — | −0,007 | — | — |
| +1 p.p. do eleitorado vindo de ABS₁ | — | +0,002 | — | — |

**Tornado** (cada parâmetro no seu IC 90 % a priori, demais fixos; amplitude em p.p. de θ_A):

| Parâmetro | Amplitude (p.p.) |
|---|---:|
| churn A | 1,03 |
| churn B | 1,00 |
| R_A | 0,91 |
| X_BA | 0,72 |
| R_B | 0,69 |
| X_AB | 0,66 |
| BN₁→A ou B | ≈ 0,41 |
| T_CA ou T_CB | ≈ 0,36 |
| T_D | ≈ 0,30 |
| T_E | ≈ 0,29 |
| ABS₁ | ≈ 0,24 |

**Grade de retenção** (R_A × R_B; demais parâmetros sorteados de pd+df+qu; se R + X > 1, o crossover é truncado em 1 − R). Em cada célula, E[θ_A] / P(θ_A > 0,5):

| | R_A = 0,88 | 0,92 | 0,96 | 0,98 |
|---|---|---|---|---|
| R_B = 0,89 | 48,4 / 3,0 % | 48,8 / 8,0 % | 49,6 / 30,6 % | 50,4 / 71,7 % |
| R_B = 0,93 | 48,0 / 0,3 % | 48,4 / 1,0 % | 49,1 / 7,9 % | 49,9 / 45,9 % |
| R_B = 0,95 | 47,6 / 0,0 % | 48,0 / 0,1 % | 48,7 / 1,3 % | 49,6 / 21,7 % |
| R_B = 0,97 | 46,8 / 0,0 % | 47,2 / 0,0 % | 47,9 / 0,0 % | 48,8 / 1,6 % |

O salto entre R_A = 0,96 e 0,98 vem em parte do truncamento de X_AB.

**Cenário hipotético do bloco 6** (ponto central, comparecimento igual ao 1º turno):

| Cenário | θ_A | z contra o nowcast das pesquisas |
|---|---:|---:|
| pd | 47,47 % | +1,73 |
| Retenções do bloco 6, ABS = pd | 48,53 % | −0,03 |
| Retenções pd, novos comparecentes 2:1 | 48,59 % | −0,12 |
| Retenções do bloco 6 + novos 2:1 | 49,66 % | −1,90 |
| Retenções do bloco 6 + novos à taxa qu (43:38) | 48,89 % | −0,62 |

O cenário combinado (bloco 6 + 2:1) só é compatível com as pesquisas nacionais em cerca de 1,9 dp, e usa dois parâmetros fora do IC 90 % das observações (R_A = 0,97 e X_BA = 0,02).

**Modelo 1 contra Modelo 2:**
- O Modelo 1 (conservador, κ = 95,7 para todas as coortes) dá dp de θ_A de 1,58 p.p. a priori, contra 0,86 p.p. no Modelo 2 com DEFF = 2. P(θ_A > 0,5) vai a 5,5 % (só pd) e 8,6 % (pd+df+qu).
- Com as pesquisas, todos os modelos convergem para E[θ_A] entre 48,35 % e 48,44 % e dp ≈ 0,5 p.p.
- O ESS nas sub-rodadas de 200 mil sorteios fica entre cerca de 290 e 7 mil, então essas linhas são indicativas.

**House effects e viés comum** (sinal não imposto):
- Aumentar σ_house de 0 para 0,08 logit (≈ 2 p.p.) leva o dp do nowcast de 0,57 para 0,96 p.p. A média quase não muda.
- Um viés **comum** a todos os institutos não é identificável. Simulei ±1 p.p. em θ_B (δ = ∓0,04 logit) no modelo completo:

| σ_drift | H (dias) | δ = −1 p.p. | δ = 0 | δ = +1 p.p. |
|---|---:|---|---|---|
| 0,01 | 0 | 49,03 / 2,3 % | 48,37 / 0,04 % | 47,73 / 0,00 % |
| 0,01 | 14 | 48,61 / 1,8 % | 48,25 / 0,4 % | 47,91 / 0,1 % |
| 0,02 | 14 | 48,34 / 1,5 % | 48,21 / 0,9 % | 48,07 / 0,6 % |

Em cada célula: E[θ_A] em % / P(θ_A > 0,5).

---

## H. Break-even (equações condicionais, NÃO previsões)

Em cada caso, um parâmetro varia e todo o resto fica fixo na base.

**Base A: média posterior completa** (θ_A = 48,38 %, V_B − V_A = 3,85 mi).

| θ_A alvo | R_A (X_AB = 5,0 % fixo; máx. 95,0 %) | R_A com X_AB = 0 | R_B (X_BA = 5,3 % fixo) | A entre válidos de C:F | X_BA (tirado de R_B) |
|---|---|---|---|---|---|
| 48 % | 92,2 % | 87,6 % | (já superado) | 30,2 % | 4,4 % |
| 49 % | inviável | 91,9 % | 91,8 % | 47,8 % | 6,7 % |
| 50 % | inviável | 96,4 % | 87,4 % | 65,4 % | 8,9 % |
| 51 % | inviável | inviável | 83,2 % | 83,0 % | 11,1 % |
| 52 % | inviável | inviável | 79,1 % | inviável | 13,4 % |

Valores da base: R_A = 93,9 %, R_B = 94,6 %, A entre válidos de C:F = 36,9 %, X_BA = 5,3 %.

**Base B: ponto central pd** (θ_A = 47,47 %, V_B − V_A = 6,00 mi). Para θ_A = 50 %:
- R_A fica inviável mesmo com X_AB = 0;
- R_B = 83,7 %;
- A entre válidos de C:F = 72,7 %;
- X_BA = 10,7 %.

**Transferências C:F** (base posterior): para zerar a diferença, 1,93 mi de votos precisam passar de B para A, e o estoque de votos B em C:F é 4,27 mi. Isso exige **45 % do voto B de C:F** migrando de forma uniforme. Nenhuma coorte isolada basta: C sozinha precisaria de 122 %, D de 168 % e E de 143%.

**Novos comparecentes** necessários para zerar V_B − V_A, com o resto fixo: N_válidos = (V_B − V_A)/(a − b).

| Divisão A:B dos novos | Base posterior: novos comparecentes | p.p. do eleitorado | % dos abstêmios do 1º turno | Base pd: novos comparecentes |
|---|---:|---:|---:|---:|
| 50:50 | não fecha | — | — | não fecha |
| 55:45 | 46,2 mi | 29,1 | 138 % (inviável) | 75,0 mi |
| 60:40 | 23,1 mi | 14,6 | 69 % | 37,5 mi |
| 2:1 | 13,9 mi | 8,7 | 41 % | 22,5 mi |
| 45:55, 40:60, 1:2 | ampliam a diferença | — | — | — |

O total de novos comparecentes inclui a fração BN da linha ABS (16,7 % na base posterior, 20 % na base pd).

---

## 11. Sensibilidade: resumo

1. O resultado estrutural varia pouco com DEFF (E[θ_A] entre 47,5 % e 48,2 %) e com o método de indecisos (≈ 0,35 p.p.). A amplitude depende muito do Modelo 1 contra o Modelo 2.
2. Os parâmetros de maior alavancagem por p.p. são retenção, crossover e comparecimento **diferencial** de A e B: cerca de 0,2 p.p. de θ por p.p. no modo parcial e cerca de 0,45 no modo troca. Transferências de C:F valem cerca de 0,01–0,03 por p.p. (cerca de 15 a 20 vezes menos), e preferência de BN e ABS cerca de 0,025–0,05.
3. A **divisão dos novos comparecentes** só tem efeito material quando é muito desequilibrada **e** acompanhada de grande aumento de comparecimento. Com 2:1 e +5 p.p., E[θ_A] sobe ≈ 1,7 p.p. contra a base pd.
4. Do lado das pesquisas, o que domina a incerteza é **deriva temporal e horizonte até a eleição** (73 % da variância do bloco), além do viés comum não identificável.

---

## 12. Peso da matriz pd, viés de recordação e eleição em 10 dias

**Motivação.** A matriz pd fica centrada em θ_A ≈ 47,5 %, mas a topline pd e as demais pesquisas ficam em ≈ 48,5 % (inconsistência nº 5). Com horizonte longo, as pesquisas perdem precisão e a matriz passa a dominar o posterior. Por isso a confiança na matriz virou um parâmetro explícito, em vez de ficar implícita.

**Implementação** (`modelo.py`, seção 15):
- **Peso λ da matriz pd:** α_g = λ · n_eff,g · m_g + 0,5, o que equivale a um DEFF da pd de 2/λ. Os valores de df e qu continuam com DEFF = 2.
  - λ = 1 é o modelo das seções anteriores.
  - λ = 0 equivale a usar só as pesquisas nacionais.
- **Viés de recordação:** θ_A,estr ← θ_A,estr + b, com b ~ N(0, σ_r²) e sem sinal imposto. Esse termo representa um deslocamento da matriz inteira por erro na lembrança ou na ponderação do voto do 1º turno. Como o 1º turno foi recente, a hipótese é de viés baixo (σ_r = 0,5 p.p.), e testei também 0 e 1 p.p.
- **Pesquisas:** H = 11 dias, σ_house = 0,02, σ_extra = 0,02.

Em cada célula: E[θ_A] / P(θ_A > 0,5). A linha em negrito é a configuração recomendada.

| λ | σ_r | Estrutural (sem pesquisas) | Completo, σ_drift = 0,01 | Completo, σ_drift = 0,02 |
|---|---|---|---|---|
| 1 | 0 | 48,1 % / 1,5 % | 48,3 % / 0,4 % | 48,2 % / 1,2 % |
| 1 | 0,5 p.p. | 48,1 % / 3,2 % | 48,3 % / 0,9 % | 48,3 % / 2,5 % |
| 1 | 1,0 p.p. | 48,1 % / 7,7 % | 48,4 % / 2,1 % | 48,4 % / 6,1 % |
| 0,5 | 0 | 48,3 % / 5,4 % | 48,4 % / 1,5 % | 48,4 % / 4,2 % |
| **0,5** | **0,5 p.p.** | **48,3 % / 6,9 %** | **48,4 % / 1,9 %** | **48,4 % / 5,3 %** |
| 0,5 | 1,0 p.p. | 48,3 % / 12,5 % | 48,4 % / 3,2 % | 48,5 % / 9,4 % |
| 0,25 | 0 | 48,5 % / 14,5 % | 48,5 % / 3,9 % | 48,6 % / 10,7 % |
| 0,25 | 0,5 p.p. | 48,5 % / 16,2 % | 48,5 % / 4,0 % | 48,6 % / 11,8 % |
| 0,25 | 1,0 p.p. | 48,5 % / 19,5 % | 48,5 % / 4,7 % | 48,6 % / 14,1 % |
| 0 (só pesquisas) | — | — | 48,5 % / 7,4 % | 48,8 % / 25,4 % |

**Leitura:**
- O centro quase não muda: E[θ_A] fica entre 48,2 % e 48,8 % em todas as configurações. O que muda é a **largura** da distribuição e, com ela, a cauda acima de 50 %.
- Na configuração recomendada, o fator dominante é a **deriva da intenção nos 10 dias** (1,9 % contra 5,3 %). O peso da matriz e o viés de recordação vêm depois.
- O ESS com λ < 1 fica entre 2,2 mil e 4,4 mil sorteios efetivos: adequado para probabilidades de alguns por cento.

---

## 13. Limitações

1. **n das subamostras desconhecido.** Todo n_eff é aproximação (Modelo 2), e o Modelo 1 é uma escolha ad hoc (σ_add = 5 p.p.). As tensões z ≈ −2 (C→B) e z ≈ +3 (BN+ABS→A) dependem dessa aproximação.
2. **Dependência pd–pd.** A matriz pd e a topline pd vêm da mesma pesquisa (ou de rodadas próximas). Ao ponderar pela topline, o modelo trata as duas como informação separada, o que subestima a incerteza. Além disso, as duas são internamente inconsistentes (inconsistência nº 5).
3. **Intenção ≠ comparecimento.** Os priors de τ (churn 5 % ± 1,5 % e τ_ABS ≈ 18,7 %) são suposições sem dados que os apoiem. A ponderação por pesquisas supõe que o θ das pesquisas é o θ entre comparecentes. Se o filtro de comparecimento das pesquisas for diferente da realidade, os cenários de comparecimento da seção 8 deixam de ser comparáveis.
4. **Abstenção na pd.** A linha "absteve-se no 1º turno" mede intenção declarada, não comparecimento. Quem não compareceu tende a estar sub-representado em pesquisas telefônicas.
5. **Linha B sem BN e sem NS na pd (0 %).** O prior de 0,5 pseudo-contagem por célula introduz uma massa pequena (≈ 0,2 %) que não está nos dados.
6. **Viés comum dos institutos** não é identificável com uma única eleição. O prior centrado em 0 subestima esse risco, por isso a tabela de ±1 p.p.
7. **Data da eleição não informada.** O horizonte H é livre. Com σ_drift = 0,02 e H = 14 dias, o dp do nowcast passa de 2 p.p.
8. **Amostragem por importância.** No modelo completo, ESS ≈ 13,7 mil em 1 mi de sorteios: suficiente para médias e IC 90 %, mas probabilidades de cauda abaixo de 0,1 % têm erro relativo alto. As sub-rodadas de sensibilidade (200 mil sorteios) têm ESS entre cerca de 290 e 7 mil.
9. **Decomposição da variância** feita de um fator por vez em torno da média (efeitos de primeira ordem). As interações são pequenas (soma das partes/total = 1,02).
10. **Erro do 1º turno não foi aplicado ao 2º turno**, como pedido. Nenhum h_j recebeu sinal a priori.
11. **λ e σ_r são escolhas de julgamento.** O valor recomendado (λ = 0,5, σ_r = 0,5 p.p.) segue a premissa de que, com o 1º turno recente, o erro de recordação é baixo, mas a matriz pd não deve ter peso total, por causa da inconsistência nº 5. A seção 12 mostra a amplitude de resultados.
12. As probabilidades P(θ_A > 0,5) aqui são **funções das hipóteses**. Mudam materialmente com o Modelo 1, com viés comum de ±1 p.p., com horizonte longo ou com cenários extremos de retenção e comparecimento (grades acima). Não são previsões.

---

### Reprodução

```bash
cd analise_segundo_turno
python3 modelo.py      # ~2–3 min, ~3 GB RAM; gera resultados.md e resultados.json
```
