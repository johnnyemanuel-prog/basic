# Resultados v4 — rodadas finais de 24/10 (gerado por modelo_v4.py)

Semente 20261024; M = 1.000.000 sorteios. Eleição em 25/out; último campo 24/out (H = 1 dia).

## A. Auditoria de consistência dos dados novos

### A1. Pesquisas nacionais novas

| id | campo | n | Σ totais | B válido (calc.) | B válido (publ.) | calc − publ | MOE | MOE AAS | DEFF impl. | fonte da likelihood | σ_j válido (p.p.) | mesmo levant. tem cruzamentos? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| df-r4 | 23–24/10 | 4050 | 100% | 50.53% | 51% | -0.47 | 2.00 | 1.54 | 1.69 | totais | 1.07 | não |
| qu-r3 | 23–24/10 | 3702 | 100% | 50.55% | 51% | -0.45 | 2.00 | 1.61 | 1.54 | totais | 1.09 | não |
| nx-r3 | 23–24/10 | 2000 | 100% | 50.54% | 50.5% | +0.04 | 2.20 | 2.19 | 1.01 | totais | 1.18 | não |
| pv-r3 | 22–24/10 | 5000 | 100% | 50.51% | ND | — | 2.20 | 1.39 | 2.52 | totais | 1.15 | não |

- Modo de coleta: df-r4 e qu-r3 presenciais, nx-r3 telefônica, pv-r3 não informado. Não há parâmetro de modo no modelo: diferenças de modo ficam absorvidas no efeito de instituto (h_j) e em σ_extra.
- Uma única likelihood por levantamento (B/(A+B) dos totais). Válidos publicados (df 51, qu 51, nx 50,5) são só checagem; a diferença para o calculado (≤ 0,47 p.p.) é compatível com arredondamento a inteiro (df, qu) ou a 0,5 (nx). pv não publicou válidos: B/(A+B) = 50/99 calculado dos totais arredondados (resolução ±0,5 p.p. em A e B entra em σ_j).
- DEFF implícito das margens: df-r4 1,69 e qu-r3 1,54 (n maiores que nas rodadas anteriores com margem igual); pv-r3 2,52; nx-r3 1,01. Usa-se max(MOE publicada, AAS), como antes.
- Não há cruzamentos de transferência nestas rodadas: sem tempera de dependência; nenhuma nova taxa de migração direta foi criada.

Rodadas anteriores preservadas: v1 (8), v2 (qu-r2, fu-r1, pv-r2, mi-r1, rt-r1, at-r2, nx-r2, pd-r2), v3 (df-r3, pd-r3; margem não informada → AAS × √DEFF do instituto).

† (v2) Data de início do campo NÃO informada; janela suposta = duração da rodada anterior do instituto (qu 4 dias, at 6, nx/pd 3) ou 3 dias (fu, mi, rt). pv: 18–20/10 informado na divulgação de transferências. Sensibilidade com janela de 1 dia (só último dia) na seção E.

- Uma única likelihood por levantamento: binomial (logit) da fração B/(A+B). Quando os totais existem, ela é calculada deles (mais resolução) e os válidos publicados servem só como checagem; fu só tem válidos (1 decimal) → σ usa a razão média (A+B) das novas (94.0%) como denominador, por falta do dado.
- at-r2: MOE ±1,0 continua abaixo da AAS (±1,39) → usa-se ±1,39 (mesma regra do v1). BN+NS = 2,6 agregados, não desagregados.
- pv-r2 soma 99% e pd-r2 soma 101%: diferenças de arredondamento preservadas; a fração B/(A+B) não depende delas. Arredondamento de ±0,5 p.p. em A e B entra em σ_j.
- rt e pd: válidos publicados inteiros (52) vs calculados (51,61 / 51,58): compatíveis com arredondamento; usa-se o calculado.

### A2. Transferências (sem novas matrizes em 24/10; históricas preservadas com data e desconto temporal)

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

