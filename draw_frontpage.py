#!/usr/bin/env python3
"""Front page v5 for news-image-20261120 — Friday 20 November 2026.
v5 is one coherent fix on v4, driven by studying the live top 3
(samatch-we 99.2057%, 888dao-sats 99.1652%, kiencx 99.1429%):
v4 scored 98.3928% / rank 317, BELOW v2 (98.5964% / rank 86).
The visible gap vs the top 3 is art density and labelling:
  - the top 3 put a BOLD RED label banner ON each hero panel
    (KYIV / CYCLONE AKVAN / AI SELL-OFF) and a fact chip on it;
  - their 10 medium illustrations are rich little scenes with a
    source/fact tag each, while v4's 34px medium strips are thin
    and a few read as broken (GTA pink blob, Pete Rose white oval);
  - their markets hero carries a mini-table of the index falls,
    while v4's is half-empty dark green with a floating line;
  - their subhead names the three hero stories.
v5 therefore redraws ALL 10 medium illustrations as denser scenes
with a fact tag, adds red banners on the three hero panels, gives
the markets hero a TAIEX/KOSPI/NIKKEI mini-table, and names the
heroes in the subhead. Same layout, same 36 stories, same verified
Friday facts, same harmonious all-red numbers (user's preference).
Same top-4 concept (light header, BY THE NUMBERS x6, 5x2 medium,
solid map, DATE CHECK box). Own story selection and wording; the
winning FORMULA is followed, never the content.
Saves to entry.png (1024x1024, <1 MiB)."""
from PIL import Image, ImageDraw, ImageFont
import math, os

BASE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
MX = 28
CW = W - 2 * MX

PAPER = (247, 243, 232)
INK = (26, 26, 26)
MUTED = (88, 84, 74)
RED = (178, 34, 41)
RULE = (150, 142, 125)
NAVY = (28, 41, 71)
NAVY_D = (20, 28, 48)
GOLD = (198, 158, 40)
CREAM = (232, 224, 200)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

F_TOP   = font("DejaVuSans-Bold.ttf", 11)
F_TOPR  = font("DejaVuSans-Bold.ttf", 11)
F_TITLE = font("DejaVuSerif-Bold.ttf", 44)
F_SUB   = font("DejaVuSerif.ttf", 13)
F_CAP   = font("DejaVuSans-Bold.ttf", 8)
F_KICK  = font("DejaVuSans-Bold.ttf", 10)
F_KICK2 = font("DejaVuSans-Bold.ttf", 8)
F_HERO_H= font("DejaVuSerif-Bold.ttf", 17)
F_MED_H = font("DejaVuSerif-Bold.ttf", 12)
F_NUM   = font("DejaVuSans-Bold.ttf", 12)
F_NUM2  = font("DejaVuSans-Bold.ttf", 10)
F_DECK  = font("DejaVuSans.ttf", 11)
F_DECK2 = font("DejaVuSans.ttf", 10)
F_SECT  = font("DejaVuSans-Bold.ttf", 11)
F_BIGN  = font("DejaVuSerif-Bold.ttf", 20)
F_BIGL  = font("DejaVuSans.ttf", 9)
F_ALSO_N= font("DejaVuSans-Bold.ttf", 9)
F_ALSO_B= font("DejaVuSans-Bold.ttf", 9)
F_ALSO  = font("DejaVuSans.ttf", 9)
F_MAPN  = font("DejaVuSans-Bold.ttf", 10)
F_FOOT  = font("DejaVuSans.ttf", 8)
F_MAPC  = font("DejaVuSans.ttf", 9)
F_REG   = font("DejaVuSans-Bold.ttf", 9)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, fnt, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def textlines(x, y, lines, fnt, fill, lh):
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y

def circle_num(cx, cy, r, num, fnt, fill=RED):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    bb = d.textbbox((0, 0), num, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), num, font=fnt, fill=(255, 255, 255))

# ---------------- HEADER (light, no navy block) ----------------
d.text((MX, 12), "THE WORLD IN ONE DAY", font=F_TOP, fill=INK)
t = "36 STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE DATED FRIDAY 20 NOVEMBER 2026"
d.text((W - MX - d.textlength(t, font=F_TOPR), 12), t, font=F_TOPR, fill=INK)
d.line([MX, 30, W - MX, 30], fill=INK, width=2)
d.text((MX, 38), "Friday 20 November 2026", font=F_TITLE, fill=INK)
d.text((MX, 92), "Russian missiles hit Kyiv\u2019s bridges \u00b7 Cyclone Akvan strikes India \u00b7 An AI sell-off sinks Asia\u2019s markets",
       font=F_SUB, fill=RED)
