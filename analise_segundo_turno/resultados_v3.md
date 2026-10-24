# Resultados v3 — recalibração com dados até 23/10 (gerado por modelo_v3.py)

Semente 20261023; M = 1.000.000 sorteios. Eleição em 25/out; último campo 22/out (H = 3 dias).

## A. Auditoria de consistência dos dados novos

### A1. Pesquisas nacionais novas

| id | campo | n | Σ totais | B válido (calc.) | B válido (publ.) | calc − publ | MOE | MOE AAS | DEFF impl. | fonte da likelihood | σ_j válido (p.p.) | mesmo levant. tem cruzamentos? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| df-r3 | 20–22/10 | 2520 | 100% | 50.54% | 50.47% | +0.07 | 2.00* | 1.95 | 1.05 | totais | 1.08 | sim |
| pd-r3 | 19–21/10 | 4000 | 101% ⚠ | 50.52% | 51% | -0.48 | 1.56* | 1.55 | 1.01 | totais | 0.83 | sim |

* Margem NÃO informada para df-r3 e pd-r3: usa-se a margem AAS do n informado × √DEFF implícito da rodada anterior do instituto (df 1,05; pd 1,01). Datas de campo informadas.
- Duplicidade evitada: só B/(A+B) dos totais entra; os válidos publicados (df 50,47; pd 51) são checagem. df: 47/93 = 50,54% vs 50,47% publicado (≤ 0,07 p.p., arredondamento dos totais).
- Pedido de adicionar vx, ip, ve, al e rt 'da tabela anterior': ip (6–8/10, id ip-r1) e rt (17–19/10, id rt-r1) JÁ estão no modelo e não são duplicados. vx, ve e al NÃO constam de nenhuma tabela recebida: sem dados, não foram incluídos nem imputados.

Rodadas v2 (já incorporadas em 21/10), para referência: qu-r2, fu-r1, pv-r2, mi-r1, rt-r1, at-r2, nx-r2, pd-r2.

† (v2) Data de início do campo NÃO informada; janela suposta = duração da rodada anterior do instituto (qu 4 dias, at 6, nx/pd 3) ou 3 dias (fu, mi, rt). pv: 18–20/10 informado na divulgação de transferências. Sensibilidade com janela de 1 dia (só último dia) na seção E.

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

### A2b. Transferências novas de 23/10 (pd-r3 e df-r3)

| rodada | coorte | A / B / BN / NS | Σ | n efetivo antes de tempera/data (DEFF_sub = 2) |
|---|---|---|---|---|
| pd-r3 | A | 95 / 4 / resto 1 | 100% | 679 |
| pd-r3 | B | 3 / 96 / resto 1 | 100% | 707 |
| pd-r3 | C | 48 / 42 / 8 / 2 | 100% | 43 |
| pd-r3 | D | 34 / 49 / 17 / 1 | 101% (arred.) | 34 |
| pd-r3 | E | 30 / 49 / 20 / 1 | 100% | 33 |
| pd-r3 | BN | 46 / 23 / 7 / 24 | 100% | 75 |
| pd-r3 | ABS | 48 / 39 / 11 / 3 | 101% (arred.) | 422 |
| pd-r3 | F:L | 20 / 70 / 6 / 4 | 100% | 7.4 |
| df-r3 | C:F | 26 / 47 / 21 / 6 | 100% | 72 |

- pd-r3 A e B: 'retenção declarada' (A→A 95, B→B 96) com 'migração direta' (A→B 4, B→A 3): cada linha soma 99%; o 1% restante entra como categoria não discriminada (BN+NS), sem imputação.
- Retenção ≠ voto firme: 95/96% é a fração da coorte do 1T que declara o mesmo voto agora, não a fração com voto 'decidido' (mi 83,7%, pv 79% seguem só descritivos).
- pd-r3 D e ABS somam 101% (arredondamento): normalizados. F:L é agregado de F e G:L → entra como mistura ponderada por votos, como df C:F.
- BN₁ (pd-r3): 46/23/7/24 — 24% NS. A diferença para pd-r1 (18/22/47/14) é grande, mas o subgrupo tem n efetivo ≈ 75 e são amostras diferentes: duas observações, nenhuma migração inferida.
- Subamostras com erro adicional: DEFF_sub = 2 sobre n × peso eleitoral, potência 0,5 por dependência com o resultado geral do mesmo levantamento e desconto temporal σ_q²·Δt.

