"""
Modelo estrutural + pesquisas para um segundo turno hipotético A x B.

Reprodutível: `python3 modelo.py` (só numpy). Semente fixa.
Gera `resultados.md` (todas as tabelas) e `resultados.json`.

Convenções
  - coortes g: B, A, C, D, E, F, GL (G:L), BN (branco+nulo 1T), ABS (abstenção 1T)
  - colunas de preferência: (B, A, BN, NS)  -- mesma ordem da matriz pd
  - θ_A = V_A / (V_A + V_B); θ_B = 1 - θ_A
  - "logit" sempre de θ_B nas pesquisas (z_t = logit θ_B,t)
"""
import json
import math
import numpy as np

SEED = 20261015
M = 1_000_000                       # sorteios de Monte Carlo (>= 500.000)
rng = np.random.default_rng(SEED)
OUT = []                          # linhas do markdown
RES = {}                          # resultados numéricos


def out(s=""):
    OUT.append(s)


def table(header, rows, fmt=None):
    out("| " + " | ".join(header) + " |")
    out("|" + "|".join(["---"] * len(header)) + "|")
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


def wq(x, w, qs):
    """quantis ponderados"""
    idx = np.argsort(x)
    xs, ws = x[idx], w[idx]
    c = np.cumsum(ws)
    c /= c[-1]
    return [float(xs[np.searchsorted(c, q)]) for q in qs]


def wmean(x, w):
    return float(np.sum(x * w) / np.sum(w))


def ess(w):
    return float(w.sum() ** 2 / np.sum(w ** 2))


# =====================================================================
# 1. AUDITORIA DOS DADOS
# =====================================================================
cand = dict(A=53_876_617, B=56_104_268, C=3_448_569, D=2_675_887,
            E=2_605_148, F=326_488, G=122_911, H=43_103, I=40_043,
            J=22_693, K=16_881, L=15_024)
BRANCOS, NULOS = 2_300_781, 3_674_149
ABST = 33_470_000                 # "aproximadamente 33,47 milhões"

tot_cand = sum(cand.values())
CL = sum(cand[k] for k in "CDEFGHIJKL")
GL = sum(cand[k] for k in "GHIJKL")
CF = sum(cand[k] for k in "CDEF")
BN = BRANCOS + NULOS
COMP = tot_cand + BN
ELEIT = COMP + ABST
T1 = COMP / ELEIT

out("# Resultados numéricos (gerado por modelo.py)")
out()
out(f"Semente = {SEED}; sorteios Monte Carlo M = {M:,}".replace(",", "."))
out()
out("## A. Auditoria aritmética")
out()
rows = []
for k, v in cand.items():
    rows.append([k, f"{v:,}".replace(",", "."), pct(v / tot_cand, 3),
                 pct(v / COMP, 3), pct(v / ELEIT, 3)])
rows.append(["**Σ candidatos**", f"{tot_cand:,}".replace(",", "."), "100%",
             pct(tot_cand / COMP, 3), pct(tot_cand / ELEIT, 3)])
rows.append(["C:L", f"{CL:,}".replace(",", "."), pct(CL / tot_cand, 3),
             pct(CL / COMP, 3), pct(CL / ELEIT, 3)])
rows.append(["C:F", f"{CF:,}".replace(",", "."), pct(CF / tot_cand, 3),
             pct(CF / COMP, 3), pct(CF / ELEIT, 3)])
rows.append(["G:L", f"{GL:,}".replace(",", "."), pct(GL / tot_cand, 3),
             pct(GL / COMP, 3), pct(GL / ELEIT, 3)])
rows.append(["Brancos", f"{BRANCOS:,}".replace(",", "."), "—",
             pct(BRANCOS / COMP, 3), pct(BRANCOS / ELEIT, 3)])
rows.append(["Nulos", f"{NULOS:,}".replace(",", "."), "—",
             pct(NULOS / COMP, 3), pct(NULOS / ELEIT, 3)])
rows.append(["**BN**", f"{BN:,}".replace(",", "."), "—",
             pct(BN / COMP, 3), pct(BN / ELEIT, 3)])
rows.append(["**Comparecimento**", f"{COMP:,}".replace(",", "."), "—",
             "100%", pct(COMP / ELEIT, 3)])
rows.append(["Abstenção (aprox.)", f"{ABST:,}".replace(",", "."), "—", "—",
             pct(ABST / ELEIT, 3)])
rows.append(["**Eleitorado implícito**", f"{ELEIT:,}".replace(",", "."),
             "—", "—", "100%"])
table(["Item", "Votos", "% válidos (cand.)", "% comparecimento",
       "% eleitorado"], rows)
out(f"- Diferença B − A no 1º turno: {cand['B'] - cand['A']:,} votos "
    f"({pct((cand['B'] - cand['A']) / tot_cand, 3)} dos válidos).".replace(",", "."))
out(f"- θ_A no 1º turno restrito a A+B: "
    f"{pct(cand['A'] / (cand['A'] + cand['B']), 3)}")
ordem_ok = all(cand[a] >= cand[b] for a, b in zip("CDEFGHIJK", "DEFGHIJKL"))
out(f"- Ordem C ≥ D ≥ … ≥ L: {'OK' if ordem_ok else 'VIOLADA'}")
out("- Abstenção é aproximada (±5 mil por arredondamento a 0,01 mi); "
    "o eleitorado é derivado, não informado.")
out()

# coortes
COH = ["B", "A", "C", "D", "E", "F", "GL", "BN", "ABS"]
N = np.array([cand["B"], cand["A"], cand["C"], cand["D"], cand["E"],
              cand["F"], GL, BN, ABST], float)
G = len(COH)
iB, iA, iC, iD, iE, iF, iGL, iBN, iABS = range(G)
share_el = N / ELEIT

# matriz pd (B, A, BN, NS)
PD = np.array([[94, 5, 0, 0], [5, 92, 1, 2], [56, 27, 11, 6],
               [48, 25, 27, 1], [57, 19, 17, 6], [72, 10, 15, 3],
               [19, 39, 15, 27], [22, 18, 47, 14], [42, 34, 19, 5]], float)
rowsum = PD.sum(1)
MPD = PD / rowsum[:, None]
out("### Matriz pd: somas das linhas e normalização")
out()
rows = []
for g in range(G):
    rows.append([COH[g], f"{rowsum[g]:.0f}%",
                 "OK" if rowsum[g] == 100 else f"**{rowsum[g] - 100:+.0f} p.p.**",
                 *[pct(x, 2) for x in MPD[g]]])
table(["Coorte", "Σ publicado", "resíduo", "B norm.", "A norm.", "BN norm.",
       "NS norm."], rows)

# =====================================================================
# 2. PESQUISAS
# =====================================================================
# (nome, instituto, dia_ini, dia_fim, n, MOE pp, A, B, BN, NS, resolução do arredondamento pp)
POLLS = [
    ("df-1", "df", 6, 7, 2520, 2.0, 45, 49, 5, 1, 1.0),
    ("df-2", "df", 13, 14, 2520, 2.0, 45, 47, 6, 2, 1.0),
    ("qu", "qu", 10, 13, 2154, 2.0, 44, 46, 9, 1, 1.0),
    ("pd", "pd", 10, 12, 3000, 1.8, 46, 48, 5, 2, 1.0),
    ("nx", "nx", 10, 12, 2002, 2.0, 45, 48, 5, 2, 1.0),
    ("at", "at", 3, 8, 5026, 1.0, 45.7, 51.1, 3.2, 0, 0.1),
    ("ip", "ip", 6, 8, 1500, 2.6, 44, 49, 5, 3, 1.0),
    ("pv", "pv", 10, 13, 5000, 2.3, 49, 50, 1, 0, 1.0),
]
PUB_VALID_B = {"df-1": 52, "df-2": 51, "qu": None, "pd": 51, "nx": 52,
               "at": 52.8, "ip": 52.7, "pv": None}
INST = ["df", "qu", "pd", "nx", "at", "ip", "pv"]

out("### Pesquisas: consistência interna")
out()
rows = []
PINFO = []
for (nm, ins, d0, d1, n, moe, a, b, bn, ns, res) in POLLS:
    s = a + b + bn + ns
    yB = b / (a + b)
    v = (a + b) / 100
    moe_srs = 196 * math.sqrt(0.25 / n)
    moe_used = max(moe, moe_srs)
    deff_impl = (moe / moe_srs) ** 2
    # σ na escala da proporção válida (amostral) e do arredondamento
    sig_samp = (moe_used / 196) / math.sqrt(v)
    sig_lit = (moe / 196) / math.sqrt(v)
    var_round = ((res / 100) ** 2 / 12) * ((b / 100) ** 2 + (a / 100) ** 2) / v ** 4
    sig_p = math.sqrt(sig_samp ** 2 + var_round)
    sig_p_lit = math.sqrt(sig_lit ** 2 + var_round)
    sig_l = sig_p / (yB * (1 - yB))
    sig_l_lit = sig_p_lit / (yB * (1 - yB))
    PINFO.append(dict(nm=nm, ins=ins, d0=d0, d1=d1, n=n, moe=moe, y=yB,
                      sig_p=sig_p, sig_l=sig_l, sig_l_lit=sig_l_lit,
                      sig_round=math.sqrt(var_round)))
    pub = PUB_VALID_B[nm]
    rows.append([nm, f"{d0}–{d1}/out", n, f"{s:g}%", pct(yB, 2),
                 "—" if pub is None else f"{pub}%",
                 "—" if pub is None else f"{100 * yB - pub:+.2f}",
                 f"{moe:.1f}", f"{moe_srs:.2f}", f"{deff_impl:.2f}",
                 f"{100 * sig_p:.2f}", f"{100 * math.sqrt(var_round):.2f}"])
table(["Pesquisa", "Campo", "n", "Σ totais", "B válido (calc.)",
       "B válido (publ.)", "calc−publ (p.p.)", "MOE publ.", "MOE AAS 50%",
       "DEFF implícito", "σ_j válido usado (p.p.)", "σ arred. (p.p.)"], rows)
out("Notas: σ_j = max(MOE publ., MOE AAS)/1,96 reescalado para a base de "
    "válidos (÷√(A+B)), somado em quadratura ao erro de arredondamento "
    "(uniforme ±0,5 p.p. em A e B; ±0,05 p.p. para 'at'). "
    "Para 'at' a MOE publicada (±1,0) é MENOR que a de amostragem aleatória "
    "simples (±1,38) — inconsistência sinalizada; usa-se ±1,38 no caso-base "
    "e a MOE literal em sensibilidade.")
out()

# =====================================================================
# 3. MODELO DAS PESQUISAS (Gaussiano exato: passeio aleatório + house effects)
# =====================================================================
DAYS = list(range(3, 15))          # 3..14 de outubro
ND, NI = len(DAYS), len(INST)