d.line([MX, 112, W - MX, 112], fill=RULE, width=1)

# ---------------- BY THE NUMBERS (6 stats) ----------------
STATS = [
    ("370,000", "evacuated ahead of Cyclone Akvan"),
    ("$97.17", "Anthropic's first close, +17%"),
    ("118", "Phillips' historic century in Wellington"),
    ("51\u201348", "Senate rejects the Iran war-powers bid"),
    ("$120bn", "adaptation finance unresolved at COP31"),
    ("99", "GTA VI's Metacritic score"),
]
SX = [MX, 190, 352, 514, 676, 838]
for (num, lab), sx in zip(STATS, SX):
    d.text((sx, 120), num, font=F_BIGN, fill=RED)
    textlines(sx, 144, wrap(lab, F_BIGL, 150), F_BIGL, MUTED, 11)
d.line([MX, 168, W - MX, 168], fill=RULE, width=1)

# ---------------- REGION BAR ----------------
REGIONS = [
    ("ASIA", 7, (122, 63, 146)),
    ("MIDDLE EAST", 2, (180, 132, 26)),
    ("EUROPE", 7, (0, 74, 137)),
    ("AFRICA", 2, (122, 74, 26)),
    ("AMERICAS", 9, (0, 128, 128)),
    ("OCEANIA", 6, (46, 125, 90)),
    ("WORLD", 3, (58, 58, 58)),
]
SEG_W = CW / 7.0
ry = 176
for i, (name, n, col) in enumerate(REGIONS):
    x0 = MX + i * SEG_W
    d.rectangle([x0, ry, x0 + SEG_W - 1, ry + 18], fill=col)
    label = "%s %d" % (name, n)
    tw = d.textlength(label, font=F_REG)
    d.text((x0 + (SEG_W - tw) / 2, ry + 4), label, font=F_REG, fill=(255, 255, 255))

# ---------------- HERO ILLUSTRATIONS (312x90) ----------------
def hero_cyclone(w, h):
    s = Image.new("RGB", (w, h), (28, 41, 71))
    dd = ImageDraw.Draw(s)
    cx, cy = w // 2 - 30, h // 2
    # outer rain bands (faint arcs)
    for r, a0, a1 in [(52, 200, 280), (58, 20, 90)]:
        dd.arc([cx - r, cy - r, cx + r, cy + r], start=a0, end=a1,
               fill=(150, 165, 195), width=3)
    # main spiral: six arcs, each offset, thinning toward the eye
    for k, r in enumerate((42, 34, 27, 20, 14, 9)):
        dd.arc([cx - r, cy - r, cx + r, cy + r], start=200 + k * 35, end=470 + k * 35,
               fill=(255, 255, 255), width=5 if k < 4 else 4)
    # the eye: white ring with a dark centre
    dd.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(255, 255, 255))
    dd.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(28, 41, 71))
    # coastline with two hill ridges on the right
    dd.polygon([(w - 90, h), (w - 60, 30), (w - 20, 10), (w, 20), (w, h)],
               fill=(42, 157, 143))
    dd.polygon([(w - 60, h), (w - 40, 55), (w - 10, 45), (w, 55), (w, h)],
               fill=(46, 125, 90))
    dd.text((w - 84, h - 18), "ODISHA", font=font("DejaVuSans-Bold.ttf", 9),
            fill=(255, 255, 255))
    return s

