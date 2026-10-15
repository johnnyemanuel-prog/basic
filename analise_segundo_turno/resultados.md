# Resultados numéricos (gerado por modelo.py)

Semente = 20261015; sorteios Monte Carlo M = 1.000.000

## A. Auditoria aritmética

| Item | Votos | % válidos (cand.) | % comparecimento | % eleitorado |
|---|---|---|---|---|
| A | 53.876.617 | 45.162% | 43.008% | 33.940% |
| B | 56.104.268 | 47.029% | 44.786% | 35.343% |
| C | 3.448.569 | 2.891% | 2.753% | 2.172% |
| D | 2.675.887 | 2.243% | 2.136% | 1.686% |
| E | 2.605.148 | 2.184% | 2.080% | 1.641% |
| F | 326.488 | 0.274% | 0.261% | 0.206% |
| G | 122.911 | 0.103% | 0.098% | 0.077% |
| H | 43.103 | 0.036% | 0.034% | 0.027% |
| I | 40.043 | 0.034% | 0.032% | 0.025% |
| J | 22.693 | 0.019% | 0.018% | 0.014% |
| K | 16.881 | 0.014% | 0.013% | 0.011% |
| L | 15.024 | 0.013% | 0.012% | 0.009% |
| **Σ candidatos** | 119.297.632 | 100% | 95.230% | 75.152% |
| C:L | 9.316.747 | 7.810% | 7.437% | 5.869% |
| C:F | 9.056.092 | 7.591% | 7.229% | 5.705% |
| G:L | 260.655 | 0.218% | 0.208% | 0.164% |
| Brancos | 2.300.781 | — | 1.837% | 1.449% |
| Nulos | 3.674.149 | — | 2.933% | 2.315% |
| **BN** | 5.974.930 | — | 4.770% | 3.764% |
| **Comparecimento** | 125.272.562 | — | 100% | 78.916% |
| Abstenção (aprox.) | 33.470.000 | — | — | 21.084% |
| **Eleitorado implícito** | 158.742.562 | — | — | 100% |

- Diferença B − A no 1º turno: 2.227.651 votos (1.867% dos válidos).
- θ_A no 1º turno restrito a A+B: 48.987%
- Ordem C ≥ D ≥ … ≥ L: OK
- Abstenção é aproximada (±5 mil por arredondamento a 0,01 mi); o eleitorado é derivado, não informado.

### Matriz pd: somas das linhas e normalização

| Coorte | Σ publicado | resíduo | B norm. | A norm. | BN norm. | NS norm. |
|---|---|---|---|---|---|---|
| B | 99% | **-1 p.p.** | 94.95% | 5.05% | 0.00% | 0.00% |
| A | 100% | OK | 5.00% | 92.00% | 1.00% | 2.00% |
| C | 100% | OK | 56.00% | 27.00% | 11.00% | 6.00% |
| D | 101% | **+1 p.p.** | 47.52% | 24.75% | 26.73% | 0.99% |
| E | 99% | **-1 p.p.** | 57.58% | 19.19% | 17.17% | 6.06% |
| F | 100% | OK | 72.00% | 10.00% | 15.00% | 3.00% |
| GL | 100% | OK | 19.00% | 39.00% | 15.00% | 27.00% |
| BN | 101% | **+1 p.p.** | 21.78% | 17.82% | 46.53% | 13.86% |
| ABS | 100% | OK | 42.00% | 34.00% | 19.00% | 5.00% |

### Pesquisas: consistência interna

| Pesquisa | Campo | n | Σ totais | B válido (calc.) | B válido (publ.) | calc−publ (p.p.) | MOE publ. | MOE AAS 50% | DEFF implícito | σ_j válido usado (p.p.) | σ arred. (p.p.) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| df-1 | 6–7/out | 2520 | 100% | 52.13% | 52% | +0.13 | 2.0 | 1.95 | 1.05 | 1.07 | 0.22 |
| df-2 | 13–14/out | 2520 | 100% | 51.09% | 51% | +0.09 | 2.0 | 1.95 | 1.05 | 1.09 | 0.22 |
| qu | 10–13/out | 2154 | 100% | 51.11% | — | — | 2.0 | 2.11 | 0.90 | 1.16 | 0.23 |
| pd | 10–12/out | 3000 | 101% | 51.06% | 51% | +0.06 | 1.8 | 1.79 | 1.01 | 0.97 | 0.22 |
| nx | 10–12/out | 2002 | 100% | 51.61% | 52% | -0.39 | 2.0 | 2.19 | 0.83 | 1.18 | 0.22 |
| at | 3–8/out | 5026 | 100% | 52.79% | 52.8% | -0.01 | 1.0 | 1.38 | 0.52 | 0.72 | 0.02 |
| ip | 6–8/out | 1500 | 101% | 52.69% | 52.7% | -0.01 | 2.6 | 2.53 | 1.06 | 1.39 | 0.22 |
| pv | 10–13/out | 5000 | 100% | 50.51% | — | — | 2.3 | 1.39 | 2.75 | 1.20 | 0.21 |

Notas: σ_j = max(MOE publ., MOE AAS)/1,96 reescalado para a base de válidos (÷√(A+B)), somado em quadratura ao erro de arredondamento (uniforme ±0,5 p.p. em A e B; ±0,05 p.p. para 'at'). Para 'at' a MOE publicada (±1,0) é MENOR que a de amostragem aleatória simples (±1,38) — inconsistência sinalizada; usa-se ±1,38 no caso-base e a MOE literal em sensibilidade.

## Modelo de pesquisas

### Sensibilidade a σ_drift, σ_house, σ_extra (nowcast em 14/out, H=0)

θ_B latente em 14/out (sem house effect), desvio-padrão posterior e log-verossimilhança marginal (prior z_3 ~ N(0,1) em logit).