### A2b. Transferências de 23/10 (pd-r3 e df-r3) — preservadas

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
| df-r4 | voto decidido | 95% | descritivo; firmeza ≠ retenção |
| nx-r3 | voto definitivo / pode mudar / NS-NR | 94,3 / 4,7 / 1,1 (Σ 100,1, arred.) | descritivo |
| nx-r3 | voto definitivo entre eleitores de A / de B | 95,7% / 97,4% | descritivo; não é probabilidade de retenção |
| nx-r3 | LVM: A / B entre válidos (exclui 21% menos prováveis) | 47,6 / 52,4 | só sensibilidade de comparecimento (seção C) |
| pv-r3 | rejeição A / B | 49 / 47 | descritivo; não é voto |
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
| df | df-r3 (22/10) → df-r4 (24/10) | 50.54% | 50.53% | -0.01 | -0.01 |
| qu | qu-r1 (13/10) → qu-r2 (20/10) | 51.11% | 50.56% | -0.55 | -0.33 |
| qu | qu-r2 (20/10) → qu-r3 (24/10) | 50.56% | 50.55% | -0.01 | -0.01 |
| pd | pd-r1 (12/10) → pd-r2 (18/10) | 51.06% | 51.58% | +0.52 | +0.38 |
| pd | pd-r2 (18/10) → pd-r3 (21/10) | 51.58% | 50.52% | -1.06 | -0.83 |
| nx | nx-r1 (12/10) → nx-r2 (18/10) | 51.61% | 50.32% | -1.29 | -0.78 |
| nx | nx-r2 (18/10) → nx-r3 (24/10) | 50.32% | 50.54% | +0.21 | +0.13 |
| at | at-r1 (8/10) → at-r2 (18/10) | 52.79% | 51.13% | -1.66 | -1.64 |
| pv | pv-r1 (13/10) → pv-r2 (20/10) | 50.51% | 51.02% | +0.52 | +0.30 |
| pv | pv-r2 (20/10) → pv-r3 (24/10) | 51.02% | 50.51% | -0.52 | -0.30 |

Maior |z| = 1.64: todas as variações entre rodadas consecutivas são compatíveis com erro amostral isolado (|z| < 1,96). Sem atribuição de causa.

### D2. Tendência latente (todas as pesquisas; σ_drift 0,01, σ_house 0,02, σ_extra 0,02)

| dia | θ_B latente | dp (p.p.) |
|---|---|---|
| 4/10 | 51.89% | 0.64 |
| 6/10 | 51.84% | 0.57 |
| 8/10 | 51.71% | 0.52 |
| 10/10 | 51.52% | 0.49 |
| 12/10 | 51.36% | 0.46 |
| 14/10 | 51.23% | 0.45 |
| 16/10 | 51.13% | 0.43 |
| 18/10 | 51.04% | 0.41 |
| 20/10 | 50.94% | 0.44 |
| 22/10 | 50.86% | 0.47 |
| 24/10 | 50.81% | 0.51 |

Previsão para 25/10 (H = 1): θ_B = 50.81% ± 0.57 p.p. → θ_A = 49.19%.

### D3. House effects posteriores (prior N(0; 0,02²) sem sinal)

| instituto | rodadas | h_j ≈ p.p. em θ_B | dp (p.p.) | h/σ_house | identificação |
|---|---|---|---|---|---|
| df | 4 | -0.06 | 0.42 | -0.11 | parcial |
| qu | 3 | -0.08 | 0.44 | -0.16 | parcial |
| pd | 3 | -0.00 | 0.43 | -0.01 | parcial |
| nx | 3 | -0.09 | 0.43 | -0.19 | parcial |
| at | 2 | +0.18 | 0.42 | +0.36 | parcial |
| ip | 1 | +0.09 | 0.48 | +0.19 | fraco (1 rodada) |
| pv | 3 | -0.13 | 0.44 | -0.27 | parcial |
| fu | 1 | +0.01 | 0.47 | +0.03 | fraco (1 rodada) |
| mi | 1 | +0.00 | 0.47 | +0.01 | fraco (1 rodada) |
| rt | 1 | +0.08 | 0.47 | +0.15 | fraco (1 rodada) |

### D4. Calibração anterior × atual (bloco de pesquisas)

