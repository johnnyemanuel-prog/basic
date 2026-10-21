# Atualização de 21/10 — recalibração do modelo (v2)

Este relatório incorpora os dados divulgados até 21/10 ao modelo existente.

- **Histórico preservado:** `modelo.py`, `resultados.md` e `RELATORIO.md` continuam como estavam (versão v1).
- **Versão nova:** a v2 está em `modelo_v2.py`. As tabelas completas estão em `resultados_v2.md`, e os números principais em `resultados_v2.json` (semente 20261021, 1.000.000 de sorteios).
- **Rótulos:** candidatos A–L e institutos em minúsculas, como antes. Cada rodada nova tem identificador próprio (`qu-r2`, `fu-r1`, `pv-r2`, `mi-r1`, `rt-r1`, `at-r2`, `nx-r2`, `pd-r2`).
- **Datas:** eleição em 25/10 e último dia de campo em 20/10, o que dá um horizonte de 5 dias.

Todas as probabilidades são **condicionais às hipóteses**. Não são previsões.

---

## 1. Auditoria de consistência dos dados novos

### 1.1 Pesquisas nacionais

| id | Campo | Σ totais | B válido calculado | B válido publicado | MOE / MOE de amostragem aleatória simples (AAS) | Observação |
|---|---|---|---:|---:|---|---|
| qu-r2 | 17–20/10 † | 100 % | 50,56 % | ND (49,44/50,56 calculado) | 2,0 / 2,11 | o mesmo levantamento tem cruzamentos de transferência |
| fu-r1 | 18–20/10 † | ND | — | 51,1 % | 2,2 / 2,19 | só válidos; totais ND **não imputados** |
| pv-r2 | 18–20/10 | **99 %** | 51,02 % | ND | 2,4 / 1,39 (DEFF ≈ 3,0) | soma de 99 % preservada; tem cruzamentos |
| mi-r1 | 17–19/10 † | 100 % | 51,06 % | 51,1 % | 2,5 / 2,53 | — |
| rt-r1 | 17–19/10 † | 100 % | 51,61 % | 52 % | 2,0 / 2,19 | válido publicado arredondado para inteiro |
| at-r2 | 13–18/10 † | 100 % | 51,13 % | 51,1 % | **1,0 / 1,39** ⚠ | MOE abaixo da AAS (como na r1); BN+NS = 2,6 agregados |
| nx-r2 | 16–18/10 † | 100 % | 50,32 % | 50,3 % | 2,0 / 2,19 | — |
| pd-r2 | 16–18/10 † | **101 %** | 51,58 % | 52 % | 1,8 / 1,79 | soma de 101 % preservada |

† **A data de início do campo não foi informada.** Supus que cada rodada durou o mesmo que a rodada anterior do instituto (qu 4 dias, at 6, nx e pd 3), ou 3 dias para os institutos novos (fu, mi, rt). Usar só o último dia não muda o resultado: θ_B = 51,19 % nos dois casos.

**Como cada levantamento entra no modelo:**
- **Uma única likelihood por levantamento:** a fração B/(A+B), em logit. Se há totais, ela é calculada deles. Os válidos publicados servem só de checagem e **não** entram como segunda observação.
- **Diferença entre calculado e publicado** fica sempre ≤ 0,42 p.p. (rt e pd), o que é compatível com arredondamento para inteiro.
- **fu:** sem totais, a variância usa a mediana de (A+B) das rodadas novas (94,0 %) como denominador. É uma suposição explícita.
- **at:** mantive a regra do v1, usando a margem da AAS (±1,39) em vez da publicada (±1,0).

### 1.2 Transferências

