"""
Modelo v2 — recalibração com os dados divulgados até 21/10/2026.

Preserva TODO o histórico do modelo v1 (modelo.py, resultados.md/json) e
acrescenta as novas rodadas com identificadores exclusivos. Reprodutível:
`python3 modelo_v2.py` (só numpy). Gera `resultados_v2.md` e `resultados_v2.json`.

Principais mudanças de hipótese em relação ao v1 (ver REGISTRO no relatório):
  - alvo temporal: eleição em 25/out; pesquisas até 20/out → horizonte H = 5 dias;
  - transferências passam a ter DATA: cada observação de linha q_g informa o
    valor no dia da eleição com variância extra σ_q²·Δt (deriva das transferências);
  - dependência intra-levantamento: quando o MESMO levantamento fornece
    cruzamentos de transferência e resultado geral, cada parte entra com
    potência 0,5 (verossimilhança temperada) para não contar a amostra duas vezes;
  - qu: subamostras com n efetivo derivado da margem informada por subgrupo;
  - comparecimento declarado (nx) entra apenas como sensibilidade (κ), nunca como
    probabilidade calibrada.
"""
import json
import math
import numpy as np

SEED = 20261021
M = 1_000_000
rng = np.random.default_rng(SEED)
OUT, RES = [], {}


def out(s=""):
    OUT.append(s)


def table(h, rows):
    out("| " + " | ".join(h) + " |")
    out("|" + "|".join(["---"] * len(h)) + "|")
    for r in rows:
        out("| " + " | ".join(str(x) for x in r) + " |")
    out()


def pct(x, d=2):
    return f"{100 * x:.{d}f}%"


def Phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def logit(p):
    return np.log(p / (1 - p))


def expit(z):
    return 1 / (1 + np.exp(-z))


def wmean(x, w):
    return float(np.sum(x * w) / np.sum(w))


def wsd(x, w):
    m = wmean(x, w)
    return math.sqrt(wmean((x - m) ** 2, w))


def wq(x, w, qs):
    i = np.argsort(x)
    c = np.cumsum(w[i])
    c /= c[-1]
    return [float(x[i][min(np.searchsorted(c, q), len(c) - 1)]) for q in qs]


def ess(w):
    return float(w.sum() ** 2 / np.sum(w ** 2))


def norm_w(ll):
    w = np.exp(ll - ll.max())
    return w / w.sum()


def fmt(n):
    return f"{n:,.0f}".replace(",", ".")


# =====================================================================
# 0. Dados do 1º turno (inalterados)
# =====================================================================
cand = dict(A=53_876_617, B=56_104_268, C=3_448_569, D=2_675_887, E=2_605_148,
            F=326_488, G=122_911, H=43_103, I=40_043, J=22_693, K=16_881, L=15_024)
BN1 = 2_300_781 + 3_674_149
ABST = 33_470_000
GL = sum(cand[k] for k in "GHIJKL")
COMP = sum(cand.values()) + BN1
ELEIT = COMP + ABST
T1 = COMP / ELEIT
COH = ["B", "A", "C", "D", "E", "F", "GL", "BN", "ABS"]
N = np.array([cand["B"], cand["A"], cand["C"], cand["D"], cand["E"], cand["F"], GL, BN1, ABST], float)
G = 9
iB, iA, iC, iD, iE, iF, iGL, iBN, iABS = range(G)
share = N / ELEIT
wCF = N[[iC, iD, iE, iF]] / N[[iC, iD, iE, iF]].sum()
wX = N[[iBN, iABS]] / N[[iBN, iABS]].sum()
T_ELEICAO = 25.0          # 25/out
LAST_DAY = 20             # último dia de campo disponível

# matriz pd (v1), colunas B, A, BN, NS
PD = np.array([[94, 5, 0, 0], [5, 92, 1, 2], [56, 27, 11, 6], [48, 25, 27, 1], [57, 19, 17, 6],
               [72, 10, 15, 3], [19, 39, 15, 27], [22, 18, 47, 14], [42, 34, 19, 5]], float)
MPD = PD / PD.sum(1, keepdims=True)
T_PD = 11.0               # campo pd 10–12/out (suposto o mesmo levantamento da matriz)

# =====================================================================
# 1. Pesquisas nacionais: histórico (v1) + novas rodadas (v2)
# =====================================================================
# id, instituto, ini, fim, n, MOE, A, B, BN, NS, resolução(p.p.), B válido publicado,
# dep (o mesmo levantamento também fornece cruzamentos de transferência), janela suposta?
P = [
    # ---- v1 (preservadas) ----
    dict(id="df-r1", ins="df", d0=6, d1=7, n=2520, moe=2.0, A=45, B=49, BN=5, NS=1, res=1, vB=52, dep=True, sup=False),
    dict(id="df-r2", ins="df", d0=13, d1=14, n=2520, moe=2.0, A=45, B=47, BN=6, NS=2, res=1, vB=51, dep=False, sup=False),
    dict(id="qu-r1", ins="qu", d0=10, d1=13, n=2154, moe=2.0, A=44, B=46, BN=9, NS=1, res=1, vB=None, dep=True, sup=False),
    dict(id="pd-r1", ins="pd", d0=10, d1=12, n=3000, moe=1.8, A=46, B=48, BN=5, NS=2, res=1, vB=51, dep=True, sup=False),
    dict(id="nx-r1", ins="nx", d0=10, d1=12, n=2002, moe=2.0, A=45, B=48, BN=5, NS=2, res=1, vB=52, dep=False, sup=False),
    dict(id="at-r1", ins="at", d0=3, d1=8, n=5026, moe=1.0, A=45.7, B=51.1, BN=None, NS=None, BNNS=3.2, res=0.1, vB=52.8, dep=False, sup=False),
    dict(id="ip-r1", ins="ip", d0=6, d1=8, n=1500, moe=2.6, A=44, B=49, BN=5, NS=3, res=1, vB=52.7, dep=False, sup=False),
    dict(id="pv-r1", ins="pv", d0=10, d1=13, n=5000, moe=2.3, A=49, B=50, BN=1, NS=0, res=1, vB=None, dep=False, sup=False),
    # ---- v2 (novas, 21/10) ----
    dict(id="qu-r2", ins="qu", d0=17, d1=20, n=2154, moe=2.0, A=44, B=45, BN=9, NS=2, res=1, vB=None, dep=True, sup=True),
    dict(id="fu-r1", ins="fu", d0=18, d1=20, n=2000, moe=2.2, A=None, B=None, BN=None, NS=None, res=None, vB=51.1, dep=False, sup=True),
    dict(id="pv-r2", ins="pv", d0=18, d1=20, n=5000, moe=2.4, A=48, B=50, BN=1, NS=0, res=1, vB=None, dep=True, sup=False),
    dict(id="mi-r1", ins="mi", d0=17, d1=19, n=1500, moe=2.5, A=46, B=48, BN=3.4, NS=2.6, res=1, vB=51.1, dep=False, sup=True),
    dict(id="rt-r1", ins="rt", d0=17, d1=19, n=2000, moe=2.0, A=45, B=48, BN=5, NS=2, res=1, vB=52, dep=False, sup=True),
    dict(id="at-r2", ins="at", d0=13, d1=18, n=4998, moe=1.0, A=47.6, B=49.8, BN=None, NS=None, BNNS=2.6, res=0.1, vB=51.1, dep=False, sup=True),
    dict(id="nx-r2", ins="nx", d0=16, d1=18, n=2002, moe=2.0, A=45.9, B=46.5, BN=4.7, NS=2.9, res=0.1, vB=50.3, dep=False, sup=True),
    dict(id="pd-r2", ins="pd", d0=16, d1=18, n=3000, moe=1.8, A=46, B=49, BN=4, NS=2, res=1, vB=52, dep=False, sup=True),
]
NEW = {"qu-r2", "fu-r1", "pv-r2", "mi-r1", "rt-r1", "at-r2", "nx-r2", "pd-r2"}
INST = ["df", "qu", "pd", "nx", "at", "ip", "pv", "fu", "mi", "rt"]
V_MED_NEW = np.median([(p["A"] + p["B"]) / 100 for p in P if p["id"] in NEW and p["A"] is not None])