| versão | pesquisas | tempera dependência? | θ_B em 25/10 | dp (p.p.) | P(θ_B>0,5) |
|---|---|---|---|---|---|
| v1 (até 14/10) | 8 | não | 51.48% | 1.03 | 92.6% |
| v2 (até 20/10) | 16 | sim | 51.19% | 0.78 | 93.5% |
| v3 (até 22/10) | 18 | sim | 51.04% | 0.74 | 92.0% |
| v4 (até 24/10) | 22 | sim | 50.81% | 0.57 | 92.2% |

Todas as versões avaliadas com o mesmo estado até 24/10 e H = 1 (o v1 propaga a deriva de 14→25/10).

### D5. Rodadas finais: comparação entre institutos

| rodada | modo | n | θ_B (B/(A+B)) | σ_j (p.p.) | z vs média ponderada | h_j do instituto (p.p.) |
|---|---|---|---|---|---|---|
| df-r4 | presencial | 4050 | 50.53% | 1.07 | -0.00 | -0.06 |
| qu-r3 | presencial | 3702 | 50.55% | 1.09 | +0.02 | -0.08 |
| nx-r3 | telefone | 2000 | 50.54% | 1.18 | +0.01 | -0.09 |
| pv-r3 | não informado | 5000 | 50.51% | 1.15 | -0.02 | -0.13 |

Média ponderada das quatro rodadas finais: θ_B = 50.53%; Q de Cochran = 0.001 com 3 g.l. (dispersão muito abaixo da esperada só pelo erro amostral: as quatro medições praticamente coincidem).

## E. Resíduos e verificações preditivas das pesquisas

| pesquisa | θ_B obs. | previsto (nível comum) | resíduo (p.p.) | r_j | previsto LOO | r_j LOO |
|---|---|---|---|---|---|---|
| df-r1 | 52.13% | 51.97% | +0.15 | +0.10 | 51.69% | +0.25 |
| df-r2 | 51.09% | 51.28% | -0.19 | -0.18 | 51.23% | -0.11 |
| qu-r1 | 51.11% | 51.44% | -0.33 | -0.20 | 51.35% | -0.13 |
| pd-r1 | 51.06% | 51.49% | -0.42 | -0.31 | 51.50% | -0.27 |
| nx-r1 | 51.61% | 51.49% | +0.12 | +0.11 | 51.28% | +0.23 |
| at-r1 | 52.79% | 52.01% | +0.78 | +1.09 | 51.46% | +1.16 |
| ip-r1 | 52.69% | 51.93% | +0.76 | +0.55 | 51.67% | +0.62 |
| pv-r1 | 50.51% | 51.44% | -0.94 | -0.78 | 51.44% | -0.65 |
| qu-r2 | 50.56% | 51.00% | -0.44 | -0.27 | 50.97% | -0.23 |
| fu-r1 | 51.10% | 50.97% | +0.13 | +0.11 | 50.98% | +0.08 |
| pv-r2 | 51.02% | 50.97% | +0.05 | +0.03 | 50.84% | +0.09 |
| mi-r1 | 51.06% | 51.03% | +0.03 | +0.02 | 51.04% | +0.02 |
| rt-r1 | 51.61% | 51.03% | +0.58 | +0.49 | 50.99% | +0.43 |
| at-r2 | 51.13% | 51.17% | -0.04 | -0.06 | 51.43% | -0.29 |
| nx-r2 | 50.32% | 51.09% | -0.77 | -0.66 | 51.13% | -0.58 |
| pd-r2 | 51.58% | 51.09% | +0.49 | +0.50 | 50.95% | +0.51 |
| df-r3 | 50.54% | 50.85% | -0.32 | -0.21 | 50.88% | -0.20 |
| pd-r3 | 50.52% | 50.91% | -0.40 | -0.34 | 51.02% | -0.36 |
| df-r4 (nova) | 50.53% | 50.75% | -0.23 | -0.21 | 50.83% | -0.23 |
| qu-r3 (nova) | 50.55% | 50.75% | -0.20 | -0.19 | 50.80% | -0.18 |
| nx-r3 (nova) | 50.54% | 50.75% | -0.21 | -0.18 | 50.78% | -0.17 |
| pv-r3 (nova) | 50.51% | 50.77% | -0.26 | -0.23 | 50.75% | -0.18 |