### A3. Comparecimento declarado, estabilidade e rejeição (camada descritiva)

| fonte | medida | valor | uso no modelo |
|---|---|---|---|
| nx-r2 | certeza de comparecer / provável / provável não ou não / não discriminado | 85,9 / 7,0 / 5,4 / 1,7 | descritivo; Σ declarada ≫ comparecimento real do 1T (78,9%) |
| nx-r2 | convictos de A / de B que declaram que vão votar | 95,0% / 91,6% | sensibilidade κ (seção C); não é probabilidade calibrada |
| nx-r2 | rejeitam ambos: certeza / provável / provável não / não vota | 70,9 / 13,4 / 5,2 / 10,4 | descritivo (Σ = 99,9%) |
| pd-r3 | certeza / talvez / não vai / NS | 95 / 3 / 1 / 1 | descritivo; 98% declarado ≫ 78,9% real do 1T (comparecimento separado da intenção) |
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
| df | df-r2 (14/10) → df-r3 (22/10) | 51.09% | 50.54% | -0.55 | -0.36 |
| qu | qu-r1 (13/10) → qu-r2 (20/10) | 51.11% | 50.56% | -0.55 | -0.33 |
| pd | pd-r1 (12/10) → pd-r2 (18/10) | 51.06% | 51.58% | +0.52 | +0.38 |
| pd | pd-r2 (18/10) → pd-r3 (21/10) | 51.58% | 50.52% | -1.06 | -0.83 |
| nx | nx-r1 (12/10) → nx-r2 (18/10) | 51.61% | 50.32% | -1.29 | -0.78 |
| at | at-r1 (8/10) → at-r2 (18/10) | 52.79% | 51.13% | -1.66 | -1.64 |
| pv | pv-r1 (13/10) → pv-r2 (20/10) | 50.51% | 51.02% | +0.52 | +0.30 |

Maior |z| = 1.64: todas as variações entre rodadas consecutivas são compatíveis com erro amostral isolado (|z| < 1,96). Sem atribuição de causa.

### D2. Tendência latente (todas as pesquisas; σ_drift 0,01, σ_house 0,02, σ_extra 0,02)

| dia | θ_B latente | dp (p.p.) |
|---|---|---|
| 4/10 | 51.91% | 0.64 |
| 6/10 | 51.86% | 0.57 |
| 8/10 | 51.73% | 0.53 |
| 10/10 | 51.54% | 0.49 |
| 12/10 | 51.38% | 0.46 |
| 14/10 | 51.26% | 0.45 |
| 16/10 | 51.18% | 0.44 |
| 18/10 | 51.11% | 0.44 |
| 20/10 | 51.06% | 0.50 |
| 22/10 | 51.04% | 0.60 |

Previsão para 25/10 (H = 3): θ_B = 51.04% ± 0.74 p.p. → θ_A = 48.96%.

### D3. House effects posteriores (prior N(0; 0,02²) sem sinal)

| instituto | rodadas | h_j ≈ p.p. em θ_B | dp (p.p.) | h/σ_house | identificação |
|---|---|---|---|---|---|
| df | 3 | -0.04 | 0.44 | -0.08 | parcial |
| qu | 2 | -0.06 | 0.47 | -0.12 | parcial |
| pd | 3 | -0.03 | 0.43 | -0.05 | parcial |
| nx | 2 | -0.08 | 0.45 | -0.16 | parcial |
| at | 2 | +0.17 | 0.42 | +0.34 | parcial |
| ip | 1 | +0.09 | 0.48 | +0.18 | fraco (1 rodada) |
| pv | 2 | -0.12 | 0.46 | -0.23 | parcial |
| fu | 1 | +0.00 | 0.47 | +0.00 | fraco (1 rodada) |
| mi | 1 | -0.01 | 0.47 | -0.01 | fraco (1 rodada) |
| rt | 1 | +0.07 | 0.47 | +0.13 | fraco (1 rodada) |

### D4. Calibração anterior × atual (bloco de pesquisas)

