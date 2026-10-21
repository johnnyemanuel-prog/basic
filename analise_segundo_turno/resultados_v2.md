# Resultados v2 — recalibração com dados até 21/10 (gerado por modelo_v2.py)

Semente 20261021; M = 1.000.000 sorteios. Eleição em 25/out; último campo 20/out (H = 5 dias).

## A. Auditoria de consistência dos dados novos

### A1. Pesquisas nacionais novas

| id | campo | n | Σ totais | B válido (calc.) | B válido (publ.) | calc − publ | MOE | MOE AAS | DEFF impl. | fonte da likelihood | σ_j válido (p.p.) | mesmo levant. tem cruzamentos? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qu-r2 | 17–20/10† | 2154 | 100% | 50.56% | ND | — | 2.0 | 2.11 | 0.90 ⚠ | totais | 1.16 | sim |
| fu-r1 | 18–20/10† | 2000 | ND | — | 51.1% | — | 2.2 | 2.19 | 1.01 | válidos publicados | 1.16 | não |
| pv-r2 | 18–20/10 | 5000 | 99% ⚠ | 51.02% | ND | — | 2.4 | 1.39 | 3.00 | totais | 1.25 | sim |
| mi-r1 | 17–19/10† | 1500 | 100% | 51.06% | 51.1% | -0.04 | 2.5 | 2.53 | 0.98 | totais | 1.35 | não |
| rt-r1 | 17–19/10† | 2000 | 100% | 51.61% | 52% | -0.39 | 2.0 | 2.19 | 0.83 ⚠ | totais | 1.18 | não |
| at-r2 | 13–18/10† | 4998 | 100% | 51.13% | 51.1% | +0.03 | 1.0 | 1.39 | 0.52 ⚠ | totais | 0.72 | não |
| nx-r2 | 16–18/10† | 2002 | 100% | 50.32% | 50.3% | +0.02 | 2.0 | 2.19 | 0.83 ⚠ | totais | 1.16 | não |
| pd-r2 | 16–18/10† | 3000 | 101% ⚠ | 51.58% | 52% | -0.42 | 1.8 | 1.79 | 1.01 | totais | 0.97 | não |

† Data de início do campo NÃO informada; janela suposta = duração da rodada anterior do instituto (qu 4 dias, at 6, nx/pd 3) ou 3 dias (fu, mi, rt). pv: 18–20/10 informado na divulgação de transferências. Sensibilidade com janela de 1 dia (só último dia) na seção E.

- Uma única likelihood por levantamento: binomial (logit) da fração B/(A+B). Quando os totais existem, ela é calculada deles (mais resolução) e os válidos publicados servem só como checagem; fu só tem válidos (1 decimal) → σ usa a razão média (A+B) das novas (94.0%) como denominador, por falta do dado.
- at-r2: MOE ±1,0 continua abaixo da AAS (±1,39) → usa-se ±1,39 (mesma regra do v1). BN+NS = 2,6 agregados, não desagregados.
- pv-r2 soma 99% e pd-r2 soma 101%: diferenças de arredondamento preservadas; a fração B/(A+B) não depende delas. Arredondamento de ±0,5 p.p. em A e B entra em σ_j.
- rt e pd: válidos publicados inteiros (52) vs calculados (51,61 / 51,58): compatíveis com arredondamento; usa-se o calculado.

### A2. Transferências novas