Σ r_j² = 3.64 com ≈21 g.l.; p ≈ 1.000; razão de dispersão = 0.17.

Perfil de σ_extra (σ_house≈0): máximo em 0.000 logit (≈0.00 p.p.).

### E2. Verificação preditiva fora da amostra: pesquisas até 22/10 preveem as rodadas finais?

| nova pesquisa | θ_B obs. | previsto pelo v3 (com deriva) | z |
|---|---|---|---|
| df-r4 | 50.53% | 51.00% | -0.34 |
| qu-r3 | 50.55% | 50.98% | -0.30 |
| nx-r3 | 50.54% | 50.96% | -0.28 |
| pv-r3 | 50.51% | 50.92% | -0.29 |

Média dos z = -0.30; máximo |z| = 0.34.

### E3. Sensibilidade do bloco de pesquisas (25/10)

| variação | θ_B | dp (p.p.) | P(θ_B>0,5) só pesquisas |
|---|---|---|---|
| caso-base | 50.81% | 0.57 | 92.2% |
| janela = só último dia | 50.83% | 0.54 | 93.9% |
| sem temperar dependência | 50.78% | 0.56 | 91.7% |
| σ_house 0,04 | 50.88% | 0.65 | 91.4% |
| σ_extra 0 | 50.80% | 0.55 | 92.6% |
| σ_drift 0,005 | 51.01% | 0.42 | 99.2% |
| σ_drift 0,02 | 50.65% | 0.83 | 78.6% |

## B. Retenção e transferência atualizadas (alvo: 25/10)

Modelo 2 com datas: n_eff de cada observação = 1/(1/n + Δt·σ_q²/0,25), σ_q = 0.005 por √dia; matriz pd com peso λ = 0.5; levantamentos com cruzamento + resultado geral entram com potência 0.5 em cada parte; indecisos III; viés de recordação σ_r = 0.5 p.p. ESS: transferências 34.232, completo 32.856.

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
| R_A = A₁→A | 93.5 [91.6; 95.3] | 93.5 [91.6; 95.3] | 93.7 [91.9; 95.3] |
| X_AB = A₁→B | 4.5 [3.0; 6.1] | 4.5 [3.0; 6.1] | 4.3 [3.0; 5.8] |
| R_B = B₁→B | 95.3 [93.6; 96.8] | 95.3 [93.6; 96.8] | 95.2 [93.6; 96.6] |
| X_BA = B₁→A | 3.9 [2.6; 5.4] | 3.9 [2.6; 5.4] | 4.0 [2.7; 5.4] |
| C→A | 38.3 [26.1; 51.3] | 40.9 [32.9; 49.0] | 41.1 [33.2; 49.1] |
| C→B | 46.8 [34.0; 59.8] | 40.8 [32.8; 49.0] | 40.7 [32.6; 48.8] |
| D→A | 29.6 [17.1; 43.5] | 27.2 [19.0; 36.1] | 27.4 [19.2; 36.2] |
| D→B | 46.6 [32.2; 61.2] | 45.7 [36.3; 55.3] | 45.6 [36.2; 55.1] |
| E→A | 25.4 [13.5; 39.0] | 27.7 [19.1; 37.1] | 27.9 [19.3; 37.3] |
| E→B | 50.9 [36.1; 65.5] | 49.4 [39.3; 59.5] | 49.1 [39.1; 59.2] |
| F→A | 16.1 [0.3; 47.9] | 15.1 [0.3; 45.3] | 15.3 [0.3; 45.5] |
| F→B | 58.6 [21.7; 89.6] | 57.4 [20.9; 88.7] | 57.1 [20.8; 88.6] |
| G:L→A | 31.5 [2.9; 71.7] | 31.7 [2.9; 71.7] | 31.7 [2.9; 71.7] |
| G:L→B | 30.2 [1.3; 71.9] | 30.4 [1.3; 72.2] | 30.3 [1.4; 72.0] |
| C:F agregado →A | 31.2 [24.2; 38.6] | 32.1 [27.8; 36.6] | 32.3 [28.0; 36.8] |
| C:F agregado →B | 48.3 [40.5; 56.2] | 45.3 [40.6; 50.1] | 45.1 [40.5; 49.8] |
| X (BN₁+ABS₁) →A | 40.7 [36.6; 44.8] | 41.0 [37.7; 44.2] | 41.1 [37.9; 44.3] |
| X →B | 37.3 [33.3; 41.3] | 37.1 [34.0; 40.3] | 37.0 [33.9; 40.1] |
| X →BN/não vota | 15.7 [12.8; 18.8] | 17.0 [14.5; 19.5] | 17.0 [14.6; 19.5] |
| θ_A (válidos) | 48.6 [47.0; 50.2] | 48.8 [47.2; 50.3] | 49.1 [48.3; 49.9] |