def poll_model(sd_drift, sd_house, sd_extra, H=0.0, lit=False, exclude=None,
               house_zero=False, prior_sd=1.0):
    """Posterior exato de (z_3..z_14, h_j). Retorna dict com média/var de
    z_14 (+ deriva por H dias), log-verossimilhança marginal, resíduos."""
    use = [p for p in PINFO if p["nm"] != exclude]
    P = np.zeros((ND + NI, ND + NI))
    for i in range(ND):
        for j in range(ND):
            P[i, j] = prior_sd ** 2 + sd_drift ** 2 * min(i, j)
    for k in range(NI):
        P[ND + k, ND + k] = 0.0 if house_zero else max(sd_house, 1e-9) ** 2
    Hm = np.zeros((len(use), ND + NI))
    y = np.zeros(len(use))
    R = np.zeros(len(use))
    for r, p in enumerate(use):
        dd = [DAYS.index(d) for d in range(p["d0"], p["d1"] + 1)]
        Hm[r, dd] = 1 / len(dd)
        Hm[r, ND + INST.index(p["ins"])] = 1
        y[r] = logit(p["y"])
        R[r] = (p["sig_l_lit"] if lit else p["sig_l"]) ** 2 + sd_extra ** 2
    S = Hm @ P @ Hm.T + np.diag(R)
    Si = np.linalg.inv(S)
    K = P @ Hm.T @ Si
    mu = K @ y
    C = P - K @ Hm @ P
    sign, logdet = np.linalg.slogdet(S)
    ll = -0.5 * (y @ Si @ y + logdet + len(y) * math.log(2 * math.pi))
    zT, vT = mu[ND - 1], C[ND - 1, ND - 1] + sd_drift ** 2 * H
    return dict(mu=mu, C=C, zT=zT, vT=vT, ll=ll, H=Hm, y=y, R=R, use=use)


def loo(sd_drift, sd_house, sd_extra, lit=False):
    res = []
    for p in PINFO:
        m = poll_model(sd_drift, sd_house, sd_extra, exclude=p["nm"], lit=lit)
        h = np.zeros(ND + NI)
        dd = [DAYS.index(d) for d in range(p["d0"], p["d1"] + 1)]
        h[dd] = 1 / len(dd)
        h[ND + INST.index(p["ins"])] = 1
        # se o instituto só aparece nesta pesquisa, h_j fica no prior
        mean = h @ m["mu"]
        var = h @ m["C"] @ h + (p["sig_l_lit"] if lit else p["sig_l"]) ** 2 + sd_extra ** 2
        res.append((p["nm"], float(logit(p["y"]) - mean), float(math.sqrt(var)),
                    float(expit(mean))))
    return res


out("## Modelo de pesquisas")
out()
# grade de hiperparâmetros (escala logit; 0,04 logit ≈ 1 p.p. perto de 50%)
grid_drift = [0.0, 0.005, 0.01, 0.02]
grid_house = [0.0, 0.01, 0.02, 0.04]
grid_extra = [0.0, 0.01, 0.02, 0.03, 0.04]
rows = []
best = None
for sdd in grid_drift:
    for sh in grid_house:
        for se in grid_extra:
            m = poll_model(sdd, sh, se)
            th = expit(m["zT"])
            sdp = math.sqrt(m["vT"]) * th * (1 - th)
            rows.append((sdd, sh, se, m["ll"], th, sdp))
            if best is None or m["ll"] > best[3]:
                best = (sdd, sh, se, m["ll"], th, sdp)
out("### Sensibilidade a σ_drift, σ_house, σ_extra (nowcast em 14/out, H=0)")
out()
out("θ_B latente em 14/out (sem house effect), desvio-padrão posterior e "
    "log-verossimilhança marginal (prior z_3 ~ N(0,1) em logit).")
out()
table(["σ_drift/√dia", "σ_house", "σ_extra", "log ML", "θ_B médio",
       "dp θ_B (p.p.)", "P(θ_B>0,5)"],
      [[f"{a:.3f}", f"{b:.2f}", f"{c:.2f}", f"{d:.3f}", pct(e, 2),
        f"{100 * f:.2f}", pct(1 - Phi((0.5 - e) / f), 1)] for a, b, c, d, e, f in rows
       if c in (0.0, 0.02, 0.04)])
out(f"Máxima verossimilhança marginal na grade: σ_drift={best[0]}, "
    f"σ_house={best[1]}, σ_extra={best[2]} (log ML={best[3]:.3f}).")
out()

# perfil de σ_extra (house=0, drift=0.01)
prof = []
for se in np.linspace(0, 0.08, 33):
    prof.append((se, poll_model(0.01, 0.0, se)["ll"]))
se_hat = max(prof, key=lambda t: t[1])[0]
out(f"Perfil de σ_extra (σ_house=0, σ_drift=0,01): máximo em σ_extra ≈ "
    f"{se_hat:.4f} logit ≈ {100 * se_hat / 4:.2f} p.p.; "
    f"ΔlogML(σ_extra=0 vs máx) = {prof[0][1] - max(p[1] for p in prof):.3f}")
out()
RES["sigma_extra_hat"] = se_hat

# caso-base das pesquisas
BASE_POLL = dict(sd_drift=0.01, sd_house=0.02, sd_extra=0.02)
pm = poll_model(**BASE_POLL)
th_poll = float(expit(pm["zT"]))
sd_poll_p = math.sqrt(pm["vT"]) * th_poll * (1 - th_poll)
RES["poll_base"] = dict(theta_B=th_poll, sd_pp=100 * sd_poll_p, z=float(pm["zT"]),
                        sd_z=math.sqrt(pm["vT"]))
out(f"**Caso-base das pesquisas** (σ_drift=0,01/√dia, σ_house=0,02, "
    f"σ_extra=0,02, logit): θ_B(14/out) = {pct(th_poll)} ± "
    f"{100 * sd_poll_p:.2f} p.p. (1 dp) → θ_A = {pct(1 - th_poll)}.")
out()

# trajetória latente
out("### Trajetória latente z_t (caso-base)")
out()
rows = []
for i, d in enumerate(DAYS):
    t = expit(pm["mu"][i])
    s = math.sqrt(pm["C"][i, i]) * t * (1 - t)
    rows.append([f"{d}/out", pct(t), f"{100 * s:.2f}"])
table(["dia", "θ_B latente", "dp (p.p.)"], rows)

# house effects
out("### House effects posteriores (caso-base; prior N(0, 0,02²) sem sinal)")
out()
rows = []
for k, ins in enumerate(INST):
    h = pm["mu"][ND + k]
    s = math.sqrt(pm["C"][ND + k, ND + k])
    rows.append([ins, f"{h:+.4f}", f"{s:.4f}", f"{100 * h / 4:+.2f}",
                 f"{h / 0.02:+.2f}"])
table(["instituto", "h_j (logit)", "dp", "≈ p.p. em θ_B", "h_j / σ_house"], rows)

# drift horizon
out("### Efeito do horizonte até a eleição (data não informada)")
out()
rows = []
for sdd in [0.005, 0.01, 0.02]:
    for H in [0, 7, 14]:
        m = poll_model(sdd, 0.02, 0.02, H=H)
        t = expit(m["zT"])
        s = math.sqrt(m["vT"]) * t * (1 - t)
        rows.append([f"{sdd:.3f}", H, pct(t), f"{100 * s:.2f}",
                     pct(1 - Phi((0.5 - t) / s), 1)])
table(["σ_drift", "H (dias após 14/out)", "θ_B", "dp (p.p.)",
       "P(θ_B>0,5)"], rows)

# df-1 -> df-2 atualização
out("### df rodada 1 → rodada 2 (atualização temporal, não média)")
out()
m_only_df = None
for H in [0]:
    pass
z1, z2 = logit(PINFO[0]["y"]), logit(PINFO[1]["y"])
s1, s2 = PINFO[0]["sig_l"], PINFO[1]["sig_l"]
rows = []
for sdd in [0.0, 0.005, 0.01, 0.02]:
    q = sdd ** 2 * 7          # 7 dias entre os pontos médios
    # filtro de Kalman: prior para z(13.5) = N(z1, s1²+q); atualiza com z2
    pv = s1 ** 2 + q
    k = pv / (pv + s2 ** 2)
    zf = z1 + k * (z2 - z1)
    vf = (1 - k) * pv
    t = expit(zf)
    rows.append([f"{sdd:.3f}", f"{k:.3f}", pct(t), f"{100 * math.sqrt(vf) * t * (1 - t):.2f}"])
table(["σ_drift", "ganho de Kalman da rodada 2", "θ_B df filtrado (13–14/out)",
       "dp (p.p.)"], rows)
out(f"Variação df-1→df-2 em θ_B: {100 * (PINFO[1]['y'] - PINFO[0]['y']):+.2f} p.p.; "
    f"z = {(z2 - z1) / math.sqrt(s1 ** 2 + s2 ** 2):+.2f} (só amostragem).")
out()

# PPC / resíduos
out("## Validação: resíduos por pesquisa")
out()
pm0 = poll_model(0.01, 0.0, 0.0, house_zero=True)
lo = loo(**BASE_POLL)
rows = []
chi2 = 0.0
for r, p in enumerate(PINFO):
    h = pm0["H"][r].copy()
    pred = expit(h @ pm0["mu"])
    resid = p["y"] - pred
    rj = resid / p["sig_p"]
    chi2 += rj ** 2
    nm, dl, sl, plo = lo[r]
    rows.append([p["nm"], pct(p["y"]), pct(pred), f"{100 * resid:+.2f}",
                 f"{100 * p['sig_p']:.2f}", f"{rj:+.2f}", pct(plo),
                 f"{dl / sl:+.2f}"])
table(["pesquisa", "observado θ_B", "previsto (sem house, σ_extra=0)",
       "resíduo (p.p.)", "σ_j (p.p.)", "r_j", "previsto LOO (caso-base)",
       "r_j LOO"], rows)
dfree = len(PINFO) - 1
# Wilson–Hilferty
wh = ((chi2 / dfree) ** (1 / 3) - (1 - 2 / (9 * dfree))) / math.sqrt(2 / (9 * dfree))
pchi = 1 - Phi(wh)
out(f"Σ r_j² = {chi2:.2f} com ≈{dfree} g.l. (nível comum estimado); "
    f"p ≈ {pchi:.3f} (Wilson–Hilferty). Razão de dispersão = {chi2 / dfree:.2f}.")
out()
RES["chi2"] = chi2
RES["chi2_p"] = pchi

# literal MOE sensitivity
pml = poll_model(**BASE_POLL, lit=True)
tl = expit(pml["zT"])
out(f"Sensibilidade: MOE literal de 'at' (±1,0): θ_B = {pct(tl)} ± "
    f"{100 * math.sqrt(pml['vT']) * tl * (1 - tl):.2f} p.p.")
# leave-one-institute-out on the nowcast
rows = []
for p in PINFO:
    m = poll_model(**BASE_POLL, exclude=p["nm"])
    t = expit(m["zT"])
    rows.append([p["nm"], pct(t), f"{100 * (t - th_poll):+.2f}"])
out()
out("Influência (remove uma pesquisa por vez; caso-base):")
out()
table(["removida", "θ_B 14/out", "Δ vs. todas (p.p.)"], rows)

# =====================================================================
# 4. MODELO ESTRUTURAL — Monte Carlo
# =====================================================================
CHURN_MU, CHURN_SD = 0.05, 0.015
TAU_ABS_MU = float((N[:iABS] * CHURN_MU).sum() / N[iABS])   # mantém o comparecimento do 1T em média
TAU_ABS_SD = 0.03


def beta_ab(mu, sd):
    k = mu * (1 - mu) / sd ** 2 - 1
    return mu * k, (1 - mu) * k


