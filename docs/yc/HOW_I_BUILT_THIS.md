# How I built subgrad

> Draft for the YC application's founder/progress narrative. Written to be
> trimmed, not padded — cut to whatever the actual field's length is rather
> than shrinking the font. Same honesty rules as everywhere else in this
> repo: nothing here that BRAND.md's do-not-say list would reject.

---

## Full version (~320 words)

I'm a student, and I built subgrad alone — no co-founder, no engineering
team, and I'm not a professional software engineer. I directed Claude Code
as my engineering team: I wrote the specs, made every product and design
call, tested every feature myself before it shipped, and killed the ones
that didn't work.

It started as an AI math tutor. About a week in, I realized I was building a
worse ChatGPT — nobody needs another chat box that explains the chain rule.
My actual problem was never that nobody explained gradient descent to me. I
could recite the update rule. I had no feel for what a learning rate of 0.9
would do to a real run until I watched it happen. So I threw out the tutor
and built four labs instead: a 3D loss surface you step through by hand, a
backprop graph where you can trigger exploding or vanishing gradients on
purpose, an outlier/leverage sandbox, and a static shape checker for PyTorch
models.

The one rule I didn't compromise on: the AI never does the math. Every
derivative, integral, and equivalence check runs through SymPy — the model
only decides when to call it and writes the explanation around the result.
If the model could just assert an answer, the whole thing would be exactly
the tool I was trying not to build again.

I rebuilt the hero section of the landing page three times in one week and
scrapped an entire light-mode redesign the same day I shipped it, because it
looked wrong the moment it was live. I'd rather throw work away than ship
something I don't actually believe in.

It's live at subgrad.vercel.app, zero users as of writing, desktop only —
I'm not going to pretend the mobile experience exists yet. I posted the
first real comments about it three days ago and got my Reddit account banned
for it, which is its own lesson about moving too fast on a channel I hadn't
earned yet. I'm not stopping.

---

## Condensed version (~90 words, for a short-answer field)

I built subgrad alone as a student, directing Claude Code as my engineering
team — I wrote the specs, made every product call, and tested everything
myself. It started as an AI tutor; a week in I realized I was building a
worse ChatGPT, so I scrapped it for four interactive labs where you break
gradient descent, backprop, and tensor shapes on purpose instead of reading
about them. The one non-negotiable: the AI never computes the math — every
result runs through SymPy first. Live, zero users, desktop only, and honest
about both.

---

## If there's room for a "what this proves" line

Building this alone, at this speed, with no formal engineering background,
is itself the argument: one person with the right tools can now ship and
iterate at a pace that used to need a team. That's the bet behind the
product and the bet behind how it got made.