| versão | pesquisas | tempera dependência? | θ_B em 25/10 | dp (p.p.) | P(θ_B>0,5) |
|---|---|---|---|---|---|
| v1 (até 14/10) | 8 | não | 51.48% | 1.03 | 92.6% |
| v2 (até 20/10) | 16 | sim | 51.19% | 0.78 | 93.5% |
| v3 (até 22/10) | 18 | sim | 51.04% | 0.74 | 92.0% |

## E. Resíduos e verificações preditivas das pesquisas

| pesquisa | θ_B obs. | previsto (nível comum) | resíduo (p.p.) | r_j | previsto LOO | r_j LOO |
|---|---|---|---|---|---|---|
| df-r1 | 52.13% | 51.98% | +0.14 | +0.10 | 51.72% | +0.23 |
| df-r2 | 51.09% | 51.31% | -0.22 | -0.20 | 51.29% | -0.15 |
| qu-r1 | 51.11% | 51.46% | -0.35 | -0.22 | 51.40% | -0.16 |
| pd-r1 | 51.06% | 51.51% | -0.44 | -0.32 | 51.50% | -0.27 |
| nx-r1 | 51.61% | 51.51% | +0.11 | +0.09 | 51.32% | +0.21 |
| at-r1 | 52.79% | 52.01% | +0.77 | +1.08 | 51.46% | +1.16 |
| ip-r1 | 52.69% | 51.94% | +0.75 | +0.54 | 51.68% | +0.61 |
| pv-r1 | 50.51% | 51.46% | -0.96 | -0.80 | 51.51% | -0.69 |
| qu-r2 | 50.56% | 51.10% | -0.54 | -0.33 | 51.10% | -0.30 |
| fu-r1 | 51.10% | 51.08% | +0.02 | +0.02 | 51.08% | +0.01 |
| pv-r2 | 51.02% | 51.08% | -0.06 | -0.03 | 50.96% | +0.03 |
| mi-r1 | 51.06% | 51.11% | -0.05 | -0.04 | 51.12% | -0.03 |
| rt-r1 | 51.61% | 51.11% | +0.50 | +0.42 | 51.07% | +0.38 |
| at-r2 | 51.13% | 51.22% | -0.09 | -0.13 | 51.49% | -0.34 |
| nx-r2 | 50.32% | 51.15% | -0.83 | -0.71 | 51.24% | -0.65 |
| pd-r2 | 51.58% | 51.15% | +0.43 | +0.44 | 50.99% | +0.48 |
| df-r3 (nova) | 50.54% | 51.03% | -0.50 | -0.32 | 51.09% | -0.32 |
| pd-r3 (nova) | 50.52% | 51.05% | -0.54 | -0.45 | 51.16% | -0.45 |

Σ r_j² = 3.62 com ≈17 g.l.; p ≈ 1.000; razão de dispersão = 0.21.

Perfil de σ_extra (σ_house≈0): máximo em 0.000 logit (≈0.00 p.p.).

### E2. Verificação preditiva fora da amostra: pesquisas até 20/10 preveem as de 23/10?

| nova pesquisa | θ_B obs. | previsto pelo v2 (com deriva) | z |
|---|---|---|---|
| df-r3 | 50.54% | 51.18% | -0.36 |
| pd-r3 | 50.52% | 51.21% | -0.49 |

Média dos z = -0.42; máximo |z| = 0.49.

### E3. Sensibilidade do bloco de pesquisas (25/10)

| variação | θ_B | dp (p.p.) | P(θ_B>0,5) só pesquisas |
|---|---|---|---|
| caso-base | 51.04% | 0.74 | 92.0% |
| janela = só último dia | 51.04% | 0.69 | 93.4% |
| sem temperar dependência | 50.95% | 0.71 | 91.1% |
| σ_house 0,04 | 51.05% | 0.79 | 90.7% |
| σ_extra 0 | 51.02% | 0.72 | 92.0% |
| σ_drift 0,005 | 51.21% | 0.49 | 99.3% |
| σ_drift 0,02 | 50.86% | 1.25 | 75.4% |

## B. Retenção e transferência atualizadas (alvo: 25/10)

