import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round0(x): return jsnum(math.floor(x + 0.5))

DRIFT_OZ = 0.25

def spool_plan(ratedYards, ratedDia, lineDia):
    if not (ratedYards > 0) or not (ratedDia > 0) or not (lineDia > 0):
        return {"error": "the spool and the diameters must be positive"}
    r = ratedDia / lineDia
    yards = round0(ratedYards * r * r)
    if lineDia < ratedDia: verdict = "thinner line, deeper spool"
    elif lineDia == ratedDia: verdict = "the box promise"
    else: verdict = "thicker line, honest shortfall"
    return {"yards": yards, "verdict": verdict}

def knot_plan(lb, pct):
    if not (lb > 0) or not (pct > 0):
        return {"error": "the line and the knot must be positive"}
    if pct > 100:
        return {"error": "a knot cannot beat the line"}
    strength = round1(lb * pct / 100)
    if pct < 70: verdict = "the knot is the weak link"
    elif pct <= 90: verdict = "a fair knot"
    else: verdict = "nearly the line itself"
    return {"strength": strength, "verdict": verdict}

def sinker_plan(depthFt, driftMph):
    if not (depthFt > 0):
        return {"error": "the depth must be positive"}
    if not (driftMph >= 0):
        return {"error": "the drift cannot be negative"}
    oz = round1(depthFt / 10 + driftMph * DRIFT_OZ)
    if oz <= 1: verdict = "a split-shot day"
    elif oz <= 3: verdict = "a standard sinker"
    elif oz <= 6: verdict = "a drift weight"
    else: verdict = "an anchor in disguise"
    return {"oz": oz, "verdict": verdict}

def render_spool(r, ratedYards, ratedDia, lineDia):
    return ("A spool rated for " + fmt(ratedYards) + " yd of " + fmt(ratedDia) + " mm takes about " + fmt(r["yards"])
            + " yd of your " + fmt(lineDia) + " mm line - " + r["verdict"] + ".")

def render_knot(r, lb, pct):
    return "Your " + fmt(lb) + " lb line with a labeled " + fmt(pct) + "% knot holds " + fmt(r["strength"]) + " lb - " + r["verdict"] + "."

def render_sinker(r, depthFt, driftMph):
    return "At " + fmt(depthFt) + " ft with " + fmt(driftMph) + " mph of drift you need about " + fmt(r["oz"]) + " oz - " + r["verdict"] + "."

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[200,0.3,0.2],[200,0.3,0.3],[200,0.3,0.4],[150,0.25,0.2],[300,0.35,0.25],[200,0.28,0.2],[250,0.3,0.15],[100,0.25,0.3],[0,0.3,0.2],[200,0.3,0]]:
    add("spoolPlan", spool_plan, render_spool, a)
for a in [[20,80],[20,60],[20,95],[10,75],[30,85],[15,50],[25,90],[12,70],[0,80],[20,0],[20,110]]:
    add("knotPlan", knot_plan, render_knot, a)
for a in [[30,4],[10,0],[60,8],[20,2],[45,6],[15,1],[80,10],[25,3],[0,4],[30,-1]]:
    add("sinkerPlan", sinker_plan, render_sinker, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