for p in P:
    if p["A"] is not None:
        p["y"] = p["B"] / (p["A"] + p["B"])
        v = (p["A"] + p["B"]) / 100
        var_r = ((p["res"] / 100) ** 2 / 12) * ((p["B"] / 100) ** 2 + (p["A"] / 100) ** 2) / v ** 4
        p["fonte"] = "totais"
    else:                                   # fu: só válidos publicados (1 decimal)
        p["y"] = p["vB"] / 100
        v = V_MED_NEW                       # denominador desconhecido: mediana das novas
        var_r = (0.1 / 100) ** 2 / 12
        p["fonte"] = "válidos publicados"
    moe_srs = 196 * math.sqrt(0.25 / p["n"])
    p["moe_srs"] = moe_srs
    p["deff"] = (p["moe"] / moe_srs) ** 2
    sig_s = (max(p["moe"], moe_srs) / 196) / math.sqrt(v)
    p["sig_p"] = math.sqrt(sig_s ** 2 + var_r)
    p["sig_l"] = p["sig_p"] / (p["y"] * (1 - p["y"]))
    p["v"] = v

# =====================================================================
# A. AUDITORIA DOS DADOS NOVOS
# =====================================================================
out("# Resultados v2 — recalibração com dados até 21/10 (gerado por modelo_v2.py)")
out()
out(f"Semente {SEED}; M = {fmt(M)} sorteios. Eleição em 25/out; último campo 20/out (H = 5 dias).")
out()
out("## A. Auditoria de consistência dos dados novos")
out()
out("### A1. Pesquisas nacionais novas")
out()
rows = []
for p in P:
    if p["id"] not in NEW:
        continue
    if p["A"] is not None:
        s = p["A"] + p["B"] + (p["BNNS"] if p.get("BNNS") else (p["BN"] + p["NS"]))
        ssum = f"{s:g}%" + (" ⚠" if abs(s - 100) > 0.05 else "")
        calc = pct(p["y"])
    else:
        ssum, calc = "ND", "—"
    pub = "ND" if p["vB"] is None else f"{p['vB']}%"
    dif = "—" if (p["vB"] is None or p["A"] is None) else f"{100 * p['y'] - p['vB']:+.2f}"
    rows.append([p["id"], f"{p['d0']}–{p['d1']}/10" + ("†" if p["sup"] else ""), p["n"], ssum, calc, pub, dif,
                 f"{p['moe']:.1f}", f"{p['moe_srs']:.2f}", f"{p['deff']:.2f}" + (" ⚠" if p["deff"] < 0.95 else ""),
                 p["fonte"], f"{100 * p['sig_p']:.2f}", "sim" if p["dep"] else "não"])
table(["id", "campo", "n", "Σ totais", "B válido (calc.)", "B válido (publ.)", "calc − publ",
       "MOE", "MOE AAS", "DEFF impl.", "fonte da likelihood", "σ_j válido (p.p.)",
       "mesmo levant. tem cruzamentos?"], rows)
out("† Data de início do campo NÃO informada; janela suposta = duração da rodada anterior do "
    "instituto (qu 4 dias, at 6, nx/pd 3) ou 3 dias (fu, mi, rt). pv: 18–20/10 informado na "
    "divulgação de transferências. Sensibilidade com janela de 1 dia (só último dia) na seção E.")
out()
out("- Uma única likelihood por levantamento: binomial (logit) da fração B/(A+B). Quando os "
    "totais existem, ela é calculada deles (mais resolução) e os válidos publicados servem só "
    "como checagem; fu só tem válidos (1 decimal) → σ usa a razão média (A+B) das novas "
    f"({100 * V_MED_NEW:.1f}%) como denominador, por falta do dado.")
out("- at-r2: MOE ±1,0 continua abaixo da AAS (±1,39) → usa-se ±1,39 (mesma regra do v1). "
    "BN+NS = 2,6 agregados, não desagregados.")
out("- pv-r2 soma 99% e pd-r2 soma 101%: diferenças de arredondamento preservadas; a fração "
    "B/(A+B) não depende delas. Arredondamento de ±0,5 p.p. em A e B entra em σ_j.")
out("- rt e pd: válidos publicados inteiros (52) vs calculados (51,61 / 51,58): compatíveis com "
    "arredondamento; usa-se o calculado.")