| Rodada | Coorte | A / B / BN-não vota / NS | Σ | Margem do subgrupo | n efetivo implícito | DEFF implícito |
|---|---|---|---|---:|---:|---:|
| qu-r1 (13/10) | C | 34 / 30 / 30 / 6 | 100 | ±17 | 33 | 1,4 |
| qu-r2 (20/10) | C | 48 / 33 / 16 / 3 | 100 | ±17 | 33 | 1,4 |
| qu-r1 | D | 14 / 40 / 43 / 3 | 100 | ±20 | 24 | 1,5 |
| qu-r2 | D | 25 / 51 / 24 / 0 | 100 | ±20 | 24 | 1,5 |
| qu-r1 | E | 23 / 42 / 33 / 2 | 100 | ±24 | 17 | 2,1 |
| qu-r2 | E | 21 / 57 / 22 / 0 | 100 | ±24 | 17 | 2,1 |
| qu-r1 | X | 43 / 38 / 17 / 2 | 100 | ±6 | 267 | 2,0 |
| qu-r2 | X | 40 / 36 / 21 / 3 | 100 | ±6 | 267 | 2,0 |
| pv-r2 | C | 52 / 43 / resto 5 | 100 | — | 36 (DEFF 3) | — |
| pv-r2 | D | 39 / 42 / resto 19 | 100 | — | 28 | — |
| pv-r2 | E | 44 / 44 / resto 12 | 100 | — | 27 | — |

- **Todas as linhas somam 100.**
- **Rodada qu-r1 completa:** qu publicou agora a decomposição em 4 categorias da rodada de 13/10. Ela substitui a versão com "restante" não decomposto usada no v1, e o valor publicado é usado sem imputação.
- **"BN/não vota" (qu):** foi mapeado na categoria BN do modelo. A separação entre voto branco/nulo e abstenção **não é identificável** nesses dados.
- **"Restante" (pv):** entra como categoria agregada {BN, NS, não vota}, sem decomposição.
- **n efetivo de qu:** vem da margem de cada subgrupo, n = 0,25·(1,96/MOE)². Os DEFF implícitos (1,4–2,1) são coerentes com o DEFF 2 que o v1 supunha.
- **Rodadas qu-r1 e qu-r2 são duas amostras transversais.** As diferenças entre elas (por exemplo, C→A de 34 para 48) **não** são tratadas como migração individual. Cada rodada entra como observação da mesma margem de transição, com sua data.

### 1.3 Variáveis descritivas: fora da likelihood

As medidas abaixo não entram na likelihood, como pedido:
- **Comparecimento declarado (nx):** certeza de comparecer 85,9 %, provável 7,0 %, provável não ou não 5,4 %. Sobram 1,7 % não discriminados. A soma do declarado fica muito acima do comparecimento real do 1º turno (78,9 %), por isso não é usado como probabilidade.
- **Rejeição (qu e mi):** não entra.
- **Estabilidade (mi 83,7 % com voto decidido; pv 79 % "nada me faria mudar"):** são perguntas diferentes e não foram comparadas entre si.
- **Espontânea de qu (40/40/14):** não é comparável com a estimulada (44/45).

O diferencial de comparecimento declarado entre os convictos de A e de B (95,0 % contra 91,6 %) entra **só** como sensibilidade, na seção 3.

---

## 2. Parâmetros de retenção e transferência atualizados

**Mudanças de método nesta versão:**
- **Data de cada observação de transferência.** Cada observação informa o valor no dia da eleição com uma variância extra de σ_q²·Δt, onde Δt é a distância até 25/10 e σ_q = 0,5 p.p. por √dia. Assim, observações mais antigas pesam menos, sem que as mais novas as substituam silenciosamente.
- **Dependência intra-levantamento.** Quando o mesmo levantamento fornece cruzamentos de transferência e resultado geral, cada parte entra com potência 0,5 (verossimilhança temperada). Isso vale para pd (matriz e rodada 10–12), df-r1, qu-r1, qu-r2 e pv-r2.
- **Matriz pd:** peso λ = 0,5, como no v1.

**Parâmetros estimados** (média [IC 90 %], em %, para 25/10):