Modelo 2 com datas: n_eff de cada observação = 1/(1/n + Δt·σ_q²/0,25), σ_q = 0.005 por √dia; matriz pd com peso λ = 0.5; levantamentos com cruzamento + resultado geral entram com potência 0.5 em cada parte; indecisos III; viés de recordação σ_r = 0.5 p.p. ESS: transferências 56.271, completo 50.723.

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
| pd-r3 A | 20.0 | 290.2 |
| pd-r3 B | 20.0 | 300.4 |
| pd-r3 C | 20.0 | 21.5 |
| pd-r3 D | 20.0 | 16.7 |
| pd-r3 E | 20.0 | 16.3 |
| pd-r3 BN | 20.0 | 36.9 |
| pd-r3 ABS | 20.0 | 190.7 |
| pd-r3 F:L | 20.0 | 3.7 |
| df-r3 C:F | 21.0 | 35.4 |

| parâmetro (% , média [IC 90%]) | só pd r1 + r3 (com datas) | pd + df + qu + pv | completo (+ pesquisas) |
|---|---|---|---|
| R_A = A₁→A | 93.5 [91.6; 95.3] | 93.5 [91.6; 95.3] | 93.6 [91.8; 95.2] |
| X_AB = A₁→B | 4.5 [3.0; 6.1] | 4.5 [3.0; 6.1] | 4.4 [3.1; 5.9] |
| R_B = B₁→B | 95.3 [93.6; 96.8] | 95.3 [93.7; 96.8] | 95.3 [93.7; 96.7] |
| X_BA = B₁→A | 3.9 [2.6; 5.4] | 3.9 [2.6; 5.4] | 3.9 [2.6; 5.3] |
| C→A | 38.4 [26.1; 51.2] | 40.9 [32.9; 49.2] | 41.0 [33.0; 49.1] |
| C→B | 46.8 [34.0; 59.8] | 40.8 [32.7; 49.1] | 40.8 [32.7; 49.0] |
| D→A | 29.5 [17.1; 43.5] | 27.2 [19.1; 36.0] | 27.3 [19.2; 36.1] |
| D→B | 46.6 [32.3; 61.3] | 45.8 [36.3; 55.4] | 45.7 [36.3; 55.2] |
| E→A | 25.3 [13.6; 39.0] | 27.8 [19.1; 37.1] | 27.8 [19.2; 37.2] |
| E→B | 50.9 [36.1; 65.5] | 49.3 [39.2; 59.3] | 49.2 [39.1; 59.2] |
| F→A | 16.1 [0.3; 47.8] | 15.0 [0.3; 45.3] | 15.1 [0.3; 45.5] |
| F→B | 58.6 [21.8; 89.5] | 57.6 [21.1; 89.0] | 57.6 [21.1; 89.0] |
| G:L→A | 31.5 [2.9; 71.8] | 31.8 [3.0; 71.9] | 31.9 [3.1; 71.9] |
| G:L→B | 30.2 [1.3; 71.9] | 30.2 [1.3; 72.1] | 30.1 [1.3; 71.9] |
| C:F agregado →A | 31.2 [24.1; 38.6] | 32.2 [27.8; 36.6] | 32.2 [27.9; 36.6] |
| C:F agregado →B | 48.3 [40.5; 56.2] | 45.3 [40.6; 50.1] | 45.3 [40.6; 50.0] |
| X (BN₁+ABS₁) →A | 40.7 [36.6; 44.8] | 41.0 [37.7; 44.2] | 41.0 [37.8; 44.2] |
| X →B | 37.3 [33.3; 41.3] | 37.1 [34.0; 40.3] | 37.1 [33.9; 40.2] |
| X →BN/não vota | 15.7 [12.8; 18.8] | 17.0 [14.6; 19.5] | 17.0 [14.6; 19.5] |
| θ_A (válidos) | 48.6 [47.0; 50.2] | 48.8 [47.2; 50.3] | 48.9 [47.9; 49.8] |

Linhas q_g = intenção declarada normalizada, antes de indecisos e comparecimento.

### B2. Identificação: quanto cada fonte estreitou cada parâmetro

