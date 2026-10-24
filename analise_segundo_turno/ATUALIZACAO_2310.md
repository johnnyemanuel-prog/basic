# Atualização de 23/10 — recalibração v3

Esta versão incorpora df-r3 (20–22/10) e pd-r3 (19–21/10).

- **O que foi preservado:** todas as rodadas e versões anteriores.
  - v1: `modelo.py` e `RELATORIO.md`.
  - v2: `modelo_v2.py` e `ATUALIZACAO_2110.md`.
- **Onde está a versão nova:** o código em `modelo_v3.py`, as tabelas completas em `resultados_v3.md` e os números principais em `resultados_v3.json` (semente 20261023, 1.000.000 de sorteios).
- **Datas:** eleição em 25/10 e último dia de campo em 22/10, o que dá um horizonte de 3 dias.

As probabilidades são **condicionais às hipóteses**. Não são previsões.

---

## 1. Auditoria dos dados novos

### Pesquisas nacionais

| id | Campo | n | Σ totais | B/(A+B) calculado | B válido publicado | Margem usada |
|---|---|---:|---|---:|---:|---|
| df-r3 | 20–22/10 | 2.520 | 100 % | 50,54 % | 50,47 % | ±2,00 * |
| pd-r3 | 19–21/10 | 4.000 | **101 %** (arredondamento) | 50,52 % | 51 % | ±1,56 * |

\* **Nenhuma das duas margens foi informada.** Usei a margem de amostragem aleatória simples (AAS) do n declarado, multiplicada pela raiz do DEFF implícito da rodada anterior do mesmo instituto (df 1,05; pd 1,01).

- **Total e válido não foram duplicados (regra 3).** Cada levantamento entra uma única vez, como B/(A+B) calculado dos totais. Os válidos publicados servem só de checagem.
  - df: a diferença de 0,07 p.p. entre calculado e publicado vem do arredondamento dos totais.
  - pd: o publicado (51 %) está arredondado para inteiro.
- **vx, ip, ve, al e rt.**
  - ip (ip-r1, 6–8/10) e rt (rt-r1, 17–19/10) **já estão no modelo** como observações independentes. Não foram duplicados.
  - **vx, ve e al não aparecem em nenhuma tabela recebida.** Não há números para incluir, e eles **não foram imputados**. Se você enviar os dados (campo, n, margem e totais ou válidos), entram como rodadas novas.

### Transferências pd-r3 e df-r3

| Coorte | A / B / BN / NS | Σ | Observação |
|---|---|---|---|
| A₁ | **95** / 4 / resto 1 | 100 | Retenção declarada + migração direta; o 1 % restante não está discriminado |
| B₁ | 3 / **96** / resto 1 | 100 | Idem |
| C | 48 / 42 / 8 / 2 | 100 | |
| D | 34 / 49 / 17 / 1 | **101** | Arredondamento; linha normalizada |
| E | 30 / 49 / 20 / 1 | 100 | |
| F:L | 20 / 70 / 6 / 4 | 100 | Agregado de F e G:L; entra como mistura ponderada pelos votos |
| BN₁ | 46 / 23 / 7 / **24** | 100 | NS alto |
| ABS₁ | 48 / 39 / 11 / 3 | **101** | Arredondamento; linha normalizada |
| df-r3 C:F | 26 / 47 / 21 / 6 | 100 | Agregado; mistura ponderada pelos votos |

**Como as regras foram aplicadas:**
- **Regra 2 (voto firme ≠ retenção).** 95 % e 96 % são as frações de cada coorte do 1º turno que declaram o mesmo voto agora; isso é retenção. Os indicadores de "voto decidido" (mi 83,7 %; pv 79 %) medem firmeza, não retenção, e continuam só descritivos.
- **Regra 4 (subamostras com erro adicional).** Cada subamostra recebe:
  - n efetivo = n × peso eleitoral da coorte ÷ DEFF_sub, com DEFF_sub = 2;
  - potência 0,5, porque cruzamentos e resultado geral vêm do mesmo levantamento;
  - desconto temporal σ_q²·Δt.