| σ_drift/√dia | σ_house | σ_extra | log ML | θ_B médio | dp θ_B (p.p.) | P(θ_B>0,5) |
|---|---|---|---|---|---|---|
| 0.000 | 0.00 | 0.00 | 11.080 | 51.76% | 0.37 | 100.0% |
| 0.000 | 0.00 | 0.02 | 10.952 | 51.71% | 0.41 | 100.0% |
| 0.000 | 0.00 | 0.04 | 10.203 | 51.66% | 0.52 | 99.9% |
| 0.000 | 0.01 | 0.00 | 11.063 | 51.75% | 0.38 | 100.0% |
| 0.000 | 0.01 | 0.02 | 10.897 | 51.71% | 0.43 | 100.0% |
| 0.000 | 0.01 | 0.04 | 10.140 | 51.66% | 0.53 | 99.9% |
| 0.000 | 0.02 | 0.00 | 10.947 | 51.72% | 0.42 | 100.0% |
| 0.000 | 0.02 | 0.02 | 10.719 | 51.69% | 0.46 | 100.0% |
| 0.000 | 0.02 | 0.04 | 9.957 | 51.66% | 0.56 | 99.9% |
| 0.000 | 0.04 | 0.00 | 10.257 | 51.67% | 0.54 | 99.9% |
| 0.000 | 0.04 | 0.02 | 10.005 | 51.66% | 0.57 | 99.8% |
| 0.000 | 0.04 | 0.04 | 9.314 | 51.65% | 0.65 | 99.4% |
| 0.005 | 0.00 | 0.00 | 11.242 | 51.66% | 0.42 | 100.0% |
| 0.005 | 0.00 | 0.02 | 11.037 | 51.64% | 0.46 | 100.0% |
| 0.005 | 0.00 | 0.04 | 10.222 | 51.62% | 0.56 | 99.8% |
| 0.005 | 0.01 | 0.00 | 11.201 | 51.65% | 0.44 | 100.0% |
| 0.005 | 0.01 | 0.02 | 10.972 | 51.63% | 0.47 | 100.0% |
| 0.005 | 0.01 | 0.04 | 10.157 | 51.62% | 0.57 | 99.8% |
| 0.005 | 0.02 | 0.00 | 11.039 | 51.64% | 0.47 | 100.0% |
| 0.005 | 0.02 | 0.02 | 10.773 | 51.63% | 0.50 | 99.9% |
| 0.005 | 0.02 | 0.04 | 9.969 | 51.61% | 0.59 | 99.7% |
| 0.005 | 0.04 | 0.00 | 10.287 | 51.61% | 0.58 | 99.7% |
| 0.005 | 0.04 | 0.02 | 10.024 | 51.61% | 0.61 | 99.6% |
| 0.005 | 0.04 | 0.04 | 9.317 | 51.61% | 0.68 | 99.1% |
| 0.010 | 0.00 | 0.00 | 11.535 | 51.46% | 0.54 | 99.7% |
| 0.010 | 0.00 | 0.02 | 11.199 | 51.47% | 0.57 | 99.5% |
| 0.010 | 0.00 | 0.04 | 10.258 | 51.51% | 0.65 | 99.0% |
| 0.010 | 0.01 | 0.00 | 11.455 | 51.46% | 0.55 | 99.6% |
| 0.010 | 0.01 | 0.02 | 11.115 | 51.47% | 0.58 | 99.5% |
| 0.010 | 0.01 | 0.04 | 10.189 | 51.51% | 0.66 | 98.9% |
| 0.010 | 0.02 | 0.00 | 11.212 | 51.47% | 0.57 | 99.5% |
| 0.010 | 0.02 | 0.02 | 10.876 | 51.48% | 0.60 | 99.3% |
| 0.010 | 0.02 | 0.04 | 9.992 | 51.51% | 0.68 | 98.7% |
| 0.010 | 0.04 | 0.00 | 10.340 | 51.48% | 0.67 | 98.7% |
| 0.010 | 0.04 | 0.02 | 10.055 | 51.50% | 0.69 | 98.5% |
| 0.010 | 0.04 | 0.04 | 9.317 | 51.52% | 0.76 | 97.7% |
| 0.020 | 0.00 | 0.00 | 11.794 | 51.16% | 0.75 | 94.0% |
| 0.020 | 0.00 | 0.02 | 11.337 | 51.19% | 0.78 | 93.6% |
| 0.020 | 0.00 | 0.04 | 10.256 | 51.27% | 0.87 | 92.7% |
| 0.020 | 0.01 | 0.00 | 11.676 | 51.17% | 0.76 | 93.9% |
| 0.020 | 0.01 | 0.02 | 11.234 | 51.20% | 0.79 | 93.5% |
| 0.020 | 0.01 | 0.04 | 10.182 | 51.27% | 0.88 | 92.6% |
| 0.020 | 0.02 | 0.00 | 11.351 | 51.20% | 0.78 | 93.7% |
| 0.020 | 0.02 | 0.02 | 10.946 | 51.22% | 0.82 | 93.3% |
| 0.020 | 0.02 | 0.04 | 9.971 | 51.28% | 0.90 | 92.4% |
| 0.020 | 0.04 | 0.00 | 10.338 | 51.25% | 0.87 | 92.6% |
| 0.020 | 0.04 | 0.02 | 10.033 | 51.27% | 0.90 | 92.2% |
| 0.020 | 0.04 | 0.04 | 9.262 | 51.32% | 0.97 | 91.4% |

Máxima verossimilhança marginal na grade: σ_drift=0.02, σ_house=0.0, σ_extra=0.0 (log ML=11.794).

Perfil de σ_extra (σ_house=0, σ_drift=0,01): máximo em σ_extra ≈ 0.0000 logit ≈ 0.00 p.p.; ΔlogML(σ_extra=0 vs máx) = 0.000

**Caso-base das pesquisas** (σ_drift=0,01/√dia, σ_house=0,02, σ_extra=0,02, logit): θ_B(14/out) = 51.48% ± 0.60 p.p. (1 dp) → θ_A = 48.52%.

### Trajetória latente z_t (caso-base)

| dia | θ_B latente | dp (p.p.) |
|---|---|---|
| 3/out | 51.97% | 0.68 |
| 4/out | 51.97% | 0.64 |
| 5/out | 51.95% | 0.60 |
| 6/out | 51.92% | 0.56 |
| 7/out | 51.87% | 0.54 |
| 8/out | 51.80% | 0.53 |
| 9/out | 51.72% | 0.52 |
| 10/out | 51.63% | 0.51 |
| 11/out | 51.57% | 0.51 |
| 12/out | 51.52% | 0.53 |
| 13/out | 51.49% | 0.56 |
| 14/out | 51.48% | 0.60 |

### House effects posteriores (caso-base; prior N(0, 0,02²) sem sinal)

| instituto | h_j (logit) | dp | ≈ p.p. em θ_B | h_j / σ_house |
|---|---|---|---|---|
| df | -0.0008 | 0.0179 | -0.02 | -0.04 |
| qu | -0.0024 | 0.0188 | -0.06 | -0.12 |
| pd | -0.0035 | 0.0185 | -0.09 | -0.18 |
| nx | +0.0002 | 0.0188 | +0.01 | +0.01 |
| at | +0.0086 | 0.0182 | +0.22 | +0.43 |
| ip | +0.0034 | 0.0191 | +0.08 | +0.17 |
| pv | -0.0054 | 0.0188 | -0.14 | -0.27 |

### Efeito do horizonte até a eleição (data não informada)

| σ_drift | H (dias após 14/out) | θ_B | dp (p.p.) | P(θ_B>0,5) |
|---|---|---|---|---|
| 0.005 | 0 | 51.63% | 0.50 | 99.9% |
| 0.005 | 7 | 51.63% | 0.60 | 99.6% |
| 0.005 | 14 | 51.63% | 0.69 | 99.1% |
| 0.010 | 0 | 51.48% | 0.60 | 99.3% |
| 0.010 | 7 | 51.48% | 0.90 | 95.1% |
| 0.010 | 14 | 51.48% | 1.11 | 90.8% |
| 0.020 | 0 | 51.22% | 0.82 | 93.3% |
| 0.020 | 7 | 51.22% | 1.55 | 78.4% |
| 0.020 | 14 | 51.22% | 2.04 | 72.6% |

### df rodada 1 → rodada 2 (atualização temporal, não média)

| σ_drift | ganho de Kalman da rodada 2 | θ_B df filtrado (13–14/out) | dp (p.p.) |
|---|---|---|---|
| 0.000 | 0.495 | 51.61% | 0.76 |
| 0.005 | 0.518 | 51.59% | 0.78 |
| 0.010 | 0.575 | 51.53% | 0.82 |
| 0.020 | 0.711 | 51.39% | 0.92 |

Variação df-1→df-2 em θ_B: -1.04 p.p.; z = -0.68 (só amostragem).

## Validação: resíduos por pesquisa

| pesquisa | observado θ_B | previsto (sem house, σ_extra=0) | resíduo (p.p.) | σ_j (p.p.) | r_j | previsto LOO (caso-base) | r_j LOO |
|---|---|---|---|---|---|---|---|
| df-1 | 52.13% | 52.02% | +0.11 | 1.07 | +0.10 | 51.79% | +0.25 |
| df-2 | 51.09% | 51.46% | -0.37 | 1.09 | -0.34 | 51.61% | -0.37 |
| qu | 51.11% | 51.55% | -0.44 | 1.16 | -0.38 | 51.62% | -0.35 |
| pd | 51.06% | 51.57% | -0.51 | 0.97 | -0.53 | 51.67% | -0.46 |
| nx | 51.61% | 51.57% | +0.04 | 1.18 | +0.03 | 51.57% | +0.03 |
| at | 52.79% | 52.05% | +0.74 | 0.72 | +1.03 | 51.56% | +1.03 |
| ip | 52.69% | 51.98% | +0.71 | 1.39 | +0.51 | 51.76% | +0.56 |
| pv | 50.51% | 51.55% | -1.04 | 1.20 | -0.87 | 51.70% | -0.80 |

Σ r_j² = 2.62 com ≈7 g.l. (nível comum estimado); p ≈ 0.917 (Wilson–Hilferty). Razão de dispersão = 0.37.

Sensibilidade: MOE literal de 'at' (±1,0): θ_B = 51.51% ± 0.59 p.p.

Influência (remove uma pesquisa por vez; caso-base):

| removida | θ_B 14/out | Δ vs. todas (p.p.) |
|---|---|---|
| df-1 | 51.46% | -0.02 |
| df-2 | 51.58% | +0.10 |
| qu | 51.55% | +0.07 |
| pd | 51.58% | +0.10 |
| nx | 51.48% | -0.01 |
| at | 51.31% | -0.18 |
| ip | 51.42% | -0.06 |
| pv | 51.63% | +0.15 |