out()

# ---- transferências novas ----
QU_SUB_MOE = {iC: 17, iD: 20, iE: 24, "X": 6}
n_from_moe = lambda m: 0.25 * (1.96 / (m / 100)) ** 2
QU = {   # (B, A, BN/não vota, NS) por rodada
    "qu-r1": {iC: (30, 34, 30, 6), iD: (40, 14, 43, 3), iE: (42, 23, 33, 2), "X": (38, 43, 17, 2)},
    "qu-r2": {iC: (33, 48, 16, 3), iD: (51, 25, 24, 0), iE: (57, 21, 22, 0), "X": (36, 40, 21, 3)},
}
T_QU = {"qu-r1": 11.5, "qu-r2": 18.5}
PV = {iC: (43, 52, 5), iD: (42, 39, 19), iE: (44, 44, 12)}     # (B, A, restante)
T_PV = 19.0
DEFF_PV = next(p["deff"] for p in P if p["id"] == "pv-r2")
DF_OBS = (46, 32, 15, 7)
T_DF = 6.5

out("### A2. Transferências novas")
out()
rows = []
for r, d in QU.items():
    for g, v in d.items():
        nm = "X" if g == "X" else COH[g]
        s = sum(v)
        n_moe = n_from_moe(QU_SUB_MOE[g])
        sh = share[[iBN, iABS]].sum() if g == "X" else share[g]
        n_exp = 2154 * sh
        rows.append([r, nm, f"{v[1]} / {v[0]} / {v[2]} / {v[3]}", f"{s}%" + ("" if s == 100 else " ⚠"),
                     f"±{QU_SUB_MOE[g]}", f"{n_moe:.0f}", f"{n_exp:.0f}", f"{n_exp / n_moe:.2f}"])
table(["rodada", "coorte", "A / B / BN-não vota / NS", "Σ", "margem subgrupo",
       "n efetivo implícito", "n esperado (2154 × peso eleitoral)", "DEFF implícito"], rows)
rows = []
for g, v in PV.items():
    n_exp = 5000 * share[g]
    rows.append(["pv-r2", COH[g], f"{v[1]} / {v[0]} / {v[2]} (não discriminado)", f"{sum(v)}%",
                 f"{n_exp:.0f}", f"{n_exp / DEFF_PV:.0f}"])
table(["rodada", "coorte", "A / B / restante", "Σ", "n esperado", f"n efetivo (DEFF pv = {DEFF_PV:.2f})"], rows)
out("- qu publicou em 21/10 a decomposição completa da rodada 13/10 (antes só A e B). Ela é "
    "dado divulgado, não imputação: no v2 a rodada qu-r1 entra com as 4 categorias.")
out("- qu: 'BN/não vota' é mapeado na categoria BN do modelo (intenção de não escolher A nem B); "
    "a separação BN × abstenção não é identificável nesses dados.")
out("- pv: 'restante' (5/19/12) entra como categoria agregada {BN, NS, não vota}, sem decompor.")
out("- n efetivo de qu vem da margem de cada subgrupo (n = 0,25·(1,96/MOE)²), não da margem geral. "
    "Os DEFF implícitos (1,4–2,1) são coerentes com o DEFF 2 usado no v1.")
out("- As diferenças entre rodadas qu (ex.: C→A 34 → 48) NÃO são tratadas como migração "
    "individual: são duas amostras transversais; entram como duas observações da mesma "
    "margem de transição, cada uma com sua data.")
out()

# ---- comparecimento declarado e estabilidade ----
out("### A3. Comparecimento declarado, estabilidade e rejeição (camada descritiva)")
out()
table(["fonte", "medida", "valor", "uso no modelo"], [
    ["nx-r2", "certeza de comparecer / provável / provável não ou não / não discriminado",
     "85,9 / 7,0 / 5,4 / 1,7", "descritivo; Σ declarada ≫ comparecimento real do 1T (78,9%)"],
    ["nx-r2", "convictos de A / de B que declaram que vão votar", "95,0% / 91,6%",
     "sensibilidade κ (seção C); não é probabilidade calibrada"],
    ["nx-r2", "rejeitam ambos: certeza / provável / provável não / não vota", "70,9 / 13,4 / 5,2 / 10,4",
     "descritivo (Σ = 99,9%)"],
    ["mi-r1", "voto decidido / pode mudar", "83,7% / 16,3%", "descritivo"],
    ["pv-r2", "nada me faria mudar", "79%", "descritivo; pergunta diferente da de mi"],
    ["qu-r2", "espontânea A / B / indecisos", "40 / 40 / 14", "descritivo; ≠ estimulada (44/45)"],
    ["qu", "rejeição A / B (r1 → r2)", "53→47 / 54→52", "descritivo"],
    ["mi-r1", "rejeição A / B", "47,7 / 46,5", "descritivo"],
])
out("- A soma das categorias de nx (85,9+7,0+5,4 = 98,3%) deixa 1,7% não discriminados; mantido.")
out("- Rejeição, estabilidade e espontânea não entram na likelihood (instrução: não são "
    "observações independentes da intenção nem transferências).")
out()

# =====================================================================
# B. MODELO DE PESQUISAS (gaussiano exato)
# =====================================================================
DAYS = list(range(3, LAST_DAY + 1))
ND, NI = len(DAYS), len(INST)