| parâmetro | dp só pd (p.p.) | dp + transferências | dp completo | razão completo/pd | identificação |
|---|---|---|---|---|---|
| R_A = A₁→A | 1.12 | 1.12 | 1.05 | 0.94 | insuficiente |
| X_AB = A₁→B | 0.94 | 0.94 | 0.87 | 0.93 | insuficiente |
| R_B = B₁→B | 0.95 | 0.94 | 0.90 | 0.95 | insuficiente |
| X_BA = B₁→A | 0.87 | 0.86 | 0.82 | 0.95 | insuficiente |
| C→A | 7.63 | 4.91 | 4.89 | 0.64 | parcial |
| C→B | 7.84 | 4.97 | 4.94 | 0.63 | parcial |
| D→A | 8.05 | 5.13 | 5.13 | 0.64 | parcial |
| D→B | 8.80 | 5.77 | 5.75 | 0.65 | parcial |
| E→A | 7.76 | 5.49 | 5.48 | 0.71 | parcial |
| E→B | 8.93 | 6.16 | 6.14 | 0.69 | parcial |
| F→A | 15.48 | 14.70 | 14.73 | 0.95 | insuficiente |
| F→B | 20.66 | 20.62 | 20.64 | 1.00 | insuficiente |
| G:L→A | 21.40 | 21.42 | 21.37 | 1.00 | insuficiente |
| G:L→B | 22.37 | 22.42 | 22.38 | 1.00 | insuficiente |
| C:F agregado →A | 4.41 | 2.69 | 2.66 | 0.60 | parcial |
| C:F agregado →B | 4.78 | 2.90 | 2.86 | 0.60 | boa |
| X (BN₁+ABS₁) →A | 2.49 | 1.96 | 1.94 | 0.78 | parcial |
| X →B | 2.44 | 1.93 | 1.91 | 0.78 | parcial |
| X →BN/não vota | 1.83 | 1.49 | 1.49 | 0.81 | parcial |
| θ_A (válidos) | 0.98 | 0.93 | 0.58 | 0.59 | boa |

### B3. Verificação preditiva das observações de transferência (modelo completo)

| observação | → | observado | previsto (completo) | z preditivo |
|---|---|---|---|---|
| pd-matriz B | A | 5% | 3.9% | +0.64 |
| pd-matriz B | B | 95% | 95.3% | -0.18 |
| pd-matriz A | A | 92% | 93.6% | -0.72 |
| pd-matriz A | B | 5% | 4.4% | +0.33 |
| pd-matriz C | A | 27% | 41.0% | -1.15 |
| pd-matriz C | B | 56% | 40.8% | +1.14 |
| pd-matriz D | A | 25% | 27.3% | -0.19 |
| pd-matriz D | B | 48% | 45.7% | +0.12 |
| pd-matriz E | A | 19% | 27.8% | -0.69 |
| pd-matriz E | B | 58% | 49.2% | +0.54 |
| pd-matriz F | A | 10% | 15.1% | -0.18 |
| pd-matriz F | B | 72% | 57.6% | +0.35 |
| pd-matriz GL | A | 39% | 31.9% | +0.15 |
| pd-matriz GL | B | 19% | 30.1% | -0.27 |
| pd-matriz BN | A | 18% | 35.0% | -1.85 |
| pd-matriz BN | B | 22% | 22.9% | -0.12 |
| pd-matriz ABS | A | 34% | 42.1% | -1.71 |
| pd-matriz ABS | B | 42% | 39.6% | +0.49 |
| df C:F | A | 32% | 32.2% | -0.03 |
| df C:F | B | 46% | 45.3% | +0.08 |
| qu-r1 C | A | 34% | 41.0% | -0.55 |
| qu-r1 C | B | 30% | 40.8% | -0.87 |
| qu-r1 D | A | 14% | 27.3% | -1.17 |
| qu-r1 D | B | 40% | 45.7% | -0.37 |
| qu-r1 E | A | 23% | 27.8% | -0.31 |
| qu-r1 E | B | 42% | 49.2% | -0.39 |
| qu-r1 X | A | 43% | 41.0% | +0.40 |
| qu-r1 X | B | 38% | 37.1% | +0.19 |
| qu-r2 C | A | 48% | 41.0% | +0.53 |
| qu-r2 C | B | 33% | 40.8% | -0.62 |
| qu-r2 D | A | 25% | 27.3% | -0.17 |
| qu-r2 D | B | 51% | 45.7% | +0.34 |
| qu-r2 E | A | 21% | 27.8% | -0.45 |
| qu-r2 E | B | 57% | 49.2% | +0.43 |
| qu-r2 X | A | 40% | 41.0% | -0.21 |
| qu-r2 X | B | 36% | 37.1% | -0.23 |
| pv-r2 C | A | 52% | 41.0% | +0.86 |
| pv-r2 C | B | 43% | 40.8% | +0.17 |
| pv-r2 D | A | 39% | 27.3% | +0.83 |
| pv-r2 D | B | 42% | 45.7% | -0.25 |
| pv-r2 E | A | 44% | 27.8% | +1.11 |
| pv-r2 E | B | 44% | 49.2% | -0.35 |
| pd-r3 A | A | 95% | 93.6% | +0.84 |
| pd-r3 A | B | 4% | 4.4% | -0.28 |
| pd-r3 B | A | 3% | 3.9% | -0.71 |
| pd-r3 B | B | 96% | 95.3% | +0.50 |
| pd-r3 C | A | 48% | 41.0% | +0.59 |
| pd-r3 C | B | 42% | 40.8% | +0.10 |
| pd-r3 D | A | 34% | 27.3% | +0.50 |
| pd-r3 D | B | 49% | 45.7% | +0.21 |
| pd-r3 E | A | 30% | 27.8% | +0.17 |
| pd-r3 E | B | 49% | 49.2% | -0.01 |
| pd-r3 BN | A | 46% | 35.0% | +1.11 |
| pd-r3 BN | B | 23% | 22.9% | +0.02 |
| pd-r3 ABS | A | 48% | 42.1% | +1.28 |
| pd-r3 ABS | B | 39% | 39.6% | -0.24 |
| pd-r3 F:L | A | 20% | 22.5% | -0.11 |
| pd-r3 F:L | B | 70% | 45.4% | +0.90 |
| df-r3 C:F | A | 26% | 32.2% | -0.79 |
| df-r3 C:F | B | 47% | 45.3% | +0.20 |

