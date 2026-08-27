# subgrad — Content Tracker

One row per thing that goes out. The point is to notice what actually moves
traffic before making more of it. Cross-check the **Result** column against
Vercel Analytics (vercel.com → subgrad → Analytics) the day after each post.

**Status key:** `IDEA` → `DRAFTED` → `POSTED` → `DEAD` (blocked / abandoned)

---

## Assets on hand

| Asset | File | Where it works |
|---|---|---|
| λ logo, 600×600 | `subgrad-mark.png` | LinkedIn page, profile, favicon source |
| **Sizzle reel**, 1280×720, 5.2s | `clips/subgrad-sizzle-16x9.gif` | Lead asset. Both labs + end card. IndieHackers, LinkedIn, Twitter. |
| Surface Lab, 1280×720, 2.7s | `clips/subgrad-surface-lab-16x9.gif` | The saddle escape, captioned |
| Graph Lab, 1280×720, 3.3s | `clips/subgrad-graph-lab-16x9.gif` | Best single asset for the "tutor reacts to state" claim |
| Graph Lab **vertical**, 1080×1920 | `clips/subgrad-graph-lab-9x16.gif` | Reels / Shorts / TikTok. Stacked crops, legible on a phone. |
| Carousel slides, 1080×1080 | `carousel/subgrad-slide-*.png` | LinkedIn / Twitter / IG carousel |
| Clip build script | `make_clips.py` | Regenerates every clip above from the raw exports. Re-run after UI changes. |
| Launch post drafts (4 channels) | `../LAUNCH_KIT_FINAL.md` | — |

> Raw `gif_creator` exports play at **2300 ms/frame (~0.43 fps)** regardless of
> capture spacing — that, not the capture rate, is why the first cuts looked
> laggy. `make_clips.py` retimes to 140 ms/frame. Never post a raw export.

---

## Log

| Date | Channel | What went out | Status | Result | Notes |
|---|---|---|---|---|---|
| *(fill in)* | Reddit — r/learnmachinelearning | Genuine comment, no link | POSTED | — | Part of account warm-up, pre-ban |
| *(fill in)* | Reddit — r/learnmachinelearning | Genuine comment, no link | POSTED | — | Same |
| *(fill in)* | Reddit — account | — | **DEAD** | Account banned | Whole channel closed. Appeal via reddit.com/appeals is low-odds; a genuinely fresh account would need a long slow runway before any mention. |
| 2026-08-27 | Hacker News | Show HN submission | **DEAD (for now)** | "Sorry, your account isn't able to submit this site" | New-account submission gate. Two paths: comment genuinely for ~2 weeks then retry, **or** email `hn@ycombinator.com` describing the project honestly (documented route, mods do enable accounts this way). Do both. |
| | IndieHackers | Launch post + Product listing | DRAFTED | | Draft is in `LAUNCH_KIT_FINAL.md`. No account-age gate — this is the next real move. |
| | LinkedIn | Company Page + Founder position | IDEA | | Page needs creating; logo + skills + media list already prepared |
| | LinkedIn | Carousel post | DRAFTED | | Slides generated, see `carousel/` |
| | Direct — friends / classmates / Discords | Personal ask, 5-10 people | IDEA | | Highest-conviction channel available right now: no gatekeeper, no ban risk, people who already trust you |
| | r/learnmath | Megathread comment (**not** a post) | BLOCKED | | Blocked by the ban anyway. Note for later: 5/5 comparable standalone posts there scored 0; mods route self-made resources to the pinned megathread. |

---

## What to actually watch

Not vanity numbers. These three:

1. **Did anyone open a lab?** Vercel Analytics, `/app/*` routes vs. landing-only.
   Landing views with no lab opens = the pitch works, the product doesn't land.
2. **Which lab?** If it's lopsided, that's the real product and the other three
   are scaffolding. Worth knowing before building more.
3. **Did anyone say something specific?** One comment describing an actual
   moment ("the saddle one surprised me") is worth more than 200 upvotes.

## Standing lessons

- **Sign-in walls kill launches.** Guest mode shipping is why the current drafts
  are honest. Don't add a wall to measure users — Vercel Analytics already does it.
- **Account age is a real gate**, on both Reddit and HN, and it can't be shortcut.
  Every channel that gates on history needs its runway started *before* you need it.
- **Lead with the labs, not the tutor.** Show HN base rates are lopsided: "AI
  tutor" posts landed at 1-5 points; interactive-explorable framing cleared 119+.