| Parâmetro | Só pd (com datas) | pd + df + qu + pv | **Completo (+ pesquisas)** | v1 (referência aprox.) ¹ |
|---|---|---|---|---|
| R_A = A₁→A | 91,3 [87,7; 94,4] | 91,3 | **91,6 [88,4; 94,4]** | ≈ 91,9 [90,1; 93,6] |
| X_AB = A₁→B | 5,2 [2,9; 8,1] | 5,2 | **5,0 [2,9; 7,4]** | ≈ 5,1 |
| R_B = B₁→B | 94,2 [91,3; 96,7] | 94,2 | **94,2 [91,6; 96,4]** | ≈ 94,6 |
| X_BA = B₁→A | 5,3 [2,9; 8,1] | 5,3 | **5,3 [3,2; 7,8]** | ≈ 5,2 |
| C→A / C→B | 26,8 / 52,5 | 40,1 / 40,2 | **40,3 [31,0; 49,9] / 40,1 [30,8; 49,6]** | 32,9 / 43,6 |
| D→A / D→B | 24,8 / 44,4 | 26,3 / 44,8 | **26,4 [17,1; 36,5] / 44,7 [33,9; 55,8]** | 23,1 / 43,9 |
| E→A / E→B | 20,0 / 52,9 | 28,1 / 49,4 | **28,3 [18,0; 39,4] / 49,3 [37,4; 61,3]** | 23,3 / 49,8 |
| F→A / F→B | 18,5 / 45,5 | = | **18,1 [0,3; 56] / 44,9 [9; 85]** | 17,6 / 53,3 |
| G:L→A / G:L→B | 30,3 / 22,7 | = | **30,5 [2; 74] / 22,5 [1; 64]** | 33,0 / 21,5 |
| C:F agregado →A / →B | 24,0 / 50,0 | 31,8 / 44,4 | **31,9 [26,8; 37,2] / 44,3 [38,7; 49,9]** | 26,7 / 45,8 |
| X (BN₁+ABS₁) → A / B / BN-não vota | 31,5 / 38,8 / 23,0 | 37,3 / 37,6 / 20,8 | **37,4 [33,5; 41,4] / 37,5 [33,6; 41,5] / 20,8** | ≈ 37 / 38 / 18 |
| **θ_A (válidos)** | 47,6 [45,4; 49,8] | 48,5 [46,4; 50,6] | **48,7 [47,6; 49,8]** | 48,4 [47,2; 49,7] |

As linhas q_g representam intenção declarada normalizada, antes da resolução de indecisos e do comparecimento.

¹ A coluna do v1 é aproximada: as linhas dos eliminados vêm do modelo completo do v1 com λ = 1, e θ_A vem da configuração recomendada (λ = 0,5, horizonte de 11 dias).

**Leitura:**
- **Retenção e troca direta entre finalistas:** os centros são os mesmos do v1, mas os intervalos ficaram mais largos. A única fonte continua sendo a matriz pd de cerca de 11/10, agora com desconto temporal de 14 dias.
- **A assimetria de cerca de 4 p.p.** do "ponto mais provável" de simulações anteriores (7,0 % contra 3,3 %) é resultado condicional do modelo. **Não foi usada como dado nem como prior.**
- **Eliminados:** as novas observações deslocam as estimativas na direção de A, principalmente em C (de 33/44 para 40/40) e E, mas os intervalos continuam largos (±10 p.p.).
- **Faltantes e brancos/nulos do 1º turno (X):** a divisão entre os válidos fica em cerca de 50:50.

---

## 3. Sensibilidade às hipóteses de comparecimento

**a) Diferencial declarado → efetivo (κ).** κ é a fração do diferencial declarado por nx (convictos de A 95,0 % contra convictos de B 91,6 %) que se converte em diferença real de comparecimento. O diferencial é aplicado depois da ponderação pelas pesquisas, porque elas medem intenção e não comparecimento. Estender o comportamento dos "convictos" a todo o eleitorado de cada lado já é uma suposição.