def alphas(model="M2", deff=2.0, sig_add=0.05):
    A = np.zeros((G, 4))
    for g in range(G):
        if model == "M1":
            s2 = (1.8 / 196) ** 2 + sig_add ** 2
            kap = 0.25 / s2 - 1
        else:
            kap = 3000 * share_el[g] / deff
        A[g] = kap * MPD[g] + 0.5
    return A


def draw_Q(A, n=M):
    Q = np.empty((n, G, 4))
    for g in range(G):
        Q[:, g, :] = rng.dirichlet(A[g], n)
    return Q


def draw_turnout(n=M):
    a, b = beta_ab(CHURN_MU, CHURN_SD)
    churn = rng.beta(a, b, (n, G - 1))
    a2, b2 = beta_ab(TAU_ABS_MU, TAU_ABS_SD)
    tabs = rng.beta(a2, b2, n)
    tau = np.concatenate([1 - churn, tabs[:, None]], axis=1)
    return tau


def resolve(Q, method, nsplit=None):
    """Q: (n,G,4) B,A,BN,NS -> P: (n,G,3) B,A,BN"""
    B, A_, BNq, NS = Q[..., 0], Q[..., 1], Q[..., 2], Q[..., 3]
    if method == "I":        # proporcional aos decididos (global)
        rB = (Q[..., 0] * N).sum(-1) / ((Q[..., 0] + Q[..., 1]) * N).sum(-1)
        rB = rB[:, None]
        return np.stack([B + NS * rB, A_ + NS * (1 - rB), BNq], -1)
    if method == "II":       # 50:50
        return np.stack([B + NS / 2, A_ + NS / 2, BNq], -1)
    if method == "III":      # coorte de origem (proporcional a B, A, BN da coorte)
        d = B + A_ + BNq
        return np.stack([B + NS * B / d, A_ + NS * A_ / d, BNq + NS * BNq / d], -1)
    if method == "IV":       # Dirichlet(1,1,1) por coorte e sorteio
        if nsplit is None:
            nsplit = rng.dirichlet([1, 1, 1], Q.shape[:2])
        return np.stack([B + NS * nsplit[..., 0], A_ + NS * nsplit[..., 1],
                         BNq + NS * nsplit[..., 2]], -1)
    raise ValueError(method)


def votes(P, tau):
    W = N * tau                        # (n,G)
    V = np.einsum("ng,ngk->nk", W, P)  # B, A, BN
    return V


def theta_A(P, tau):
    V = votes(P, tau)
    return V[:, 1] / (V[:, 0] + V[:, 1])


# ---- likelihoods das observações independentes de transferência ----
DF_OBS = np.array([0.46, 0.32, 0.15, 0.07])          # B, A, BN, NS
QU_OBS = {iC: (0.30, 0.34), iD: (0.40, 0.14), iE: (0.42, 0.23)}
QU_POOL = (0.38, 0.43)                                # BN+ABS
wCF = N[[iC, iD, iE, iF]] / N[[iC, iD, iE, iF]].sum()
wPool = N[[iBN, iABS]] / N[[iBN, iABS]].sum()


def ll_transfer(Q, deff=2.0, use_df=True, use_qu=True):
    ll = np.zeros(Q.shape[0])
    if use_df:
        n = 2520 * share_el[[iC, iD, iE, iF]].sum() / deff
        pm_ = np.einsum("g,ngk->nk", wCF, Q[:, [iC, iD, iE, iF], :])
        ll += n * (DF_OBS * np.log(np.clip(pm_, 1e-12, 1))).sum(-1)
    if use_qu:
        for g, (b, a) in QU_OBS.items():
            n = 2154 * share_el[g] / deff
            qb, qa = Q[:, g, 0], Q[:, g, 1]
            ll += n * (b * np.log(qb) + a * np.log(qa) +
                       (1 - a - b) * np.log(np.clip(1 - qa - qb, 1e-12, 1)))
        n = 2154 * share_el[[iBN, iABS]].sum() / deff
        qb = wPool @ Q[:, [iBN, iABS], 0].T
        qa = wPool @ Q[:, [iBN, iABS], 1].T
        b, a = QU_POOL
        ll += n * (b * np.log(qb) + a * np.log(qa) +
                   (1 - a - b) * np.log(np.clip(1 - qa - qb, 1e-12, 1)))
    return ll


LAMBDA_PROP = 0.6   # fração das pseudo-contagens na proposta (proposta mais larga que o alvo)


def draw_Q_post(A, deff=2.0, use_df=True, use_qu=True, n=M):
    """Amostragem por importância com proposta conjugada.

    - qu C, D, E (observação agrupada B, A, 'resto'): atualização Dirichlet
      EXATA via propriedade de agregação (B, A, BN+NS) e partição BN|NS ~ Beta
      independente; o termo de verossimilhança cancela no peso.
    - df (C:F agregado) e qu (BN+ABS agrupado) não são conjugados: a proposta
      usa pseudo-contagens distribuídas por peso eleitoral (n·w_g·p_obs) e o
      peso corrige: log w = ll_exata − ll_pseudo.
    Retorna (Q, logw)."""
    Ap = A.copy()
    coarse = {g: np.zeros(3) for g in range(G)}
    pseudo = []                               # (g, vetor4 ou None, vetor3 ou None)
    if use_df:
        n_df = 2520 * share_el[[iC, iD, iE, iF]].sum() / deff
        for j, g in enumerate([iC, iD, iE, iF]):
            if g == iF:
                continue        # coorte F: n_eff ~3, pseudo-contagem instabiliza pesos
            c = LAMBDA_PROP * n_df * wCF[j] * DF_OBS
            Ap[g] += c
            pseudo.append((g, c, None))
    if use_qu:
        for g, (b, a) in QU_OBS.items():
            ng = 2154 * share_el[g] / deff
            coarse[g] += ng * np.array([b, a, 1 - a - b])
        n_pool = 2154 * share_el[[iBN, iABS]].sum() / deff
        b, a = QU_POOL
        for j, g in enumerate([iBN, iABS]):
            if g == iBN:
                continue        # só a coorte ABS (85% do peso) recebe pseudo-contagem
            c = LAMBDA_PROP * n_pool * wPool[j] * np.array([b, a, 1 - a - b])
            coarse[g] += c
            pseudo.append((g, None, c))
    Q = np.empty((n, G, 4))
    for g in range(G):
        if coarse[g].sum() == 0:
            Q[:, g, :] = rng.dirichlet(Ap[g], n)
        else:
            agg = np.array([Ap[g, 0], Ap[g, 1], Ap[g, 2] + Ap[g, 3]]) + coarse[g]
            D = rng.dirichlet(agg, n)
            s = rng.beta(Ap[g, 2], Ap[g, 3], n)
            Q[:, g, 0], Q[:, g, 1] = D[:, 0], D[:, 1]
            Q[:, g, 2], Q[:, g, 3] = D[:, 2] * s, D[:, 2] * (1 - s)
    logw = np.zeros(n)
    if use_df:
        n_df = 2520 * share_el[[iC, iD, iE, iF]].sum() / deff
        pm_ = np.einsum("g,ngk->nk", wCF, Q[:, [iC, iD, iE, iF], :])
        logw += n_df * (DF_OBS * np.log(np.clip(pm_, 1e-300, 1))).sum(-1)
    if use_qu:
        n_pool = 2154 * share_el[[iBN, iABS]].sum() / deff
        qb = wPool @ Q[:, [iBN, iABS], 0].T
        qa = wPool @ Q[:, [iBN, iABS], 1].T
        b, a = QU_POOL
        logw += n_pool * (b * np.log(qb) + a * np.log(qa) +
                          (1 - a - b) * np.log(np.clip(1 - qa - qb, 1e-300, 1)))
    for g, c4, c3 in pseudo:
        if c4 is not None:
            logw -= (c4 * np.log(np.clip(Q[:, g, :], 1e-300, 1))).sum(-1)
        else:
            o = np.clip(1 - Q[:, g, 0] - Q[:, g, 1], 1e-300, 1)
            logw -= c3[0] * np.log(Q[:, g, 0]) + c3[1] * np.log(Q[:, g, 1]) + c3[2] * np.log(o)
    return Q, logw


def ll_poll(thA, zT=None, vT=None):
    zT = pm["zT"] if zT is None else zT
    vT = pm["vT"] if vT is None else vT
    z = logit(1 - thA)
    return -0.5 * (z - zT) ** 2 / vT


def norm_w(ll):
    w = np.exp(ll - ll.max())
    return w / w.sum()


# ---- ponto base (determinístico) ----
def base_point(method="III"):
    Q = MPD[None].copy()
    P = resolve(Q, method)[0]
    tau = np.concatenate([np.full(G - 1, 1 - CHURN_MU), [TAU_ABS_MU]])
    return P, tau


def th_point(P, tau):
    W = N * tau
    V = W @ P
    return V[1] / (V[0] + V[1]), V


out("## Modelo estrutural (Monte Carlo)")
out()
out(f"Churn de eleitores do 1T: c_g ~ Beta(μ={CHURN_MU}, dp={CHURN_SD}) "
    f"independente por coorte; τ_ABS ~ Beta(μ={TAU_ABS_MU:.4f}, dp={TAU_ABS_SD}) "
    f"(μ escolhido para manter o comparecimento esperado = 1º turno, "
    f"{pct(T1, 3)}).")
out()
rows = []
for meth in ["I", "II", "III", "IV"]:
    P, tau = base_point(meth)
    t, V = th_point(P, tau)
    rows.append([meth, pct(t, 3), f"{V[1]:,.0f}".replace(",", "."),
                 f"{V[0]:,.0f}".replace(",", "."),
                 f"{V[0] - V[1]:,.0f}".replace(",", ".")])
out("### Ponto central (matriz pd normalizada, sem incerteza)")
out()
table(["Indecisos", "θ_A", "V_A", "V_B", "V_B − V_A"], rows)
# implícito pd com τ=1
Pt = resolve(MPD[None], "III")[0]
t_all, _ = th_point(Pt, np.ones(G))
t_noabs, _ = th_point(Pt, np.concatenate([np.ones(G - 1), [0]]))
out(f"Checagem de coerência pd: matriz × coortes com τ=1 para todos → "
    f"θ_A = {pct(t_all)}; só comparecentes do 1T (τ_ABS=0) → θ_A = "
    f"{pct(t_noabs)}; topline pd publicada → θ_A = {pct(46 / 94)}.")
out()


def _th_k(k):
    Nk = N.copy()
    Nk[iA] *= k
    V = (Nk[:, None] * Pt).sum(0)
    return V[1] / (V[0] + V[1])


lo_, hi_ = 0.5, 2.0
for _ in range(100):
    mid = (lo_ + hi_) / 2
    if _th_k(mid) < 46 / 94:
        lo_ = mid
    else:
        hi_ = mid
out(f"Inconsistência interna pd: a matriz aplicada ao resultado oficial do 1T "
    f"não reproduz a própria topline pd ({pct(t_all)} vs {pct(46 / 94)}). "
    f"Para reproduzi-la só via composição, a coorte A precisaria pesar "
    f"{mid:.3f}× o seu tamanho oficial (relativo às demais coortes), i.e. "
    f"recordação/ponderação de voto do 1T diferente do resultado oficial, ou "
    f"linhas da matriz com viés. Não corrigido: tratado pela ponderação com as "
    f"pesquisas nacionais (pd topline entra apenas nelas).")