- **Regra 5 (comparecimento separado da intenção).** O comparecimento declarado pela pd (certeza 95 %, talvez 3 %, não 1 %, NS 1 %) fica na camada descritiva. A soma de 98 % está muito acima do comparecimento real do 1º turno (78,9 %).
- **Regra 7 (variação amostral ≠ mudança individual).** Algumas diferenças entre pd-r1 e pd-r3 são grandes, mas vêm de amostras diferentes: BN₁→A foi de 18 para 46, e A→B de 5 para 4. Entram como duas observações datadas e **não** como migração comprovada. O mesmo vale para df C:F→A, de 32 (r1) para 26 (r3).

---

## 2. Instituto e tempo (regra 6)

**Rodadas consecutivas novas:**

| Instituto | Rodadas | θ_B | Δ (p.p.) | z |
|---|---|---|---:|---:|
| df | 14/10 → 22/10 | 51,09 → 50,54 | −0,55 | −0,36 |
| pd | 18/10 → 21/10 | 51,58 → 50,52 | −1,06 | −0,83 |

Nenhuma variação entre rodadas consecutivas de qualquer instituto chega a |z| = 1,96. O maior valor continua sendo at, com 1,64.

**Tendência latente** (passeio aleatório + house effects): θ_B vai de 51,9 % (4/10) para 51,3 % (14/10) e 51,0 % (22/10). A previsão para 25/10 é **θ_B = 51,04 % ± 0,74 p.p.**

**House effects:** todos ficam entre −0,12 e +0,17 p.p. (dp ≈ 0,45), e nenhum instituto se destaca.

**Resíduos:** todas as 18 pesquisas têm |r_j| < 1,1. Σ r² = 3,6 para 17 graus de liberdade, ou seja, não há sobredispersão.

**Previsão fora da amostra:** o modelo ajustado só com as pesquisas até 20/10 previu df-r3 e pd-r3 com z de −0,36 e −0,49. Ambas vieram um pouco mais favoráveis a A, mas dentro do previsto.

| Versão (só pesquisas, 25/10) | θ_B | dp | P(θ_B > 0,5) |
|---|---:|---:|---:|
| v1 (até 14/10) | 51,48 % | 1,03 | 92,6 % |
| v2 (até 20/10) | 51,19 % | 0,78 | 93,5 % |
| **v3 (até 22/10)** | **51,04 %** | **0,74** | **92,0 %** |

---

## 3. Parâmetros atualizados

Médias para 25/10 [IC 90 %], modelo completo:

| Parâmetro | v3 | v2 | O que mudou |
|---|---|---|---|
| R_A = A₁→A | **93,6 [91,8; 95,2]** | 91,6 [88,4; 94,4] | Nova matriz pd-r3 (95 % declarado) |
| X_AB = A₁→B | **4,4 [3,1; 5,9]** | 5,0 [2,9; 7,4] | Idem |
| R_B = B₁→B | **95,3 [93,7; 96,7]** | 94,2 [91,6; 96,4] | Idem (96 % declarado) |
| X_BA = B₁→A | **3,9 [2,6; 5,3]** | 5,3 [3,2; 7,8] | Idem (3 % declarado) |
| C→A / C→B | 41,0 / 40,8 | 40,3 / 40,1 | Estável |
| D→A / D→B | 27,3 / 45,7 | 26,4 / 44,7 | Estável |
| E→A / E→B | 27,8 / 49,2 | 28,3 / 49,3 | Estável |
| C:F agregado →A / →B | 32,2 / 45,3 | 31,9 / 44,3 | Estável |
| X (BN₁+ABS₁) →A / →B | **41,0 / 37,1** | 37,4 / 37,5 | Linhas BN₁ e ABS₁ de pd-r3 pendem para A |
| **θ_A (válidos)** | **48,9 [47,9; 49,8]** | 48,7 [47,6; 49,8] | +0,2 p.p. |

A diferença média entre B e A caiu para **2,68 milhões de votos** (3,04 mi no v2; 3,76 mi no v1).