| rodada | coorte | A / B / BN-não vota / NS | Σ | margem subgrupo | n efetivo implícito | n esperado (2154 × peso eleitoral) | DEFF implícito |
|---|---|---|---|---|---|---|---|
| qu-r1 | C | 34 / 30 / 30 / 6 | 100% | ±17 | 33 | 47 | 1.41 |
| qu-r1 | D | 14 / 40 / 43 / 3 | 100% | ±20 | 24 | 36 | 1.51 |
| qu-r1 | E | 23 / 42 / 33 / 2 | 100% | ±24 | 17 | 35 | 2.12 |
| qu-r1 | X | 43 / 38 / 17 / 2 | 100% | ±6 | 267 | 535 | 2.01 |
| qu-r2 | C | 48 / 33 / 16 / 3 | 100% | ±17 | 33 | 47 | 1.41 |
| qu-r2 | D | 25 / 51 / 24 / 0 | 100% | ±20 | 24 | 36 | 1.51 |
| qu-r2 | E | 21 / 57 / 22 / 0 | 100% | ±24 | 17 | 35 | 2.12 |
| qu-r2 | X | 40 / 36 / 21 / 3 | 100% | ±6 | 267 | 535 | 2.01 |

| rodada | coorte | A / B / restante | Σ | n esperado | n efetivo (DEFF pv = 3.00) |
|---|---|---|---|---|---|
| pv-r2 | C | 52 / 43 / 5 (não discriminado) | 100% | 109 | 36 |
| pv-r2 | D | 39 / 42 / 19 (não discriminado) | 100% | 84 | 28 |
| pv-r2 | E | 44 / 44 / 12 (não discriminado) | 100% | 82 | 27 |

- qu publicou em 21/10 a decomposição completa da rodada 13/10 (antes só A e B). Ela é dado divulgado, não imputação: no v2 a rodada qu-r1 entra com as 4 categorias.
- qu: 'BN/não vota' é mapeado na categoria BN do modelo (intenção de não escolher A nem B); a separação BN × abstenção não é identificável nesses dados.
- pv: 'restante' (5/19/12) entra como categoria agregada {BN, NS, não vota}, sem decompor.
- n efetivo de qu vem da margem de cada subgrupo (n = 0,25·(1,96/MOE)²), não da margem geral. Os DEFF implícitos (1,4–2,1) são coerentes com o DEFF 2 usado no v1.
- As diferenças entre rodadas qu (ex.: C→A 34 → 48) NÃO são tratadas como migração individual: são duas amostras transversais; entram como duas observações da mesma margem de transição, cada uma com sua data.

### A3. Comparecimento declarado, estabilidade e rejeição (camada descritiva)

| fonte | medida | valor | uso no modelo |
|---|---|---|---|
| nx-r2 | certeza de comparecer / provável / provável não ou não / não discriminado | 85,9 / 7,0 / 5,4 / 1,7 | descritivo; Σ declarada ≫ comparecimento real do 1T (78,9%) |
| nx-r2 | convictos de A / de B que declaram que vão votar | 95,0% / 91,6% | sensibilidade κ (seção C); não é probabilidade calibrada |
| nx-r2 | rejeitam ambos: certeza / provável / provável não / não vota | 70,9 / 13,4 / 5,2 / 10,4 | descritivo (Σ = 99,9%) |
| mi-r1 | voto decidido / pode mudar | 83,7% / 16,3% | descritivo |
| pv-r2 | nada me faria mudar | 79% | descritivo; pergunta diferente da de mi |
| qu-r2 | espontânea A / B / indecisos | 40 / 40 / 14 | descritivo; ≠ estimulada (44/45) |
| qu | rejeição A / B (r1 → r2) | 53→47 / 54→52 | descritivo |
| mi-r1 | rejeição A / B | 47,7 / 46,5 | descritivo |

- A soma das categorias de nx (85,9+7,0+5,4 = 98,3%) deixa 1,7% não discriminados; mantido.
- Rejeição, estabilidade e espontânea não entram na likelihood (instrução: não são observações independentes da intenção nem transferências).

## D. Diferenças de mensuração entre institutos e evolução temporal

### D1. Rodadas repetidas do mesmo instituto (diferença bruta, sem atribuir causa)

