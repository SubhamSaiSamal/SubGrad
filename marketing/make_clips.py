"""
Rebuild the subgrad launch clips from the raw gif_creator exports.

The raw exports play at 2300ms per frame (~0.43 fps) no matter how the frames
were captured — that, not the capture spacing, is why they read as "laggy".
Everything here retimes to a real cadence and burns in the captions a silent
autoplay clip needs to be readable.

Vertical does NOT letterbox the desktop UI (illegible on a phone) — it crops
the two regions that carry the story and stacks them.

Outputs into OUT:
  subgrad-surface-lab-16x9.gif   1280x720, captioned
  subgrad-graph-lab-16x9.gif     1280x720, captioned
  subgrad-graph-lab-9x16.gif     1080x1920, stacked crops
  subgrad-sizzle-16x9.gif        both clips + brand end card
"""
import os
from PIL import Image, ImageSequence, ImageDraw, ImageFont

SRC = r"C:\Users\Subham\Downloads"
OUT = r"C:\Users\Subham\Desktop\backup\FlowLogic\marketing\clips"
os.makedirs(OUT, exist_ok=True)

CLIP1 = os.path.join(SRC, "subgrad-clip1-surface-lab-saddle-escape-v2.gif")
CLIP2 = os.path.join(SRC, "subgrad-clip2-graph-lab-explode-tutor-interrupt-v2.gif")

# brand tokens (frontend/src/index.css)
BG     = (11, 10, 10)
PANEL  = (23, 21, 20)
BORDER = (68, 63, 61)
EM400  = (82, 201, 138)
EM500  = (52, 173, 112)
FG     = (245, 244, 243)
MUTED  = (138, 132, 130)

# Cascadia is the 3rd fallback in the site's own font stack, so this stays
# on-brand even though JetBrains Mono isn't installed system-wide.
F_BOLD = r"C:\Windows\Fonts\CascadiaCode.ttf"
F_REG  = r"C:\Windows\Fonts\CascadiaMono.ttf"

def font(p, s):
    return ImageFont.truetype(p, s)

def load(path):
    im = Image.open(path)
    return [f.convert("RGB") for f in ImageSequence.Iterator(im)]

# NB: the site's dot-grid texture is deliberately NOT reproduced here.
# Thousands of 2px dots is high-entropy noise that roughly doubles the GIF
# size for a texture nobody can see at social-feed scale.

# ---------------------------------------------------------------- landscape
def captioned_16x9(frames, captions, W=1280):
    """Clip on top, brand caption strip below. Exact 16:9."""
    H = round(W * 9 / 16)
    ch = round(frames[0].height * W / frames[0].width)
    strip = H - ch

    f_cap = font(F_BOLD, 25)
    f_tag = font(F_REG, 17)
    out = []
    for i, fr in enumerate(frames):
        c = Image.new("RGB", (W, H), BG)
        c.paste(fr.resize((W, ch), Image.LANCZOS), (0, 0))
        d = ImageDraw.Draw(c)
        d.rectangle([0, ch, W, H], fill=PANEL)
        d.line([(0, ch), (W, ch)], fill=BORDER, width=2)

        ty = ch + strip // 2
        d.rectangle([44, ty - 13, 49, ty + 13], fill=EM500)
        d.text((66, ty), captions[min(i, len(captions) - 1)], font=f_cap, fill=FG, anchor="lm")
        d.text((W - 44, ty), "subgrad.vercel.app", font=f_tag, fill=MUTED, anchor="rm")
        out.append(c)
    return out

# ----------------------------------------------------------------- vertical
# Source frames are 1568x749. These are the two regions that carry clip 2's
# story; the rest of the desktop UI is dead weight at phone size.
CROP_CHAT  = (238, 60, 762, 200)    # the tutor's interrupt message
CROP_GRAPH = (762, 255, 1568, 749)  # node graph + epoch/loss ticker

def vertical_9x16(frames, headline, captions):
    VW, VH = 1080, 1920
    inner = VW - 96
    x0 = 48

    cw, chh = CROP_CHAT[2] - CROP_CHAT[0], CROP_CHAT[3] - CROP_CHAT[1]
    gw, ghh = CROP_GRAPH[2] - CROP_GRAPH[0], CROP_GRAPH[3] - CROP_GRAPH[1]
    chat_h  = round(chh * inner / cw)
    graph_h = round(ghh * inner / gw)

    f_head = font(F_BOLD, 54)
    f_cap  = font(F_BOLD, 30)
    f_lbl  = font(F_REG, 22)
    f_url  = font(F_BOLD, 40)
    f_sub  = font(F_REG, 26)

    chat_y  = 470
    graph_y = chat_y + chat_h + 92
    out = []

    for i, fr in enumerate(frames):
        c = Image.new("RGB", (VW, VH), BG)
        d = ImageDraw.Draw(c)

        hy = 190
        for line in headline:
            d.text((x0, hy), line, font=f_head, fill=FG)
            hy += 70

        # panel 1 — the tutor
        d.text((x0, chat_y - 34), "THE TUTOR", font=f_lbl, fill=EM500)
        c.paste(fr.crop(CROP_CHAT).resize((inner, chat_h), Image.LANCZOS), (x0, chat_y))
        d.rectangle([x0 - 2, chat_y - 2, x0 + inner + 1, chat_y + chat_h + 1],
                    outline=BORDER, width=3)

        # panel 2 — the graph
        d.text((x0, graph_y - 34), "THE GRAPH", font=f_lbl, fill=EM500)
        c.paste(fr.crop(CROP_GRAPH).resize((inner, graph_h), Image.LANCZOS), (x0, graph_y))
        d.rectangle([x0 - 2, graph_y - 2, x0 + inner + 1, graph_y + graph_h + 1],
                    outline=BORDER, width=3)

        capy = graph_y + graph_h + 62
        d.rectangle([x0, capy - 15, x0 + 5, capy + 15], fill=EM500)
        d.text((x0 + 22, capy), captions[min(i, len(captions) - 1)],
               font=f_cap, fill=EM400, anchor="lm")

        d.text((x0, VH - 180), "subgrad.vercel.app", font=f_url, fill=FG)
        d.text((x0, VH - 126), "four labs · no signup · free", font=f_sub, fill=MUTED)
        d.rectangle([x0, VH - 84, x0 + 96, VH - 78], fill=EM500)
        out.append(c)
    return out