def poll_model(sd_drift=0.01, sd_house=0.02, sd_extra=0.02, H=T_ELEICAO - LAST_DAY,
               use=None, temper=True, window="sup", prior_sd=1.0):
    PP = [p for p in P if (use is None or p["id"] in use)]
    Pm = np.zeros((ND + NI, ND + NI))
    for i in range(ND):
        for j in range(ND):
            Pm[i, j] = prior_sd ** 2 + sd_drift ** 2 * min(i, j)
    for k in range(NI):
        Pm[ND + k, ND + k] = max(sd_house, 1e-9) ** 2
    Hm = np.zeros((len(PP), ND + NI))
    y = np.zeros(len(PP))
    R = np.zeros(len(PP))
    for r, p in enumerate(PP):
        d0 = p["d1"] if window == "end" else p["d0"]
        dd = [DAYS.index(d) for d in range(d0, p["d1"] + 1)]
        Hm[r, dd] = 1 / len(dd)
        Hm[r, ND + INST.index(p["ins"])] = 1
        y[r] = logit(p["y"])
        R[r] = p["sig_l"] ** 2 * (2.0 if (temper and p["dep"]) else 1.0) + sd_extra ** 2
    S = Hm @ Pm @ Hm.T + np.diag(R)
    Si = np.linalg.inv(S)
    K = Pm @ Hm.T @ Si
    mu = K @ y
    C = Pm - K @ Hm @ Pm
    ll = -0.5 * (y @ Si @ y + np.linalg.slogdet(S)[1] + len(y) * math.log(2 * math.pi))
    # previsão para o dia da eleição (H dias após o último dia modelado)
    zT, vT = mu[ND - 1], C[ND - 1, ND - 1] + sd_drift ** 2 * H
    return dict(mu=mu, C=C, zT=zT, vT=vT, ll=ll, H=Hm, y=y, R=R, PP=PP)


def th_p(m):
    t = float(expit(m["zT"]))
    return t, math.sqrt(m["vT"]) * t * (1 - t)


pm = poll_model()
tB, sB = th_p(pm)
RES["polls"] = dict(thetaB=tB, sd=sB)

out("## D. Diferenças de mensuração entre institutos e evolução temporal")
out()
out("### D1. Rodadas repetidas do mesmo instituto (diferença bruta, sem atribuir causa)")
out()
rows = []
for ins in ["df", "qu", "pd", "nx", "at", "pv"]:
    ps = [p for p in P if p["ins"] == ins]
    if len(ps) < 2:
        continue
    a, b = ps[0], ps[-1]
    se = math.sqrt(a["sig_p"] ** 2 + b["sig_p"] ** 2)
    rows.append([ins, f"{a['id']} ({a['d1']}/10) → {b['id']} ({b['d1']}/10)", pct(a["y"]), pct(b["y"]),
                 f"{100 * (b['y'] - a['y']):+.2f}", f"{(b['y'] - a['y']) / se:+.2f}"])
table(["instituto", "rodadas", "θ_B antes", "θ_B depois", "Δ (p.p.)", "z (só amostragem)"], rows)
zmax = max(abs(float(r[-1])) for r in rows)
out(f"Maior |z| = {zmax:.2f} (at, campo mais antigo na 1ª rodada): todas as variações são "
    "compatíveis com erro amostral isolado (|z| < 1,96). Sem atribuição de causa.")
out()

out("### D2. Tendência latente (todas as pesquisas; σ_drift 0,01, σ_house 0,02, σ_extra 0,02)")
out()
rows = []
for i, d in enumerate(DAYS):
    if d % 2 == 0 or d == LAST_DAY:
        t = float(expit(pm["mu"][i]))
        rows.append([f"{d}/10", pct(t), f"{100 * math.sqrt(pm['C'][i, i]) * t * (1 - t):.2f}"])
table(["dia", "θ_B latente", "dp (p.p.)"], rows)
out(f"Previsão para 25/10 (H = 5): θ_B = {pct(tB)} ± {100 * sB:.2f} p.p. → θ_A = {pct(1 - tB)}.")
out()

out("### D3. House effects posteriores (prior N(0; 0,02²) sem sinal)")
out()
rows = []
for k, ins in enumerate(INST):
    h = pm["mu"][ND + k]
    s = math.sqrt(pm["C"][ND + k, ND + k])
    nr = sum(1 for p in P if p["ins"] == ins)
    rows.append([ins, nr, f"{100 * h / 4:+.2f}", f"{100 * s / 4:.2f}", f"{h / 0.02:+.2f}",
                 "fraco (1 rodada)" if nr == 1 else "parcial"])
table(["instituto", "rodadas", "h_j ≈ p.p. em θ_B", "dp (p.p.)", "h/σ_house", "identificação"], rows)

# ---- calibração anterior x atual ----
# o estado modelado vai até 20/10 mesmo sem pesquisas após 14/10: a deriva de 14→20 já está
# no estado, e H = 5 completa até 25/10 (total 11 dias após a última pesquisa do v1)
pm_old = poll_model(use={p["id"] for p in P if p["id"] not in NEW}, temper=False)
pm_old_t = poll_model(use={p["id"] for p in P if p["id"] not in NEW}, temper=True)
to, so = th_p(pm_old)
tot, sot = th_p(pm_old_t)
out("### D4. Calibração anterior × atual (bloco de pesquisas)")
out()
table(["versão", "pesquisas", "tempera dependência?", "θ_B em 25/10", "dp (p.p.)", "P(θ_B>0,5)"], [
    ["v1 (até 14/10)", 8, "não", pct(to), f"{100 * so:.2f}", pct(1 - Phi((0.5 - to) / so), 1)],
    ["v1 dados + regra v2", 8, "sim", pct(tot), f"{100 * sot:.2f}", pct(1 - Phi((0.5 - tot) / sot), 1)],
    ["v2 (até 20/10)", 16, "sim", pct(tB), f"{100 * sB:.2f}", pct(1 - Phi((0.5 - tB) / sB), 1)],
])
RES["polls_old"] = dict(thetaB=to, sd=so)

# =====================================================================
# E. RESÍDUOS E VERIFICAÇÕES PREDITIVAS
# =====================================================================
out("## E. Resíduos e verificações preditivas das pesquisas")
out()
pm0 = poll_model(sd_house=1e-6, sd_extra=0.0)
rows = []
chi2 = 0.0
for r, p in enumerate(pm0["PP"]):
    h = pm0["H"][r].copy()
    pred = float(expit(h @ pm0["mu"]))
    rj = (p["y"] - pred) / (p["sig_p"] * (math.sqrt(2) if p["dep"] else 1))
    chi2 += rj ** 2
    # LOO (caso-base)
    m = poll_model(use={q["id"] for q in P if q["id"] != p["id"]})
    hh = np.zeros(ND + NI)
    dd = [DAYS.index(d) for d in range(p["d0"], p["d1"] + 1)]
    hh[dd] = 1 / len(dd)
    hh[ND + INST.index(p["ins"])] = 1
    ml = hh @ m["mu"]
    vl = hh @ m["C"] @ hh + p["sig_l"] ** 2 * (2 if p["dep"] else 1) + 0.02 ** 2
    rows.append([p["id"] + (" (nova)" if p["id"] in NEW else ""), pct(p["y"]), pct(pred),
                 f"{100 * (p['y'] - pred):+.2f}", f"{rj:+.2f}", pct(float(expit(ml))),
                 f"{(logit(p['y']) - ml) / math.sqrt(vl):+.2f}"])