## Modelo estrutural (Monte Carlo)

Churn de eleitores do 1T: c_g ~ Beta(μ=0.05, dp=0.015) independente por coorte; τ_ABS ~ Beta(μ=0.1871, dp=0.03) (μ escolhido para manter o comparecimento esperado = 1º turno, 78.916%).

### Ponto central (matriz pd normalizada, sem incerteza)

| Indecisos | θ_A | V_A | V_B | V_B − V_A |
|---|---|---|---|---|
| I | 47.110% | 56.240.542 | 63.140.116 | 6.899.574 |
| II | 47.180% | 56.323.387 | 63.057.272 | 6.733.885 |
| III | 47.474% | 56.403.552 | 62.406.580 | 6.003.028 |
| IV | 46.725% | 55.488.499 | 63.266.580 | 7.778.081 |

Checagem de coerência pd: matriz × coortes com τ=1 para todos → θ_A = 47.07%; só comparecentes do 1T (τ_ABS=0) → θ_A = 47.59%; topline pd publicada → θ_A = 48.94%.

Inconsistência interna pd: a matriz aplicada ao resultado oficial do 1T não reproduz a própria topline pd (47.07% vs 48.94%). Para reproduzi-la só via composição, a coorte A precisaria pesar 1.112× o seu tamanho oficial (relativo às demais coortes), i.e. recordação/ponderação de voto do 1T diferente do resultado oficial, ou linhas da matriz com viés. Não corrigido: tratado pela ponderação com as pesquisas nacionais (pd topline entra apenas nelas).

### Tamanho efetivo amostral dos pesos (importance sampling)

Proposta conjugada: qu C/D/E entram exatamente via agregação Dirichlet; df e qu(BN+ABS) via pseudo-contagens corrigidas por peso.

| Configuração | sorteios | ESS | ESS/sorteios |
|---|---|---|---|
| pd apenas (prior) | 1.000.000 | 1.000.000 | 100.00% |
| pd + df | 500.000 | 31.577 | 6.32% |
| pd + qu | 500.000 | 52.448 | 10.49% |
| pd + df + qu | 1.000.000 | 17.816 | 1.78% |
| pd + pesquisas nacionais | 1.000.000 | 526.327 | 52.63% |
| pd + df + qu + pesquisas (completo) | 1.000.000 | 13.722 | 1.37% |

### Parâmetros: média [IC 90%] em % (Modelo 2, DEFF=2, indecisos III)

Linhas q_g ANTES da resolução dos indecisos e antes do comparecimento (intenção declarada normalizada). θ_A inclui indecisos III e τ_g.

| Parâmetro | pd apenas (prior) | pd + df | pd + qu | pd + df + qu | pd + pesquisas nacionais | pd + df + qu + pesquisas (completo) |
|---|---|---|---|---|---|---|
| R_B = P(B₂|B₁) | 94.7 [93.0; 96.2] | 94.7 [93.0; 96.2] | 94.7 [93.0; 96.2] | 94.7 [93.0; 96.2] | 94.3 [92.7; 95.8] | 94.6 [93.0; 96.0] |
| X_BA = P(A₂|B₁) | 5.1 [3.7; 6.8] | 5.1 [3.6; 6.8] | 5.1 [3.7; 6.8] | 5.1 [3.6; 6.8] | 5.5 [4.0; 7.0] | 5.2 [3.8; 6.8] |
| R_A = P(A₂|A₁) | 91.7 [89.7; 93.6] | 91.8 [89.7; 93.7] | 91.7 [89.7; 93.6] | 91.7 [89.6; 93.6] | 92.1 [90.3; 93.9] | 91.9 [90.0; 93.7] |
| X_AB = P(B₂|A₁) | 5.1 [3.6; 6.8] | 5.1 [3.6; 6.8] | 5.1 [3.6; 6.7] | 5.1 [3.6; 6.8] | 4.7 [3.4; 6.2] | 4.9 [3.6; 6.4] |
| T_CB | 54.2 [40.3; 67.8] | 51.1 [38.6; 63.7] | 44.5 [33.9; 55.2] | 43.9 [34.1; 53.9] | 52.8 [39.1; 66.4] | 43.6 [34.0; 53.5] |
| T_CA | 26.9 [15.4; 39.8] | 30.7 [19.2; 42.6] | 29.7 [20.3; 39.9] | 32.6 [23.4; 42.3] | 28.2 [16.5; 41.1] | 32.9 [23.6; 42.5] |
| T_DB | 45.9 [30.6; 61.5] | 43.7 [29.5; 58.2] | 43.5 [31.7; 55.7] | 44.1 [32.6; 55.5] | 44.7 [29.7; 60.2] | 43.9 [32.5; 55.3] |
| T_DA | 24.8 [12.5; 39.2] | 28.6 [15.9; 42.6] | 20.5 [11.5; 31.0] | 22.9 [13.6; 33.4] | 25.8 [13.3; 40.3] | 23.1 [13.7; 33.6] |
| T_EB | 55.1 [39.3; 70.5] | 52.7 [38.0; 67.2] | 49.9 [37.6; 62.1] | 50.0 [38.2; 61.8] | 53.9 [38.2; 69.3] | 49.8 [38.1; 61.6] |
| T_EA | 19.6 [8.6; 33.2] | 22.7 [10.9; 36.6] | 21.0 [11.9; 31.7] | 23.2 [13.8; 33.9] | 20.6 [9.2; 34.5] | 23.3 [14.0; 34.0] |
| T_FB | 53.5 [19.5; 85.8] | 52.1 [18.7; 84.8] | 53.4 [19.5; 85.7] | 53.6 [19.6; 85.7] | 52.9 [19.0; 85.5] | 53.3 [19.5; 85.6] |
| T_FA | 15.9 [0.5; 46.5] | 17.1 [0.6; 48.5] | 15.9 [0.6; 46.4] | 17.5 [0.6; 49.6] | 16.4 [0.6; 47.4] | 17.6 [0.6; 49.8] |
| T_G:L,B | 21.7 [1.3; 56.9] | 21.7 [1.4; 57.2] | 21.7 [1.3; 56.8] | 21.7 [1.3; 57.1] | 21.2 [1.2; 56.1] | 21.5 [1.3; 57.1] |
| T_G:L,A | 32.7 [5.0; 69.9] | 32.6 [4.9; 69.6] | 32.5 [4.9; 69.7] | 32.8 [5.1; 70.3] | 33.3 [5.2; 70.5] | 33.0 [5.2; 70.6] |
| T_G:L,NS | 26.1 [2.5; 62.5] | 26.1 [2.5; 62.3] | 26.2 [2.5; 62.5] | 25.9 [2.4; 62.9] | 26.1 [2.5; 62.6] | 25.9 [2.3; 62.9] |
| BN₁→B | 21.9 [13.7; 31.2] | 21.9 [13.6; 31.2] | 23.2 [14.8; 32.6] | 23.2 [14.6; 32.6] | 21.1 [13.1; 30.0] | 22.8 [14.4; 31.9] |
| BN₁→A | 18.1 [10.5; 26.8] | 18.1 [10.5; 27.0] | 22.4 [13.7; 32.2] | 22.4 [13.7; 32.0] | 18.9 [11.1; 27.7] | 22.8 [14.1; 32.3] |
| BN₁→BN | 45.8 [35.2; 56.5] | 45.7 [35.2; 56.4] | 41.5 [31.5; 51.8] | 41.5 [31.6; 51.9] | 45.8 [35.2; 56.5] | 41.6 [31.5; 52.0] |
| ABS₁→B | 41.9 [37.4; 46.5] | 41.9 [37.3; 46.4] | 41.1 [37.5; 44.7] | 41.1 [37.5; 44.8] | 41.6 [37.1; 46.1] | 41.0 [37.5; 44.7] |
| ABS₁→A | 33.9 [29.6; 38.4] | 33.9 [29.6; 38.3] | 38.7 [35.1; 42.3] | 38.6 [35.1; 42.2] | 34.2 [29.9; 38.6] | 38.7 [35.2; 42.2] |
| ABS₁→BN | 19.0 [15.5; 22.8] | 19.0 [15.6; 22.8] | 16.0 [13.2; 18.9] | 16.0 [13.3; 18.9] | 19.0 [15.6; 22.8] | 16.0 [13.3; 18.9] |
| C:F agregado →B | 52.0 [43.6; 60.3] | 49.4 [43.1; 55.8] | 46.0 [39.5; 52.6] | 46.0 [40.6; 51.5] | 50.7 [42.7; 58.8] | 45.8 [40.5; 51.1] |
| C:F agregado →A | 23.8 [17.0; 31.2] | 27.3 [21.8; 33.0] | 24.0 [18.6; 29.7] | 26.5 [21.8; 31.4] | 24.9 [18.1; 32.2] | 26.7 [22.1; 31.5] |
| θ_A (válidos) | 47.5 [46.1; 49.0] | 47.8 [46.4; 49.2] | 48.0 [46.7; 49.4] | 48.1 [46.8; 49.5] | 48.2 [47.4; 49.0] | 48.4 [47.6; 49.2] |