| instituto | rodadas | θ_B antes | θ_B depois | Δ (p.p.) | z (só amostragem) |
|---|---|---|---|---|---|
| df | df-r1 (7/10) → df-r2 (14/10) | 52.13% | 51.09% | -1.04 | -0.68 |
| qu | qu-r1 (13/10) → qu-r2 (20/10) | 51.11% | 50.56% | -0.55 | -0.33 |
| pd | pd-r1 (12/10) → pd-r2 (18/10) | 51.06% | 51.58% | +0.52 | +0.38 |
| nx | nx-r1 (12/10) → nx-r2 (18/10) | 51.61% | 50.32% | -1.29 | -0.78 |
| at | at-r1 (8/10) → at-r2 (18/10) | 52.79% | 51.13% | -1.66 | -1.64 |
| pv | pv-r1 (13/10) → pv-r2 (20/10) | 50.51% | 51.02% | +0.52 | +0.30 |

Maior |z| = 1.64 (at, campo mais antigo na 1ª rodada): todas as variações são compatíveis com erro amostral isolado (|z| < 1,96). Sem atribuição de causa.

### D2. Tendência latente (todas as pesquisas; σ_drift 0,01, σ_house 0,02, σ_extra 0,02)

| dia | θ_B latente | dp (p.p.) |
|---|---|---|
| 4/10 | 51.92% | 0.64 |
| 6/10 | 51.87% | 0.57 |
| 8/10 | 51.74% | 0.53 |
| 10/10 | 51.56% | 0.49 |
| 12/10 | 51.40% | 0.46 |
| 14/10 | 51.30% | 0.46 |
| 16/10 | 51.23% | 0.45 |
| 18/10 | 51.20% | 0.46 |
| 20/10 | 51.19% | 0.55 |

Previsão para 25/10 (H = 5): θ_B = 51.19% ± 0.78 p.p. → θ_A = 48.81%.

### D3. House effects posteriores (prior N(0; 0,02²) sem sinal)

| instituto | rodadas | h_j ≈ p.p. em θ_B | dp (p.p.) | h/σ_house | identificação |
|---|---|---|---|---|---|
| df | 2 | -0.01 | 0.45 | -0.02 | parcial |
| qu | 2 | -0.07 | 0.47 | -0.14 | parcial |
| pd | 2 | +0.02 | 0.44 | +0.04 | parcial |
| nx | 2 | -0.09 | 0.45 | -0.18 | parcial |
| at | 2 | +0.16 | 0.42 | +0.32 | parcial |
| ip | 1 | +0.09 | 0.48 | +0.18 | fraco (1 rodada) |
| pv | 2 | -0.12 | 0.46 | -0.25 | parcial |
| fu | 1 | -0.01 | 0.47 | -0.02 | fraco (1 rodada) |
| mi | 1 | -0.01 | 0.47 | -0.03 | fraco (1 rodada) |
| rt | 1 | +0.05 | 0.47 | +0.11 | fraco (1 rodada) |

### D4. Calibração anterior × atual (bloco de pesquisas)

| versão | pesquisas | tempera dependência? | θ_B em 25/10 | dp (p.p.) | P(θ_B>0,5) |
|---|---|---|---|---|---|
| v1 (até 14/10) | 8 | não | 51.48% | 1.03 | 92.6% |
| v1 dados + regra v2 | 8 | sim | 51.54% | 1.04 | 93.0% |
| v2 (até 20/10) | 16 | sim | 51.19% | 0.78 | 93.5% |

## E. Resíduos e verificações preditivas das pesquisas