| κ | Diferencial efetivo A − B | E[θ_A] | IC 90 % | P(θ_A > 0,5) |
|---:|---:|---:|---|---:|
| **0 (hipótese do v1)** | 0 | **48,72 %** | 47,62 – 49,81 % | **2,7 %** |
| 0,25 | 0,9 p.p. | 48,95 % | 47,85 – 50,04 % | 5,6 % |
| 0,5 | 1,8 p.p. | 49,18 % | 48,07 – 50,27 % | 10,6 % |
| 1 | 3,6 p.p. | 49,63 % | 48,53 – 50,72 % | 28,9 % |

**Essa é a hipótese de maior peso nesta atualização.** Para comparar com a mudança de fontes: incorporar todos os dados novos moveu θ_A em +0,3 p.p.; κ = 0,5 o move em +0,5 p.p. Como os dados não permitem estimar κ, ele continua uma escolha de cenário, e o caso-base mantém κ = 0.

**b) Comparecimento total × divisão dos faltantes adicionais** (κ = 0; em cada célula, E[θ_A] / P(θ_A > 0,5)):

| Comparecimento | Linha ABS posterior (≈ 50:50) | 55:45 | 60:40 | 2:1 |
|---|---|---|---|---|
| −2 p.p. | 48,69 / 2,7 % | 48,58 / 1,9 % | 48,47 / 1,2 % | 48,31 / 0,7 % |
| = 1º turno | 48,72 / 2,7 % | 48,72 / 2,7 % | 48,72 / 2,7 % | 48,72 / 2,7 % |
| +2 p.p. | 48,75 / 2,7 % | 48,86 / 4,0 % | 48,96 / 5,5 % | 49,11 / 8,5 % |
| +5 p.p. | 48,78 / 2,6 % | 49,05 / 6,5 % | 49,31 / 13,6 % | 49,66 / 29,5 % |

As linhas −2, −1, +1 e +3 p.p. estão em `resultados_v2.md`. Como os faltantes posteriores se dividem em cerca de 50:50, mudar o comparecimento total quase não altera θ. O que pesa é o comparecimento **diferencial** entre os eleitores de A e de B.

---

## 4. Diferenças de mensuração entre institutos e evolução temporal

**Rodadas repetidas do mesmo instituto** (diferença bruta, sem atribuição de causa):

| Instituto | Rodadas | θ_B antes → depois | Δ (p.p.) | z |
|---|---|---|---:|---:|
| df | 7/10 → 14/10 | 52,13 → 51,09 | −1,04 | −0,68 |
| qu | 13/10 → 20/10 | 51,11 → 50,56 | −0,55 | −0,33 |
| pd | 12/10 → 18/10 | 51,06 → 51,58 | +0,52 | +0,38 |
| nx | 12/10 → 18/10 | 51,61 → 50,32 | −1,29 | −0,78 |
| at | 8/10 → 18/10 | 52,79 → 51,13 | −1,66 | −1,64 |
| pv | 13/10 → 20/10 | 50,51 → 51,02 | +0,52 | +0,30 |

Nenhuma variação isolada é estatisticamente distinguível de erro amostral (|z| < 1,96). Os sinais são mistos: quatro institutos mostram B em queda e dois em alta.

**Tendência latente.** O modelo combina todas as 16 pesquisas num passeio aleatório com house effects. Nele, θ_B vai de 51,9 % (4/10) para 51,4 % (12/10) e 51,2 % (16 a 20/10). Isso é uma variação de cerca de −0,7 p.p. no período, concentrada até cerca de 14/10, e só aparece na agregação. Leio como deslocamento do nível agregado medido, não como mudança individual demonstrada.

**House effects** (prior N(0; 0,5 p.p.²), sem sinal):
- Todos ficam entre −0,12 p.p. (pv) e +0,16 p.p. (at), com dp ≈ 0,45 p.p.
- Nenhum instituto se distingue dos demais.
- fu, mi, rt e ip têm uma rodada só, então o efeito deles é identificado apenas pelo prior.

**Calibração anterior × atual** (só pesquisas, em 25/10):