Linhas q_g = intenção declarada normalizada, antes de indecisos e comparecimento.

### B2. Identificação: quanto cada fonte estreitou cada parâmetro

| parâmetro | dp só pd (p.p.) | dp + transferências | dp completo | razão completo/pd | identificação |
|---|---|---|---|---|---|
| R_A = A₁→A | 1.12 | 1.13 | 1.04 | 0.92 | insuficiente |
| X_AB = A₁→B | 0.94 | 0.95 | 0.85 | 0.90 | insuficiente |
| R_B = B₁→B | 0.95 | 0.95 | 0.91 | 0.96 | insuficiente |
| X_BA = B₁→A | 0.87 | 0.87 | 0.83 | 0.96 | insuficiente |
| C→A | 7.64 | 4.89 | 4.88 | 0.64 | parcial |
| C→B | 7.84 | 4.93 | 4.92 | 0.63 | parcial |
| D→A | 8.05 | 5.20 | 5.15 | 0.64 | parcial |
| D→B | 8.80 | 5.79 | 5.73 | 0.65 | parcial |
| E→A | 7.77 | 5.47 | 5.48 | 0.70 | parcial |
| E→B | 8.94 | 6.14 | 6.11 | 0.68 | parcial |
| F→A | 15.50 | 14.71 | 14.82 | 0.96 | insuficiente |
| F→B | 20.68 | 20.66 | 20.67 | 1.00 | insuficiente |
| G:L→A | 21.37 | 21.38 | 21.37 | 1.00 | insuficiente |
| G:L→B | 22.36 | 22.47 | 22.37 | 1.00 | insuficiente |
| C:F agregado →A | 4.41 | 2.69 | 2.66 | 0.60 | parcial |
| C:F agregado →B | 4.78 | 2.89 | 2.84 | 0.59 | boa |
| X (BN₁+ABS₁) →A | 2.49 | 1.96 | 1.94 | 0.78 | parcial |
| X →B | 2.44 | 1.92 | 1.90 | 0.78 | parcial |
| X →BN/não vota | 1.83 | 1.50 | 1.49 | 0.82 | parcial |
| θ_A (válidos) | 0.98 | 0.94 | 0.49 | 0.50 | boa |

### B3. Verificação preditiva das observações de transferência (modelo completo)