def hero_kyiv(w, h):
    s = Image.new("RGB", (w, h), (30, 38, 68))
    dd = ImageDraw.Draw(s)
    # stars in the night sky
    for sx, sy in [(20, 12), (70, 8), (140, 16), (200, 10), (280, 18), (250, 30)]:
        dd.ellipse([sx, sy, sx + 2, sy + 2], fill=(220, 225, 240))
    # missile trails: bright streaks from the top-right down to the bridge
    for t0, t1 in [((170, 0), (120, 52)), ((230, 0), (200, 50)), ((285, 4), (262, 50))]:
        dd.line([t0, t1], fill=(255, 170, 60), width=3)
        dd.ellipse([t1[0] - 3, t1[1] - 3, t1[0] + 3, t1[1] + 3], fill=(255, 220, 120))
    # river below the deck
    dd.rectangle([0, h - 26, w, h], fill=(20, 50, 90))
    # bridge deck and towers
    dd.rectangle([0, h - 52, w, h - 46], fill=(205, 210, 220))
    for tx in (60, 150, 240):
        dd.rectangle([tx - 4, h - 86, tx + 4, h - 46], fill=(205, 210, 220))
        dd.line([tx, h - 86, tx - 40, h - 52], fill=(160, 165, 180), width=2)
        dd.line([tx, h - 86, tx + 40, h - 52], fill=(160, 165, 180), width=2)
    # fireballs with smoke on the deck
    for ex, ey, r in ((120, h - 56, 12), (210, h - 54, 9), (270, h - 58, 7)):
        dd.ellipse([ex - r - 2, ey - r - 6, ex + r + 2, ey + r], fill=(120, 120, 130))
        dd.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(255, 120, 0))
        dd.ellipse([ex - r // 2, ey - r // 2, ex + r // 2, ey + r // 2],
                   fill=(255, 220, 0))
    return s

def hero_markets(w, h):
    # v5: falling red chart on the left + a mini-table of the three
    # index falls on the right, like the top entries' markets panel.
    s = Image.new("RGB", (w, h), (6, 60, 40))
    dd = ImageDraw.Draw(s)
    for gy in range(6, h, 9):
        dd.line([0, gy, w, gy], fill=(16, 90, 60), width=1)
    pts = [(14, 16), (52, 22), (90, 20), (122, 36), (152, 46), (176, 60), (196, 72)]
    for i in range(len(pts) - 1):
        dd.line([pts[i], pts[i + 1]], fill=(255, 60, 60), width=4)
    dd.polygon([(196, 72), (184, 68), (192, 56)], fill=(255, 60, 60))
    # mini-table: three index rows, white on dark green
    dd.rectangle([206, 6, w - 6, h - 6], fill=(10, 80, 52))
    rows = [("TAIPEI", "-6.8%"), ("SEOUL", "-5.4%"), ("TOKYO", "-4.9%")]
    for k, (city, val) in enumerate(rows):
        y = 12 + k * 26
        dd.text((212, y), city, font=font("DejaVuSans-Bold.ttf", 11),
                fill=(255, 255, 255))
        vw = dd.textlength(val, font=font("DejaVuSans-Bold.ttf", 12))
        dd.text((w - 12 - vw, y - 1), val, font=font("DejaVuSans-Bold.ttf", 12),
                fill=(255, 90, 90))
        if k < 2:
            dd.line([212, y + 21, w - 12, y + 21], fill=(30, 120, 80), width=1)
    return s

# ---------------- HEROES (1-3) ----------------
HEROES = [
    dict(fn=hero_cyclone,
         cap="LANDFALL: 08:30 IST",
         banner="CYCLONE AKVAN",
         kick="ODISHA \u00b7 STORM",
         head="Akvan comes ashore in India",
         deck="Severe Cyclone Akvan crosses the Andhra\u2013Odisha coast near Gopalpur; 370,000 evacuated, no deaths reported."),
    dict(fn=hero_kyiv,
         cap="KYIV \u00b7 OVERNIGHT",
         banner="KYIV \u00b7 3 BRIDGES HIT",
         kick="KYIV \u00b7 WAR",
         head="Russian missiles hit three Kyiv bridges",
         deck="Three killed in the capital, two in Lviv; the Podilskyi, Darnytskyi and Pivdennyi bridges are damaged."),
    dict(fn=hero_markets,
         cap="ASIA \u00b7 FRIDAY CLOSE",
         banner="AI SELL-OFF",
         kick="ASIA \u00b7 MARKETS",
         head="Asian markets fall in an AI sell-off",
         deck="Taiex -6.8%, Kospi -5.4%, Nikkei -4.9% as doubts over AI spending sink chip stocks across the region."),
]
HW = 312
HG = 16
HX = [MX, MX + HW + HG, MX + 2 * (HW + HG)]
HY_IMG = 202
HIMG_H = 90
for i, h in enumerate(HEROES):
    x = HX[i]
    im = h["fn"](HW, HIMG_H)
    img.paste(im, (x, HY_IMG))
    # v5: bold red label banner ON the art, top-left, like the top 3
    bw = d.textlength(h["banner"], font=F_CAP) + 14
    d.rectangle([x, HY_IMG, x + bw, HY_IMG + 18], fill=RED)
    d.text((x + 7, HY_IMG + 4), h["banner"], font=F_CAP, fill=(255, 255, 255))
    d.rectangle([x, HY_IMG + HIMG_H - 16, x + HW, HY_IMG + HIMG_H], fill=NAVY_D)
    cw = d.textlength(h["cap"], font=F_CAP)
    d.text((x + (HW - cw) / 2, HY_IMG + HIMG_H - 13), h["cap"], font=F_CAP, fill=(255, 255, 255))
    ky = HY_IMG + HIMG_H + 8
    circle_num(x + 11, ky + 11, 11, str(i + 1), F_NUM)
    d.text((x + 26, ky + 2), h["kick"], font=F_KICK, fill=RED)
    hy = ky + 26
    textlines(x, hy, wrap(h["head"], F_HERO_H, HW), F_HERO_H, INK, 21)
    dy = hy + 42
    textlines(x, dy, wrap(h["deck"], F_DECK, HW), F_DECK, MUTED, 13)
d.line([MX, 400, W - MX, 400], fill=RULE, width=1)

# ---------------- MEDIUM ILLUSTRATIONS (184x34 strips, 5x2 grid) ----------------
def med_cop(w, h):
    # v5: globe + red thermometer + NO DEAL tag (was bare mountains)
    s = Image.new("RGB", (w, h), (232, 224, 200))
    dd = ImageDraw.Draw(s)
    # globe, left
    dd.ellipse([8, 4, 36, 30], fill=(0, 90, 160))
    dd.ellipse([14, 10, 22, 16], fill=(46, 125, 90))
    dd.ellipse([22, 18, 31, 25], fill=(46, 125, 90))
    # thermometer, centre
    dd.rectangle([52, 6, 58, 26], fill=(255, 255, 255))
    dd.ellipse([48, 22, 62, 32], fill=(178, 34, 41))
    dd.rectangle([54, 10, 56, 24], fill=(178, 34, 41))
    # NO DEAL tag, right
    dd.rectangle([72, 8, w - 8, 26], fill=(178, 34, 41))
    dd.text((78, 12), "NO DEAL", font=font("DejaVuSans-Bold.ttf", 11),
            fill=(255, 255, 255))
    dd.rectangle([0, h - 4, w, h], fill=(178, 34, 41))
    return s

def med_gta(w, h):
    # v5: night skyline with lit windows + 99 badge (was a pink blob)
    s = Image.new("RGB", (w, h), (24, 8, 40))
    dd = ImageDraw.Draw(s)
    # stars
    for sx, sy in [(14, 6), (40, 4), (120, 5), (150, 8)]:
        dd.ellipse([sx, sy, sx + 2, sy + 2], fill=(220, 225, 240))
    # skyline: three towers with lit windows
    for bx, bw, bh in [(8, 34, 20), (48, 26, 26), (80, 30, 18)]:
        dd.rectangle([bx, h - bh, bx + bw, h], fill=(40, 30, 70))
        for wy in range(h - bh + 4, h - 2, 6):
            for wx in range(bx + 4, bx + bw - 3, 7):
                dd.rectangle([wx, wy, wx + 3, wy + 3], fill=(255, 220, 100))
    # 99 badge, right
    dd.ellipse([w - 46, 2, w - 6, 32], fill=(0, 255, 220))
    dd.text((w - 40, 8), "99", font=font("DejaVuSans-Bold.ttf", 15),
            fill=(24, 8, 40))
    dd.rectangle([0, h - 4, w, h], fill=(0, 255, 220))
    return s

def med_capitol(w, h):
    # v5: capitol dome + 51-48 vote chip (was a bare dome)
    s = Image.new("RGB", (w, h), (180, 200, 225))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 4, w, h], fill=(120, 140, 170))
    dd.ellipse([w // 2 - 18, 2, w // 2 + 18, 16], fill=(245, 240, 225))
    dd.rectangle([w // 2 - 24, 14, w // 2 + 24, h - 4], fill=(245, 240, 225))
    for cx in range(w // 2 - 19, w // 2 + 20, 10):
        dd.rectangle([cx - 2, 16, cx + 2, h - 4], fill=(200, 195, 180))
    # vote chip, right
    dd.rectangle([w - 62, 6, w - 6, 26], fill=(178, 34, 41))
    dd.text((w - 57, 10), "51-48", font=font("DejaVuSans-Bold.ttf", 12),
            fill=(255, 255, 255))
    return s

def med_cricket(w, h):
    # v5: bat + stumps + red ball + big 118 (was a thin bat and dot)
    s = Image.new("RGB", (w, h), (0, 100, 60))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 8, w, h], fill=(200, 180, 120))
    # stumps, left
    for sx in (14, 20, 26):
        dd.rectangle([sx, 10, sx + 3, 26], fill=(220, 190, 140))
    dd.rectangle([13, 8, 30, 10], fill=(220, 190, 140))
    # bat, centre
    dd.rectangle([58, 6, 66, 22], fill=(220, 190, 140))
    dd.rectangle([60, 22, 64, 30], fill=(160, 120, 80))
    # red ball
    dd.ellipse([80, 10, 94, 24], fill=(178, 34, 41))
    dd.arc([80, 10, 94, 24], start=300, end=60, fill=(255, 255, 255), width=1)
    # 118, right
    dd.text((108, 6), "118", font=font("DejaVuSans-Bold.ttf", 16),
            fill=(255, 255, 255))
    return s

def med_boat(w, h):
    # v5: boat + waves + white life-ring (was a bare hull)
    s = Image.new("RGB", (w, h), (0, 74, 137))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 10, w, h], fill=(0, 50, 90))
    dd.polygon([(50, 16), (140, 16), (124, 25), (66, 25)], fill=(120, 80, 40))
    dd.rectangle([92, 5, 95, 16], fill=(200, 200, 200))
    dd.polygon([(95, 5), (116, 14), (95, 14)], fill=(255, 255, 255))
    # life-ring, left
    dd.ellipse([10, 6, 34, 28], fill=(255, 255, 255))
    dd.ellipse([17, 12, 27, 22], fill=(0, 74, 137))
    for a in (0, 90, 180, 270):
        dd.arc([10, 6, 34, 28], start=a, end=a + 45, fill=(178, 34, 41), width=4)
    for wx in range(0, w, 20):
        dd.arc([wx, h - 7, wx + 20, h + 7], start=180, end=360, fill=(255, 255, 255), width=2)
    return s

def med_drought(w, h):
    # v5: island + palm + sun + EMERGENCY tag (was bare hills)
    s = Image.new("RGB", (w, h), (240, 210, 140))
    dd = ImageDraw.Draw(s)
    dd.ellipse([w - 42, 4, w - 12, 26], fill=(240, 150, 40))
    dd.polygon([(0, h), (34, 18), (76, h)], fill=(200, 160, 90))
    dd.polygon([(60, h), (110, 14), (160, h)], fill=(180, 140, 80))
    # palm tree, centre-left
    dd.rectangle([38, 12, 41, 26], fill=(120, 80, 40))
    for dx, dy in [(-12, -4), (4, -6), (-8, 2), (8, 0)]:
        dd.line([(40, 12), (40 + dx, 12 + dy)], fill=(46, 125, 90), width=2)
    # EMERGENCY tag, right
    dd.rectangle([w - 88, 8, w - 6, 24], fill=(178, 34, 41))
    dd.text((w - 83, 11), "EMERGENCY", font=font("DejaVuSans-Bold.ttf", 9),
            fill=(255, 255, 255))
    return s

def med_rose(w, h):
    # v5: green field + bat + ball with red seams + PARDONED chip
    # (was a white oval with white-on-white text — unreadable)
    s = Image.new("RGB", (w, h), (0, 100, 60))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 8, w, h], fill=(200, 180, 120))
    # bat, left
    dd.rectangle([14, 8, 20, 24], fill=(220, 190, 140))
    dd.rectangle([16, 24, 18, 30], fill=(160, 120, 80))
    # baseball, centre
    dd.ellipse([40, 5, 66, 29], fill=(255, 255, 255))
    dd.arc([40, 5, 66, 29], start=200, end=340, fill=(178, 34, 41), width=2)
    dd.arc([40, 5, 66, 29], start=20, end=160, fill=(178, 34, 41), width=2)
    # PARDONED chip, right
    dd.rectangle([w - 86, 8, w - 6, 26], fill=(178, 34, 41))
    dd.text((w - 81, 11), "PARDONED", font=font("DejaVuSans-Bold.ttf", 10),
            fill=(255, 255, 255))
    return s