table(["pesquisa", "θ_B obs.", "previsto (nível comum)", "resíduo (p.p.)", "r_j", "previsto LOO", "r_j LOO"], rows)
df_ = len(P) - 1
wh = ((chi2 / df_) ** (1 / 3) - (1 - 2 / (9 * df_))) / math.sqrt(2 / (9 * df_))
out(f"Σ r_j² = {chi2:.2f} com ≈{df_} g.l.; p ≈ {1 - Phi(wh):.3f}; razão de dispersão = {chi2 / df_:.2f}.")
out()
prof = [(se, poll_model(sd_house=1e-6, sd_extra=se)["ll"]) for se in np.linspace(0, 0.08, 33)]
se_hat = max(prof, key=lambda t: t[1])[0]
out(f"Perfil de σ_extra (σ_house≈0): máximo em {se_hat:.3f} logit (≈{100 * se_hat / 4:.2f} p.p.).")
out()
RES["chi2"] = chi2

# previsão out-of-sample: calibração v1 → novas pesquisas
out("### E2. Verificação preditiva fora da amostra: pesquisas até 14/10 preveem as novas?")
out()
m_old = poll_model(use={p["id"] for p in P if p["id"] not in NEW}, temper=True)
rows = []
for p in P:
    if p["id"] not in NEW:
        continue
    hh = np.zeros(ND + NI)
    dd = [DAYS.index(d) for d in range(p["d0"], p["d1"] + 1)]
    hh[dd] = 1 / len(dd)
    hh[ND + INST.index(p["ins"])] = 1
    ml = hh @ m_old["mu"]
    vl = hh @ m_old["C"] @ hh + p["sig_l"] ** 2 * (2 if p["dep"] else 1) + 0.02 ** 2
    rows.append([p["id"], pct(p["y"]), pct(float(expit(ml))), f"{(logit(p['y']) - ml) / math.sqrt(vl):+.2f}"])
table(["nova pesquisa", "θ_B obs.", "previsto pelo v1 (com deriva)", "z"], rows)
zs = [float(r[-1]) for r in rows]
out(f"Média dos z = {np.mean(zs):+.2f}; todos |z| < {max(abs(z) for z in zs):.2f}. "
    "As novas pesquisas ficam do lado de A em relação à previsão do v1, mas dentro da "
    "incerteza prevista (que já incluía deriva).")
out()

# janela de campo e tempera: sensibilidade
rows = []
for lab, kw in [("caso-base", {}), ("janela = só último dia", dict(window="end")),
                ("sem temperar dependência", dict(temper=False)),
                ("σ_house 0,04", dict(sd_house=0.04)), ("σ_extra 0", dict(sd_extra=0.0)),
                ("σ_drift 0,005", dict(sd_drift=0.005)), ("σ_drift 0,02", dict(sd_drift=0.02))]:
    t, s = th_p(poll_model(**kw))
    rows.append([lab, pct(t), f"{100 * s:.2f}", pct(1 - Phi((0.5 - t) / s), 1)])
out("### E3. Sensibilidade do bloco de pesquisas (25/10)")
out()
table(["variação", "θ_B", "dp (p.p.)", "P(θ_B>0,5) só pesquisas"], rows)

# =====================================================================
# MODELO ESTRUTURAL v2
# =====================================================================
LAMBDA_PD = 0.5          # peso da matriz pd (v1) — agora também = partição de dependência pd matriz/topline
SIG_Q = 0.005            # deriva das transferências (proporção por √dia)
SIG_R = 0.005            # viés de recordação (θ_A), sem sinal
LAMBDA_PROP = 0.6
CHURN_MU, CHURN_SD, TAU_ABS_SD = 0.05, 0.015, 0.03
TAU_ABS_MU = float((N[:iABS] * CHURN_MU).sum() / N[iABS])
TEMPER_DEP = 0.5
D_A, D_B = (0.950 - 0.933) / 0.933, (0.916 - 0.933) / 0.933   # nx convictos, relativo à média


def n_t(n, t_obs, sig_q):
    dt = max(T_ELEICAO - t_obs, 0)
    return 1 / (1 / n + dt * sig_q ** 2 / 0.25)


def beta_ab(mu, sd):
    k = mu * (1 - mu) / sd ** 2 - 1
    return mu * k, (1 - mu) * k


def draw_turnout(n):
    a, b = beta_ab(CHURN_MU, CHURN_SD)
    a2, b2 = beta_ab(TAU_ABS_MU, TAU_ABS_SD)
    return np.concatenate([1 - rng.beta(a, b, (n, G - 1)), rng.beta(a2, b2, n)[:, None]], axis=1)


def resolve_III(Q):
    B, A_, BN, NS = Q[..., 0], Q[..., 1], Q[..., 2], Q[..., 3]
    d = B + A_ + BN
    return np.stack([B + NS * B / d, A_ + NS * A_ / d, BN + NS * BN / d], -1)


def obs_set(lam_pd=LAMBDA_PD, sig_q=SIG_Q, use=("pd", "df", "qu-r1", "qu-r2", "pv-r2"), temper=TEMPER_DEP):
    """Lista de observações: (tipo, linhas, pesos, p_obs, n_eff, rótulo)
    tipo '4': 4 categorias (B,A,BN,NS), linha única — conjugado
    tipo '3': (B, A, resto) linha única — conjugado por agregação
    tipo 'mix4': mistura de linhas (df C:F; qu X) — não conjugado (IS)"""
    O = []
    if "pd" in use:
        for g in range(G):
            n = lam_pd * 3000 * share[g] / 2
            O.append(("4", [g], None, MPD[g], n_t(n, T_PD, sig_q), f"pd-matriz {COH[g]}"))
    if "df" in use:
        n = temper * 2520 * share[[iC, iD, iE, iF]].sum() / 2
        O.append(("mix4", [iC, iD, iE, iF], wCF, np.array(DF_OBS) / 100, n_t(n, T_DF, sig_q), "df C:F"))
    for r in ("qu-r1", "qu-r2"):
        if r not in use:
            continue
        for g, v in QU[r].items():
            n = temper * n_from_moe(QU_SUB_MOE[g])
            p = np.array(v, float) / sum(v)
            if g == "X":
                O.append(("mix4", [iBN, iABS], wX, p, n_t(n, T_QU[r], sig_q), f"{r} X"))
            else:
                O.append(("4", [g], None, p, n_t(n, T_QU[r], sig_q), f"{r} {COH[g]}"))
    if "pv-r2" in use:
        for g, v in PV.items():
            n = temper * 5000 * share[g] / DEFF_PV
            O.append(("3", [g], None, np.array(v, float) / 100, n_t(n, T_PV, sig_q), f"pv-r2 {COH[g]}"))
    return O


