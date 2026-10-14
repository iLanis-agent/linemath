(function (root) {
  "use strict";
  var DRIFT_OZ = 0.25; // labeled ounces to add per mph of drift

  function round0(x) { return Math.round(x); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function spoolPlan(ratedYards, ratedDia, lineDia) {
    if (!(ratedYards > 0) || !(ratedDia > 0) || !(lineDia > 0)) return { error: "the spool and the diameters must be positive" };
    var r = ratedDia / lineDia; // capacity scales with cross-section
    var yards = round0(ratedYards * r * r);
    var verdict;
    if (lineDia < ratedDia) verdict = "thinner line, deeper spool";
    else if (lineDia === ratedDia) verdict = "the box promise";
    else verdict = "thicker line, honest shortfall";
    return { yards: yards, verdict: verdict };
  }

  function knotPlan(lb, pct) {
    if (!(lb > 0) || !(pct > 0)) return { error: "the line and the knot must be positive" };
    if (pct > 100) return { error: "a knot cannot beat the line" };
    var strength = round1(lb * pct / 100);
    var verdict;
    if (pct < 70) verdict = "the knot is the weak link";
    else if (pct <= 90) verdict = "a fair knot";
    else verdict = "nearly the line itself";
    return { strength: strength, verdict: verdict };
  }

  function sinkerPlan(depthFt, driftMph) {
    if (!(depthFt > 0)) return { error: "the depth must be positive" };
    if (!(driftMph >= 0)) return { error: "the drift cannot be negative" };
    var oz = round1(depthFt / 10 + driftMph * DRIFT_OZ);
    var verdict;
    if (oz <= 1) verdict = "a split-shot day";
    else if (oz <= 3) verdict = "a standard sinker";
    else if (oz <= 6) verdict = "a drift weight";
    else verdict = "an anchor in disguise";
    return { oz: oz, verdict: verdict };
  }

  function renderSpool(r, ratedYards, ratedDia, lineDia) {
    return "A spool rated for " + ratedYards + " yd of " + ratedDia + " mm takes about " + r.yards
      + " yd of your " + lineDia + " mm line - " + r.verdict + ".";
  }

  function renderKnot(r, lb, pct) {
    return "Your " + lb + " lb line with a labeled " + pct + "% knot holds " + r.strength + " lb - " + r.verdict + ".";
  }

  function renderSinker(r, depthFt, driftMph) {
    return "At " + depthFt + " ft with " + driftMph + " mph of drift you need about " + r.oz + " oz - " + r.verdict + ".";
  }

  var api = { spoolPlan: spoolPlan, knotPlan: knotPlan, sinkerPlan: sinkerPlan, renderSpool: renderSpool, renderKnot: renderKnot, renderSinker: renderSinker };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.LineMath = api;
})(this);