| pesquisa | θ_B obs. | previsto (nível comum) | resíduo (p.p.) | r_j | previsto LOO | r_j LOO |
|---|---|---|---|---|---|---|
| df-r1 | 52.13% | 51.99% | +0.13 | +0.09 | 51.77% | +0.20 |
| df-r2 | 51.09% | 51.34% | -0.25 | -0.23 | 51.38% | -0.21 |
| qu-r1 | 51.11% | 51.49% | -0.37 | -0.23 | 51.41% | -0.16 |
| pd-r1 | 51.06% | 51.53% | -0.46 | -0.34 | 51.58% | -0.32 |
| nx-r1 | 51.61% | 51.53% | +0.09 | +0.07 | 51.33% | +0.20 |
| at-r1 | 52.79% | 52.02% | +0.76 | +1.07 | 51.46% | +1.16 |
| ip-r1 | 52.69% | 51.95% | +0.74 | +0.53 | 51.70% | +0.60 |
| pv-r1 | 50.51% | 51.49% | -0.98 | -0.82 | 51.53% | -0.70 |
| qu-r2 (nova) | 50.56% | 51.20% | -0.64 | -0.39 | 51.21% | -0.35 |
| fu-r1 (nova) | 51.10% | 51.19% | -0.09 | -0.08 | 51.20% | -0.07 |
| pv-r2 (nova) | 51.02% | 51.19% | -0.17 | -0.10 | 51.07% | -0.03 |
| mi-r1 (nova) | 51.06% | 51.20% | -0.14 | -0.10 | 51.21% | -0.09 |
| rt-r1 (nova) | 51.61% | 51.20% | +0.41 | +0.35 | 51.15% | +0.32 |
| at-r2 (nova) | 51.13% | 51.27% | -0.14 | -0.20 | 51.54% | -0.39 |
| nx-r2 (nova) | 50.32% | 51.22% | -0.90 | -0.77 | 51.32% | -0.70 |
| pd-r2 (nova) | 51.58% | 51.22% | +0.36 | +0.37 | 51.12% | +0.37 |

Σ r_j² = 3.39 com ≈15 g.l.; p ≈ 0.999; razão de dispersão = 0.23.

Perfil de σ_extra (σ_house≈0): máximo em 0.000 logit (≈0.00 p.p.).

### E2. Verificação preditiva fora da amostra: pesquisas até 14/10 preveem as novas?

| nova pesquisa | θ_B obs. | previsto pelo v1 (com deriva) | z |
|---|---|---|---|
| qu-r2 | 50.56% | 51.50% | -0.48 |
| fu-r1 | 51.10% | 51.54% | -0.28 |
| pv-r2 | 51.02% | 51.40% | -0.18 |
| mi-r1 | 51.06% | 51.54% | -0.28 |
| rt-r1 | 51.61% | 51.54% | +0.05 |
| at-r2 | 51.13% | 51.75% | -0.54 |
| nx-r2 | 50.32% | 51.54% | -0.80 |
| pd-r2 | 51.58% | 51.48% | +0.07 |

Média dos z = -0.30; todos |z| < 0.80. As novas pesquisas ficam do lado de A em relação à previsão do v1, mas dentro da incerteza prevista (que já incluía deriva).

### E3. Sensibilidade do bloco de pesquisas (25/10)

| variação | θ_B | dp (p.p.) | P(θ_B>0,5) só pesquisas |
|---|---|---|---|
| caso-base | 51.19% | 0.78 | 93.5% |
| janela = só último dia | 51.19% | 0.74 | 94.6% |
| sem temperar dependência | 51.15% | 0.77 | 93.3% |
| σ_house 0,04 | 51.19% | 0.83 | 92.4% |
| σ_extra 0 | 51.17% | 0.77 | 93.6% |
| σ_drift 0,005 | 51.31% | 0.51 | 99.5% |
| σ_drift 0,02 | 51.10% | 1.36 | 79.1% |

## B. Retenção e transferência atualizadas (alvo: 25/10)

Modelo 2 com datas: n_eff de cada observação = 1/(1/n + Δt·σ_q²/0,25), σ_q = 0.005 por √dia; matriz pd com peso λ = 0.5; levantamentos com cruzamento + resultado geral entram com potência 0.5 em cada parte; indecisos III; viés de recordação σ_r = 0.5 p.p. ESS: transferências 69.365, completo 43.551.

Observações de transferência e n efetivo usado (após tempera e desconto temporal):