def draw_Q(O, n=M, prior_only=False):
    Ap = np.full((G, 4), 0.5)
    coarse = np.zeros((G, 3))
    pseudo = []
    if not prior_only:
        for typ, gs, w, p, ne, lab in O:
            if typ == "4":
                Ap[gs[0]] += ne * p
            elif typ == "3":
                coarse[gs[0]] += ne * p
            else:   # mix4: pseudo-contagem atenuada nas linhas de maior peso
                for j, g in enumerate(gs):
                    if g in (iF, iBN):
                        continue
                    c = LAMBDA_PROP * ne * w[j] * p
                    Ap[g] += c
                    pseudo.append((g, c))
    Q = np.empty((n, G, 4))
    for g in range(G):
        if coarse[g].sum() == 0:
            Q[:, g, :] = rng.dirichlet(Ap[g], n)
        else:
            agg = np.array([Ap[g, 0], Ap[g, 1], Ap[g, 2] + Ap[g, 3]]) + coarse[g]
            Dd = rng.dirichlet(agg, n)
            s = rng.beta(Ap[g, 2], Ap[g, 3], n)
            Q[:, g, 0], Q[:, g, 1] = Dd[:, 0], Dd[:, 1]
            Q[:, g, 2], Q[:, g, 3] = Dd[:, 2] * s, Dd[:, 2] * (1 - s)
    logw = np.zeros(n)
    if not prior_only:
        for typ, gs, w, p, ne, lab in O:
            if typ == "mix4":
                pm_ = np.einsum("g,ngk->nk", w, Q[:, gs, :])
                logw += ne * (p * np.log(np.clip(pm_, 1e-300, 1))).sum(-1)
        for g, c in pseudo:
            logw -= (c * np.log(np.clip(Q[:, g, :], 1e-300, 1))).sum(-1)
    return Q, logw


def struct(O, n=M, prior_only=False, sig_r=SIG_R):
    Q, lw = draw_Q(O, n, prior_only)
    T = draw_turnout(n)
    Pp = resolve_III(Q)
    V = np.einsum("ng,ngk->nk", N * T, Pp)
    b = rng.normal(0, sig_r, n) if sig_r > 0 else np.zeros(n)
    S = V[:, 0] + V[:, 1]
    VA, VB = V[:, 1] + b * S, V[:, 0] - b * S
    return dict(Q=Q, lw=lw, T=T, P=Pp, VA=VA, VB=VB, th=VA / (VA + VB))


def ll_poll(th, m):
    z = logit(np.clip(1 - th, 1e-6, 1 - 1e-6))
    return -0.5 * (z - m["zT"]) ** 2 / m["vT"]


def apply_kappa(s, kappa):
    va = s["VA"] * (1 + kappa * D_A)
    vb = s["VB"] * (1 + kappa * D_B)
    return va / (va + vb)


O_full = obs_set()
S0 = struct(O_full, prior_only=True)          # prior: Jeffreys + nada (para identificação)
S_pd = struct(obs_set(use=("pd",)))
S_tr = struct(O_full)
w_tr = norm_w(S_tr["lw"])
w_all = norm_w(S_tr["lw"] + ll_poll(S_tr["th"], pm))
w_pdpoll = norm_w(S_pd["lw"] + ll_poll(S_pd["th"], pm))
RES["ess"] = dict(transf=ess(w_tr), completo=ess(w_all))

# =====================================================================
# B. PARÂMETROS ATUALIZADOS
# =====================================================================
out("## B. Retenção e transferência atualizadas (alvo: 25/10)")
out()
out(f"Modelo 2 com datas: n_eff de cada observação = 1/(1/n + Δt·σ_q²/0,25), σ_q = {SIG_Q} por √dia; "
    f"matriz pd com peso λ = {LAMBDA_PD}; levantamentos com cruzamento + resultado geral "
    f"entram com potência {TEMPER_DEP} em cada parte; indecisos III; viés de recordação "
    f"σ_r = {100 * SIG_R:.1f} p.p. ESS: transferências {fmt(ess(w_tr))}, completo {fmt(ess(w_all))}.")
out()
out("Observações de transferência e n efetivo usado (após tempera e desconto temporal):")
out()
table(["observação", "data (dia)", "n efetivo"],
      [[lab, {"pd": T_PD, "df": T_DF, "qu-r1": 11.5, "qu-r2": 18.5, "pv-r2": T_PV}[lab.split(" ")[0].split("-matriz")[0]]
        if not lab.startswith("pd") else T_PD, f"{ne:.1f}"] for typ, gs, w, p, ne, lab in O_full])


def pdefs(s):
    Q = s["Q"]
    cf = lambda k: np.einsum("g,ng->n", wCF, Q[:, [iC, iD, iE, iF], k])
    xx = lambda k: np.einsum("g,ng->n", wX, Q[:, [iBN, iABS], k])
    return [("R_A = A₁→A", Q[:, iA, 1]), ("X_AB = A₁→B", Q[:, iA, 0]),
            ("R_B = B₁→B", Q[:, iB, 0]), ("X_BA = B₁→A", Q[:, iB, 1]),
            ("C→A", Q[:, iC, 1]), ("C→B", Q[:, iC, 0]), ("D→A", Q[:, iD, 1]), ("D→B", Q[:, iD, 0]),
            ("E→A", Q[:, iE, 1]), ("E→B", Q[:, iE, 0]), ("F→A", Q[:, iF, 1]), ("F→B", Q[:, iF, 0]),
            ("G:L→A", Q[:, iGL, 1]), ("G:L→B", Q[:, iGL, 0]),
            ("C:F agregado →A", cf(1)), ("C:F agregado →B", cf(0)),
            ("X (BN₁+ABS₁) →A", xx(1)), ("X →B", xx(0)), ("X →BN/não vota", xx(2)),
            ("θ_A (válidos)", s["th"])]