# ----------------------------------------------------------------- end card
def end_card(W, H):
    c = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(c)
    d.rectangle([30, 30, W - 30, H - 30], outline=BORDER, width=3)
    bs = 76
    bx, by = (W - bs) // 2, H // 2 - 128
    d.rectangle([bx, by, bx + bs, by + bs], fill=PANEL, outline=BORDER, width=2)
    d.text((bx + bs // 2, by + bs // 2), "λ", font=font(F_BOLD, 48), fill=EM400, anchor="mm")
    d.text((W // 2, by + bs + 56), "subgrad", font=font(F_BOLD, 52), fill=FG, anchor="mm")
    d.text((W // 2, by + bs + 110), "four labs · break them on purpose",
           font=font(F_REG, 25), fill=MUTED, anchor="mm")
    d.text((W // 2, by + bs + 168), "subgrad.vercel.app",
           font=font(F_BOLD, 38), fill=EM400, anchor="mm")
    return c

# --------------------------------------------------------------------- save
def save_gif(frames, path, hold_first=500, base=140, hold_last=1100):
    durs = [base] * len(frames)
    durs[0] = hold_first
    durs[-1] = hold_last
    # Build the shared palette from a montage sampling the WHOLE clip, not
    # frame 0. The end card's emerald only appears in the last frames, and a
    # frame-0 palette (all teal wireframe) remapped it to cyan.
    picks = [frames[0], frames[len(frames) // 2], frames[-1]]
    tw = sum(p.width for p in picks) // 4
    th = max(p.height for p in picks) // 4
    # Swatch band underneath: MEDIANCUT allocates entries by area, so the
    # brand colours need real estate or emerald gets folded into the nearest
    # teal from the 3D surface and the end card comes out washed out.
    band = th // 2
    mont = Image.new("RGB", (tw, th + band), BG)
    ox = 0
    for p in picks:
        s = p.resize((p.width // 4, p.height // 4), Image.LANCZOS)
        mont.paste(s, (ox, 0))
        ox += s.width
    brand = [EM400, EM500, FG, MUTED, BORDER, PANEL, BG]
    sw = tw // len(brand)
    for j, col in enumerate(brand):
        mont.paste(Image.new("RGB", (sw, band), col), (j * sw, th))
    pal = mont.quantize(colors=200, method=Image.MEDIANCUT)
    # dither=NONE keeps mono text crisp; with a palette this wide the 3D
    # surface still reads fine and it compresses far better than dithering.
    q = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
    q[0].save(path, save_all=True, append_images=q[1:],
              duration=durs, loop=0, optimize=True, disposal=2)
    print("  %-34s %3df  %4.1fs  %5dKB" % (
        os.path.basename(path), len(frames), sum(durs) / 1000,
        os.path.getsize(path) // 1024))


print("building clips...")
c1, c2 = load(CLIP1), load(CLIP2)

CAP1 = (["Saddle point - same start, default settings"] * 2
        + ["x collapses toward 0 ..."] * 3
        + ["... but y grows every single step"] * 5)
CAP2 = (["Explode mode: gradients scaled 1e5"] * 2
        + ["one step - loss clears 1,000"] * 2
        + ["the tutor interrupts, unprompted"] * 4
        + ["weights run away into scientific notation"] * 6)

save_gif(captioned_16x9(c1, CAP1), os.path.join(OUT, "subgrad-surface-lab-16x9.gif"))
save_gif(captioned_16x9(c2, CAP2), os.path.join(OUT, "subgrad-graph-lab-16x9.gif"))
save_gif(vertical_9x16(c2, ["Set the gradients", "to explode.", "Watch who notices."], CAP2),
         os.path.join(OUT, "subgrad-graph-lab-9x16.gif"))

sizzle = captioned_16x9(c1, CAP1) + captioned_16x9(c2, CAP2)
sizzle += [end_card(sizzle[0].width, sizzle[0].height)] * 2
save_gif(sizzle, os.path.join(OUT, "subgrad-sizzle-16x9.gif"), base=130, hold_last=1600)

print("done ->", OUT)