| observação | → | observado | previsto (completo) | z preditivo |
|---|---|---|---|---|
| pd-matriz B | A | 5% | 4.0% | +0.60 |
| pd-matriz B | B | 95% | 95.2% | -0.14 |
| pd-matriz A | A | 92% | 93.7% | -0.76 |
| pd-matriz A | B | 5% | 4.3% | +0.38 |
| pd-matriz C | A | 27% | 41.1% | -1.16 |
| pd-matriz C | B | 56% | 40.7% | +1.15 |
| pd-matriz D | A | 25% | 27.4% | -0.20 |
| pd-matriz D | B | 48% | 45.6% | +0.13 |
| pd-matriz E | A | 19% | 27.9% | -0.69 |
| pd-matriz E | B | 58% | 49.1% | +0.55 |
| pd-matriz F | A | 10% | 15.3% | -0.19 |
| pd-matriz F | B | 72% | 57.1% | +0.36 |
| pd-matriz GL | A | 39% | 31.7% | +0.15 |
| pd-matriz GL | B | 19% | 30.3% | -0.27 |
| pd-matriz BN | A | 18% | 35.2% | -1.88 |
| pd-matriz BN | B | 22% | 22.7% | -0.10 |
| pd-matriz ABS | A | 34% | 42.1% | -1.72 |
| pd-matriz ABS | B | 42% | 39.5% | +0.51 |
| df C:F | A | 32% | 32.3% | -0.04 |
| df C:F | B | 46% | 45.1% | +0.09 |
| qu-r1 C | A | 34% | 41.1% | -0.55 |
| qu-r1 C | B | 30% | 40.7% | -0.86 |
| qu-r1 D | A | 14% | 27.4% | -1.18 |
| qu-r1 D | B | 40% | 45.6% | -0.36 |
| qu-r1 E | A | 23% | 27.9% | -0.31 |
| qu-r1 E | B | 42% | 49.1% | -0.39 |
| qu-r1 X | A | 43% | 41.1% | +0.38 |
| qu-r1 X | B | 38% | 37.0% | +0.20 |
| qu-r2 C | A | 48% | 41.1% | +0.52 |
| qu-r2 C | B | 33% | 40.7% | -0.61 |
| qu-r2 D | A | 25% | 27.4% | -0.17 |
| qu-r2 D | B | 51% | 45.6% | +0.35 |
| qu-r2 E | A | 21% | 27.9% | -0.46 |
| qu-r2 E | B | 57% | 49.1% | +0.43 |
| qu-r2 X | A | 40% | 41.1% | -0.22 |
| qu-r2 X | B | 36% | 37.0% | -0.21 |
| pv-r2 C | A | 52% | 41.1% | +0.86 |
| pv-r2 C | B | 43% | 40.7% | +0.18 |
| pv-r2 D | A | 39% | 27.4% | +0.83 |
| pv-r2 D | B | 42% | 45.6% | -0.25 |
| pv-r2 E | A | 44% | 27.9% | +1.11 |
| pv-r2 E | B | 44% | 49.1% | -0.35 |
| pd-r3 A | A | 95% | 93.7% | +0.79 |
| pd-r3 A | B | 4% | 4.3% | -0.22 |
| pd-r3 B | A | 3% | 4.0% | -0.77 |
| pd-r3 B | B | 96% | 95.2% | +0.55 |
| pd-r3 C | A | 48% | 41.1% | +0.59 |
| pd-r3 C | B | 42% | 40.7% | +0.11 |
| pd-r3 D | A | 34% | 27.4% | +0.50 |
| pd-r3 D | B | 49% | 45.6% | +0.22 |
| pd-r3 E | A | 30% | 27.9% | +0.16 |
| pd-r3 E | B | 49% | 49.1% | -0.01 |
| pd-r3 BN | A | 46% | 35.2% | +1.09 |
| pd-r3 BN | B | 23% | 22.7% | +0.03 |
| pd-r3 ABS | A | 48% | 42.1% | +1.27 |
| pd-r3 ABS | B | 39% | 39.5% | -0.22 |
| pd-r3 F:L | A | 20% | 22.6% | -0.11 |
| pd-r3 F:L | B | 70% | 45.2% | +0.90 |
| df-r3 C:F | A | 26% | 32.3% | -0.80 |
| df-r3 C:F | B | 47% | 45.1% | +0.21 |

Máximo |z| = 1.88; 0 de 60 com |z| > 2.

## Probabilidades atualizadas (25/10)

**Caso-base v4:** E[θ_A] = 49.07% [IC 90% 48.27% – 49.88%]; **P(θ_A > 0,5) = 2.9%**.

