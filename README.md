# Line math

The spool names the yards, the knot names the strength, and the drift names the sinker.

Fishing tackle is sold on three hopeful numbers: spool yards measured with a line you did not buy, pound tests that stop at the first knot, and sinker guesses that ignore the current. Line math works all three honestly.

## The three tools

- **Spool plan** - rated capacity scales with the square of the diameter: `round0(ratedYards * (ratedDia / lineDia)^2)`, with the verdict naming a deeper spool, the box promise, or an honest shortfall.
- **Knot plan** - line test through the knot's labeled percentage becomes the real breaking strength: `round1(lb * pct / 100)`, banded from "the knot is the weak link" to "nearly the line itself". Over 100% is refused: a knot cannot beat the line.
- **Sinker plan** - depth at a labeled 1 oz per 10 ft plus a labeled quarter-ounce per mph of drift becomes the ounces you need: `round1(depth/10 + drift * 0.25)`, banded from a split-shot day to an anchor in disguise.

## Honesty notes

Illustrative planning arithmetic only. Every figure is a labeled default you replace by reading your own boxes. Line ages in the sun and weakens at every nick, so retie often and test the knot, not the packet. Check local regulations for seasons, limits and tackle rules before you fish.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