P(θ_A > 0,5 | modelo) — condicional às hipóteses, não previsão:

| Configuração | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|
| pd apenas (prior) | 47.55% | 46.13% – 48.97% | 0.2% |
| pd + df | 47.79% | 46.40% – 49.16% | 0.4% |
| pd + qu | 48.02% | 46.65% – 49.39% | 0.9% |
| pd + df + qu | 48.11% | 46.78% – 49.48% | 1.1% |
| pd + pesquisas nacionais | 48.20% | 47.39% – 49.01% | 0.0% |
| pd + df + qu + pesquisas (completo) | 48.37% | 47.59% – 49.18% | 0.0% |

### Sensibilidade: Modelo 1 (conservador) vs Modelo 2 (DEFF 1,5 / 2 / 3)

| Modelo | Informação | E[θ_A] | IC 90% | dp (p.p.) | R_A | R_B | P(θ_A>0,5) | ESS |
|---|---|---|---|---|---|---|---|---|
| M1 (σ_sub²=σ_geral²+5²p.p.²) | prior | 47.50% | 44.91% – 50.08% | 1.58 | 90.6 | 93.5 | 5.5% | 200.000 |
| M1 (σ_sub²=σ_geral²+5²p.p.²) | +df+qu | 47.97% | 45.53% – 50.47% | 1.52 | 90.7 | 93.6 | 8.6% | 1.948 |
| M1 (σ_sub²=σ_geral²+5²p.p.²) | +df+qu+pesq. | 48.44% | 47.54% – 49.33% | 0.55 | 91.4 | 93.3 | 0.2% | 586 |
| M2 DEFF=1,5 | prior | 47.53% | 46.25% – 48.81% | 0.78 | 91.8 | 94.8 | 0.1% | 200.000 |
| M2 DEFF=1,5 | +df+qu | 48.13% | 46.91% – 49.37% | 0.74 | 91.8 | 94.7 | 0.5% | 985 |
| M2 DEFF=1,5 | +df+qu+pesq. | 48.36% | 47.60% – 49.14% | 0.47 | 91.9 | 94.6 | 0.0% | 498 |
| M2 DEFF=2 | prior | 47.55% | 46.12% – 48.96% | 0.86 | 91.7 | 94.7 | 0.2% | 200.000 |
| M2 DEFF=2 | +df+qu | 48.06% | 46.70% – 49.40% | 0.81 | 91.7 | 94.7 | 1.0% | 613 |
| M2 DEFF=2 | +df+qu+pesq. | 48.35% | 47.58% – 49.14% | 0.47 | 91.9 | 94.6 | 0.0% | 287 |
| M2 DEFF=3 | prior | 47.58% | 45.93% – 49.24% | 1.01 | 91.6 | 94.6 | 0.8% | 200.000 |
| M2 DEFF=3 | +df+qu | 48.13% | 46.58% – 49.72% | 0.96 | 91.6 | 94.6 | 2.7% | 11.534 |
| M2 DEFF=3 | +df+qu+pesq. | 48.40% | 47.56% – 49.25% | 0.51 | 91.8 | 94.4 | 0.1% | 7.134 |

κ do Modelo 1 = 95.7 (igual para todas as coortes). n_eff (Modelo 2) por coorte: B=530.1, A=509.1, C=32.6, D=25.3, E=24.6, F=3.1, GL=2.5, BN=56.5, ABS=316.3 (DEFF=2). n_eff é APROXIMAÇÃO: o n real das subamostras não foi informado.

## C. Comparação pd × df × qu

| Fluxo | pd (normalizado) | observação externa | Δ (p.p.) | z (n_eff, DEFF=2) |
|---|---|---|---|---|
| C:F → B | 54.5% | 46.0% | -8.5 | -1.07 |
| C:F → A | 23.5% | 32.0% | +8.5 | +1.19 |
| C:F → BN | 17.6% | 15.0% | -2.6 | -0.44 |
| C:F → NS | 4.4% | 7.0% | +2.6 | +0.69 |
| C → B | 56.0% | 30.0% | -26.0 | -2.02 |
| C → A | 27.0% | 34.0% | +7.0 | +0.56 |
| D → B | 47.5% | 40.0% | -7.5 | -0.50 |
| D → A | 24.8% | 14.0% | -10.8 | -0.91 |
| E → B | 57.6% | 42.0% | -15.6 | -1.01 |
| E → A | 19.2% | 23.0% | +3.8 | +0.30 |
| BN+ABS → B | 38.9% | 38.0% | -0.9 | -0.24 |
| BN+ABS → A | 31.5% | 43.0% | +11.5 | +2.96 |

Para df, a comparação de C:F usa pd ponderado por votos de C, D, E, F. Para qu, 'restante' não é decomposto (apenas B e A são comparados). z é aproximação: n reais das subamostras desconhecidos.

## Indecisos: métodos I–IV

| Método | Informação | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|
| I | pd apenas (prior) | 47.20% | 45.79% – 48.62% | 0.1% |
| I | pd + df + qu | 47.75% | 46.42% – 49.12% | 0.3% |
| I | pd + df + qu + pesquisas (completo) | 48.24% | 47.45% – 49.06% | 0.0% |
| II | pd apenas (prior) | 47.28% | 45.89% – 48.66% | 0.1% |
| II | pd + df + qu | 47.81% | 46.50% – 49.15% | 0.3% |
| II | pd + df + qu + pesquisas (completo) | 48.26% | 47.47% – 49.06% | 0.0% |
| III | pd apenas (prior) | 47.55% | 46.13% – 48.97% | 0.2% |
| III | pd + df + qu | 48.11% | 46.78% – 49.48% | 1.1% |
| III | pd + df + qu + pesquisas (completo) | 48.37% | 47.59% – 49.18% | 0.0% |
| IV | pd apenas (prior) | 47.26% | 45.79% – 48.71% | 0.1% |
| IV | pd + df + qu | 47.79% | 46.39% – 49.20% | 0.5% |
| IV | pd + df + qu + pesquisas (completo) | 48.27% | 47.46% – 49.09% | 0.0% |

Massa de NS (ponto central. ponderada por comparecimento): 2.571.529 eleitores = 2.05% dos comparecentes.

## Comparecimento × preferência dos novos comparecentes

Para cada cenário, τ_ABS é ajustado para que o comparecimento total atinja o alvo; churn das demais coortes segue a distribuição base. A divisão A:B dos novos comparecentes é aplicada entre seus votos válidos; a fração BN deles vem da linha ABS da pd (sorteada). 'pd' = usa a linha ABS da matriz pd.

### E[θ_A] (estrutural: pd + df + qu)

| Comparecimento | A:B pd | A:B 50:50 | A:B 55:45 | A:B 60:40 | A:B 2:1 | A:B 40:60 | A:B 45:55 |
|---|---|---|---|---|---|---|---|
| = 1º turno | 48.11% | 48.18% | 48.40% | 48.62% | 48.91% | 47.74% | 47.96% |
| +1 p.p. | 48.12% | 48.20% | 48.48% | 48.75% | 49.11% | 47.66% | 47.93% |
| +2 p.p. | 48.12% | 48.22% | 48.55% | 48.87% | 49.30% | 47.58% | 47.90% |
| +3 p.p. | 48.13% | 48.24% | 48.62% | 48.99% | 49.49% | 47.49% | 47.87% |
| +5 p.p. | 48.13% | 48.28% | 48.75% | 49.22% | 49.85% | 47.34% | 47.81% |
| -1 p.p. | 48.11% | 48.16% | 48.33% | 48.49% | 48.72% | 47.83% | 48.00% |
| -2 p.p. | 48.11% | 48.14% | 48.25% | 48.36% | 48.51% | 47.92% | 48.03% |