out()
RES["pd_inconsistencia_k"] = mid

# ---- sorteios principais ----
A2 = alphas("M2", 2.0)
# conjunto "prior" (só pd) e conjunto principal (pd + df + qu, proposta conjugada)
Q0 = draw_Q(A2)
TAU0 = draw_turnout()
TH0 = theta_A(resolve(Q0, "III"), TAU0)
Q, LLT = draw_Q_post(A2, 2.0, True, True)
TAU = draw_turnout()
NSPLIT = rng.dirichlet([1, 1, 1], (M, G))
P_III = resolve(Q, "III")
TH = theta_A(P_III, TAU)
LLP = ll_poll(TH)
Qdf, LLdf = draw_Q_post(A2, 2.0, True, False, M // 2)
Qqu, LLqu = draw_Q_post(A2, 2.0, False, True, M // 2)
TAUh = draw_turnout(M // 2)
THdf = theta_A(resolve(Qdf, "III"), TAUh)
THqu = theta_A(resolve(Qqu, "III"), TAUh)

SETS = {   # nome: (Q, θ_A, log-peso)
    "pd apenas (prior)": (Q0, TH0, np.zeros(M)),
    "pd + df": (Qdf, THdf, LLdf),
    "pd + qu": (Qqu, THqu, LLqu),
    "pd + df + qu": (Q, TH, LLT),
    "pd + pesquisas nacionais": (Q0, TH0, ll_poll(TH0)),
    "pd + df + qu + pesquisas (completo)": (Q, TH, LLT + LLP),
}
W = {k: norm_w(v[2]) for k, v in SETS.items()}
out("### Tamanho efetivo amostral dos pesos (importance sampling)")
out()
out("Proposta conjugada: qu C/D/E entram exatamente via agregação Dirichlet; "
    "df e qu(BN+ABS) via pseudo-contagens corrigidas por peso.")
out()
table(["Configuração", "sorteios", "ESS", "ESS/sorteios"],
      [[k, f"{len(w):,}".replace(",", "."), f"{ess(w):,.0f}".replace(",", "."),
        pct(ess(w) / len(w), 2)] for k, w in W.items()])
RES["ess"] = {k: ess(w) for k, w in W.items()}

# ---- parâmetros posteriores ----
def par_table(wkeys):
    rows = None
    for k in wkeys:
        Q_, TH_, _ = SETS[k]
        w = W[k]
        defs = par_defs(Q_, TH_)
        if rows is None:
            rows = [[nm] for nm, _ in defs]
        for r, (nm, x) in zip(rows, defs):
            q = wq(x, w, [0.05, 0.5, 0.95])
            r.append(f"{100 * wmean(x, w):.1f} [{100 * q[0]:.1f}; {100 * q[2]:.1f}]")
    return rows


def par_defs(Q, TH):
    return [
        ("R_B = P(B₂|B₁)", Q[:, iB, 0]), ("X_BA = P(A₂|B₁)", Q[:, iB, 1]),
        ("R_A = P(A₂|A₁)", Q[:, iA, 1]), ("X_AB = P(B₂|A₁)", Q[:, iA, 0]),
        ("T_CB", Q[:, iC, 0]), ("T_CA", Q[:, iC, 1]),
        ("T_DB", Q[:, iD, 0]), ("T_DA", Q[:, iD, 1]),
        ("T_EB", Q[:, iE, 0]), ("T_EA", Q[:, iE, 1]),
        ("T_FB", Q[:, iF, 0]), ("T_FA", Q[:, iF, 1]),
        ("T_G:L,B", Q[:, iGL, 0]), ("T_G:L,A", Q[:, iGL, 1]),
        ("T_G:L,NS", Q[:, iGL, 3]),
        ("BN₁→B", Q[:, iBN, 0]), ("BN₁→A", Q[:, iBN, 1]), ("BN₁→BN", Q[:, iBN, 2]),
        ("ABS₁→B", Q[:, iABS, 0]), ("ABS₁→A", Q[:, iABS, 1]), ("ABS₁→BN", Q[:, iABS, 2]),
        ("C:F agregado →B", np.einsum("g,ng->n", wCF, Q[:, [iC, iD, iE, iF], 0])),
        ("C:F agregado →A", np.einsum("g,ng->n", wCF, Q[:, [iC, iD, iE, iF], 1])),
        ("θ_A (válidos)", TH),
    ]


keys = list(SETS.keys())
out("### Parâmetros: média [IC 90%] em % (Modelo 2, DEFF=2, indecisos III)")
out()
out("Linhas q_g ANTES da resolução dos indecisos e antes do comparecimento "
    "(intenção declarada normalizada). θ_A inclui indecisos III e τ_g.")
out()
table(["Parâmetro"] + keys, par_table(keys))
for k in keys:
    TH_ = SETS[k][1]
    RES.setdefault("thetaA", {})[k] = dict(
        mean=wmean(TH_, W[k]), q=wq(TH_, W[k], [0.05, 0.5, 0.95]),
        pA=float(np.sum(W[k] * (TH_ > 0.5))))
out("P(θ_A > 0,5 | modelo) — condicional às hipóteses, não previsão:")
out()
table(["Configuração", "E[θ_A]", "IC 90%", "P(θ_A>0,5)"],
      [[k, pct(v["mean"]), f"{pct(v['q'][0])} – {pct(v['q'][2])}",
        pct(v["pA"], 1)] for k, v in RES["thetaA"].items()])

# ---- DEFF / Modelo 1 ----
out("### Sensibilidade: Modelo 1 (conservador) vs Modelo 2 (DEFF 1,5 / 2 / 3)")
out()
rows = []
nsub = 200_000
for lab, A_ in [("M1 (σ_sub²=σ_geral²+5²p.p.²)", alphas("M1")),
                ("M2 DEFF=1,5", alphas("M2", 1.5)),
                ("M2 DEFF=2", alphas("M2", 2.0)),
                ("M2 DEFF=3", alphas("M2", 3.0))]:
    deff = 1.5 if "1,5" in lab else 3.0 if "3" in lab and "M2" in lab else 2.0
    Qp = draw_Q(A_, nsub)
    Qs, llt = draw_Q_post(A_, deff, True, True, nsub)
    taus = draw_turnout(nsub)
    thp = theta_A(resolve(Qp, "III"), taus)
    ths = theta_A(resolve(Qs, "III"), taus)
    for cfg, ll, th, Qx in [("prior", np.zeros(nsub), thp, Qp),
                            ("+df+qu", llt, ths, Qs),
                            ("+df+qu+pesq.", llt + ll_poll(ths), ths, Qs)]:
        w = norm_w(ll)
        q = wq(th, w, [0.05, 0.95])
        rows.append([lab, cfg, pct(wmean(th, w)), f"{pct(q[0])} – {pct(q[1])}",
                     f"{100 * math.sqrt(wmean((th - wmean(th, w)) ** 2, w)):.2f}",
                     f"{100 * wmean(Qx[:, iA, 1], w):.1f}",
                     f"{100 * wmean(Qx[:, iB, 0], w):.1f}",
                     pct(float(np.sum(w * (th > 0.5))), 1),
                     f"{ess(w):,.0f}".replace(",", ".")])
table(["Modelo", "Informação", "E[θ_A]", "IC 90%", "dp (p.p.)", "R_A",
       "R_B", "P(θ_A>0,5)", "ESS"], rows)
out("κ do Modelo 1 = " + f"{0.25 / ((1.8 / 196) ** 2 + 0.05 ** 2) - 1:.1f}" +
    " (igual para todas as coortes). n_eff (Modelo 2) por coorte: " +
    ", ".join(f"{COH[g]}={3000 * share_el[g] / 2:.1f}" for g in range(G)) +
    " (DEFF=2). n_eff é APROXIMAÇÃO: o n real das subamostras não foi informado.")
out()

# =====================================================================
# 5. COMPARAÇÃO pd x df x qu (testes de compatibilidade)
# =====================================================================
out("## C. Comparação pd × df × qu")
out()
rows = []
mCF = wCF @ MPD[[iC, iD, iE, iF]]
for lab, k in [("B", 0), ("A", 1), ("BN", 2), ("NS", 3)]:
    n_pd = 3000 * share_el[[iC, iD, iE, iF]].sum() / 2
    n_df = 2520 * share_el[[iC, iD, iE, iF]].sum() / 2
    se = math.sqrt(mCF[k] * (1 - mCF[k]) / n_pd + DF_OBS[k] * (1 - DF_OBS[k]) / n_df)
    rows.append([f"C:F → {lab}", pct(mCF[k], 1), pct(DF_OBS[k], 1),
                 f"{100 * (DF_OBS[k] - mCF[k]):+.1f}", f"{(DF_OBS[k] - mCF[k]) / se:+.2f}"])
for g, (b, a) in QU_OBS.items():
    for lab, k, ob in [("B", 0, b), ("A", 1, a)]:
        n_pd = 3000 * share_el[g] / 2
        n_qu = 2154 * share_el[g] / 2
        se = math.sqrt(MPD[g, k] * (1 - MPD[g, k]) / n_pd + ob * (1 - ob) / n_qu)
        rows.append([f"{COH[g]} → {lab}", pct(MPD[g, k], 1), pct(ob, 1),
                     f"{100 * (ob - MPD[g, k]):+.1f}", f"{(ob - MPD[g, k]) / se:+.2f}"])
mpool = wPool @ MPD[[iBN, iABS]]
for lab, k, ob in [("B", 0, QU_POOL[0]), ("A", 1, QU_POOL[1])]:
    n_pd = 3000 * share_el[[iBN, iABS]].sum() / 2
    n_qu = 2154 * share_el[[iBN, iABS]].sum() / 2
    se = math.sqrt(mpool[k] * (1 - mpool[k]) / n_pd + ob * (1 - ob) / n_qu)
    rows.append([f"BN+ABS → {lab}", pct(mpool[k], 1), pct(ob, 1),
                 f"{100 * (ob - mpool[k]):+.1f}", f"{(ob - mpool[k]) / se:+.2f}"])
table(["Fluxo", "pd (normalizado)", "observação externa", "Δ (p.p.)",
       "z (n_eff, DEFF=2)"], rows)
out("Para df, a comparação de C:F usa pd ponderado por votos de C, D, E, F. "
    "Para qu, 'restante' não é decomposto (apenas B e A são comparados). "
    "z é aproximação: n reais das subamostras desconhecidos.")
out()

# =====================================================================
# 6. INDECISOS — 4 métodos
# =====================================================================
out("## Indecisos: métodos I–IV")
out()
rows = []
for meth in ["I", "II", "III", "IV"]:
    th_post = theta_A(resolve(Q, meth, NSPLIT if meth == "IV" else None), TAU)
    th_prior = theta_A(resolve(Q0, meth, NSPLIT if meth == "IV" else None), TAU0)
    for cfg in ["pd apenas (prior)", "pd + df + qu",
                "pd + df + qu + pesquisas (completo)"]:
        if cfg == "pd apenas (prior)":
            th, ll = th_prior, np.zeros(M)
        else:
            th = th_post
            ll = LLT if "pesquisas" not in cfg else LLT + ll_poll(th)
        w = norm_w(ll)
        q = wq(th, w, [0.05, 0.95])
        rows.append([meth, cfg, pct(wmean(th, w)), f"{pct(q[0])} – {pct(q[1])}",
                     pct(float(np.sum(w * (th > 0.5))), 1)])
table(["Método", "Informação", "E[θ_A]", "IC 90%", "P(θ_A>0,5)"], rows)
# fração de NS no eleitorado efetivo
P_, tau = base_point("III")
ns_votes = (N * tau * MPD[:, 3]).sum()
out(f"Massa de NS (ponto central, ponderada por comparecimento): "
    f"{ns_votes:,.0f} eleitores = {pct(ns_votes / (N * tau).sum())} dos "
    f"comparecentes.".replace(",", "."))
out()

# =====================================================================
# 7. COMPARECIMENTO × PREFERÊNCIA DOS NOVOS COMPARECENTES
# =====================================================================
out("## Comparecimento × preferência dos novos comparecentes")
out()
out("Para cada cenário, τ_ABS é ajustado para que o comparecimento total "
    "atinja o alvo; churn das demais coortes segue a distribuição base. "
    "A divisão A:B dos novos comparecentes é aplicada entre seus votos "
    "válidos; a fração BN deles vem da linha ABS da pd (sorteada). "
    "'pd' = usa a linha ABS da matriz pd.")
out()
DELTAS = [0, 1, 2, 3, 5, -1, -2]
SPLITS = [("pd", None), ("50:50", 0.5), ("55:45", 0.55), ("60:40", 0.60),
          ("2:1", 2 / 3), ("40:60", 0.40), ("45:55", 0.45)]
base_votes_non_abs = (N[:iABS] * TAU[:, :iABS]).sum(1)
rows_m, rows_p, rows_pp = [], [], []
grid_res = {}
for d in DELTAS:
    target = (T1 + d / 100) * ELEIT
    tabs = (target - base_votes_non_abs) / N[iABS]
    tau_s = TAU.copy()
    tau_s[:, iABS] = np.clip(tabs, 0, 1)
    rm, rp, rpp = [f"{d:+d} p.p." if d else "= 1º turno"], [f"{d:+d} p.p." if d else "= 1º turno"], [f"{d:+d} p.p." if d else "= 1º turno"]
    for lab, a in SPLITS:
        P_ = P_III.copy()
        if a is not None:
            bnf = P_[:, iABS, 2]
            P_[:, iABS, 0] = (1 - bnf) * (1 - a)
            P_[:, iABS, 1] = (1 - bnf) * a
        th = theta_A(P_, tau_s)
        w1 = norm_w(LLT)
        w2 = norm_w(LLT + ll_poll(th))
        m1 = wmean(th, w1)
        p1 = float(np.sum(w1 * (th > 0.5)))
        p2 = float(np.sum(w2 * (th > 0.5)))
        grid_res[(d, lab)] = (m1, p1, p2)
        rm.append(pct(m1))
        rp.append(pct(p1, 1))
        rpp.append(pct(p2, 1))
    rows_m.append(rm)
    rows_p.append(rp)
    rows_pp.append(rpp)
hdr = ["Comparecimento"] + [f"A:B {s[0]}" for s in SPLITS]
out("### E[θ_A] (estrutural: pd + df + qu)")
out()
table(hdr, rows_m)
out("### P(θ_A > 0,5) (estrutural: pd + df + qu)")
out()
table(hdr, rows_p)
out("### P(θ_A > 0,5) (estrutural + pesquisas nacionais)")
out()
table(hdr, rows_pp)
out(f"τ_ABS implícito médio no cenário base: {TAU_ABS_MU:.4f} "
    f"(≈{TAU_ABS_MU * N[iABS] / 1e6:.2f} mi de abstencionistas do 1T comparecem, "
    f"compensando ≈{(N[:iABS] * CHURN_MU).sum() / 1e6:.2f} mi de eleitores do 1T que se abstêm).")
out()
RES["grid"] = {f"{k[0]}|{k[1]}": v for k, v in grid_res.items()}

# =====================================================================
# 8. RETENÇÃO: grade R_A x R_B
# =====================================================================
out("## Retenção: P(θ_A>0,5) em grade R_A × R_B (estrutural pd+df+qu)")
out()
out("R fixado; crossover X mantido no sorteio; massa restante (BN+NS) "
    "reescalada para fechar 1; demais parâmetros sorteados.")
out()
nsub = 200_000
idx = rng.choice(M, nsub, replace=True, p=norm_w(LLT))
Qs, Ts = Q[idx].copy(), TAU[idx]
RA_GRID = [0.88, 0.90, 0.92, 0.94, 0.96, 0.98]
RB_GRID = [0.89, 0.91, 0.93, 0.95, 0.97]


def set_ret(Qx, g, col, r):
    Qx = Qx.copy()
    other = 1 - col                      # crossover col (0<->1)
    x = np.minimum(Qx[:, g, other], 1 - r)
    Qx[:, g, other] = x
    rest = Qx[:, g, 2] + Qx[:, g, 3]
    newrest = np.clip(1 - r - x, 0, None)
    scale = np.where(rest > 0, newrest / np.maximum(rest, 1e-12), 0)
    Qx[:, g, col] = r
    Qx[:, g, 2] *= scale
    Qx[:, g, 3] *= scale
    Qx[:, g, :] /= Qx[:, g, :].sum(-1, keepdims=True)
    return Qx


rows = []
rows_m = []
for rb in RB_GRID:
    r, r2 = [f"R_B={rb:.2f}"], [f"R_B={rb:.2f}"]
    Qb = set_ret(Qs, iB, 0, rb)
    for ra in RA_GRID:
        Qab = set_ret(Qb, iA, 1, ra)
        th = theta_A(resolve(Qab, "III"), Ts)
        r.append(pct(float(np.mean(th > 0.5)), 1))
        r2.append(pct(float(np.mean(th))))
    rows.append(r)
    rows_m.append(r2)
table(["", *[f"R_A={x:.2f}" for x in RA_GRID]], rows)
out("E[θ_A] correspondente:")
out()
table(["", *[f"R_A={x:.2f}" for x in RA_GRID]], rows_m)

# =====================================================================
# 9. CENÁRIO HIPOTÉTICO (bloco 6)
# =====================================================================
out("## Cenário hipotético do bloco 6 (não é pesquisa)")
out()
rows = []
P0, tau0 = base_point("III")
for lab, mods in [
    ("pd (ponto central)", {}),
    ("retenções hipotéticas, ABS = pd", dict(ret=True)),
    ("retenções pd, novos = 2:1", dict(new=2 / 3)),
    ("retenções hipotéticas + novos 2:1", dict(ret=True, new=2 / 3)),
    ("retenções hipotéticas + novos = qu (43:38)", dict(ret=True, new=43 / 81)),
]:
    P = P0.copy()
    if mods.get("ret"):
        P[iA] = [0.02, 0.97, 0.01]
        P[iB] = [0.93, 0.02, 0.05]
    if "new" in mods:
        a = mods["new"]
        if lab.endswith("novos 2:1") or "= 2:1" in lab:
            P[iABS] = [1 - a, a, 0.0]          # cenário: 2/3, 1/3, sem BN
        else:
            bnf = P[iABS, 2]
            P[iABS] = [(1 - bnf) * (1 - a), (1 - bnf) * a, bnf]
    t, V = th_point(P, tau0)
    z = (logit(1 - t) - pm["zT"]) / math.sqrt(pm["vT"])
    rows.append([lab, pct(t, 2), f"{z:+.2f}"])
table(["Cenário", "θ_A", "z vs. pesquisas (caso-base)"], rows)
out("Comparação da hipótese 2/3 : 1/3 para novos comparecentes com as observações: "
    f"pd ABS (válidos) A = {pct(MPD[iABS, 1] / (MPD[iABS, 0] + MPD[iABS, 1]))}; "
    f"qu BN+ABS (válidos) A = {pct(43 / 81)}; hipótese A = 66,67%.")
out()

# =====================================================================
# 10. DECOMPOSIÇÃO DA VARIÂNCIA
# =====================================================================
out("## E. Decomposição da variância")
out()
nsub = 300_000
Qm = A2 / A2.sum(1, keepdims=True)
tau_m = np.concatenate([np.full(G - 1, 1 - CHURN_MU), [TAU_ABS_MU]])
groups = {
    "retenção A (linha A)": [iA],
    "retenção B (linha B)": [iB],
    "eliminados C:L": [iC, iD, iE, iF, iGL],
    "BN do 1º turno": [iBN],
    "abstêmios do 1º turno (preferência)": [iABS],
}
Qf = draw_Q(A2, nsub)
Tf = draw_turnout(nsub)
Sf = rng.dirichlet([1, 1, 1], (nsub, G))
var_parts = {}
for nm, gs in groups.items():
    Qx = np.broadcast_to(Qm, (nsub, G, 4)).copy()
    Qx[:, gs, :] = Qf[:, gs, :]
    th = theta_A(resolve(Qx, "III"), np.broadcast_to(tau_m, (nsub, G)))
    var_parts[nm] = float(np.var(th))
Qx = np.broadcast_to(Qm, (nsub, G, 4)).copy()
var_parts["comparecimento (τ_g)"] = float(np.var(theta_A(resolve(Qx, "III"), Tf)))
var_parts["indecisos (Dirichlet IV)"] = float(np.var(theta_A(resolve(Qx, "IV", Sf),
                                                             np.broadcast_to(tau_m, (nsub, G)))))
th_all = theta_A(resolve(Qf, "IV", Sf), Tf)
var_tot_struct = float(np.var(th_all))
# bloco de pesquisas
def vT_p(**kw):
    m = poll_model(**kw)
    t = expit(m["zT"])
    return m["vT"] * (t * (1 - t)) ** 2


H_dec = 7
v_full = vT_p(sd_drift=0.01, sd_house=0.02, sd_extra=0.02, H=H_dec)
v_nohouse = vT_p(sd_drift=0.01, sd_house=0.0, sd_extra=0.02, H=H_dec)
v_nodrift = vT_p(sd_drift=0.0, sd_house=0.02, sd_extra=0.02, H=0)
v_noextra = vT_p(sd_drift=0.01, sd_house=0.02, sd_extra=0.0, H=H_dec)
v_samp = vT_p(sd_drift=0.0, sd_house=0.0, sd_extra=0.0, H=0)
poll_parts = {
    "amostragem (MOE)": v_samp,
    "house effects": v_full - v_nohouse,
    "deriva temporal (inclui H=7 dias)": v_full - v_nodrift,
    "σ_extra (erro não amostral)": v_full - v_noextra,
}
rows = []
s1 = sum(var_parts.values())
for k, v in var_parts.items():
    rows.append(["estrutural", k, f"{100 * math.sqrt(v):.3f}", pct(v / s1, 1)])
rows.append(["estrutural", "**total conjunto (todos variando)**",
             f"{100 * math.sqrt(var_tot_struct):.3f}",
             f"Σ partes/total = {s1 / var_tot_struct:.2f}"])
s2 = sum(poll_parts.values())
for k, v in poll_parts.items():
    rows.append(["pesquisas", k, f"{100 * math.sqrt(max(v, 0)):.3f}", pct(v / s2, 1)])
rows.append(["pesquisas", "**total (caso-base, H=7)**",
             f"{100 * math.sqrt(v_full):.3f}", f"Σ partes/total = {s2 / v_full:.2f}"])
table(["Bloco", "Fonte", "dp de θ (p.p.)", "parcela no bloco"], rows)
v_post = 1 / (1 / var_tot_struct + 1 / v_full)
out(f"Combinação (aprox. Gaussiana): 1/v_post = 1/v_estr + 1/v_pesq → "
    f"dp_post = {100 * math.sqrt(v_post):.2f} p.p.; peso de informação: "
    f"estrutural {pct((1 / var_tot_struct) / (1 / var_tot_struct + 1 / v_full), 1)}, "
    f"pesquisas {pct((1 / v_full) / (1 / var_tot_struct + 1 / v_full), 1)}.")
out()
RES["var_struct"] = var_parts
RES["var_poll"] = poll_parts

# =====================================================================
# 11. SENSIBILIDADE UNIVARIADA + ELASTICIDADES
# =====================================================================
out("## F/G. Sensibilidade univariada e elasticidades")
out()
out("Duas bases: (1) ponto central da matriz pd normalizada; (2) médias "
    "posteriores do modelo completo (pd+df+qu+pesquisas). Indecisos: método III. "
    "Derivadas ANALÍTICAS de θ_A = V_A/(V_A+V_B): 'parcial' = massa vem de/para "
    "fora dos válidos (BN/abstenção), demais entradas fixas; 'troca' = massa vem "
    "do adversário na mesma coorte. Valores = variação de θ_A em p.p. por +1 p.p. "
    "no parâmetro.")
out()
wfull = W["pd + df + qu + pesquisas (completo)"]
Qpost_mean = np.einsum("n,ngk->gk", wfull, Q)
tau_post = np.einsum("n,ng->g", wfull, TAU)
BASES = {"pd (ponto central)": base_point("III"),
         "média posterior completa": (resolve(Qpost_mean[None], "III")[0], tau_post)}
PARS = [("R_A (A₁→A)", iA, 1), ("X_AB (A₁→B)", iA, 0),
        ("R_B (B₁→B)", iB, 0), ("X_BA (B₁→A)", iB, 1),
        ("T_CA", iC, 1), ("T_CB", iC, 0), ("T_DA", iD, 1), ("T_DB", iD, 0),
        ("T_EA", iE, 1), ("T_EB", iE, 0), ("T_FA", iF, 1), ("T_FB", iF, 0),
        ("T_G:L,A", iGL, 1), ("T_G:L,B", iGL, 0),
        ("BN₁→A", iBN, 1), ("BN₁→B", iBN, 0),
        ("ABS₁→A", iABS, 1), ("ABS₁→B", iABS, 0)]


def th_mod(P, tau, g, col, v):
    P1 = P.copy()
    P1[g, col] = v
    return th_point(P1, tau)[0]


def solve(fn, lo, hi, target, it=200):
    flo = fn(lo) - target
    fhi = fn(hi) - target
    if flo * fhi > 0:
        return None
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = fn(mid) - target
        if fm * flo <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


RES["base"] = {}
for bname, (P0, tau0) in BASES.items():
    t0, V0 = th_point(P0, tau0)
    VB, VA = V0[0], V0[1]
    S = VA + VB
    RES["base"][bname] = dict(thetaA=t0, VA=VA, VB=VB)
    out(f"### Base: {bname}")
    out()
    out(f"θ_A = {pct(t0, 3)}; V_A = {VA:,.0f}; V_B = {VB:,.0f}; "
        f"V_BN = {V0[2]:,.0f}; V_B − V_A = {VB - VA:,.0f}.".replace(",", "."))
    out()
    rows = []
    for lab, g, col in PARS:
        w_ = N[g] * tau0[g]
        d_par = w_ * VB / S ** 2 if col == 1 else -w_ * VA / S ** 2
        d_swap = (w_ / S) if col == 1 else -(w_ / S)
        p = P0[g, col]
        th_own = t0 if col == 1 else 1 - t0
        el = abs(d_par) * p / th_own
        rows.append([lab, pct(p, 2), f"{d_par:+.4f}", f"{d_swap:+.4f}",
                     f"{el:.4f}", f"{0.01 * w_:,.0f}".replace(",", ".")])
    table(["Parâmetro", "valor (após indecisos III)", "∂θ_A/∂p parcial",
           "∂θ_A/∂p troca", "elasticidade |∂θ_k/∂p|·p/θ_k",
           "eleitores por 1 p.p."], rows)
    out("∂θ_B/∂p = −∂θ_A/∂p. Elasticidade usa θ_k do candidato favorecido pelo parâmetro.")
    out()
    rows = []
    for lab, gs in [("τ_A (coorte A)", [iA]), ("τ_B (coorte B)", [iB]),
                    ("τ C:F", [iC, iD, iE, iF]), ("τ G:L", [iGL]),
                    ("τ BN₁", [iBN]), ("τ ABS₁", [iABS])]:
        d = sum(N[g] * (P0[g, 1] * VB - P0[g, 0] * VA) for g in gs) / S ** 2
        rows.append([lab, f"{d:+.4f}", f"{0.01 * N[gs].sum():,.0f}".replace(",", ".")])
    d_e = (P0[iABS, 1] * VB - P0[iABS, 0] * VA) / S ** 2 * ELEIT / 1.0
    rows.append(["+1 p.p. do ELEITORADO vindo de ABS₁ (pref. da coorte)",
                 f"{d_e:+.4f}", f"{0.01 * ELEIT:,.0f}".replace(",", ".")])
    table(["Comparecimento (+1 p.p. em τ)", "∂θ_A/∂τ (p.p. por p.p.)",
           "eleitores adicionais"], rows)

    # tornado
    out("Tornado: cada parâmetro varrido no seu IC 90% a priori (pd, M2, DEFF=2), "
        "demais fixos na base (parcial):")
    out()
    rows = []
    for lab, g, col in PARS[:4] + PARS[4:10] + PARS[14:]:
        lo_, hi_ = np.quantile(Q0[:, g, col], [0.05, 0.95])
        # converte da escala q (antes de NS) para P (após NS III): fator P/q
        fac = P0[g, col] / max(MPD[g, col], 1e-9) if bname.startswith("pd") else 1.0
        a_, b_ = th_mod(P0, tau0, g, col, lo_ * fac), th_mod(P0, tau0, g, col, hi_ * fac)
        rows.append([lab, f"{100 * lo_:.1f} – {100 * hi_:.1f}", pct(a_), pct(b_),
                     f"{100 * abs(b_ - a_):.3f}"])
    for lab, g in [("churn coorte A", iA), ("churn coorte B", iB)]:
        lo_, hi_ = CHURN_MU - 1.645 * CHURN_SD, CHURN_MU + 1.645 * CHURN_SD
        res = []
        for v in (lo_, hi_):
            tau1 = tau0.copy()
            tau1[g] = 1 - v
            res.append(th_point(P0, tau1)[0])
        rows.append([lab, f"{100 * lo_:.1f} – {100 * hi_:.1f}", pct(res[0]),
                     pct(res[1]), f"{100 * abs(res[1] - res[0]):.3f}"])
    rows.sort(key=lambda r: -float(r[-1]))
    table(["Parâmetro", "faixa IC 90% (q)", "θ_A no limite inf.",
           "θ_A no limite sup.", "amplitude (p.p.)"], rows)

    # break-even
    out(f"#### H. Break-even (base: {bname}) — equações condicionais, NÃO previsões")
    out()
    xab, xba = P0[iA, 0], P0[iB, 1]

    def f_RA(r):
        return th_mod(P0, tau0, iA, 1, r)

    def f_RA0(r):
        P1 = P0.copy()
        P1[iA, 0] = 0.0
        P1[iA, 1] = r
        return th_point(P1, tau0)[0]

    def f_RB(r):
        return th_mod(P0, tau0, iB, 0, r)

    def f_CF(sA):
        P1 = P0.copy()
        for g in [iC, iD, iE, iF]:
            v = P1[g, 0] + P1[g, 1]
            P1[g, 1], P1[g, 0] = v * sA, v * (1 - sA)
        return th_point(P1, tau0)[0]

    def f_X(x):
        P1 = P0.copy()
        d = x - P1[iB, 1]
        P1[iB, 1] = x
        P1[iB, 0] -= d
        return th_point(P1, tau0)[0]

    cfv = sum(N[g] * tau0[g] * (P0[g, 0] + P0[g, 1]) for g in [iC, iD, iE, iF])
    cfa = sum(N[g] * tau0[g] * P0[g, 1] for g in [iC, iD, iE, iF]) / cfv
    fm = lambda v: "inviável" if v is None else pct(v, 2)
    rows = []
    for tgt in [0.48, 0.49, 0.50, 0.51, 0.52]:
        rows.append([pct(tgt, 0),
                     fm(solve(f_RA, 0.0, 1 - xab, tgt)),
                     fm(solve(f_RA0, 0.0, 1.0, tgt)),
                     fm(solve(lambda r: -f_RB(r), 0.0, 1 - xba, -tgt)),
                     fm(solve(f_CF, 0.0, 1.0, tgt)),
                     fm(solve(f_X, 0.0, P0[iB, 0] + P0[iB, 1], tgt))])
    table(["θ_A alvo", f"R_A (X_AB={pct(xab, 1)} fixo; máx {pct(1 - xab, 1)})",
           "R_A com X_AB=0", f"R_B (X_BA={pct(xba, 1)} fixo)",
           "A entre válidos de C:F", "X_BA (tirado de R_B)"], rows)
    out(f"Valores da base: R_A = {pct(P0[iA, 1])}, R_B = {pct(P0[iB, 0])}, "
        f"A entre válidos de C:F = {pct(cfa)}, X_BA = {pct(xba)}, X_AB = {pct(xab)}.")
    out()
    gap = VB - VA
    bnf = P0[iABS, 2]
    rows = []
    for lab, a in [("50:50", 0.5), ("55:45", 0.55), ("60:40", 0.60), ("2:1", 2 / 3),
                   ("45:55", 0.45), ("40:60", 0.40), ("1:2", 1 / 3)]:
        d = 2 * a - 1
        if d != 0 and gap / d > 0:
            n = gap / d
            tot = n / (1 - bnf)
            rows.append([lab, f"{n:,.0f}".replace(",", "."), f"{tot:,.0f}".replace(",", "."),
                         f"{100 * tot / ELEIT:.2f}", pct(tot / N[iABS], 1)])
        else:
            rows.append([lab, "não fecha a diferença", "—", "—", "—"])
    out(f"Novos comparecentes para zerar V_B − V_A = {gap:,.0f}: "
        f"N_válidos = (V_B − V_A)/(a − b); total = N_válidos/(1 − f_BN), "
        f"f_BN = {pct(bnf, 1)} (linha ABS da base).".replace(",", "."))
    out()
    table(["A:B dos novos", "novos votos válidos", "novos comparecentes",
           "p.p. do eleitorado", "% dos abstêmios do 1T"], rows)
    cap = {g: N[g] * tau0[g] * P0[g, 0] for g in [iC, iD, iE, iF]}
    need = gap / 2
    tc = sum(cap.values())
    rows = [["Votos que precisam passar de B para A (cada um reduz a diferença em 2)",
             f"{need:,.0f}".replace(",", ".")],
            ["Estoque de votos B em C:F", f"{tc:,.0f}".replace(",", ".")],
            ["Fração uniforme do voto B de C:F que precisaria migrar", pct(need / tc, 1)]]
    for g in [iC, iD, iE, iF]:
        rows.append([f"Só coorte {COH[g]}", pct(need / cap[g], 1) +
                     (" (inviável)" if need > cap[g] else "")])
    table(["Combinação C:F", "Valor"], rows)


# =====================================================================
# 13. D — o que explica 50:50 vs 51:49 vs 52:48
# =====================================================================
out("## D. Parâmetros associados a θ_B ≈ 50, 51, 52% (estrutural pd+df+qu)")
out()
out("Médias ponderadas condicionais a faixas de θ_B (±0,5 p.p.) entre os "
    "sorteios; diferença em relação à média geral indica quais parâmetros "
    "'carregam' cada cenário.")
out()
w = norm_w(LLT)
thB = 1 - TH
pars = [("R_A", Q[:, iA, 1]), ("X_AB", Q[:, iA, 0]), ("R_B", Q[:, iB, 0]),
        ("X_BA", Q[:, iB, 1]),
        ("C:F→A", np.einsum("g,ng->n", wCF, Q[:, [iC, iD, iE, iF], 1])),
        ("C:F→B", np.einsum("g,ng->n", wCF, Q[:, [iC, iD, iE, iF], 0])),
        ("ABS→A", Q[:, iABS, 1]), ("ABS→B", Q[:, iABS, 0]),
        ("BN→A", Q[:, iBN, 1]), ("BN→B", Q[:, iBN, 0]),
        ("τ_A", TAU[:, iA]), ("τ_B", TAU[:, iB]), ("τ_ABS", TAU[:, iABS])]
bins = [("θ_B≈50", 0.495, 0.505), ("θ_B≈51", 0.505, 0.515), ("θ_B≈52", 0.515, 0.525)]
rows = []
masses = []
for nm, lo_, hi_ in bins:
    sel = (thB >= lo_) & (thB < hi_)
    masses.append(float(w[sel].sum()))
for nm, x in pars:
    mu_all = wmean(x, w)
    sd_all = math.sqrt(wmean((x - mu_all) ** 2, w))
    r = [nm, f"{100 * mu_all:.2f}"]
    for _, lo_, hi_ in bins:
        sel = (thB >= lo_) & (thB < hi_)
        if w[sel].sum() > 0:
            mb = wmean(x[sel], w[sel])
            r.append(f"{100 * mb:.2f} ({(mb - mu_all) / sd_all:+.2f} dp)")
        else:
            r.append("—")
    rows.append(r)
table(["Parâmetro", "média geral"] + [b[0] for b in bins], rows)
out("Massa posterior (estrutural) em cada faixa: " +
    ", ".join(f"{b[0]}: {pct(m, 1)}" for b, m in zip(bins, masses)))
out()
# correlação parcial simples: regressão linear de θ_B nos parâmetros (contribuição)
X = np.column_stack([x for _, x in pars])
Xc = X - (w[:, None] * X).sum(0)
yc = thB - wmean(thB, w)
sw = np.sqrt(w)
beta, *_ = np.linalg.lstsq(Xc * sw[:, None], yc * sw, rcond=None)
contrib = beta ** 2 * np.array([wmean(c ** 2, w) for c in Xc.T])
r2 = 1 - wmean((yc - Xc @ beta) ** 2, w) / wmean(yc ** 2, w)
rows = [[nm, f"{b:+.4f}", pct(c / wmean(yc ** 2, w), 1)]
        for (nm, _), b, c in zip(pars, beta, contrib)]
rows.sort(key=lambda r: -float(r[2].rstrip("%")))
table(["Parâmetro", "∂θ_B/∂param (regressão)", "parcela da var(θ_B) (β²·var)"], rows)
out(f"R² da regressão linear: {r2:.3f}.")
out()

# =====================================================================
# 14. h_j ≠ 0: sensibilidade a house effects com sinal não escolhido
# =====================================================================
out("## Sensibilidade a house effects (σ_house) — sinal não imposto")
out()
rows = []
for sh in [0.0, 0.01, 0.02, 0.04, 0.08]:
    m = poll_model(0.01, sh, 0.02)
    t = expit(m["zT"])
    s = math.sqrt(m["vT"]) * t * (1 - t)
    th_c = theta_A(P_III, TAU)
    w_ = norm_w(LLT + ll_poll(th_c, m["zT"], m["vT"]))
    rows.append([f"{sh:.2f}", f"≈{100 * sh / 4:.2f}", pct(t), f"{100 * s:.2f}",
                 pct(1 - Phi((0.5 - t) / s), 1), pct(wmean(th_c, w_)),
                 pct(float(np.sum(w_ * (th_c > 0.5))), 1)])
table(["σ_house (logit)", "≈ p.p.", "θ_B pesquisas", "dp (p.p.)",
       "P(θ_B>0,5) pesquisas", "E[θ_A] completo", "P(θ_A>0,5) completo"], rows)
out("Viés comum a todos os institutos (h̄ ≠ 0) não é identificável só com "
    "pesquisas: com prior centrado em zero, ele entra como incerteza. Tabela: "
    "deslocamento sistemático hipotético δ (mesmo sinal para todos) aplicado ao nowcast.")
out()
rows = []
for dlt in [-0.08, -0.04, -0.02, 0.0, 0.02, 0.04, 0.08]:
    t = expit(pm["zT"] + dlt)
    s = math.sqrt(pm["vT"]) * t * (1 - t)
    rows.append([f"{dlt:+.2f}", f"{100 * (t - th_poll):+.2f}", pct(t),
                 pct(1 - Phi((0.5 - t) / s), 1)])
table(["δ (logit)", "Δθ_B (p.p.)", "θ_B", "P(θ_B>0,5)"], rows)


out("### Modelo completo: horizonte, deriva e viés comum")
out()
out("P(θ_A>0,5) e E[θ_A] do modelo completo (pd+df+qu+pesquisas) variando o "
    "horizonte H até a eleição, σ_drift e um viés comum hipotético δ "
    "(sinal NÃO escolhido: ambos os sinais mostrados).")
out()
rows = []
for sdd in [0.01, 0.02]:
    for H in [0, 7, 14]:
        for dlt in [-0.04, 0.0, 0.04]:
            m = poll_model(sdd, 0.02, 0.02, H=H)
            w_ = norm_w(LLT + ll_poll(TH, m["zT"] + dlt, m["vT"]))
            q = wq(TH, w_, [0.05, 0.95])
            rows.append([f"{sdd:.2f}", H, f"{dlt:+.2f} (≈{100 * dlt / 4:+.0f} p.p.)",
                         pct(wmean(TH, w_)), f"{pct(q[0])} – {pct(q[1])}",
                         pct(float(np.sum(w_ * (TH > 0.5))), 2)])
table(["σ_drift", "H (dias)", "viés comum δ em θ_B", "E[θ_A]", "IC 90%",
       "P(θ_A>0,5)"], rows)

# =====================================================================
# 15. PESO INTERMEDIÁRIO DA MATRIZ pd + VIÉS DE RECORDAÇÃO + ELEIÇÃO EM 10 DIAS
# =====================================================================
H_ELEICAO = 11          # eleição em 25/out (10 dias após 15/out); última pesquisa 14/out
LAMBDAS = [1.0, 0.5, 0.25]     # peso da matriz pd: multiplica o n efetivo (κ_g) das linhas pd
SIG_RECALL = [0.0, 0.005, 0.01]  # dp do viés de recordação/ponderação do 1T, em θ_A (sem sinal)
LAMBDA_REC, SIG_REC = 0.5, 0.005  # configuração recomendada (peso intermediário, viés baixo)
out("## Peso intermediário da matriz pd, viés de recordação e eleição em 10 dias")
out()
out("Peso λ da matriz pd: α_g = λ·n_eff,g·m_g + 0,5 (equivale a DEFF_pd = 2/λ; "
    "df e qu mantêm DEFF=2). Viés de recordação: θ_A,estr ← θ_A,estr + b, "
    "b ~ N(0, σ_r²), sem sinal imposto (representa erro na lembrança/ponderação "
    "do voto do 1T que desloca a matriz como um todo). Pesquisas: σ_house=0,02, "
    "σ_extra=0,02, horizonte H=11 dias (eleição em 25/out). "
    f"Configuração recomendada: λ={LAMBDA_REC}, σ_r={100 * SIG_REC:.1f} p.p.")
out()
rng_rec = np.random.default_rng(SEED + 1)
rows = []
RES["peso_pd"] = {}
for lam in LAMBDAS:
    Ql, lll = draw_Q_post(alphas("M2", 2.0 / lam), 2.0, True, True, M)
    thl0 = theta_A(resolve(Ql, "III"), draw_turnout(M))
    del Ql
    for sr in SIG_RECALL:
        thl = np.clip(thl0 + rng_rec.normal(0, sr, M), 1e-4, 1 - 1e-4) if sr > 0 else thl0
        w0 = norm_w(lll)
        q0 = wq(thl, w0, [0.05, 0.95])
        r = [f"{lam:.2f}", f"{100 * sr:.1f}",
             f"{pct(wmean(thl, w0))} [{pct(q0[0], 1)}; {pct(q0[1], 1)}] / {pct(float(np.sum(w0 * (thl > 0.5))), 1)}"]
        for sdd in [0.01, 0.02]:
            m = poll_model(sdd, 0.02, 0.02, H=H_ELEICAO)
            w = norm_w(lll + ll_poll(thl, m["zT"], m["vT"]))
            q = wq(thl, w, [0.05, 0.95])
            pA = float(np.sum(w * (thl > 0.5)))
            RES["peso_pd"][f"lam={lam}|sr={sr}|drift={sdd}"] = dict(
                mean=wmean(thl, w), q05=q[0], q95=q[1], pA=pA, ess=ess(w))
            r.append(f"{pct(wmean(thl, w))} [{pct(q[0])}; {pct(q[1])}] / **{pct(pA, 1)}** (ESS {ess(w):,.0f})".replace(",", "."))
        rows.append(r)
table(["λ (peso pd)", "σ_r (p.p.)", "estrutural: E[θ_A] [IC90] / P(θ_A>0,5)",
       "completo, σ_drift=0,01: E [IC90] / P", "completo, σ_drift=0,02: E [IC90] / P"], rows)
rows = []
for sdd in [0.01, 0.02]:
    m = poll_model(sdd, 0.02, 0.02, H=H_ELEICAO)
    t = expit(m["zT"])
    s = math.sqrt(m["vT"]) * t * (1 - t)
    RES["peso_pd"][f"lam=0|drift={sdd}"] = dict(mean=float(1 - t), pA=Phi((0.5 - t) / s))
    rows.append([f"{sdd:.2f}", pct(1 - t), f"{100 * s:.2f}", pct(Phi((0.5 - t) / s), 1)])
out("Referência λ=0 (só pesquisas nacionais, H=11):")
out()
table(["σ_drift", "E[θ_A]", "dp (p.p.)", "P(θ_A>0,5)"], rows)

# =====================================================================
# 16. VIRADA: TROCA DE VOTOS (CROSSOVER) × COMPARECIMENTO DOS FALTANTES
# =====================================================================
out("## Virada: troca de votos × comparecimento dos faltantes (configuração recomendada)")
out()
rng_v = np.random.default_rng(SEED + 2)
Qv, llv = draw_Q_post(alphas("M2", 2.0 / LAMBDA_REC), 2.0, True, True, M)
Tv = draw_turnout(M)
Pv = resolve(Qv, "III")
del Qv
Vv = votes(Pv, Tv)
Sv = Vv[:, 0] + Vv[:, 1]
bv = rng_v.normal(0, SIG_REC, M)
thv = np.clip(Vv[:, 1] / Sv + bv, 1e-4, 1 - 1e-4)
mv = poll_model(0.01, 0.02, 0.02, H=H_ELEICAO)
wv = norm_w(llv + ll_poll(thv, mv["zT"], mv["vT"]))
P0 = np.einsum("n,ngk->gk", wv, Pv)
tau0 = np.einsum("n,ng->g", wv, Tv)
t0, V0 = th_point(P0, tau0)
NAt, NBt = N[iA] * tau0[iA], N[iB] * tau0[iB]
xab0, xba0 = P0[iA, 0], P0[iB, 1]
fbn = P0[iABS, 2]
gap = V0[0] - V0[1]
RES["virada"] = dict(thetaA=t0, gap=gap, XAB=xab0, XBA=xba0, NA=NAt, NB=NBt, fBN=fbn)
out(f"Base: médias posteriores (λ={LAMBDA_REC}, σ_r={100 * SIG_REC:.1f} p.p., H={H_ELEICAO}, "
    f"σ_drift=0,01). θ_A = {pct(t0)}; V_B − V_A = {gap:,.0f}; X_AB = {pct(xab0)}; "
    f"X_BA = {pct(xba0)}; eleitores A comparecentes = {NAt:,.0f}; B = {NBt:,.0f}; "
    f"fração BN dos faltantes = {pct(fbn, 1)}.".replace(",", "."))
out()
out("Alvo: V_A = V_B + 1 (50% + 1 dos válidos). Todo o resto fixo. "
    "Equações condicionais, NÃO previsões.")
out()

# 16a: X_BA necessário para cada X_AB
out("### 16a. Saída B→A necessária para cada saída A→B (0% a 7%)")
out()
rows = []
for xab in np.arange(0, 0.07001, 0.005):
    VA = V0[1] + NAt * (xab0 - xab)
    VB = V0[0] - NAt * (xab0 - xab)
    d = (VB - VA + 1) / (2 * NBt)
    xba = xba0 + d
    rows.append([pct(xab, 1), f"{NAt * xab / 1e6:.2f} mi", pct(VA / (VA + VB)),
                 f"**{pct(xba)}**", f"{100 * d:+.2f}", f"{NBt * xba / 1e6:.2f} mi"])
table(["X_AB (A→B)", "eleitores A→B", "θ_A sem mudar X_BA", "X_BA necessário",
       "Δ vs atual (p.p.)", "eleitores B→A"], rows)
out(f"Regra: X_BA ≈ {pct(xba0 + (gap + 1 - 2 * NAt * xab0) / (2 * NBt))} + "
    f"{NAt / NBt:.3f} × X_AB.")
out()

# 16b: faltantes necessários por divisão
out("### 16b. Faltantes do 1º turno (adicionais) necessários por divisão A:B")
out()
out(f"Faltantes = abstenção do 1T ({N[iABS]:,.0f}). O modelo já supõe "
    f"τ_ABS ≈ {pct(tau0[iABS], 1)} comparecendo com a linha ABS (≈ "
    f"{pct(P0[iABS, 1] / (P0[iABS, 0] + P0[iABS, 1]), 1)} A entre válidos); "
    "a tabela dá os ADICIONAIS.".replace(",", "."))
out()
rows = []
for lab, a in [("55:45", .55), ("60:40", .60), ("65:35", .65), ("2:1", 2 / 3), ("70:30", .70),
               ("75:25", .75), ("80:20", .80), ("85:15", .85), ("90:10", .90), ("95:5", .95),
               ("100:0", 1.0)]:
    d = 2 * a - 1
    n0 = (gap + 1) / d
    n1 = n0 / (1 - fbn)
    f = lambda n: f"{pct(n / N[iABS], 1)}" + (" ❌" if n > N[iABS] else "")
    rows.append([lab, f(n0), f"{n0 / 1e6:.1f} mi", f(n1), f"{n1 / 1e6:.1f} mi",
                 pct(T1 + n1 / ELEIT, 1)])
table(["A:B dos novos", "% faltantes (todos válidos)", "pessoas",
       f"% faltantes (BN {pct(fbn, 0)})", "pessoas", "comparecimento total resultante"], rows)

# 16c: combinações
out("### 16c. Combinações troca de votos × faltantes adicionais (com BN)")
out()
k_ba, k_ab = 2 * NBt / 100, 2 * NAt / 100       # votos de margem por p.p.
out(f"Equação: {k_ba / 1e6:.3f}·ΔX_BA + {k_ab / 1e6:.3f}·(−ΔX_AB) + "
    f"{N[iABS] * (1 - fbn) / 100 / 1e6:.3f}·x·(a−b) ≥ {gap / 1e6:.3f} (mi; ΔX em p.p., "
    "x em % dos faltantes).")
out()
rows = []
for dl in [0, 0.5, 1.0, 1.5]:
    rem = gap + 1 - dl * (k_ba + k_ab)
    r = [f"±{dl:.1f} p.p. ({pct(xba0 + dl / 100, 1)} / {pct(xab0 - dl / 100, 1)})"]
    for a in [.55, .60, 2 / 3, .75]:
        x = rem / (N[iABS] * (1 - fbn) * (2 * a - 1))
        r.append(pct(max(x, 0), 0) + (" ❌" if x > 1 else ""))
    rows.append(r)
dl0 = (gap + 1) / (k_ba + k_ab)
rows.append([f"±{dl0:.2f} p.p. ({pct(xba0 + dl0 / 100, 1)} / {pct(xab0 - dl0 / 100, 1)})",
             "0%", "0%", "0%", "0%"])
table(["Troca de votos (B→A / A→B)", "55:45", "60:40", "2:1", "75:25"], rows)

# 16d: probabilidade combinada e caminho mais provável
out("### 16d. Probabilidade combinada e caminho mais provável da virada")
out()
out("Choque de comparecimento dos faltantes e: N(0, σ_e² · eleitorado), sem sinal; "
    "fração A entre válidos dos novos s ~ N(0,5; σ_s²) (centro entre pd ≈45 e qu ≈53). "
    "PRIORS ASSUMIDOS — não há dados sobre eles. O choque é aplicado após a "
    "ponderação pelas pesquisas (erro de modelo de comparecimento que as pesquisas não veem).")
out()
VA0 = Vv[:, 1] + bv * Sv
VB0 = Vv[:, 0] - bv * Sv
XBAv, XABv = Pv[:, iB, 1], Pv[:, iA, 0]
fbv = Pv[:, iABS, 2]
mu_ = lambda x, ww: wmean(x, ww)
rows = []
RES["virada"]["combinada"] = {}
for se, ss in [(0.0, 0.05), (0.01, 0.05), (0.02, 0.05), (0.02, 0.08), (0.03, 0.08)]:
    e = rng_v.normal(0, se, M) * ELEIT
    sA = np.clip(rng_v.normal(0.5, ss, M), 0, 1)
    va = VA0 + e * (1 - fbv) * sA
    vb = VB0 + e * (1 - fbv) * (1 - sA)
    win = va > vb + 1
    pw = float(np.sum(wv * win))
    wc = wv * win / pw
    d_cross = 2 * ((XBAv - mu_(XBAv, wv)) * N[iB] * Tv[:, iB]
                   + (mu_(XABv, wv) - XABv) * N[iA] * Tv[:, iA])
    d_surge = e * (1 - fbv) * (2 * sA - 1)
    d_rec = 2 * bv * Sv
    c1, c2, c3 = mu_(d_cross, wc), mu_(d_surge, wc), mu_(d_rec, wc)
    tot = c1 + c2 + c3
    RES["virada"]["combinada"][f"se={se}|ss={ss}"] = dict(pA=pw, cross=c1, surge=c2, recall=c3)
    rows.append([f"{100 * se:.0f} p.p.", f"{100 * ss:.0f} p.p.", f"**{pct(pw, 1)}**",
                 pct(mu_(XBAv, wc), 1), pct(mu_(XABv, wc), 1),
                 f"{c1 / 1e6:.2f} mi ({pct(c1 / tot, 0)})", f"{c2 / 1e6:.2f} mi ({pct(c2 / tot, 0)})",
                 f"{c3 / 1e6:.2f} mi ({pct(c3 / tot, 0)})", f"{ess(wv * win):,.0f}".replace(",", ".")])
table(["σ_e (comparec.)", "σ_s (divisão)", "P(θ_A>0,5)", "X_BA (dado vitória A)",
       "X_AB (dado vitória A)", "contrib. troca", "contrib. comparec.", "contrib. viés recordação",
       "ESS (vitórias)"], rows)
out("Contribuições = média, nas simulações em que A vence, do quanto cada alavanca "
    "reduziu a diferença em relação ao esperado (em votos de margem).")
out()
# FORM: ponto mais provável sobre a fronteira
sxba = math.sqrt(mu_((XBAv - mu_(XBAv, wv)) ** 2, wv))
sxab = math.sqrt(mu_((XABv - mu_(XABv, wv)) ** 2, wv))
rows = []
for se, ss in [(0.02, 0.05), (0.03, 0.08)]:
    best = None
    for xs in np.linspace(0, 0.30, 301):
        for sa in np.linspace(0.5, 1, 251):
            surge = xs * N[iABS]
            rem = gap + 1 - surge * (1 - fbn) * (2 * sa - 1)
            a1, a2 = 2 * NBt, 2 * NAt
            den = (a1 * sxba) ** 2 + (a2 * sxab) ** 2
            dba, dab, dc = (0, 0, 0) if rem <= 0 else (rem * a1 * sxba ** 2 / den,
                                                       rem * a2 * sxab ** 2 / den, rem ** 2 / den)
            d2 = (surge / (se * ELEIT)) ** 2 + ((sa - 0.5) / ss) ** 2 + dc
            if best is None or d2 < best[0]:
                best = (d2, xs, sa, dba, dab)
    d2, xs, sa, dba, dab = best
    rows.append([f"{100 * se:.0f} / {100 * ss:.0f} p.p.", f"{math.sqrt(d2):.2f} dp",
                 pct(xs, 1), pct(sa, 1), f"{pct(xba0 + dba)} (+{100 * dba:.2f})",
                 f"{pct(xab0 - dab)} (−{100 * dab:.2f})"])
table(["σ_e / σ_s", "distância", "faltantes adicionais", "A entre novos",
       "X_BA", "X_AB"], rows)
out(f"Ponto mais provável sobre a fronteira de virada (menor distância em dp; "
    f"dp(X_BA)={100 * sxba:.2f} p.p., dp(X_AB)={100 * sxab:.2f} p.p.). O comparecimento só "
    "age via produto (quantidade × desequilíbrio da divisão), efeito de 2ª ordem: o "
    "ponto ótimo não o utiliza.")
out()

with open("resultados.md", "w") as f:
    f.write("\n".join(OUT) + "\n")
with open("resultados.json", "w") as f:
    json.dump(RES, f, indent=1, default=float)
print("ok")