| σ_drift | σ_r (p.p.) | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|---|
| 0.005 | 0.0 | 48.93% | 48.33% – 49.55% | 0.2% | 19.182 |
| 0.005 | 0.5 | 48.95% | 48.32% – 49.58% | 0.3% | 28.410 |
| 0.005 | 1.0 | 48.96% | 48.29% – 49.62% | 0.5% | 13.484 |
| 0.010 | 0.0 | 49.04% | 48.28% – 49.80% | 1.8% | 21.973 |
| 0.010 | 0.5 | 49.07% | 48.27% – 49.88% | 2.9% | 32.856 |
| 0.010 | 1.0 | 49.11% | 48.25% – 49.97% | 4.4% | 12.671 |
| 0.020 | 0.0 | 49.04% | 48.11% – 49.99% | 4.8% | 27.338 |
| 0.020 | 0.5 | 49.09% | 48.07% – 50.11% | 7.1% | 41.924 |
| 0.020 | 1.0 | 49.17% | 48.03% – 50.32% | 11.8% | 20.490 |

Sensibilidade às hipóteses estruturais (σ_drift 0,01; σ_r 0,5 p.p.):

| variação | E[θ_A] | IC 90% | P(θ_A>0,5) | ESS |
|---|---|---|---|---|
| λ_pd = 1 | 49.00% | 48.22% – 49.79% | 1.9% | 30.326 |
| λ_pd = 0,25 | 49.11% | 48.31% – 49.92% | 3.6% | 6.853 |
| σ_q = 0,0025 | 49.07% | 48.27% – 49.85% | 2.6% | 3.819 |
| σ_q = 0,01 | 49.09% | 48.27% – 49.91% | 3.4% | 27.983 |
| sem temperar dependência | 49.10% | 48.36% – 49.86% | 2.6% | 205 |
| só observações ≥ 18/10 (sem pd-r1, df-r1, qu-r1) | 49.19% | 48.37% – 50.02% | 5.3% | 11.434 |
| sem pd-r3 e df-r3 (= dados do v2) | 49.06% | 48.21% – 49.92% | 3.6% | 16.420 |
| sem pd-r3 | 49.06% | 48.19% – 49.92% | 3.7% | 4.905 |
| só pesquisas (sem estrutural) | 49.19% | 48.25% – 50.13% | 7.8% | — |

## C. Sensibilidade às hipóteses de comparecimento

κ = fração do diferencial DECLARADO (nx: convictos A 95,0% × B 91,6%) que se converte em diferencial EFETIVO de comparecimento entre votantes de A e de B, aplicado após a ponderação pelas pesquisas (as pesquisas medem intenção, não comparecimento). κ = 0 é a hipótese do v1 (churn simétrico). Os 'convictos' são subconjuntos; estender a todos os eleitores é suposição.

| κ | diferencial efetivo A − B (relativo) | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|
| 0.00 | 0.00 p.p. | 49.07% | 48.27% – 49.88% | 2.9% |
| 0.25 | 0.91 p.p. | 49.30% | 48.50% – 50.10% | 7.6% |
| 0.50 | 1.82 p.p. | 49.53% | 48.73% – 50.33% | 16.7% |
| 1.00 | 3.64 p.p. | 49.99% | 49.18% – 50.79% | 48.8% |

**LVM de nx-r3 (validação de comparecimento, NÃO é pesquisa independente).** Na mesma amostra, excluir os 21% com menor probabilidade estimada de votar muda A de 49.46% para 47,6% dos válidos (Δ = -1.86 p.p.; arredondamento de ±0,05 p.p. no LVM). O sinal é o OPOSTO do diferencial declarado entre convictos de nx-r2 (A 95,0 × B 91,6). Sensibilidade: ω = fração do efeito LVM aplicada ao θ_A do modelo completo, depois da ponderação pelas pesquisas.

| ω (LVM nx) | deslocamento em θ_A | E[θ_A] | IC 90% | P(θ_A>0,5) |
|---|---|---|---|---|
| 0.00 | -0.00 p.p. | 49.07% | 48.27% – 49.88% | 2.9% |
| 0.25 | -0.47 p.p. | 48.61% | 47.81% – 49.41% | 0.2% |
| 0.50 | -0.93 p.p. | 48.14% | 47.34% – 48.95% | 0.0% |
| 1.00 | -1.86 p.p. | 47.21% | 46.41% – 48.01% | 0.0% |

Combinações (as duas evidências de comparecimento apontam em direções opostas):