### P(θ_A > 0,5) (estrutural: pd + df + qu)

| Comparecimento | A:B pd | A:B 50:50 | A:B 55:45 | A:B 60:40 | A:B 2:1 | A:B 40:60 | A:B 45:55 |
|---|---|---|---|---|---|---|---|
| = 1º turno | 1.1% | 1.3% | 2.7% | 5.0% | 9.7% | 0.3% | 0.7% |
| +1 p.p. | 1.0% | 1.3% | 3.1% | 6.5% | 14.0% | 0.2% | 0.6% |
| +2 p.p. | 1.0% | 1.3% | 3.7% | 8.2% | 19.3% | 0.1% | 0.5% |
| +3 p.p. | 1.0% | 1.3% | 4.2% | 10.4% | 25.5% | 0.1% | 0.3% |
| +5 p.p. | 1.1% | 1.3% | 5.5% | 16.0% | 41.6% | 0.0% | 0.2% |
| -1 p.p. | 1.1% | 1.3% | 2.4% | 3.8% | 6.7% | 0.4% | 0.8% |
| -2 p.p. | 1.2% | 1.3% | 2.0% | 2.9% | 4.4% | 0.7% | 0.9% |

### P(θ_A > 0,5) (estrutural + pesquisas nacionais)

| Comparecimento | A:B pd | A:B 50:50 | A:B 55:45 | A:B 60:40 | A:B 2:1 | A:B 40:60 | A:B 45:55 |
|---|---|---|---|---|---|---|---|
| = 1º turno | 0.0% | 0.1% | 0.1% | 0.2% | 0.3% | 0.0% | 0.0% |
| +1 p.p. | 0.0% | 0.0% | 0.1% | 0.2% | 0.4% | 0.0% | 0.0% |
| +2 p.p. | 0.0% | 0.0% | 0.1% | 0.2% | 0.6% | 0.0% | 0.0% |
| +3 p.p. | 0.0% | 0.0% | 0.1% | 0.3% | 0.9% | 0.0% | 0.0% |
| +5 p.p. | 0.0% | 0.0% | 0.2% | 0.5% | 1.9% | 0.0% | 0.0% |
| -1 p.p. | 0.0% | 0.1% | 0.1% | 0.1% | 0.2% | 0.0% | 0.0% |
| -2 p.p. | 0.0% | 0.1% | 0.1% | 0.1% | 0.1% | 0.0% | 0.0% |

τ_ABS implícito médio no cenário base: 0.1871 (≈6.26 mi de abstencionistas do 1T comparecem, compensando ≈6.26 mi de eleitores do 1T que se abstêm).

## Retenção: P(θ_A>0,5) em grade R_A × R_B (estrutural pd+df+qu)

R fixado; crossover X mantido no sorteio; massa restante (BN+NS) reescalada para fechar 1; demais parâmetros sorteados.

|  | R_A=0.88 | R_A=0.90 | R_A=0.92 | R_A=0.94 | R_A=0.96 | R_A=0.98 |
|---|---|---|---|---|---|---|
| R_B=0.89 | 3.0% | 5.2% | 8.0% | 12.3% | 30.6% | 71.7% |
| R_B=0.91 | 1.0% | 1.8% | 3.2% | 5.2% | 17.1% | 60.9% |
| R_B=0.93 | 0.3% | 0.5% | 1.0% | 1.9% | 7.9% | 45.9% |
| R_B=0.95 | 0.0% | 0.1% | 0.1% | 0.2% | 1.3% | 21.7% |
| R_B=0.97 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 1.6% |

E[θ_A] correspondente:

|  | R_A=0.88 | R_A=0.90 | R_A=0.92 | R_A=0.94 | R_A=0.96 | R_A=0.98 |
|---|---|---|---|---|---|---|
| R_B=0.89 | 48.44% | 48.64% | 48.83% | 49.05% | 49.59% | 50.44% |
| R_B=0.91 | 48.19% | 48.39% | 48.58% | 48.80% | 49.33% | 50.18% |
| R_B=0.93 | 47.95% | 48.14% | 48.33% | 48.55% | 49.08% | 49.93% |
| R_B=0.95 | 47.57% | 47.77% | 47.96% | 48.18% | 48.71% | 49.55% |
| R_B=0.97 | 46.78% | 46.98% | 47.17% | 47.39% | 47.92% | 48.76% |

## Cenário hipotético do bloco 6 (não é pesquisa)

| Cenário | θ_A | z vs. pesquisas (caso-base) |
|---|---|---|
| pd (ponto central) | 47.47% | +1.73 |
| retenções hipotéticas, ABS = pd | 48.53% | -0.03 |
| retenções pd, novos = 2:1 | 48.59% | -0.12 |
| retenções hipotéticas + novos 2:1 | 49.66% | -1.90 |
| retenções hipotéticas + novos = qu (43:38) | 48.89% | -0.62 |

Comparação da hipótese 2/3 : 1/3 para novos comparecentes com as observações: pd ABS (válidos) A = 44.74%; qu BN+ABS (válidos) A = 53.09%; hipótese A = 66,67%.

## E. Decomposição da variância

| Bloco | Fonte | dp de θ (p.p.) | parcela no bloco |
|---|---|---|---|
| estrutural | retenção A (linha A) | 0.437 | 23.8% |
| estrutural | retenção B (linha B) | 0.431 | 23.1% |
| estrutural | eliminados C:L | 0.324 | 13.0% |
| estrutural | BN do 1º turno | 0.227 | 6.4% |
| estrutural | abstêmios do 1º turno (preferência) | 0.135 | 2.3% |
| estrutural | comparecimento (τ_g) | 0.439 | 24.0% |
| estrutural | indecisos (Dirichlet IV) | 0.244 | 7.4% |
| estrutural | **total conjunto (todos variando)** | 0.891 | Σ partes/total = 1.01 |
| pesquisas | amostragem (MOE) | 0.368 | 16.9% |
| pesquisas | house effects | 0.204 | 5.2% |
| pesquisas | deriva temporal (inclui H=7 dias) | 0.768 | 73.5% |
| pesquisas | σ_extra (erro não amostral) | 0.188 | 4.4% |
| pesquisas | **total (caso-base, H=7)** | 0.895 | Σ partes/total = 1.00 |

Combinação (aprox. Gaussiana): 1/v_post = 1/v_estr + 1/v_pesq → dp_post = 0.63 p.p.; peso de informação: estrutural 50.2%, pesquisas 49.8%.

## F/G. Sensibilidade univariada e elasticidades

Duas bases: (1) ponto central da matriz pd normalizada; (2) médias posteriores do modelo completo (pd+df+qu+pesquisas). Indecisos: método III. Derivadas ANALÍTICAS de θ_A = V_A/(V_A+V_B): 'parcial' = massa vem de/para fora dos válidos (BN/abstenção), demais entradas fixas; 'troca' = massa vem do adversário na mesma coorte. Valores = variação de θ_A em p.p. por +1 p.p. no parâmetro.

### Base: pd (ponto central)

θ_A = 47.474%; V_A = 56.403.552; V_B = 62.406.580; V_BN = 6.462.430; V_B − V_A = 6.003.028.