Máximo |z| = 1.85; 0 de 60 com |z| > 2.

## Probabilidades atualizadas (25/10)

**Caso-base v3:** E[θ_A] = 48.89% [IC 90% 47.93% – 49.84%]; **P(θ_A > 0,5) = 2.7%**.

| σ_drift | σ_r (p.p.) | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|---|
| 0.005 | 0.0 | 48.79% | 48.10% – 49.47% | 0.2% | 21.198 |
| 0.005 | 0.5 | 48.79% | 48.07% – 49.50% | 0.3% | 38.284 |
| 0.005 | 1.0 | 48.79% | 48.04% – 49.54% | 0.4% | 12.047 |
| 0.010 | 0.0 | 48.87% | 47.98% – 49.75% | 1.9% | 9.852 |
| 0.010 | 0.5 | 48.89% | 47.93% – 49.84% | 2.7% | 50.723 |
| 0.010 | 1.0 | 48.91% | 47.86% – 49.97% | 4.4% | 21.093 |
| 0.020 | 0.0 | 48.87% | 47.76% – 49.97% | 4.5% | 24.254 |
| 0.020 | 0.5 | 48.90% | 47.67% – 50.13% | 7.1% | 56.845 |
| 0.020 | 1.0 | 48.96% | 47.48% – 50.42% | 11.9% | 22.906 |

Sensibilidade às hipóteses estruturais (σ_drift 0,01; σ_r 0,5 p.p.):

| variação | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|
| λ_pd = 1 | 48.80% | 47.85% – 49.75% | 1.9% | 17.354 |
| λ_pd = 0,25 | 48.94% | 47.97% – 49.92% | 3.8% | 15.480 |
| σ_q = 0,0025 | 48.88% | 47.93% – 49.82% | 2.6% | 24.067 |
| σ_q = 0,01 | 48.90% | 47.91% – 49.88% | 3.3% | 16.409 |
| sem temperar dependência | 48.94% | 48.01% – 49.86% | 3.0% | 3.752 |
| só observações ≥ 18/10 (sem pd-r1, df-r1, qu-r1) | 49.03% | 48.05% – 50.03% | 5.5% | 1.099 |
| sem pd-r3 e df-r3 (= dados do v2) | 48.84% | 47.79% – 49.89% | 3.4% | 17.294 |
| sem pd-r3 | 48.83% | 47.78% – 49.86% | 3.1% | 7.847 |
| só pesquisas (sem estrutural) | 48.96% | 47.75% – 50.17% | 8.0% | — |