| observação | data (dia) | n efetivo |
|---|---|---|
| pd-matriz B | 11.0 | 193.3 |
| pd-matriz A | 11.0 | 187.7 |
| pd-matriz C | 11.0 | 15.9 |
| pd-matriz D | 11.0 | 12.4 |
| pd-matriz E | 11.0 | 12.1 |
| pd-matriz F | 11.0 | 1.5 |
| pd-matriz GL | 11.0 | 1.2 |
| pd-matriz BN | 11.0 | 27.2 |
| pd-matriz ABS | 11.0 | 129.5 |
| df C:F | 6.5 | 33.7 |
| qu-r1 C | 11.5 | 16.3 |
| qu-r1 D | 11.5 | 11.8 |
| qu-r1 E | 11.5 | 8.2 |
| qu-r1 X | 11.5 | 113.0 |
| qu-r2 C | 18.5 | 16.4 |
| qu-r2 D | 18.5 | 11.9 |
| qu-r2 E | 18.5 | 8.3 |
| qu-r2 X | 18.5 | 122.7 |
| pv-r2 C | 19.0 | 17.9 |
| pv-r2 D | 19.0 | 13.9 |
| pv-r2 E | 19.0 | 13.6 |

| parâmetro (% , média [IC 90%]) | só pd (com datas) | pd + df + qu + pv | completo (+ pesquisas) |
|---|---|---|---|
| R_A = A₁→A | 91.3 [87.7; 94.4] | 91.3 [87.7; 94.4] | 91.6 [88.4; 94.4] |
| X_AB = A₁→B | 5.2 [2.9; 8.1] | 5.2 [2.9; 8.1] | 5.0 [2.9; 7.4] |
| R_B = B₁→B | 94.2 [91.3; 96.7] | 94.2 [91.3; 96.7] | 94.2 [91.6; 96.4] |
| X_BA = B₁→A | 5.3 [2.9; 8.1] | 5.3 [2.9; 8.1] | 5.3 [3.2; 7.8] |
| C→A | 26.8 [11.6; 44.9] | 40.1 [30.9; 49.7] | 40.3 [31.0; 49.9] |
| C→B | 52.5 [33.5; 71.3] | 40.2 [30.9; 49.7] | 40.1 [30.8; 49.6] |
| D→A | 24.8 [8.9; 44.8] | 26.3 [17.0; 36.5] | 26.4 [17.1; 36.5] |
| D→B | 44.4 [24.0; 65.7] | 44.8 [33.9; 55.9] | 44.7 [33.9; 55.8] |
| E→A | 20.0 [5.8; 39.2] | 28.1 [18.0; 39.3] | 28.3 [18.0; 39.4] |
| E→B | 52.9 [31.5; 73.9] | 49.4 [37.5; 61.4] | 49.3 [37.4; 61.3] |
| F→A | 18.5 [0.3; 56.6] | 18.1 [0.3; 55.7] | 18.1 [0.3; 56.1] |
| F→B | 45.5 [9.2; 84.9] | 45.0 [9.0; 84.5] | 44.9 [8.9; 84.5] |
| G:L→A | 30.3 [2.1; 73.2] | 30.4 [2.1; 73.3] | 30.5 [2.1; 73.6] |
| G:L→B | 22.7 [0.6; 64.2] | 22.6 [0.6; 64.1] | 22.5 [0.6; 63.8] |
| C:F agregado →A | 24.0 [14.8; 34.2] | 31.8 [26.6; 37.2] | 31.9 [26.8; 37.2] |
| C:F agregado →B | 50.0 [38.6; 61.3] | 44.4 [38.7; 50.0] | 44.3 [38.7; 49.9] |
| X (BN₁+ABS₁) →A | 31.5 [25.6; 37.6] | 37.3 [33.4; 41.4] | 37.4 [33.5; 41.4] |
| X →B | 38.8 [32.6; 45.1] | 37.6 [33.6; 41.6] | 37.5 [33.6; 41.5] |
| X →BN/não vota | 23.0 [17.9; 28.5] | 20.8 [17.6; 24.2] | 20.8 [17.6; 24.2] |
| θ_A (válidos) | 47.6 [45.4; 49.8] | 48.5 [46.4; 50.6] | 48.7 [47.6; 49.8] |

