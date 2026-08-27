# subgrad — Brand Context

> This file exists so any future session (or person) can produce on-brand copy and
> assets without re-deriving all of this. It's the "brand-aware project" step:
> load this before writing marketing anything.

---

## The Three Ps

**Pain.** You can recite the chain rule and still have no feel for what a learning
rate of 0.9 actually does to a run. You can read the backprop equations and still
not know which node your NaN started at. You hit `mat1 and mat2 shapes cannot be
multiplied` and you're back to printing `.shape` into the void. Reading more
doesn't fix this — the gap isn't knowledge, it's intuition, and static diagrams
don't build intuition.

**Person.** Someone actively learning ML — self-taught, bootcamp, or in a course.
Past "what is a neuron," not yet fluent. They've already tried the textbook and
the lecture and the 3Blue1Brown video. They can write a training loop that
converges and still couldn't tell you why it diverged when it did. Skews student,
skews technical enough to read `nn.Linear(128, 64)` without flinching.

**Promise.** Four labs where you break the thing on purpose and watch exactly what
happens — with a tutor that reacts to your actual simulation state instead of
following a syllabus, and math computed by SymPy rather than guessed by a model.

---

## What it actually is

Four interactive browser labs + a Socratic tutor. Free, no signup, desktop-only.

| Lab | What you do | What it teaches |
|---|---|---|
| **Surface Lab** | Step gradient descent through a 3D loss surface (bowl / saddle / Rosenbrock), learning-rate slider | Step size vs. convergence vs. divergence; why saddles are the real problem |
| **Graph Lab** | Watch gradients flow backward through a computation graph; flip on exploding / vanishing / chaotic modes | Where in the graph the damage starts, not just NaN at the end |
| **Data Sandbox** | Drag one point, watch an OLS fit and MSE recompute live | Leverage and influence — why one outlier owns the whole line |
| **Shape Checker** | Paste a model definition, get dimension mismatches flagged statically | Distance between where a shape first broke and where it finally threw |

**The tutor.** Watches lab state, not just chat. When loss diverges, it interrupts
*there* and asks what you think just happened. Currently threshold-triggered, not
the model reasoning over your full trajectory — say it that way, don't inflate it.

---

## Visual identity

| Token | Hex | Use |
|---|---|---|
| `slate-950` | `#0b0a0a` | Page background (warm near-black) |
| `slate-900` | `#171514` | Card / panel background |
| `slate-700` | `#443f3d` | Borders, dividers |
| `emerald-400` | `#52c98a` | The λ mark, accent text |
| `emerald-500` | `#34ad70` | Primary buttons, key highlights |

- **Type:** JetBrains Mono throughout. The terminal register is the whole look —
  it's why the dark background is load-bearing, not decorative.
- **Mark:** λ in `emerald-400` on `slate-900`, thin `slate-700` frame. Sharp
  corners, no rounding, no gradients, no glow except the functional kind
  (a diverging value going red).
- **Logo file:** `subgrad-mark.png` (600×600)

**Learned the hard way:** a light-mode version of this landing page was built and
immediately scrapped — inverting the tokens produced something that read as
unfinished, and the monospace loses its justification without the dark backdrop.
Don't re-litigate that.

---

## Voice

Direct, plain, slightly blunt. Written by someone who was stuck on this stuff
recently, not by a marketing department.

**Do:**
- State limits before someone else finds them ("desktop only — on a phone it's bad
  and I won't pretend otherwise")
- Name what's shaky ("the interrupts are thresholds right now, not the model
  reading your state")
- Credit prior art plainly (TensorFlow Playground, distill.pub, micrograd)
- Ask real questions you actually want answered

**Don't:**
- "Revolutionary," "game-changing," "AI-powered platform," "supercharge," "unlock"
- Claim AST parsing — the shape checker is **regex**, and it gives up on dynamic
  control flow
- Call SymPy equivalence "verification" in a strong sense — `equals()` leans on
  numeric sampling and heuristics
- Call the Data Sandbox "data poisoning" — there's no adversary and no threat
  model. It's leverage and influence.
- Imply traction, users, or metrics that don't exist

---

## Standing facts (keep current)

- **Live:** https://subgrad.vercel.app — guest mode works, all four labs, no login
- **Repo:** github.com/SubhamSaiSamal/SubGrad
- **Stack:** FastAPI · SymPy · Gemini (function calling) · React/Vite · Three.js ·
  React Flow · Zustand · Supabase · Tailwind
- **Infra:** Vercel (frontend) + Render free tier (backend — 30-60s cold start,
  say this every time) + Supabase
- **Analytics:** Vercel Web Analytics is on
- **Users:** zero, and say so