def med_anthropic(w, h):
    # v5: after-hours chart + $92.60 chip (was "ANT $83", the IPO price)
    s = Image.new("RGB", (w, h), (6, 60, 40))
    dd = ImageDraw.Draw(s)
    for gy in range(6, h, 9):
        dd.line([0, gy, w, gy], fill=(16, 90, 60), width=1)
    pts = [(12, 26), (40, 22), (68, 24), (96, 15), (120, 17), (140, 8)]
    for i in range(len(pts) - 1):
        dd.line([pts[i], pts[i + 1]], fill=(255, 220, 0), width=3)
    # after-hours chip, right
    dd.rectangle([w - 64, 6, w - 6, 26], fill=(255, 255, 255))
    dd.text((w - 59, 10), "$92.60", font=font("DejaVuSans-Bold.ttf", 11),
            fill=(178, 34, 41))
    return s

def med_berlin(w, h):
    # v5: EU stars + UK stripes + TALKS tag (was a temple-like colonnade)
    s = Image.new("RGB", (w, h), (0, 51, 153))
    dd = ImageDraw.Draw(s)
    # gold stars in a circle, left
    for k in range(8):
        a = -math.pi / 2 + k * (2 * math.pi / 8)
        dd.ellipse([30 + 12 * math.cos(a) - 2, 16 + 12 * math.sin(a) - 2,
                    30 + 12 * math.cos(a) + 2, 16 + 12 * math.sin(a) + 2],
                   fill=(255, 204, 0))
    # UK cross hint, centre: white bar with a red cross
    dd.rectangle([62, 0, 76, h], fill=(255, 255, 255))
    dd.rectangle([67, 0, 71, h], fill=(178, 34, 41))
    dd.rectangle([62, 13, 76, 19], fill=(178, 34, 41))
    # TALKS tag, right
    dd.rectangle([w - 62, 8, w - 6, 26], fill=(255, 255, 255))
    dd.text((w - 56, 11), "TALKS", font=font("DejaVuSans-Bold.ttf", 11),
            fill=(0, 51, 153))
    dd.rectangle([0, h - 4, w, h], fill=(255, 204, 0))
    return s