Linhas q_g = intenção declarada normalizada, antes de indecisos e comparecimento.

### B2. Identificação: quanto cada fonte estreitou cada parâmetro

| parâmetro | dp só pd (p.p.) | dp + transferências | dp completo | razão completo/pd | identificação |
|---|---|---|---|---|---|
| R_A = A₁→A | 2.04 | 2.04 | 1.83 | 0.89 | insuficiente |
| X_AB = A₁→B | 1.61 | 1.61 | 1.37 | 0.85 | insuficiente |
| R_B = B₁→B | 1.66 | 1.66 | 1.48 | 0.89 | insuficiente |
| X_BA = B₁→A | 1.59 | 1.59 | 1.40 | 0.88 | insuficiente |
| C→A | 10.17 | 5.69 | 5.69 | 0.56 | boa |
| C→B | 11.47 | 5.70 | 5.69 | 0.50 | boa |
| D→A | 10.99 | 5.91 | 5.93 | 0.54 | boa |
| D→B | 12.64 | 6.65 | 6.64 | 0.53 | boa |
| E→A | 10.30 | 6.51 | 6.50 | 0.63 | parcial |
| E→B | 12.85 | 7.27 | 7.25 | 0.56 | boa |
| F→A | 18.21 | 17.92 | 18.00 | 0.99 | insuficiente |
| F→B | 23.35 | 23.29 | 23.34 | 1.00 | insuficiente |
| G:L→A | 22.33 | 22.36 | 22.46 | 1.01 | insuficiente |
| G:L→B | 20.34 | 20.29 | 20.20 | 0.99 | insuficiente |
| C:F agregado →A | 5.89 | 3.20 | 3.17 | 0.54 | boa |
| C:F agregado →B | 6.89 | 3.46 | 3.42 | 0.50 | boa |
| X (BN₁+ABS₁) →A | 3.64 | 2.42 | 2.41 | 0.66 | parcial |
| X →B | 3.81 | 2.41 | 2.40 | 0.63 | parcial |
| X →BN/não vota | 3.21 | 2.00 | 2.00 | 0.62 | parcial |
| θ_A (válidos) | 1.36 | 1.28 | 0.66 | 0.49 | boa |

### B3. Verificação preditiva das observações de transferência (modelo completo)