| cenário | E[θ_A] | P(θ_A>0,5) |
|---|---|---|
| κ = 0.5, ω = 0.5 | 48.60% | 0.2% |
| κ = 0.25, ω = 0.25 | 48.84% | 0.9% |
| κ = 0.5, ω = 1.0 | 47.67% | 0.0% |
| κ = 1.0, ω = 1.0 | 48.12% | 0.0% |

### Erro comum entre pesquisas (viés compartilhado por todos os institutos, sinal não imposto)

| viés comum δ | E[θ_A] | P(θ_A>0,5) |
|---|---|---|
| -0.04 (≈-1.0 p.p. em θ_B) | 49.80% | 34.2% |
| -0.02 (≈-0.5 p.p. em θ_B) | 49.44% | 12.4% |
| +0.00 (≈+0.0 p.p. em θ_B) | 49.07% | 2.9% |
| +0.02 (≈+0.5 p.p. em θ_B) | 48.71% | 0.4% |
| +0.04 (≈+1.0 p.p. em θ_B) | 48.34% | 0.0% |
| incerto, dp 0.02 (≈0.5 p.p.) | 49.02% | 4.8% |
| incerto, dp 0.04 (≈1.0 p.p.) | 48.93% | 7.1% |

Diferença média V_B − V_A (completo, κ=0) = 2.225.856 votos; linha ABS posterior: A entre válidos = 51.6%, BN = 15.8%.

Comparecimento total (variação dos faltantes do 1T, em p.p. do eleitorado) × divisão A:B dos faltantes adicionais; célula = E[θ_A] / P(θ_A>0,5), modelo completo, κ = 0:

| comparecimento | linha ABS posterior | 50:50 | 55:45 | 60:40 | 2:1 |
|---|---|---|---|---|---|
| -2 p.p. | 49.02% / 2.5% | 49.05% / 2.9% | 48.94% / 1.7% | 48.83% / 0.9% | 48.67% / 0.4% |
| -1 p.p. | 49.05% / 2.7% | 49.06% / 2.9% | 49.01% / 2.2% | 48.95% / 1.7% | 48.88% / 1.1% |
| = 1º turno | 49.07% / 2.9% | 49.07% / 2.9% | 49.07% / 2.9% | 49.07% / 2.9% | 49.07% / 2.9% |
| +1 p.p. | 49.10% / 3.1% | 49.08% / 2.9% | 49.14% / 3.7% | 49.19% / 4.8% | 49.27% / 6.5% |
| +2 p.p. | 49.13% / 3.4% | 49.09% / 2.9% | 49.20% / 4.8% | 49.31% / 7.5% | 49.46% / 12.7% |
| +3 p.p. | 49.16% / 3.7% | 49.10% / 2.9% | 49.27% / 6.0% | 49.43% / 11.2% | 49.64% / 22.2% |
| +5 p.p. | 49.21% / 4.3% | 49.12% / 2.9% | 49.39% / 9.3% | 49.65% / 22.2% | 50.00% / 50.1% |

## Fronteira de virada recalibrada

X_AB = 4.38%, X_BA = 4.00% (médias posteriores; baseadas nas matrizes pd r1 (~11/10) e pd-r3 (19–21/10), com desconto temporal). X_BA necessário = 1.88% + 0.964 × X_AB.

| X_AB | X_BA necessário | Δ vs atual |
|---|---|---|
| 0.0% | 1.88% | -2.13 |
| 1.0% | 2.84% | -1.16 |
| 2.0% | 3.80% | -0.20 |
| 3.0% | 4.77% | +0.76 |
| 4.0% | 5.73% | +1.73 |
| 4.4% (atual) | 6.09% | +2.09 |
| 5.0% | 6.69% | +2.69 |
| 6.0% | 7.66% | +3.66 |
| 7.0% | 8.62% | +4.62 |

Ponto mais provável sobre a fronteira (só troca de votos, com correlação ρ = 0.16): X_BA = 5.06%, X_AB = 3.31%; distância ≈ 1.96 dp (dp X_BA 0.83, dp X_AB 0.85 p.p.).