| Versão | θ_B | dp | P(θ_B > 0,5) |
|---|---:|---:|---:|
| v1 (8 pesquisas até 14/10; 11 dias de horizonte) | 51,48 % | 1,03 p.p. | 92,6 % |
| v2 (16 pesquisas até 20/10; 5 dias) | 51,19 % | 0,78 p.p. | 93,5 % |

A média se deslocou −0,29 p.p. para B, mas o horizonte menor reduziu a incerteza. As duas mudanças quase se compensam na probabilidade.

---

## 5. Resíduos e verificações preditivas

**Resíduos por pesquisa** (nível comum, sem house effects nem σ_extra): todas as 16 têm |r_j| < 1,1, e o maior é at-r1 com +1,07. Σ r² = 3,4 para cerca de 15 graus de liberdade (razão 0,23; p ≈ 0,999). **Não há sobredispersão**, e o perfil de σ_extra tem máximo em 0. As pesquisas variam **menos** do que as margens publicadas preveem, o que é compatível com margens conservadoras. Mantive σ_extra = 0,02 (≈ 0,5 p.p.) para cobrir erro não amostral.

**Previsão fora da amostra:**
- Usei o modelo ajustado só com as pesquisas até 14/10 para prever as 8 novas.
- O z médio é −0,30 (as novas ficam um pouco mais favoráveis a A que o previsto), e o maior |z| é 0,80 (nx-r2).
- **A calibração anterior previu as novas pesquisas dentro da incerteza.**

**Leave-one-out** (prever cada pesquisa a partir das outras): nenhum |r_j| passa de 1,16. Nenhum instituto foi descartado.

**Verificação preditiva das transferências:** são 42 comparações (observado contra previsto pelo modelo completo). O maior |z| é 1,17 e nenhuma passa de 2. As tensões que o v1 apontava (C→B da pd contra qu; X→A) ficam absorvidas pelo desconto temporal e pelo n efetivo derivado da margem de cada subgrupo.

**Sensibilidade do bloco de pesquisas:** ignorar a dependência intra-levantamento, usar janela de 1 dia ou dobrar σ_house muda θ_B em no máximo 0,04 p.p. A deriva diária é que domina: σ_drift = 0,005 leva o dp a 0,51 p.p., e σ_drift = 0,02 leva a 1,36 p.p.

---

## 6. Parâmetros com identificação ainda insuficiente

Critério: dp no modelo completo dividido pelo dp só com pd maior que 0,85.

| Parâmetro | Razão | Situação |
|---|---:|---|
| **X_AB e X_BA** (troca direta entre finalistas) | 0,85–0,88 | Só a matriz pd de cerca de 11/10 os informa; não há matriz nova. As pesquisas identificam apenas a **combinação** de retenção e troca, não cada fluxo. |
| R_A, R_B | 0,89 | Mesmo motivo. |
| F→A/B, G:L→A/B | ≈ 1,0 | Subamostras de 1 a 3 entrevistas efetivas; o prior domina. |
| Separação BN × não vota | — | qu agrega as duas categorias, e pv não discrimina o "restante". |
| κ (comparecimento declarado → efetivo) | — | Não há calibração possível com estes dados. |
| Comparecimento por coorte do 1º turno (τ_g) | — | Continua só com prior (churn de 5 % ± 1,5 %). |
| Viés de recordação (σ_r) e viés comum a todos os institutos | — | Não identificáveis em uma única eleição. |
| House effects de fu, mi, rt, ip | — | Uma rodada cada. |
| Divisão dos indecisos (NS) | — | Sem dado de destino. |

Parâmetros com identificação **parcial** (razão de 0,6 a 0,85): E→A e as linhas de X.
Parâmetros com identificação **boa** (razão abaixo de 0,6): C, D, C:F agregado e θ_A.

---

## 7. Registro de hipóteses

### Alteradas