| observação | → | observado | previsto (completo) | z preditivo |
|---|---|---|---|---|
| pd-matriz B | A | 5% | 5.3% | -0.13 |
| pd-matriz B | B | 95% | 94.2% | +0.37 |
| pd-matriz A | A | 92% | 91.6% | +0.16 |
| pd-matriz A | B | 5% | 5.0% | +0.02 |
| pd-matriz C | A | 27% | 40.3% | -1.06 |
| pd-matriz C | B | 56% | 40.1% | +1.17 |
| pd-matriz D | A | 25% | 26.4% | -0.12 |
| pd-matriz D | B | 48% | 44.7% | +0.18 |
| pd-matriz E | A | 19% | 28.3% | -0.69 |
| pd-matriz E | B | 58% | 49.3% | +0.52 |
| pd-matriz F | A | 10% | 18.1% | -0.27 |
| pd-matriz F | B | 72% | 44.9% | +0.63 |
| pd-matriz GL | A | 39% | 30.5% | +0.17 |
| pd-matriz GL | B | 19% | 22.5% | -0.09 |
| pd-matriz BN | A | 18% | 23.0% | -0.49 |
| pd-matriz BN | B | 22% | 22.7% | -0.08 |
| pd-matriz ABS | A | 34% | 40.0% | -1.17 |
| pd-matriz ABS | B | 42% | 40.1% | +0.36 |
| df C:F | A | 32% | 31.9% | +0.01 |
| df C:F | B | 46% | 44.3% | +0.19 |
| qu-r1 C | A | 34% | 40.3% | -0.48 |
| qu-r1 C | B | 30% | 40.1% | -0.79 |
| qu-r1 D | A | 14% | 26.4% | -1.06 |
| qu-r1 D | B | 40% | 44.7% | -0.30 |
| qu-r1 E | A | 23% | 28.3% | -0.33 |
| qu-r1 E | B | 42% | 49.3% | -0.39 |
| qu-r1 X | A | 43% | 37.4% | +1.07 |
| qu-r1 X | B | 38% | 37.5% | +0.10 |
| qu-r2 C | A | 48% | 40.3% | +0.57 |
| qu-r2 C | B | 33% | 40.1% | -0.55 |
| qu-r2 D | A | 25% | 26.4% | -0.10 |
| qu-r2 D | B | 51% | 44.7% | +0.39 |
| qu-r2 E | A | 21% | 28.3% | -0.47 |
| qu-r2 E | B | 57% | 49.3% | +0.41 |
| qu-r2 X | A | 40% | 37.4% | +0.52 |
| qu-r2 X | B | 36% | 37.5% | -0.30 |
| pv-r2 C | A | 52% | 40.3% | +0.90 |
| pv-r2 C | B | 43% | 40.1% | +0.23 |
| pv-r2 D | A | 39% | 26.4% | +0.88 |
| pv-r2 D | B | 42% | 44.7% | -0.18 |
| pv-r2 E | A | 44% | 28.3% | +1.05 |
| pv-r2 E | B | 44% | 49.3% | -0.34 |

Máximo |z| = 1.17; 0 de 42 com |z| > 2.

## Probabilidades atualizadas (25/10)

**Caso-base v2:** E[θ_A] = 48.72% [IC 90% 47.62% – 49.81%]; **P(θ_A > 0,5) = 2.7%**.

| σ_drift | σ_r (p.p.) | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|---|
| 0.005 | 0.0 | 48.66% | 47.89% – 49.43% | 0.2% | 18.124 |
| 0.005 | 0.5 | 48.66% | 47.88% – 49.44% | 0.2% | 32.695 |
| 0.005 | 1.0 | 48.67% | 47.88% – 49.47% | 0.3% | 8.704 |
| 0.010 | 0.0 | 48.71% | 47.64% – 49.79% | 2.4% | 20.395 |
| 0.010 | 0.5 | 48.72% | 47.62% – 49.81% | 2.7% | 43.551 |
| 0.010 | 1.0 | 48.75% | 47.60% – 49.90% | 3.7% | 12.915 |
| 0.020 | 0.0 | 48.66% | 47.20% – 50.13% | 6.6% | 21.765 |
| 0.020 | 0.5 | 48.68% | 47.16% – 50.21% | 7.7% | 57.615 |
| 0.020 | 1.0 | 48.71% | 47.04% – 50.38% | 10.3% | 23.307 |

Sensibilidade às hipóteses estruturais (σ_drift 0,01; σ_r 0,5 p.p.):

| variação | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|
| λ_pd = 1 | 48.64% | 47.59% – 49.67% | 1.5% | 29.421 |
| λ_pd = 0,25 | 48.78% | 47.63% – 49.93% | 4.1% | 7.491 |
| σ_q = 0,0025 | 48.71% | 47.65% – 49.77% | 2.4% | 15.471 |
| σ_q = 0,01 | 48.74% | 47.60% – 49.89% | 3.6% | 26.825 |
| sem temperar dependência | 48.74% | 47.64% – 49.85% | 3.2% | 3.857 |
| sem qu-r1/df (só observações ≥ 18/10 + pd) | 48.70% | 47.61% – 49.80% | 2.6% | 108.773 |
| sem pv-r2 | 48.67% | 47.57% – 49.77% | 2.4% | 19.056 |
| só pesquisas (sem estrutural) | 48.81% | 47.53% – 50.10% | 6.5% | — |