## C. Sensibilidade às hipóteses de comparecimento

κ = fração do diferencial DECLARADO (nx: convictos A 95,0% × B 91,6%) que se converte em diferencial EFETIVO de comparecimento entre votantes de A e de B, aplicado após a ponderação pelas pesquisas (as pesquisas medem intenção, não comparecimento). κ = 0 é a hipótese do v1 (churn simétrico). Os 'convictos' são subconjuntos; estender a todos os eleitores é suposição.

| κ | diferencial efetivo A − B (relativo) | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|
| 0.00 | 0.00 p.p. | 48.89% | 47.93% – 49.84% | 2.7% |
| 0.25 | 0.91 p.p. | 49.11% | 48.16% – 50.06% | 6.3% |
| 0.50 | 1.82 p.p. | 49.34% | 48.39% – 50.29% | 12.6% |
| 1.00 | 3.64 p.p. | 49.80% | 48.84% – 50.75% | 36.3% |

Diferença média V_B − V_A (completo, κ=0) = 2.680.137 votos; linha ABS posterior: A entre válidos = 51.5%, BN = 15.8%.

Comparecimento total (variação dos faltantes do 1T, em p.p. do eleitorado) × divisão A:B dos faltantes adicionais; célula = E[θ_A] / P(θ_A>0,5), modelo completo, κ = 0:

| comparecimento | linha ABS posterior | 50:50 | 55:45 | 60:40 | 2:1 |
|---|---|---|---|---|---|
| -2 p.p. | 48.83% / 2.4% | 48.86% / 2.7% | 48.75% / 1.7% | 48.63% / 1.1% | 48.48% / 0.5% |
| -1 p.p. | 48.86% / 2.5% | 48.87% / 2.7% | 48.82% / 2.2% | 48.76% / 1.7% | 48.69% / 1.3% |
| = 1º turno | 48.89% / 2.7% | 48.89% / 2.7% | 48.89% / 2.7% | 48.89% / 2.7% | 48.89% / 2.7% |
| +1 p.p. | 48.91% / 2.9% | 48.90% / 2.7% | 48.95% / 3.3% | 49.01% / 4.1% | 49.08% / 5.4% |
| +2 p.p. | 48.94% / 3.1% | 48.91% / 2.7% | 49.02% / 4.1% | 49.13% / 6.2% | 49.27% / 9.9% |
| +3 p.p. | 48.97% / 3.3% | 48.92% / 2.7% | 49.08% / 5.0% | 49.24% / 8.8% | 49.46% / 16.6% |
| +5 p.p. | 49.02% / 3.7% | 48.94% / 2.7% | 49.21% / 7.4% | 49.47% / 16.6% | 49.82% / 37.3% |

## Fronteira de virada recalibrada

X_AB = 4.46%, X_BA = 3.93% (médias posteriores; baseadas nas matrizes pd r1 (~11/10) e pd-r3 (19–21/10), com desconto temporal). X_BA necessário = 2.15% + 0.962 × X_AB.

| X_AB | X_BA necessário | Δ vs atual |
|---|---|---|
| 0.0% | 2.15% | -1.77 |
| 1.0% | 3.12% | -0.81 |
| 2.0% | 4.08% | +0.15 |
| 3.0% | 5.04% | +1.11 |
| 4.0% | 6.00% | +2.07 |
| 4.5% (atual) | 6.44% | +2.51 |
| 5.0% | 6.96% | +3.03 |
| 6.0% | 7.92% | +3.99 |
| 7.0% | 8.88% | +4.96 |

Ponto mais provável sobre a fronteira (só troca de votos, com correlação ρ = 0.13): X_BA = 5.15%, X_AB = 3.12%; distância ≈ 2.30 dp (dp X_BA 0.82, dp X_AB 0.87 p.p.).