| Hipótese | v1 | v2 | Motivo |
|---|---|---|---|
| Horizonte | 11 dias (14→25/10) | 5 dias (20→25/10) | Novas pesquisas |
| Datas das transferências | Todas tratadas como contemporâneas | Cada observação com data; variância extra σ_q²·Δt (σ_q = 0,5 p.p./√dia; sensibilidade 0,25 e 1,0) | Instrução 7 e item 8.10 |
| Dependência intra-levantamento | Topline e cruzamentos independentes | Potência 0,5 em cada parte (pd, df-r1, qu-r1, qu-r2, pv-r2) | Itens 8.4–8.5 |
| n efetivo de qu por subgrupo | 2154 × peso eleitoral / 2 | Derivado da margem de cada subgrupo (33/24/17/267) | Item 8.7 |
| Categorias de qu-r1 | B, A e "restante" | 4 categorias (divulgadas) | Dado novo, sem imputação |
| Modelo de pesquisas | 7 institutos, 8 rodadas | 10 institutos, 16 rodadas; house effect comum entre rodadas | — |
| Comparecimento declarado | Não usado | Sensibilidade κ, sem entrar no caso-base | Item 8.8 |

### Constantes

- Dados do 1º turno.
- Matriz pd e seu peso λ = 0,5, agora reinterpretado também como a partição da dependência entre matriz e topline da pd.
- Viés de recordação σ_r = 0,5 p.p.
- Indecisos pelo método III.
- Churn de 5 % ± 1,5 % e τ_ABS ≈ 18,7 %.
- σ_drift = 0,01, σ_house = 0,02, σ_extra = 0,02.
- Regra max(MOE, AAS) para a margem de cada pesquisa.
- Prior sem sinal para house effects.
- Nenhum erro do 1º turno transferido para o 2º.
- Rejeição, estabilidade e espontânea mantidas fora da likelihood.

---

## 8. Modelo e probabilidades atualizados (25/10)

**Caso-base v2:** E[θ_A] = **48,72 %** [IC 90 % 47,62 – 49,81 %]; **P(θ_A > 0,5) = 2,7 %**. No v1 (configuração recomendada) eram 48,4 % e 1,9 %.

| Variação (resto no caso-base) | E[θ_A] | P(θ_A > 0,5) |
|---|---:|---:|
| σ_drift 0,005 / **0,01** / 0,02 | 48,66 / **48,72** / 48,68 % | 0,2 / **2,7** / 7,7 % |
| σ_r 0 / 0,5 / 1,0 p.p. (σ_drift 0,01) | 48,71 / 48,72 / 48,75 % | 2,4 / 2,7 / 3,7 % |
| σ_drift 0,02 e σ_r 1,0 | 48,71 % | 10,3 % |
| λ_pd 1 / 0,25 | 48,64 / 48,78 % | 1,5 / 4,1 % |
| σ_q 0,0025 / 0,01 | 48,71 / 48,74 % | 2,4 / 3,6 % |
| Sem temperar a dependência | 48,74 % | 3,2 % |
| Sem pv-r2 / só observações de 18/10 em diante + pd | 48,67 / 48,70 % | 2,4 / 2,6 % |
| κ 0,25 / 0,5 / 1 | 48,95 / 49,18 / 49,63 % | 5,6 / 10,6 / 28,9 % |
| Só pesquisas | 48,81 % | 6,5 % |

**Faixa:** sem efeito de comparecimento diferencial, **P(θ_A > 0,5) ≈ 2 a 8 %**. Admitindo κ entre 0,25 e 0,5, a faixa vai a **6 a 11 %**.

**Fronteira de virada recalibrada:** a diferença média entre B e A caiu de 3,76 mi para **3,04 mi** de votos.
- Regra: X_BA necessário = 3,32 % + 0,962 × X_AB. No X_AB atual (5,1 %), seriam precisos cerca de 8,2 %.
- O ponto mais provável sobre a fronteira fica agora a **≈ 1,5 dp**, contra 2,0 dp no v1. Duas causas: a diferença ficou menor, e a incerteza temporal da matriz pd ficou maior.

O gráfico `fronteira_virada.html` ainda mostra a calibração v1.