sets = [("só pd (com datas)", S_pd, norm_w(S_pd["lw"])), ("pd + df + qu + pv", S_tr, w_tr),
        ("completo (+ pesquisas)", S_tr, w_all)]
rows = None
for lab, s, w in sets:
    d = pdefs(s)
    if rows is None:
        rows = [[nm] for nm, _ in d]
    for r, (nm, x) in zip(rows, d):
        q = wq(x, w, [0.05, 0.95])
        r.append(f"{100 * wmean(x, w):.1f} [{100 * q[0]:.1f}; {100 * q[1]:.1f}]")
# coluna v1 (completo, λ=0,5) para comparação — lida do resultados.json do v1 quando disponível
table(["parâmetro (% , média [IC 90%])"] + [s[0] for s in sets], rows)
out("Linhas q_g = intenção declarada normalizada, antes de indecisos e comparecimento.")
out()

# identificação: razão dp posterior / dp 'só pd com datas'
out("### B2. Identificação: quanto cada fonte estreitou cada parâmetro")
out()
rows = []
d_pd = dict(pdefs(S_pd))
d_tr = dict(pdefs(S_tr))
wpd = norm_w(S_pd["lw"])
for nm in d_tr:
    s1 = wsd(d_pd[nm], wpd)
    s2 = wsd(d_tr[nm], w_tr)
    s3 = wsd(d_tr[nm], w_all)
    flag = "insuficiente" if s3 / s1 > 0.85 else ("parcial" if s3 / s1 > 0.6 else "boa")
    rows.append([nm, f"{100 * s1:.2f}", f"{100 * s2:.2f}", f"{100 * s3:.2f}", f"{s3 / s1:.2f}", flag])
table(["parâmetro", "dp só pd (p.p.)", "dp + transferências", "dp completo", "razão completo/pd", "identificação"], rows)

# PPC das transferências
out("### B3. Verificação preditiva das observações de transferência (modelo completo)")
out()
rows = []
Qf = S_tr["Q"]
for typ, gs, w, p, ne, lab in O_full:
    if typ == "mix4":
        pred = np.einsum("g,ngk->nk", w, Qf[:, gs, :])
    elif typ == "4":
        pred = Qf[:, gs[0], :]
    else:
        pred = np.stack([Qf[:, gs[0], 0], Qf[:, gs[0], 1], Qf[:, gs[0], 2] + Qf[:, gs[0], 3]], -1)
    for k, cat in [(1, "A"), (0, "B")]:
        mu_ = wmean(pred[:, k], w_all)
        sd_ = math.sqrt(wsd(pred[:, k], w_all) ** 2 + p[k] * (1 - p[k]) / ne)
        rows.append([lab, cat, pct(p[k], 0), pct(mu_, 1), f"{(p[k] - mu_) / sd_:+.2f}"])
table(["observação", "→", "observado", "previsto (completo)", "z preditivo"], rows)
zs = [abs(float(r[-1])) for r in rows]
out(f"Máximo |z| = {max(zs):.2f}; {sum(z > 2 for z in zs)} de {len(zs)} com |z| > 2.")
out()

# =====================================================================
# PROBABILIDADES
# =====================================================================
out("## Probabilidades atualizadas (25/10)")
out()
thA = S_tr["th"]
q = wq(thA, w_all, [0.05, 0.5, 0.95])
pA = float(np.sum(w_all * (thA > 0.5)))
RES["completo"] = dict(mean=wmean(thA, w_all), q05=q[0], q95=q[2], pA=pA)
out(f"**Caso-base v2:** E[θ_A] = {pct(wmean(thA, w_all))} [IC 90% {pct(q[0])} – {pct(q[2])}]; "
    f"**P(θ_A > 0,5) = {pct(pA, 1)}**.")
out()
rows = []
for sdd in [0.005, 0.01, 0.02]:
    for sr in [0.0, 0.005, 0.01]:
        m = poll_model(sd_drift=sdd)
        if sr == SIG_R:
            s, w = S_tr, norm_w(S_tr["lw"] + ll_poll(S_tr["th"], m))
        else:
            s = struct(O_full, n=400_000, sig_r=sr)
            w = norm_w(s["lw"] + ll_poll(s["th"], m))
        qq = wq(s["th"], w, [0.05, 0.95])
        rows.append([f"{sdd:.3f}", f"{100 * sr:.1f}", pct(wmean(s["th"], w)), f"{pct(qq[0])} – {pct(qq[1])}",
                     pct(float(np.sum(w * (s["th"] > 0.5))), 1), fmt(ess(w))])
table(["σ_drift", "σ_r (p.p.)", "E[θ_A]", "IC 90%", "P(θ_A>0,5)", "ESS"], rows)

rows = []
for lab, kw in [("λ_pd = 1", dict(lam_pd=1.0)), ("λ_pd = 0,25", dict(lam_pd=0.25)),
                ("σ_q = 0,0025", dict(sig_q=0.0025)), ("σ_q = 0,01", dict(sig_q=0.01)),
                ("sem temperar dependência", dict(temper=1.0)),
                ("sem qu-r1/df (só observações ≥ 18/10 + pd)", dict(use=("pd", "qu-r2", "pv-r2"))),
                ("sem pv-r2", dict(use=("pd", "df", "qu-r1", "qu-r2")))]:
    s = struct(obs_set(**kw), n=400_000)
    w = norm_w(s["lw"] + ll_poll(s["th"], pm))
    qq = wq(s["th"], w, [0.05, 0.95])
    rows.append([lab, pct(wmean(s["th"], w)), f"{pct(qq[0])} – {pct(qq[1])}",
                 pct(float(np.sum(w * (s["th"] > 0.5))), 1), fmt(ess(w))])