## C. Sensibilidade às hipóteses de comparecimento

κ = fração do diferencial DECLARADO (nx: convictos A 95,0% × B 91,6%) que se converte em diferencial EFETIVO de comparecimento entre votantes de A e de B, aplicado após a ponderação pelas pesquisas (as pesquisas medem intenção, não comparecimento). κ = 0 é a hipótese do v1 (churn simétrico). Os 'convictos' são subconjuntos; estender a todos os eleitores é suposição.

| κ | diferencial efetivo A − B (relativo) | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|
| 0.00 | 0.00 p.p. | 48.72% | 47.62% – 49.81% | 2.7% |
| 0.25 | 0.91 p.p. | 48.95% | 47.85% – 50.04% | 5.6% |
| 0.50 | 1.82 p.p. | 49.18% | 48.07% – 50.27% | 10.6% |
| 1.00 | 3.64 p.p. | 49.63% | 48.53% – 50.72% | 28.9% |

Diferença média V_B − V_A (completo, κ=0) = 3.041.411 votos; linha ABS posterior: A entre válidos = 49.9%, BN = 17.2%.

Comparecimento total (variação dos faltantes do 1T, em p.p. do eleitorado) × divisão A:B dos faltantes adicionais; célula = E[θ_A] / P(θ_A>0,5), modelo completo, κ = 0:

| comparecimento | linha ABS posterior | 50:50 | 55:45 | 60:40 | 2:1 |
|---|---|---|---|---|---|
| -2 p.p. | 48.69% / 2.7% | 48.69% / 2.7% | 48.58% / 1.9% | 48.47% / 1.2% | 48.31% / 0.7% |
| -1 p.p. | 48.71% / 2.7% | 48.71% / 2.7% | 48.65% / 2.2% | 48.59% / 1.9% | 48.52% / 1.4% |
| = 1º turno | 48.72% / 2.7% | 48.72% / 2.7% | 48.72% / 2.7% | 48.72% / 2.7% | 48.72% / 2.7% |
| +1 p.p. | 48.73% / 2.7% | 48.73% / 2.7% | 48.79% / 3.3% | 48.84% / 4.0% | 48.92% / 4.9% |
| +2 p.p. | 48.75% / 2.7% | 48.75% / 2.7% | 48.86% / 4.0% | 48.96% / 5.5% | 49.11% / 8.5% |
| +3 p.p. | 48.76% / 2.7% | 48.76% / 2.7% | 48.92% / 4.7% | 49.08% / 7.7% | 49.30% / 13.6% |
| +5 p.p. | 48.78% / 2.6% | 48.79% / 2.7% | 49.05% / 6.5% | 49.31% / 13.6% | 49.66% / 29.5% |

## Fronteira de virada recalibrada

X_AB = 5.07%, X_BA = 5.34% (médias posteriores; ainda baseadas apenas na matriz pd de ~11/10, agora com incerteza temporal maior). X_BA necessário = 3.32% + 0.962 × X_AB.

| X_AB | X_BA necessário | Δ vs atual |
|---|---|---|
| 0.0% | 3.32% | -2.02 |
| 1.0% | 4.28% | -1.06 |
| 2.0% | 5.25% | -0.10 |
| 3.0% | 6.21% | +0.86 |
| 4.0% | 7.17% | +1.82 |
| 5.0% | 8.13% | +2.79 |
| 5.1% (atual) | 8.20% | +2.85 |
| 6.0% | 9.09% | +3.75 |
| 7.0% | 10.05% | +4.71 |

Ponto mais provável sobre a fronteira (só troca de votos): X_BA = 6.86%, X_AB = 3.68%; distância ≈ 1.48 dp (dp X_BA 1.40, dp X_AB 1.37 p.p.).