**O que a nova matriz pd mudou:**
- **A troca direta entre os finalistas passou a ser medida duas vezes** (pd-r1 e pd-r3), e a incerteza caiu à metade (dp de ≈ 1,4 para ≈ 0,85 p.p.).
- **Os valores medidos não ajudam A.** A troca direta agora favorece levemente B: 4,4 % de A para B contra 3,9 % de B para A. Ao mesmo tempo, a retenção subiu dos dois lados.
- **O ganho de A vem de outro lugar:** os brancos/nulos e os faltantes do 1º turno.

---

## 4. Probabilidades (25/10)

**Caso-base v3:** E[θ_A] = **48,89 %** [47,93 – 49,84 %]; **P(θ_A > 0,5) = 2,7 %**. É o mesmo valor do v2: a média subiu, mas a incerteza caiu.

| Variação | E[θ_A] | P(θ_A > 0,5) |
|---|---:|---:|
| Deriva diária (σ_drift) 0,005 / **0,01** / 0,02 | 48,79 / **48,89** / 48,90 % | 0,3 / **2,7** / 7,1 % |
| Viés de recordação σ_r 0 / 1,0 p.p. | 48,87 / 48,91 % | 1,9 / 4,4 % |
| σ_drift 0,02 e σ_r 1,0 | 48,96 % | 11,9 % |
| Peso da matriz pd λ = 1 / 0,25 | 48,80 / 48,94 % | 1,9 / 3,8 % |
| Sem temperar a dependência | 48,94 % | 3,0 % |
| Só observações de 18/10 em diante | 49,03 % | 5,5 % (ESS 1,1 mil) |
| Sem pd-r3 e df-r3 (equivale ao v2) | 48,84 % | 3,4 % |
| Só pesquisas | 48,96 % | 8,0 % |

**Comparecimento.** κ é a fração do diferencial declarado por nx (convictos de A 95 % contra convictos de B 91,6 %) que vira diferença real de comparecimento. É só um cenário, não está no caso-base.

| κ | E[θ_A] | P(θ_A > 0,5) |
|---:|---:|---:|
| 0 (caso-base) | 48,89 % | 2,7 % |
| 0,25 | 49,11 % | 6,3 % |
| 0,5 | 49,34 % | 12,6 % |
| 1 | 49,80 % | 36,3 % |

**Faixa:**
- Sem comparecimento diferencial: **P ≈ 2 a 7 %**. O teto chega a cerca de 12 % se o viés de recordação for de 1 p.p. e a deriva for alta.
- Com κ entre 0,25 e 0,5: **6 a 13 %**.
- Só com as pesquisas: 8 %.

**Fronteira de virada (com a correlação entre os dois fluxos, ρ = 0,13):**
- **Regra:** X_BA necessário = 2,15 % + 0,962 × X_AB.
- **No ponto atual** (4,5 % de A indo para B), B→A precisaria chegar a **6,4 %**, contra 3,9 % estimados hoje.
- **Ponto mais provável sobre a fronteira:** B→A 5,2 % e A→B 3,1 %, a **2,3 dp** do esperado (no v2 era 1,5 dp).
- **Por que ficou mais longe**, embora a diferença em votos seja menor: a troca direta agora é medida com mais precisão, e seu centro pende levemente para B.

---

## 5. Identificação ainda insuficiente

- **Troca direta entre os finalistas (R_A, R_B, X_AB, X_BA).** A precisão melhorou com pd-r3, mas as duas matrizes vêm do mesmo instituto. Não é possível separar house effect do instituto e mudança real.
- **Linhas F e G:L, inclusive o agregado F:L:** o prior domina.
- **Separação entre BN e abstenção; κ; comparecimento por coorte; viés comum a todos os institutos.**
- **NS de 24 % entre os brancos/nulos do 1º turno (pd-r3):** o destino desse grupo depende da regra usada para os indecisos (método III).

## 6. Hipóteses

- **Alteradas:**
  - horizonte de 3 dias;
  - margem de df-r3 e pd-r3 imputada como AAS × √DEFF, porque não foi informada;
  - fronteira de virada passa a considerar a correlação entre X_AB e X_BA;
  - nova regra de leitura da retenção declarada: o 1 % restante entra como categoria não discriminada.
- **Mantidas:** todas as demais (ver `ATUALIZACAO_2110.md`, seção 7).