| Parâmetro | valor (após indecisos III) | ∂θ_A/∂p parcial | ∂θ_A/∂p troca | elasticidade |∂θ_k/∂p|·p/θ_k | eleitores por 1 p.p. |
|---|---|---|---|---|---|
| R_A (A₁→A) | 93.88% | +0.2263 | +0.4308 | 0.4475 | 511.828 |
| X_AB (A₁→B) | 5.10% | -0.2045 | -0.4308 | 0.0199 | 511.828 |
| R_B (B₁→B) | 94.95% | -0.2130 | -0.4486 | 0.3850 | 532.991 |
| X_BA (B₁→A) | 5.05% | +0.2356 | +0.4486 | 0.0251 | 532.991 |
| T_CA | 28.72% | +0.0145 | +0.0276 | 0.0088 | 32.761 |
| T_CB | 59.57% | -0.0131 | -0.0276 | 0.0148 | 32.761 |
| T_DA | 25.00% | +0.0112 | +0.0214 | 0.0059 | 25.421 |
| T_DB | 48.00% | -0.0102 | -0.0214 | 0.0093 | 25.421 |
| T_EA | 20.43% | +0.0109 | +0.0208 | 0.0047 | 24.749 |
| T_EB | 61.29% | -0.0099 | -0.0208 | 0.0115 | 24.749 |
| T_FA | 10.31% | +0.0014 | +0.0026 | 0.0003 | 3.102 |
| T_FB | 74.23% | -0.0012 | -0.0026 | 0.0018 | 3.102 |
| T_G:L,A | 53.42% | +0.0011 | +0.0021 | 0.0012 | 2.476 |
| T_G:L,B | 26.03% | -0.0010 | -0.0021 | 0.0005 | 2.476 |
| BN₁→A | 20.69% | +0.0251 | +0.0478 | 0.0109 | 56.762 |
| BN₁→B | 25.29% | -0.0227 | -0.0478 | 0.0109 | 56.762 |
| ABS₁→A | 35.79% | +0.0277 | +0.0527 | 0.0209 | 62.636 |
| ABS₁→B | 44.21% | -0.0250 | -0.0527 | 0.0211 | 62.636 |

∂θ_B/∂p = −∂θ_A/∂p. Elasticidade usa θ_k do candidato favorecido pelo parâmetro.

| Comparecimento (+1 p.p. em τ) | ∂θ_A/∂τ (p.p. por p.p.) | eleitores adicionais |
|---|---|---|
| τ_A (coorte A) | +0.2126 | 538.766 |
| τ_B (coorte B) | -0.2003 | 561.043 |
| τ C:F | -0.0109 | 90.561 |
| τ G:L | +0.0003 | 2.607 |
| τ BN₁ | -0.0006 | 59.749 |
| τ ABS₁ | -0.0062 | 334.700 |
| +1 p.p. do ELEITORADO vindo de ABS₁ (pref. da coorte) | -0.0293 | 1.587.426 |

Tornado: cada parâmetro varrido no seu IC 90% a priori (pd, M2, DEFF=2), demais fixos na base (parcial):

| Parâmetro | faixa IC 90% (q) | θ_A no limite inf. | θ_A no limite sup. | amplitude (p.p.) |
|---|---|---|---|---|
| churn coorte A | 2.5 – 7.5 | 47.99% | 46.94% | 1.049 |
| churn coorte B | 2.5 – 7.5 | 46.99% | 47.97% | 0.989 |
| R_A (A₁→A) | 89.7 – 93.6 | 46.93% | 47.85% | 0.925 |
| X_BA (B₁→A) | 3.7 – 6.8 | 47.14% | 47.88% | 0.736 |
| R_B (B₁→B) | 93.0 – 96.2 | 47.89% | 47.21% | 0.679 |
| X_AB (A₁→B) | 3.6 – 6.8 | 47.77% | 47.11% | 0.662 |
| BN₁→A | 10.5 – 26.8 | 47.26% | 47.74% | 0.476 |
| BN₁→B | 13.7 – 31.2 | 47.69% | 47.23% | 0.463 |
| T_CB | 40.3 – 67.8 | 47.69% | 47.31% | 0.384 |
| T_CA | 15.4 – 39.8 | 47.29% | 47.67% | 0.376 |
| T_EB | 39.3 – 70.5 | 47.67% | 47.34% | 0.329 |
| T_DB | 30.6 – 61.5 | 47.65% | 47.33% | 0.317 |
| T_DA | 12.5 – 39.2 | 47.33% | 47.64% | 0.302 |
| T_EA | 8.6 – 33.2 | 47.35% | 47.64% | 0.286 |
| ABS₁→A | 29.6 – 38.4 | 47.35% | 47.60% | 0.254 |
| ABS₁→B | 37.4 – 46.5 | 47.60% | 47.36% | 0.239 |

#### H. Break-even (base: pd (ponto central)) — equações condicionais, NÃO previsões

| θ_A alvo | R_A (X_AB=5.1% fixo; máx 94.9%) | R_A com X_AB=0 | R_B (X_BA=5.1% fixo) | A entre válidos de C:F | X_BA (tirado de R_B) |
|---|---|---|---|---|---|
| 48% | inviável | 91.52% | 92.51% | 38.95% | 6.22% |
| 49% | inviável | 95.92% | 88.01% | 55.84% | 8.45% |
| 50% | inviável | inviável | 83.69% | 72.74% | 10.68% |
| 51% | inviável | inviável | 79.54% | 89.63% | 12.91% |
| 52% | inviável | inviável | 75.55% | inviável | 15.14% |

Valores da base: R_A = 93.88%, R_B = 94.95%, A entre válidos de C:F = 30.06%, X_BA = 5.05%, X_AB = 5.10%.

Novos comparecentes para zerar V_B − V_A = 6.003.028: N_válidos = (V_B − V_A)/(a − b); total = N_válidos/(1 − f_BN). f_BN = 20.0% (linha ABS da base).

| A:B dos novos | novos votos válidos | novos comparecentes | p.p. do eleitorado | % dos abstêmios do 1T |
|---|---|---|---|---|
| 50:50 | não fecha a diferença | — | — | — |
| 55:45 | 60.030.279 | 75.037.848 | 47.27 | 224.2% |
| 60:40 | 30.015.139 | 37.518.924 | 23.64 | 112.1% |
| 2:1 | 18.009.084 | 22.511.355 | 14.18 | 67.3% |
| 45:55 | não fecha a diferença | — | — | — |
| 40:60 | não fecha a diferença | — | — | — |
| 1:2 | não fecha a diferença | — | — | — |

| Combinação C:F | Valor |
|---|---|
| Votos que precisam passar de B para A (cada um reduz a diferença em 2) | 3.001.514 |
| Estoque de votos B em C:F | 4.919.041 |
| Fração uniforme do voto B de C:F que precisaria migrar | 61.0% |
| Só coorte C | 153.8% (inviável) |
| Só coorte D | 246.0% (inviável) |
| Só coorte E | 197.9% (inviável) |
| Só coorte F | 1303.7% (inviável) |

### Base: média posterior completa

θ_A = 48.369%; V_A = 57.574.886; V_B = 61.457.339; V_BN = 6.266.201; V_B − V_A = 3.882.453.

| Parâmetro | valor (após indecisos III) | ∂θ_A/∂p parcial | ∂θ_A/∂p troca | elasticidade |∂θ_k/∂p|·p/θ_k | eleitores por 1 p.p. |
|---|---|---|---|---|---|
| R_A (A₁→A) | 93.89% | +0.2225 | +0.4309 | 0.4319 | 512.921 |
| X_AB (A₁→B) | 5.01% | -0.2084 | -0.4309 | 0.0202 | 512.921 |
| R_B (B₁→B) | 94.66% | -0.2163 | -0.4471 | 0.3965 | 532.180 |
| X_BA (B₁→A) | 5.25% | +0.2308 | +0.4471 | 0.0251 | 532.180 |
| T_CA | 36.42% | +0.0142 | +0.0275 | 0.0107 | 32.760 |
| T_CB | 48.28% | -0.0133 | -0.0275 | 0.0124 | 32.760 |
| T_DA | 23.92% | +0.0110 | +0.0214 | 0.0055 | 25.421 |
| T_DB | 45.44% | -0.0103 | -0.0214 | 0.0091 | 25.421 |
| T_EA | 25.55% | +0.0107 | +0.0208 | 0.0057 | 24.747 |
| T_EB | 54.48% | -0.0101 | -0.0208 | 0.0106 | 24.747 |
| T_FA | 19.95% | +0.0013 | +0.0026 | 0.0006 | 3.103 |
| T_FB | 60.41% | -0.0013 | -0.0026 | 0.0015 | 3.103 |
| T_G:L,A | 44.49% | +0.0011 | +0.0021 | 0.0010 | 2.476 |
| T_G:L,B | 29.05% | -0.0010 | -0.0021 | 0.0006 | 2.476 |
| BN₁→A | 26.17% | +0.0246 | +0.0477 | 0.0133 | 56.750 |
| BN₁→B | 26.14% | -0.0231 | -0.0477 | 0.0117 | 56.750 |
| ABS₁→A | 40.43% | +0.0272 | +0.0526 | 0.0227 | 62.628 |
| ABS₁→B | 42.89% | -0.0254 | -0.0526 | 0.0211 | 62.628 |