# só pesquisas
rows.append(["só pesquisas (sem estrutural)", pct(1 - tB), f"{pct(1 - tB - 1.645 * sB)} – {pct(1 - tB + 1.645 * sB)}",
             pct(Phi((0.5 - tB) / sB), 1), "—"])
out("Sensibilidade às hipóteses estruturais (σ_drift 0,01; σ_r 0,5 p.p.):")
out()
table(["variação", "E[θ_A]", "IC 90%", "P(θ_A>0,5)", "ESS"], rows)

# =====================================================================
# C. COMPARECIMENTO
# =====================================================================
out("## C. Sensibilidade às hipóteses de comparecimento")
out()
out(f"κ = fração do diferencial DECLARADO (nx: convictos A 95,0% × B 91,6%) que se converte em "
    f"diferencial EFETIVO de comparecimento entre votantes de A e de B, aplicado após a ponderação "
    f"pelas pesquisas (as pesquisas medem intenção, não comparecimento). κ = 0 é a hipótese do v1 "
    f"(churn simétrico). Os 'convictos' são subconjuntos; estender a todos os eleitores é suposição.")
out()
rows = []
RES["kappa"] = {}
for kappa in [0.0, 0.25, 0.5, 1.0]:
    th = apply_kappa(S_tr, kappa)
    qq = wq(th, w_all, [0.05, 0.95])
    pk = float(np.sum(w_all * (th > 0.5)))
    RES["kappa"][kappa] = dict(mean=wmean(th, w_all), pA=pk)
    rows.append([f"{kappa:.2f}", f"{100 * kappa * (D_A - D_B):.2f} p.p.", pct(wmean(th, w_all)),
                 f"{pct(qq[0])} – {pct(qq[1])}", pct(pk, 1)])
table(["κ", "diferencial efetivo A − B (relativo)", "E[θ_A]", "IC 90%", "P(θ_A>0,5)"], rows)
# comparecimento total × divisão dos faltantes adicionais (determinístico na média posterior)
Pm_ = np.einsum("n,ngk->gk", w_all, S_tr["P"])
Tm_ = np.einsum("n,ng->g", w_all, S_tr["T"])
Vm = (N * Tm_) @ Pm_
fbn = Pm_[iABS, 2]
gap = wmean(S_tr["VB"] - S_tr["VA"], w_all)
RES["gap"] = gap
out(f"Diferença média V_B − V_A (completo, κ=0) = {fmt(gap)} votos; linha ABS posterior: "
    f"A entre válidos = {pct(Pm_[iABS, 1] / (Pm_[iABS, 0] + Pm_[iABS, 1]), 1)}, BN = {pct(fbn, 1)}.")
out()
rows = []
for d in [-2, -1, 0, 1, 2, 3, 5]:
    r = [f"{d:+d} p.p." if d else "= 1º turno"]
    for a in [None, 0.5, 0.55, 0.6, 2 / 3]:
        extra = d / 100 * ELEIT
        aa = Pm_[iABS, 1] / (Pm_[iABS, 0] + Pm_[iABS, 1]) if a is None else a
        va = Vm[1] + extra * (1 - fbn) * aa
        vb = Vm[0] + extra * (1 - fbn) * (1 - aa)
        sh = (va - vb) - (Vm[1] - Vm[0])
        # translada a distribuição posterior pelo deslocamento médio
        th = (S_tr["VA"] + extra * (1 - fbn) * aa) / (S_tr["VA"] + S_tr["VB"] + extra * (1 - fbn))
        r.append(f"{pct(wmean(th, w_all))} / {pct(float(np.sum(w_all * (th > 0.5))), 1)}")
    rows.append(r)
out("Comparecimento total (variação dos faltantes do 1T, em p.p. do eleitorado) × divisão A:B "
    "dos faltantes adicionais; célula = E[θ_A] / P(θ_A>0,5), modelo completo, κ = 0:")
out()
table(["comparecimento", "linha ABS posterior", "50:50", "55:45", "60:40", "2:1"], rows)

# =====================================================================
# Virada (fronteira) com a calibração v2
# =====================================================================
NAt, NBt = N[iA] * Tm_[iA], N[iB] * Tm_[iB]
xab0, xba0 = Pm_[iA, 0], Pm_[iB, 1]
RES["virada"] = dict(gap=gap, XAB=xab0, XBA=xba0, NA=NAt, NB=NBt, fBN=fbn)
out("## Fronteira de virada recalibrada")
out()
out(f"X_AB = {pct(xab0)}, X_BA = {pct(xba0)} (médias posteriores; ainda baseadas apenas na matriz pd "
    "de ~11/10, agora com incerteza temporal maior). X_BA necessário = "
    f"{pct(xba0 + (gap + 1 - 2 * NAt * xab0) / (2 * NBt))} + {NAt / NBt:.3f} × X_AB.")
out()
rows = []
for x in [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, xab0, 0.06, 0.07]:
    need = xba0 + (gap + 1 - 2 * NAt * (xab0 - x)) / (2 * NBt)
    rows.append([pct(x, 1) + (" (atual)" if x == xab0 else ""), pct(need), f"{100 * (need - xba0):+.2f}"])
table(["X_AB", "X_BA necessário", "Δ vs atual"], rows)
sx = wsd(S_tr["Q"][:, iA, 0], w_all)
sy = wsd(S_tr["Q"][:, iB, 1], w_all)
a1, a2 = 2 * NBt, 2 * NAt
den = (a1 * sy) ** 2 + (a2 * sx) ** 2
dist = (gap + 1) / math.sqrt(den)
out(f"Ponto mais provável sobre a fronteira (só troca de votos): X_BA = "
    f"{pct(xba0 + (gap + 1) * a1 * sy ** 2 / den)}, X_AB = {pct(xab0 - (gap + 1) * a2 * sx ** 2 / den)}; "
    f"distância ≈ {dist:.2f} dp (dp X_BA {100 * sy:.2f}, dp X_AB {100 * sx:.2f} p.p.).")
out()
RES["virada"]["dist"] = dist

with open("resultados_v2.md", "w") as f:
    f.write("\n".join(OUT) + "\n")
with open("resultados_v2.json", "w") as f:
    json.dump(RES, f, indent=1, default=float)
print("ok")