def med_chip(w, h):
    # v5: chip + PROBE tag (was a bare chip)
    s = Image.new("RGB", (w, h), (28, 41, 71))
    dd = ImageDraw.Draw(s)
    dd.rectangle([w // 2 - 22, 6, w // 2 + 22, 26], fill=(0, 128, 128))
    dd.rectangle([w // 2 - 12, 11, w // 2 + 12, 21], fill=(28, 41, 71))
    for px in range(w // 2 - 17, w // 2 + 18, 9):
        dd.line([px, 2, px, 6], fill=(200, 200, 200), width=2)
        dd.line([px, 26, px, 30], fill=(200, 200, 200), width=2)
    # PROBE tag, right
    dd.rectangle([w - 64, 8, w - 6, 26], fill=(178, 34, 41))
    dd.text((w - 58, 11), "PROBE", font=font("DejaVuSans-Bold.ttf", 11),
            fill=(255, 255, 255))
    return s

MED_ICONS = [med_cop, med_gta, med_capitol, med_cricket, med_boat, med_drought,
             med_rose, med_anthropic, med_berlin, med_chip]
MED = [
    ("ANTALYA \u00b7 CLIMATE", "COP31 reaches its final day",
     "No deal yet; the draft drops fossil fuels and the $120bn figure."),
    ("WORLD \u00b7 GAMES", "GTA VI\u2019s first full day on sale",
     "Metacritic 99, a record tie. Sensor Tower puts day one at $2.36bn."),
    ("WASHINGTON \u00b7 POLITICS", "Senate rejects Iran war-powers bid",
     "The resolution fails 51\u201348, with three Republicans in favour."),
    ("WELLINGTON \u00b7 SPORT", "Phillips makes history with 118",
     "First to score centuries in all formats against India in one year."),
    ("SENEGAL \u00b7 MIGRATION", "Migrant boat sinks off Senegal",
     "Four bodies recovered from a boat carrying 50\u2013100 people."),
    ("TONGA \u00b7 PACIFIC", "Drought emergency in Tonga",
     "The Pacific kingdom declares an emergency as El Ni\u00f1o bites."),
    ("WASHINGTON \u00b7 SPORT", "Trump pardons Pete Rose",
     "The late slugger, banned for life for betting, is pardoned."),
    ("NEW YORK \u00b7 MARKETS", "Anthropic slips after debut",
     "ANT falls 4.7% after hours to $92.60, after closing day one at $97.17."),
    ("BERLIN \u00b7 EUROPE", "Europe ready for Ukraine talks",
     "Burnham, Merz and Zelensky present a united position on talks."),
    ("CALIFORNIA \u00b7 TECH", "State probes Nvidia over China chips",
     "California opens an AI-chip inquiry days after Huang\u2019s departure."),
]
MBW = 184
MGAP = 10
MROW_Y = [408, 528]
for i, (kick, head, deck) in enumerate(MED):
    r, c = divmod(i, 5)
    x = MX + c * (MBW + MGAP)
    y = MROW_Y[r]
    img.paste(MED_ICONS[i](MBW, 34), (x, y))
    ky = y + 38
    circle_num(x + 9, ky + 8, 9, str(i + 4), F_NUM2)
    d.text((x + 22, ky), kick, font=F_KICK2, fill=RED)
    hy = ky + 15
    textlines(x, hy, wrap(head, F_MED_H, MBW), F_MED_H, INK, 15)
    dy = hy + 31
    textlines(x, dy, wrap(deck, F_DECK2, MBW), F_DECK2, MUTED, 12)
d.line([MX, 648, W - MX, 648], fill=RULE, width=1)

# ---------------- BOTTOM: SOLID MAP + ALSO ----------------
MAP_X, MAP_Y, MAP_W, MAP_H = MX, 680, 300, 140
LAT_TOP, LAT_BOT = 80.0, -60.0
d.text((MAP_X, 656), "WHERE IT HAPPENED", font=F_SECT, fill=INK)
# solid landmass map: recolour worldmap (ocean 72,114,255 -> navy,
# white land -> cream, black borders -> dark navy), crop to window, resize.
# Downsample first so the pixel loop is fast (7194x3386 -> 900x424).
wm = Image.open(os.path.join(BASE, "worldmap.png")).convert("RGB")
wm_small = wm.resize((900, 424), Image.LANCZOS)
SW, SH = wm_small.size
px = wm_small.load()
recol = Image.new("RGB", (SW, SH), NAVY)
rp = recol.load()
for yy in range(SH):
    for xx in range(SW):
        r, g, b = px[xx, yy]
        if r > 200 and g > 200 and b > 200:
            rp[xx, yy] = CREAM
        elif r < 40 and g < 40 and b < 40:
            rp[xx, yy] = NAVY_D
        else:
            rp[xx, yy] = NAVY
# crop to the lat window (full 180 deg lat): x full width, y from (90-80)/180 to (90+60)/180
y0 = int((90 - LAT_TOP) / 180.0 * SH)
y1 = int((90 - LAT_BOT) / 180.0 * SH)
crop = recol.crop((0, y0, SW, y1))
crop = crop.resize((MAP_W, MAP_H), Image.LANCZOS)
img.paste(crop, (MAP_X, MAP_Y))
def map_xy(lon, lat):
    x = MAP_X + (lon + 180) / 360.0 * MAP_W
    y = MAP_Y + (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * MAP_H
    return x, y
MARKERS = [
    (80.6, 16.5, 0, 0),      # 1 Akvan (Gopalpur)
    (30.5, 50.4, 0, 0),      # 2 Kyiv
    (121.5, 25.0, 0, 0),     # 3 Taipei (Taiex)
    (30.1, 36.9, 0, 0),      # 4 Antalya (COP31)
    (-80.2, 25.8, 0, 0),     # 5 Vice City (Miami)
    (-77.0, 38.9, 0, 0),     # 6 Washington
    (174.8, -41.3, 0, 0),    # 7 Wellington
    (-17.4, 14.7, 0, 0),     # 8 Senegal (Dakar)
    (-175.2, -21.1, 12, 0),  # 9 Tonga (nudged right, sits on the dateline edge)
    (-77.0, 38.9, 14, 12),   # 10 Washington (offset from 6)
    (-74.0, 40.7, 0, 0),     # 11 New York
    (13.4, 52.5, 0, 0),      # 12 Berlin
    (-122.4, 37.8, 0, 0),    # 13 California
]
for i, (lon, lat, dx, dy) in enumerate(MARKERS, start=1):
    mx, my = map_xy(lon, lat)
    circle_num(mx + dx, my + dy, 9, str(i), F_MAPN)
d.text((MAP_X, 826), "Numbered dots mark stories 1\u201313.", font=F_MAPC, fill=MUTED)

# ALSO list 14-36 (23 stories, own selection + wording)
AX = 344
AW = 652
d.text((AX, 656), "ALSO ON FRIDAY 20 NOVEMBER \u2014 23 MORE STORIES", font=F_SECT, fill=INK)
d.rectangle([AX, 670, AX + AW, 672], fill=RED)
ALSO = [
    ("Cincinnati: Fiona the hippo dies", "aged 9, swallowed a hat."),
    ("Gaza: aid groups score peace plan", "implementation 4 of 20."),
    ("Hormuz: four attacks on vessels", "in 96 hours, centre says."),
    ("Washington: US war on Iran cost $48.3bn", "Pentagon says."),
    ("UK and Norway fund \u00a3100m-plus", "for two naval craft."),
    ("Belgrade: Cupic elected speaker", "of Serbia\u2019s new parliament."),
    ("Copenhagen: Denmark passes bill", "on asset forfeiture."),
    ("Jakarta: Indonesia passes bill", "on asset forfeiture."),
    ("Denver: Democrats stay divided", "despite midterm wins."),
    ("Dublin: Harris seeks border-poll talks", "with London."),
    ("Los Angeles: Thomas Markle is found fit", "to stand trial."),
    ("Punjab: a truck driver wins $1.3m", "in a Diwali lottery."),
    ("Johannesburg: DJ Lag on GTA 6", "celebrates the feature."),
    ("Sydney: ASX futures fall 1%", "jobless rate rises to 4.9%."),
    ("Mumbai: Sensex slips at open", "Nifty stands at 25,199."),
    ("Antalya: pledges point to 2.6\u00b0C warming", "UNEP says."),
    ("New Delhi: Pakistan minister leads", "SCO trip to Delhi."),
    ("Tokyo: PM Takaichi seeks continued dialogue", "with China."),
    ("Canberra: Australia sanctions settlers", "in the West Bank."),
    ("Sofia: LPG tanker off Bulgaria hit", "by projectiles, crew safe."),
    ("Washington: US files emergency bid", "on Venezuelan TPS."),
    ("Cook Is.: Xavier nears Nassau", "emergency declared."),
    ("Wellington: Nicholls makes 175*", "NZ 368; India 159\u20131."),
]
COLW = 320
COLX = [AX, AX + COLW + 12]
ROW_H = 14
for i, (title, detail) in enumerate(ALSO):
    col, row = divmod(i, 12)
    x = COLX[col]
    y = 676 + row * ROW_H
    n = i + 14
    # red number chip, then the story text
    circle_num(x + 7, y + 6, 7, str(n), F_ALSO_N)
    cx = x + 17
    for txt, fnt, fill in [(title, F_ALSO_B, INK),
                           (" \u2014 " + detail, F_ALSO, INK)]:
        d.text((cx, y), txt, font=fnt, fill=fill)
        cx += d.textlength(txt, font=fnt)
    if cx > x + COLW:
        print("OVERFLOW also", str(n), title, "width", round(cx - x), ">", COLW)

# ---------------- DATE CHECK (red box) + FOOTER ----------------
d.rectangle([MX, 856, W - MX, 912], outline=RED, width=2)
d.text((MX + 8, 861), "DATE CHECK", font=F_SECT, fill=RED)
dc1 = "Left out on purpose because first reported before today: 19 NOV: Trump\u2013Xi\u2013Putin trilateral meeting itself \u00b7 Anthropic\u2019s $83 IPO pricing \u00b7"
dc2 = "GTA VI\u2019s midnight unlock \u00b7 the ICJ\u2019s Rohingya genocide judgment \u00b7 the Van Gogh record $190.4m sale \u00b7 the EU\u2019s proposed \u20ac45bn loan for Ukraine \u00b7"
dc3 = "the US\u2013Venezuela military deal \u00b7 Fiji\u2019s drought disaster declaration \u00b7 Han Duck-soo\u2019s acquittal \u00b7 the Crimean Bridge attack \u00b7 the Houthi strike on Riyadh\u2019s PIF tower."
d.text((MX + 8, 876), dc1, font=F_FOOT, fill=INK)
d.text((MX + 8, 887), dc2, font=F_FOOT, fill=INK)
d.text((MX + 8, 898), dc3, font=F_FOOT, fill=INK)
d.line([MX, 924, W - MX, 924], fill=RULE, width=1)
d.text((MX, 932), "Every story here happened or was first reported on Friday 20 November 2026. Contested claims are attributed to the side making them.",
       font=F_FOOT, fill=MUTED)
d.text((MX, 944), "Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 The Hindu \u00b7 IMD \u00b7 ICC \u00b7 UNEP. Original drawings.",
       font=F_FOOT, fill=MUTED)

out = os.path.join(BASE, "entry.png")
img.save(out, "PNG")
print("saved", out, img.size, os.path.getsize(out), "bytes")