∂θ_B/∂p = −∂θ_A/∂p. Elasticidade usa θ_k do candidato favorecido pelo parâmetro.

| Comparecimento (+1 p.p. em τ) | ∂θ_A/∂τ (p.p. por p.p.) | eleitores adicionais |
|---|---|---|
| τ_A (coorte A) | +0.2085 | 538.766 |
| τ_B (coorte B) | -0.2030 | 561.043 |
| τ C:F | -0.0069 | 90.561 |
| τ G:L | +0.0002 | 2.607 |
| τ BN₁ | +0.0004 | 59.749 |
| τ ABS₁ | +0.0004 | 334.700 |
| +1 p.p. do ELEITORADO vindo de ABS₁ (pref. da coorte) | +0.0017 | 1.587.426 |

Tornado: cada parâmetro varrido no seu IC 90% a priori (pd, M2, DEFF=2), demais fixos na base (parcial):

| Parâmetro | faixa IC 90% (q) | θ_A no limite inf. | θ_A no limite sup. | amplitude (p.p.) |
|---|---|---|---|---|
| churn coorte A | 2.5 – 7.5 | 48.84% | 47.81% | 1.031 |
| churn coorte B | 2.5 – 7.5 | 47.85% | 48.85% | 1.001 |
| R_A (A₁→A) | 89.7 – 93.6 | 47.41% | 48.31% | 0.906 |
| X_BA (B₁→A) | 3.7 – 6.8 | 48.00% | 48.72% | 0.722 |
| R_B (B₁→B) | 93.0 – 96.2 | 48.73% | 48.04% | 0.688 |
| X_AB (A₁→B) | 3.6 – 6.8 | 48.67% | 48.01% | 0.662 |
| BN₁→B | 13.7 – 31.2 | 48.66% | 48.25% | 0.407 |
| BN₁→A | 10.5 – 26.8 | 47.98% | 48.39% | 0.405 |
| T_CB | 40.3 – 67.8 | 48.48% | 48.11% | 0.365 |
| T_CA | 15.4 – 39.8 | 48.07% | 48.42% | 0.348 |
| T_DB | 30.6 – 61.5 | 48.52% | 48.20% | 0.319 |
| T_EB | 39.3 – 70.5 | 48.52% | 48.21% | 0.314 |
| T_DA | 12.5 – 39.2 | 48.24% | 48.54% | 0.293 |
| T_EA | 8.6 – 33.2 | 48.19% | 48.45% | 0.265 |
| ABS₁→A | 29.6 – 38.4 | 48.07% | 48.31% | 0.238 |
| ABS₁→B | 37.4 – 46.5 | 48.51% | 48.28% | 0.231 |

#### H. Break-even (base: média posterior completa) — equações condicionais, NÃO previsões

| θ_A alvo | R_A (X_AB=5.0% fixo; máx 95.0%) | R_A com X_AB=0 | R_B (X_BA=5.2% fixo) | A entre válidos de C:F | X_BA (tirado de R_B) |
|---|---|---|---|---|---|
| 48% | 92.24% | 87.62% | inviável | 30.38% | 4.42% |
| 49% | inviável | 91.95% | 91.78% | 47.97% | 6.66% |
| 50% | inviável | 96.45% | 87.36% | 65.55% | 8.90% |
| 51% | inviável | inviável | 83.12% | 83.14% | 11.13% |
| 52% | inviável | inviável | 79.04% | inviável | 13.37% |

Valores da base: R_A = 93.89%, R_B = 94.66%, A entre válidos de C:F = 36.87%, X_BA = 5.25%, X_AB = 5.01%.

Novos comparecentes para zerar V_B − V_A = 3.882.453: N_válidos = (V_B − V_A)/(a − b); total = N_válidos/(1 − f_BN). f_BN = 16.7% (linha ABS da base).

| A:B dos novos | novos votos válidos | novos comparecentes | p.p. do eleitorado | % dos abstêmios do 1T |
|---|---|---|---|---|
| 50:50 | não fecha a diferença | — | — | — |
| 55:45 | 38.824.526 | 46.598.552 | 29.35 | 139.2% |
| 60:40 | 19.412.263 | 23.299.276 | 14.68 | 69.6% |
| 2:1 | 11.647.358 | 13.979.566 | 8.81 | 41.8% |
| 45:55 | não fecha a diferença | — | — | — |
| 40:60 | não fecha a diferença | — | — | — |
| 1:2 | não fecha a diferença | — | — | — |

| Combinação C:F | Valor |
|---|---|
| Votos que precisam passar de B para A (cada um reduz a diferença em 2) | 1.941.226 |
| Estoque de votos B em C:F | 4.272.486 |
| Fração uniforme do voto B de C:F que precisaria migrar | 45.4% |
| Só coorte C | 122.7% (inviável) |
| Só coorte D | 168.0% (inviável) |
| Só coorte E | 144.0% (inviável) |
| Só coorte F | 1035.7% (inviável) |

## D. Parâmetros associados a θ_B ≈ 50, 51, 52% (estrutural pd+df+qu)

Médias ponderadas condicionais a faixas de θ_B (±0,5 p.p.) entre os sorteios; diferença em relação à média geral indica quais parâmetros 'carregam' cada cenário.

| Parâmetro | média geral | θ_B≈50 | θ_B≈51 | θ_B≈52 |
|---|---|---|---|---|
| R_A | 91.73 | 92.75 (+0.84 dp) | 92.25 (+0.43 dp) | 91.69 (-0.03 dp) |
| X_AB | 5.08 | 4.20 (-0.91 dp) | 4.61 (-0.49 dp) | 5.10 (+0.02 dp) |
| R_B | 94.69 | 93.52 (-1.21 dp) | 94.20 (-0.51 dp) | 94.81 (+0.11 dp) |
| X_BA | 5.12 | 6.26 (+1.20 dp) | 5.61 (+0.52 dp) | 5.00 (-0.12 dp) |
| C:F→A | 26.50 | 28.05 (+0.53 dp) | 27.10 (+0.21 dp) | 26.41 (-0.03 dp) |
| C:F→B | 46.03 | 44.34 (-0.51 dp) | 45.36 (-0.21 dp) | 46.11 (+0.02 dp) |
| ABS→A | 38.64 | 39.01 (+0.17 dp) | 38.75 (+0.05 dp) | 38.65 (+0.00 dp) |
| ABS→B | 41.11 | 40.73 (-0.17 dp) | 40.94 (-0.08 dp) | 41.12 (+0.01 dp) |
| BN→A | 22.37 | 25.02 (+0.48 dp) | 23.58 (+0.22 dp) | 22.32 (-0.01 dp) |
| BN→B | 23.20 | 21.04 (-0.40 dp) | 22.00 (-0.22 dp) | 23.25 (+0.01 dp) |
| τ_A | 95.00 | 95.96 (+0.64 dp) | 95.54 (+0.36 dp) | 94.98 (-0.01 dp) |
| τ_B | 94.99 | 93.69 (-0.86 dp) | 94.46 (-0.35 dp) | 95.12 (+0.08 dp) |
| τ_ABS | 18.69 | 18.58 (-0.04 dp) | 18.70 (+0.00 dp) | 18.71 (+0.01 dp) |

Massa posterior (estrutural) em cada faixa: θ_B≈50: 4.6%, θ_B≈51: 26.5%, θ_B≈52: 46.4%

| Parâmetro | ∂θ_B/∂param (regressão) | parcela da var(θ_B) (β²·var) |
|---|---|---|
| X_AB | +0.3427 | 16.3% |
| X_BA | -0.3301 | 15.0% |
| τ_A | -0.2092 | 14.7% |
| τ_B | +0.2028 | 14.0% |
| BN→A | -0.0285 | 3.8% |
| BN→B | +0.0263 | 3.1% |
| C:F→A | -0.0429 | 2.3% |
| R_A | -0.0968 | 2.1% |
| C:F→B | +0.0355 | 2.1% |
| R_B | +0.1178 | 2.0% |
| ABS→A | -0.0279 | 0.5% |
| ABS→B | +0.0270 | 0.5% |
| τ_ABS | -0.0004 | 0.0% |

