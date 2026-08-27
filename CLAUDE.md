# CLAUDE.md

Guidance for Claude Code sessions working in this repo. Read this before
touching anything — it's the non-negotiables, not a tour.

## What this is

**subgrad** — four interactive browser labs (3D gradient descent, backprop
graph, OLS/leverage sandbox, PyTorch shape checker) plus a Socratic tutor.
Live at [subgrad.vercel.app](https://subgrad.vercel.app), no signup. Solo
project, pre-traction. Full pitch/voice/do-not-say list: `marketing/BRAND.md`
— read that before writing anything user-facing (landing copy, launch posts,
error messages).

## Non-negotiable: the zero-hallucination math policy

**The LLM never computes math.** Every derivative, integral, and equivalence
check runs through SymPy in `backend/app/math_engine/verifier.py` — the model
only decides *when* to call it and writes the pedagogy around the result. If
you're touching anything in the tutor/chat path and find yourself asking the
model to produce a numeric or symbolic result directly, stop — that's the one
architectural line this product can't cross without lying about what it is.
Full detail: `backend/README.md`.

## Architecture

```
frontend/     React 19 + Vite + Tailwind v4 + Zustand (persist) + Three.js
              (react-three-fiber) for Surface Lab + React Flow for Graph Lab
backend/      FastAPI + SymPy + Gemini (function calling) + pydantic-settings
supabase/     Auth + session persistence (optional — guest mode needs none of it)
marketing/    Brand context, launch copy, demo clips + the script that builds them
docs/         Planning docs / PRDs from the build — historical record, not current spec
```

## Commands

```bash
# frontend
cd frontend && npm install && npm run dev      # localhost:5173
npm run build && npm run lint

# backend
cd backend && pip install -r requirements.txt
cp .env.example .env   # needs GEMINI_API_KEY for the tutor chat
uvicorn app.main:app --reload                  # localhost:8000
pytest                                          # 35+ tests, math_engine is the one that matters most
```

Guest mode (no login, no Supabase) covers all four labs. Only the tutor chat
needs `GEMINI_API_KEY`.

## Gotchas already paid for — don't rediscover these

- **`CORS_ORIGINS` must stay `Annotated[List[str], NoDecode]`.** Without
  `NoDecode`, pydantic-settings JSON-decodes the env var *before* the
  `field_validator` runs, so pasting a bare URL (exactly what the deploy
  runbook says to do) raises `SettingsError` at import and the app never
  boots. See `backend/app/core/config.py`.
- **`GEMINI_MODEL` must be a currently-servable model for new API keys.**
  `gemini-2.5-flash` is retired for newly-created keys/projects (still works
  for old grandfathered ones) — this fails as a confusing 404, not an
  obvious "wrong model name" error. Check current model availability before
  assuming a stale model string is fine.
- **Render Blueprint deploys** should use the public-repo URL path, not the
  GitHub-connected import flow — the latter triggers an OAuth authorization
  grant prompt that isn't necessary for a public repo.
- **`.gemini/` and `backend/.env` must never be committed.** Both are
  gitignored. `.gemini/settings.json` in particular can carry a live API key
  in an MCP request header — if you ever see it untracked and unignored,
  that's one commit away from a public leak. Verify with
  `git add -An | grep -Ei "\.env$|\.gemini"` before any push.
- **The Graph Lab node cards clip long values on purpose.** Under
  'exploding' pathology mode, derived values can print as 20+ char `e+NNN`
  strings — `LossNode`/`ParameterNode`/`InputNode` truncate with a hover
  title rather than letting the card blow past the viewport (it used to).
  Don't remove the `max-w`/`overflow-hidden`/`truncate` combo without
  re-testing Explode mode.
- **The hero has been rebuilt three times** (mini-compiler → live loss
  surface → back to mini-compiler) and a full light-mode landing page was
  built and scrapped same-session. Both are settled, not open questions —
  see `marketing/BRAND.md`'s "learned the hard way" note before re-litigating
  either.
- **Raw GIF recordings from browser-automation tools play at ~0.43fps**
  regardless of capture spacing — that's a frame-delay-metadata issue, not a
  capture-rate issue. `marketing/make_clips.py` retimes correctly; never post
  a raw export as a demo clip.

## Voice, if you're writing anything user-facing

Direct, plain, states its own limits before someone else finds them. Full
do/don't list in `marketing/BRAND.md`. The short version: never call the
shape checker an AST parser (it's regex), never call SymPy `equals()`
"verification" in a strong sense (it leans on numeric sampling), never call
the Data Sandbox "data poisoning" (no adversary, no threat model — it's
leverage), never imply users or traction that don't exist.

## Deploy

Full runbook: `docs/DEPLOYMENT.md`. Backend → Render (free tier, cold-starts
30-60s after idle), frontend → Vercel, auth/db → Supabase, all free tier.