R² da regressão linear: 0.987.

## Sensibilidade a house effects (σ_house) — sinal não imposto

| σ_house (logit) | ≈ p.p. | θ_B pesquisas | dp (p.p.) | P(θ_B>0,5) pesquisas | E[θ_A] completo | P(θ_A>0,5) completo |
|---|---|---|---|---|---|---|
| 0.00 | ≈0.00 | 51.47% | 0.57 | 99.5% | 48.39% | 0.0% |
| 0.01 | ≈0.25 | 51.47% | 0.58 | 99.5% | 48.38% | 0.0% |
| 0.02 | ≈0.50 | 51.48% | 0.60 | 99.3% | 48.37% | 0.0% |
| 0.04 | ≈1.00 | 51.50% | 0.69 | 98.5% | 48.33% | 0.1% |
| 0.08 | ≈2.00 | 51.52% | 0.96 | 94.4% | 48.26% | 0.3% |

Viés comum a todos os institutos (h̄ ≠ 0) não é identificável só com pesquisas: com prior centrado em zero, ele entra como incerteza. Tabela: deslocamento sistemático hipotético δ (mesmo sinal para todos) aplicado ao nowcast.

| δ (logit) | Δθ_B (p.p.) | θ_B | P(θ_B>0,5) |
|---|---|---|---|
| -0.08 | -2.00 | 49.48% | 19.5% |
| -0.04 | -1.00 | 50.48% | 78.7% |
| -0.02 | -0.50 | 50.98% | 94.8% |
| +0.00 | +0.00 | 51.48% | 99.3% |
| +0.02 | +0.50 | 51.98% | 99.9% |
| +0.04 | +1.00 | 52.48% | 100.0% |
| +0.08 | +1.99 | 53.48% | 100.0% |

### Modelo completo: horizonte, deriva e viés comum

P(θ_A>0,5) e E[θ_A] do modelo completo (pd+df+qu+pesquisas) variando o horizonte H até a eleição, σ_drift e um viés comum hipotético δ (sinal NÃO escolhido: ambos os sinais mostrados).

| σ_drift | H (dias) | viés comum δ em θ_B | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|---|
| 0.01 | 0 | -0.04 (≈-1 p.p.) | 49.03% | 48.22% – 49.84% | 2.26% |
| 0.01 | 0 | +0.00 (≈+0 p.p.) | 48.37% | 47.59% – 49.18% | 0.04% |
| 0.01 | 0 | +0.04 (≈+1 p.p.) | 47.73% | 46.95% – 48.52% | 0.00% |
| 0.01 | 7 | -0.04 (≈-1 p.p.) | 48.75% | 47.76% – 49.76% | 2.00% |
| 0.01 | 7 | +0.00 (≈+0 p.p.) | 48.29% | 47.30% – 49.29% | 0.25% |
| 0.01 | 7 | +0.04 (≈+1 p.p.) | 47.85% | 46.87% – 48.83% | 0.02% |
| 0.01 | 14 | -0.04 (≈-1 p.p.) | 48.61% | 47.53% – 49.71% | 1.77% |
| 0.01 | 14 | +0.00 (≈+0 p.p.) | 48.25% | 47.18% – 49.35% | 0.41% |
| 0.01 | 14 | +0.04 (≈+1 p.p.) | 47.91% | 46.84% – 48.99% | 0.08% |
| 0.02 | 0 | -0.04 (≈-1 p.p.) | 48.95% | 47.99% – 49.91% | 3.50% |
| 0.02 | 0 | +0.00 (≈+0 p.p.) | 48.44% | 47.50% – 49.40% | 0.36% |
| 0.02 | 0 | +0.04 (≈+1 p.p.) | 47.95% | 47.01% – 48.89% | 0.02% |
| 0.02 | 7 | -0.04 (≈-1 p.p.) | 48.47% | 47.29% – 49.69% | 1.80% |
| 0.02 | 7 | +0.00 (≈+0 p.p.) | 48.26% | 47.07% – 49.46% | 0.82% |
| 0.02 | 7 | +0.04 (≈+1 p.p.) | 48.04% | 46.86% – 49.24% | 0.35% |
| 0.02 | 14 | -0.04 (≈-1 p.p.) | 48.34% | 47.10% – 49.61% | 1.50% |
| 0.02 | 14 | +0.00 (≈+0 p.p.) | 48.21% | 46.97% – 49.47% | 0.93% |
| 0.02 | 14 | +0.04 (≈+1 p.p.) | 48.07% | 46.83% – 49.32% | 0.56% |

## Peso intermediário da matriz pd, viés de recordação e eleição em 10 dias

Peso λ da matriz pd: α_g = λ·n_eff,g·m_g + 0,5 (equivale a DEFF_pd = 2/λ; df e qu mantêm DEFF=2). Viés de recordação: θ_A,estr ← θ_A,estr + b, b ~ N(0, σ_r²), sem sinal imposto (representa erro na lembrança/ponderação do voto do 1T que desloca a matriz como um todo). Pesquisas: σ_house=0,02, σ_extra=0,02, horizonte H=11 dias (eleição em 25/out). Configuração recomendada: λ=0.5, σ_r=0.5 p.p.

| λ (peso pd) | σ_r (p.p.) | estrutural: E[θ_A] [IC90] / P(θ_A>0,5) | completo, σ_drift=0,01: E [IC90] / P | completo, σ_drift=0,02: E [IC90] / P |
|---|---|---|---|---|
| 1.00 | 0.0 | 48.14% [46.8%; 49.5%] / 1.5% | 48.28% [47.23%; 49.35%] / **0.4%** (ESS 16.541) | 48.24% [47.00%; 49.51%] / **1.2%** (ESS 17.166) |
| 1.00 | 0.5 | 48.13% [46.5%; 49.7%] / 3.2% | 48.30% [47.16%; 49.45%] / **0.9%** (ESS 17.044) | 48.27% [46.87%; 49.69%] / **2.5%** (ESS 18.430) |
| 1.00 | 1.0 | 48.14% [46.0%; 50.3%] / 7.7% | 48.37% [47.06%; 49.70%] / **2.1%** (ESS 14.648) | 48.35% [46.59%; 50.11%] / **6.1%** (ESS 16.643) |
| 0.50 | 0.0 | 48.30% [46.6%; 50.0%] / 5.4% | 48.41% [47.20%; 49.61%] / **1.5%** (ESS 3.381) | 48.41% [46.94%; 49.92%] / **4.2%** (ESS 4.409) |
| 0.50 | 0.5 | 48.29% [46.4%; 50.2%] / 6.9% | 48.43% [47.15%; 49.69%] / **1.9%** (ESS 3.687) | 48.43% [46.79%; 50.03%] / **5.3%** (ESS 4.331) |
| 0.50 | 1.0 | 48.32% [45.9%; 50.7%] / 12.5% | 48.44% [47.08%; 49.82%] / **3.2%** (ESS 2.532) | 48.49% [46.64%; 50.37%] / **9.4%** (ESS 3.822) |
| 0.25 | 0.0 | 48.48% [46.2%; 50.8%] / 14.5% | 48.50% [47.15%; 49.89%] / **3.9%** (ESS 2.216) | 48.58% [46.77%; 50.38%] / **10.7%** (ESS 2.466) |
| 0.25 | 0.5 | 48.50% [46.0%; 51.0%] / 16.2% | 48.51% [47.13%; 49.91%] / **4.0%** (ESS 2.222) | 48.61% [46.72%; 50.49%] / **11.8%** (ESS 2.578) |
| 0.25 | 1.0 | 48.49% [45.7%; 51.4%] / 19.5% | 48.50% [47.04%; 49.99%] / **4.7%** (ESS 2.731) | 48.62% [46.55%; 50.65%] / **14.1%** (ESS 2.664) |

Referência λ=0 (só pesquisas nacionais, H=11):

| σ_drift | E[θ_A] | dp (p.p.) | P(θ_A>0,5) |
|---|---|---|---|
| 0.01 | 48.52% | 1.03 | 7.4% |
| 0.02 | 48.78% | 1.85 | 25.4% |

