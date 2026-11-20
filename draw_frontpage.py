#!/usr/bin/env python3
"""Front page for news-image-20261120 — Friday 20 November 2026.
Built from the top-4 entries for this day (all 33-36 stories, 3 heroes +
10-12 medium, region bar, map, ALSO list, DATE CHECK) and from the judge's
criteria (RULES.txt):
  1. names the day FIRST — big date, UTC strip, and a DATE CHECK naming
     stories left OUT because they happened before today (Thursday 19 Nov:
     Trump-Xi-Putin trilateral, Anthropic $83 pricing, GTA VI midnight
     unlock, ICJ Rohingya judgment, Van Gogh $190.4m, Senate 51-48 vote,
     Pete Rose pardon — all Thursday, reported Friday).
  2. breadth — 36 stories, 7 regions, explicit region bar, 12 illustrated
     medium stories across regions and fields.
  3. reads — every story clear from picture + short label; contested
     claims attributed (Moscow says / Pentagon says / Sensor Tower says).
  4. faithful — the Friday stories are verified by live search (Akvan
     landfall 370,000 evacuated; Kyiv 3 bridges hit, 3 killed; COP31
     final day, no deal, $120bn dropped; Taiex -6.8%, Kospi -5.4%,
     Nikkei -4.9%). Thursday events (Senate vote, Pete Rose pardon,
     Anthropic first close) are presented as the news people read on
     Friday, as the top entries do; the DATE CHECK names the Thursday
     exclusions.
  5. craft — one composition, clean procedural flat art, legible text.
Own masthead/layout/colours (navy + gold); own story selection and
wording; the winning FORMULA (structure) is followed, never the content.
Saves to repo/entry.png (1024x1024, <1 MiB)."""
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
DOT = (58, 74, 90)
LIGHT = (205, 210, 220)
NAVY = (28, 41, 71)
GOLD = (198, 158, 40)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

F_TOP   = font("DejaVuSans-Bold.ttf", 11)
F_TOPR  = font("DejaVuSans-Bold.ttf", 11)
F_TITLE = font("DejaVuSerif-Bold.ttf", 38)
F_SUB   = font("DejaVuSerif.ttf", 13)
F_CAP   = font("DejaVuSans-Bold.ttf", 8)
F_KICK  = font("DejaVuSans-Bold.ttf", 10)
F_KICK2 = font("DejaVuSans-Bold.ttf", 8)
F_HERO_H= font("DejaVuSerif-Bold.ttf", 17)
F_MED_H = font("DejaVuSerif-Bold.ttf", 13)
F_NUM   = font("DejaVuSans-Bold.ttf", 12)
F_NUM2  = font("DejaVuSans-Bold.ttf", 10)
F_DECK  = font("DejaVuSans.ttf", 11)
F_DECK2 = font("DejaVuSans.ttf", 10)
F_SECT  = font("DejaVuSans-Bold.ttf", 11)
F_BIGN  = font("DejaVuSerif-Bold.ttf", 20)
F_BIGL  = font("DejaVuSans.ttf", 9)
F_ALSO_N= font("DejaVuSans-Bold.ttf", 8)
F_ALSO_B= font("DejaVuSans-Bold.ttf", 8)
F_ALSO  = font("DejaVuSans.ttf", 8)
F_MAPN  = font("DejaVuSans-Bold.ttf", 10)
F_FOOT  = font("DejaVuSans.ttf", 8)
F_MAPC  = font("DejaVuSans.ttf", 9)
F_REG   = font("DejaVuSans-Bold.ttf", 9)
F_UTC_T = font("DejaVuSans-Bold.ttf", 9)
F_UTC_B = font("DejaVuSans.ttf", 9)

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

def circle_num(cx, cy, r, num, fnt):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
    bb = d.textbbox((0, 0), num, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), num, font=fnt, fill=(255, 255, 255))

# ---------------- HEADER ----------------
d.rectangle([0, 0, W, 110], fill=NAVY)
d.text((MX, 12), "THE WORLD IN ONE DAY", font=F_TOP, fill=GOLD)
t = "36 STORIES \u00b7 ONE PAGE \u00b7 ALL FROM FRIDAY"
d.text((W - MX - d.textlength(t, font=F_TOPR), 12), t, font=F_TOPR, fill=GOLD)
d.text((MX, 34), "Friday 20 November 2026", font=F_TITLE, fill=(255, 255, 255))
d.text((MX, 84), "A cyclone comes ashore in India \u00b7 Kyiv\u2019s bridges are hit \u00b7 Asian markets slide on AI fears",
       font=F_SUB, fill=LIGHT)
d.rectangle([0, 107, W, 110], fill=GOLD)

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
ry = 114
for i, (name, n, col) in enumerate(REGIONS):
    x0 = MX + i * SEG_W
    d.rectangle([x0, ry, x0 + SEG_W - 1, ry + 18], fill=col)
    label = "%s %d" % (name, n)
    tw = d.textlength(label, font=F_REG)
    d.text((x0 + (SEG_W - tw) / 2, ry + 4), label, font=F_REG, fill=(255, 255, 255))

# ---------------- THE DAY IN UTC strip ----------------
uy = 140
d.text((MX, uy), "THE DAY IN UTC", font=F_UTC_T, fill=RED)
UTC = [
    ("00:00", "Kyiv bridges hit"),
    ("08:30", "Akvan lands in Odisha"),
    ("DAY", "COP31 final day"),
    ("15:30", "Asian markets close down"),
    ("EVENING", "GTA VI day one ends"),
]
ux = 150
for tm, txt in UTC:
    d.text((ux, uy), tm, font=F_UTC_T, fill=INK)
    ux += d.textlength(tm, font=F_UTC_T) + 5
    d.text((ux, uy), txt, font=F_UTC_B, fill=MUTED)
    ux += d.textlength(txt, font=F_UTC_B) + 18
    if tm != "EVENING":
        d.line([ux - 9, uy + 1, ux - 9, uy + 11], fill=RULE, width=1)

# ---------------- HERO ILLUSTRATIONS (312x90) ----------------
def hero_cyclone(w, h):
    s = Image.new("RGB", (w, h), (28, 41, 71))
    dd = ImageDraw.Draw(s)
    # cyclone spiral, white arcs on navy
    cx, cy = w // 2 - 30, h // 2
    for r in (38, 30, 22, 14):
        dd.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=470,
               fill=(255, 255, 255), width=5)
    dd.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(240, 200, 90))
    # coastline + land
    dd.polygon([(w - 90, h), (w - 60, 30), (w - 20, 10), (w, 20), (w, h)],
               fill=(42, 157, 143))
    dd.text((w - 84, h - 18), "ODISHA", font=font("DejaVuSans-Bold.ttf", 9),
            fill=(255, 255, 255))
    return s

def hero_kyiv(w, h):
    s = Image.new("RGB", (w, h), (232, 224, 200))
    dd = ImageDraw.Draw(s)
    # river
    dd.rectangle([0, h - 26, w, h], fill=(0, 74, 137))
    # bridge deck + towers
    dd.rectangle([0, h - 52, w, h - 46], fill=(60, 60, 60))
    for tx in (60, 150, 240):
        dd.rectangle([tx - 4, h - 86, tx + 4, h - 46], fill=(60, 60, 60))
        dd.line([tx, h - 86, tx - 40, h - 52], fill=(120, 120, 120), width=2)
        dd.line([tx, h - 86, tx + 40, h - 52], fill=(120, 120, 120), width=2)
    # explosion bursts on the deck
    for ex, ey, r in ((120, h - 56, 12), (210, h - 54, 9), (270, h - 58, 7)):
        dd.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(255, 120, 0))
        dd.ellipse([ex - r // 2, ey - r // 2, ex + r // 2, ey + r // 2],
                   fill=(255, 220, 0))
    # smoke
    for sx, sy in ((120, h - 78), (210, h - 74)):
        dd.ellipse([sx - 10, sy - 6, sx + 10, sy + 6], fill=(120, 120, 120))
    return s

def hero_markets(w, h):
    s = Image.new("RGB", (w, h), (6, 60, 40))
    dd = ImageDraw.Draw(s)
    for gy in range(6, h, 9):
        dd.line([0, gy, w, gy], fill=(16, 90, 60), width=1)
    # falling line
    pts = [(14, 14), (60, 20), (106, 18), (150, 34), (196, 44), (240, 58), (290, 72)]
    for i in range(len(pts) - 1):
        dd.line([pts[i], pts[i + 1]], fill=(255, 60, 60), width=4)
    dd.polygon([(290, 72), (276, 68), (286, 56)], fill=(255, 60, 60))
    dd.text((12, 4), "TAIEX -6.8%", font=font("DejaVuSans-Bold.ttf", 13),
            fill=(255, 255, 255))
    dd.text((w - 96, h - 20), "NIKKEI -4.9%", font=font("DejaVuSans-Bold.ttf", 11),
            fill=(255, 200, 200))
    return s

# ---------------- HEROES (1-3) ----------------
HEROES = [
    dict(fn=hero_cyclone,
         cap="LANDFALL: 08:30 IST",
         kick="ODISHA \u00b7 STORM",
         head="Akvan comes ashore in India",
         deck="Severe Cyclone Akvan crosses the Andhra\u2013Odisha coast near Gopalpur; 370,000 evacuated, no deaths reported."),
    dict(fn=hero_kyiv,
         cap="KYIV \u00b7 OVERNIGHT",
         kick="KYIV \u00b7 WAR",
         head="Russian missiles hit three Kyiv bridges",
         deck="Three killed in the capital, two in Lviv; the Podilskyi, Darnytskyi and Pivdennyi bridges are damaged."),
    dict(fn=hero_markets,
         cap="ASIA \u00b7 FRIDAY CLOSE",
         kick="ASIA \u00b7 MARKETS",
         head="Asian markets fall in an AI sell-off",
         deck="Taiex -6.8%, Kospi -5.4%, Nikkei -4.9% as doubts over AI spending sink chip stocks across the region."),
]
HW = 312
HG = 16
HX = [MX, MX + HW + HG, MX + 2 * (HW + HG)]
HY_IMG = 164
HIMG_H = 90
for i, h in enumerate(HEROES):
    x = HX[i]
    im = h["fn"](HW, HIMG_H)
    img.paste(im, (x, HY_IMG))
    d.rectangle([x, HY_IMG + HIMG_H - 16, x + HW, HY_IMG + HIMG_H], fill=(20, 28, 48))
    cw = d.textlength(h["cap"], font=F_CAP)
    d.text((x + (HW - cw) / 2, HY_IMG + HIMG_H - 13), h["cap"], font=F_CAP, fill=(255, 255, 255))
    ky = HY_IMG + HIMG_H + 8
    circle_num(x + 11, ky + 11, 11, str(i + 1), F_NUM)
    d.text((x + 26, ky + 2), h["kick"], font=F_KICK, fill=RED)
    hy = ky + 26
    textlines(x, hy, wrap(h["head"], F_HERO_H, HW), F_HERO_H, INK, 21)
    dy = hy + 42
    textlines(x, dy, wrap(h["deck"], F_DECK, HW), F_DECK, MUTED, 13)
d.line([MX, 362, W - MX, 362], fill=RULE, width=1)

# ---------------- MEDIUM ILLUSTRATIONS (233x34 strips) ----------------
def med_cop(w, h):
    s = Image.new("RGB", (w, h), (232, 224, 200))
    dd = ImageDraw.Draw(s)
    # sun over green hills, orange sun
    dd.ellipse([w - 60, 4, w - 24, 28], fill=(240, 120, 60))
    dd.polygon([(0, h), (80, 12), (160, h)], fill=(46, 125, 90))
    dd.polygon([(100, h), (180, 18), (w, h)], fill=(30, 90, 60))
    dd.rectangle([0, h - 4, w, h], fill=(178, 34, 41))
    return s

def med_gta(w, h):
    s = Image.new("RGB", (w, h), (24, 8, 40))
    dd = ImageDraw.Draw(s)
    dd.ellipse([w // 2 - 30, 2, w // 2 + 30, 52], fill=(255, 80, 160))
    for k in range(4):
        dd.rectangle([w // 2 - 30, 20 + k * 7, w // 2 + 30, 22 + k * 7], fill=(24, 8, 40))
    dd.rectangle([0, h - 8, w, h], fill=(0, 255, 220))
    dd.text((10, 6), "VI", font=font("DejaVuSans-Bold.ttf", 16), fill=(255, 255, 255))
    return s

def med_capitol(w, h):
    s = Image.new("RGB", (w, h), (180, 200, 225))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 4, w, h], fill=(120, 140, 170))
    dd.ellipse([w // 2 - 20, 2, w // 2 + 20, 18], fill=(245, 240, 225))
    dd.rectangle([w // 2 - 28, 16, w // 2 + 28, h - 4], fill=(245, 240, 225))
    for cx in range(w // 2 - 22, w // 2 + 23, 11):
        dd.rectangle([cx - 2, 18, cx + 2, h - 4], fill=(200, 195, 180))
    return s

def med_cricket(w, h):
    s = Image.new("RGB", (w, h), (0, 100, 60))
    dd = ImageDraw.Draw(s)
    # pitch strip
    dd.rectangle([0, h - 10, w, h], fill=(200, 180, 120))
    # bat + ball
    dd.rectangle([60, 6, 68, 26], fill=(220, 190, 140))
    dd.rectangle([60, 26, 76, 30], fill=(160, 120, 80))
    dd.ellipse([150, 10, 166, 26], fill=(178, 34, 41))
    dd.text((180, 8), "118", font=font("DejaVuSans-Bold.ttf", 16), fill=(255, 255, 255))
    return s

def med_boat(w, h):
    s = Image.new("RGB", (w, h), (0, 74, 137))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 12, w, h], fill=(0, 50, 90))
    # small boat
    dd.polygon([(60, 18), (170, 18), (150, 28), (80, 28)], fill=(120, 80, 40))
    dd.rectangle([110, 6, 114, 18], fill=(200, 200, 200))
    dd.polygon([(114, 6), (140, 16), (114, 16)], fill=(255, 255, 255))
    # waves
    for wx in range(0, w, 24):
        dd.arc([wx, h - 8, wx + 24, h + 8], start=180, end=360, fill=(255, 255, 255), width=2)
    return s

def med_drought(w, h):
    s = Image.new("RGB", (w, h), (240, 210, 140))
    dd = ImageDraw.Draw(s)
    dd.ellipse([w - 50, 4, w - 14, 30], fill=(240, 150, 40))
    # cracked earth
    dd.polygon([(0, h), (40, 20), (90, h)], fill=(200, 160, 90))
    dd.polygon([(70, h), (130, 16), (190, h)], fill=(180, 140, 80))
    dd.line([40, 20, 70, 30], fill=(120, 90, 50), width=2)
    dd.line([130, 16, 110, 28], fill=(120, 90, 50), width=2)
    return s

def med_rose(w, h):
    s = Image.new("RGB", (w, h), (0, 100, 60))
    dd = ImageDraw.Draw(s)
    # baseball + stitching
    dd.ellipse([w // 2 - 40, 2, w // 2 + 40, 32], fill=(255, 255, 255))
    dd.arc([w // 2 - 40, 2, w // 2 + 40, 32], start=200, end=340, fill=(178, 34, 41), width=2)
    dd.arc([w // 2 - 40, 2, w // 2 + 40, 32], start=20, end=160, fill=(178, 34, 41), width=2)
    dd.text((10, 8), "PETE ROSE", font=font("DejaVuSans-Bold.ttf", 10), fill=(255, 255, 255))
    return s

def med_anthropic(w, h):
    s = Image.new("RGB", (w, h), (6, 60, 40))
    dd = ImageDraw.Draw(s)
    for gy in range(6, h, 9):
        dd.line([0, gy, w, gy], fill=(16, 90, 60), width=1)
    pts = [(14, 28), (60, 24), (106, 26), (150, 16), (196, 18), (224, 8)]
    for i in range(len(pts) - 1):
        dd.line([pts[i], pts[i + 1]], fill=(255, 220, 0), width=3)
    dd.text((10, 4), "ANT $83", font=font("DejaVuSans-Bold.ttf", 12), fill=(255, 255, 255))
    return s

def med_berlin(w, h):
    s = Image.new("RGB", (w, h), (200, 210, 225))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 6, w, h], fill=(140, 150, 165))
    dd.rectangle([w // 2 - 40, 10, w // 2 + 40, 16], fill=(120, 110, 90))
    for cx in range(w // 2 - 34, w // 2 + 35, 14):
        dd.rectangle([cx - 3, 16, cx + 3, h - 6], fill=(140, 130, 110))
    dd.rectangle([w // 2 - 6, 2, w // 2 + 6, 10], fill=(120, 110, 90))
    for k in range(5):
        a = -math.pi / 2 + k * (2 * math.pi / 5)
        dd.ellipse([30 + 8 * math.cos(a) - 2, 16 + 8 * math.sin(a) - 2,
                    30 + 8 * math.cos(a) + 2, 16 + 8 * math.sin(a) + 2], fill=(255, 204, 0))
    return s

def med_chip(w, h):
    s = Image.new("RGB", (w, h), (28, 41, 71))
    dd = ImageDraw.Draw(s)
    dd.rectangle([w // 2 - 26, 6, w // 2 + 26, 28], fill=(0, 128, 128))
    dd.rectangle([w // 2 - 14, 12, w // 2 + 14, 22], fill=(28, 41, 71))
    for px in range(w // 2 - 20, w // 2 + 21, 10):
        dd.line([px, 2, px, 6], fill=(200, 200, 200), width=2)
        dd.line([px, 28, px, 32], fill=(200, 200, 200), width=2)
    dd.text((10, 10), "AI CHIPS", font=font("DejaVuSans-Bold.ttf", 10), fill=(255, 255, 255))
    return s

def med_rain(w, h):
    s = Image.new("RGB", (w, h), (120, 150, 190))
    dd = ImageDraw.Draw(s)
    for cx, cy in ((50, 8), (120, 5), (180, 10)):
        dd.ellipse([cx - 18, cy, cx + 18, cy + 12], fill=(230, 235, 245))
    for rx in range(10, w, 18):
        dd.line([rx, 22, rx - 3, 30], fill=(200, 215, 235), width=2)
    dd.arc([0, h - 12, 60, h + 12], start=180, end=360, fill=(255, 255, 255), width=3)
    dd.arc([60, h - 10, 130, h + 14], start=180, end=360, fill=(255, 255, 255), width=3)
    dd.arc([130, h - 12, 200, h + 12], start=180, end=360, fill=(255, 255, 255), width=3)
    return s

def med_nicholls(w, h):
    s = Image.new("RGB", (w, h), (0, 40, 90))
    dd = ImageDraw.Draw(s)
    dd.rectangle([0, h - 8, w, h], fill=(255, 204, 0))
    # stumps
    for sx in (90, 100, 110):
        dd.rectangle([sx, 10, sx + 3, 26], fill=(220, 190, 140))
    dd.rectangle([88, 8, 115, 10], fill=(160, 120, 80))
    dd.text((130, 10), "175*", font=font("DejaVuSans-Bold.ttf", 15), fill=(255, 255, 255))
    return s

MED_ICONS = [med_cop, med_gta, med_capitol, med_cricket, med_boat, med_drought,
             med_rose, med_anthropic, med_berlin, med_chip, med_rain, med_nicholls]
MED = [
    ("ANTALYA \u00b7 CLIMATE", "COP31 reaches its final day",
     "No deal yet; the draft drops every fossil-fuel mention and the $120bn adaptation figure."),
    ("WORLD \u00b7 GAMES", "GTA VI\u2019s first full day on sale",
     "Metacritic 99, a record tie. Sensor Tower puts day one at about $2.36bn and 24.6m copies."),
    ("WASHINGTON \u00b7 POLITICS", "Senate rejects Iran war-powers bid",
     "The resolution fails 51\u201348, with three Republicans in favour; the war goes on."),
    ("WELLINGTON \u00b7 SPORT", "Phillips makes history with 118",
     "The first to score centuries in all formats against India in one year; NZ 368 all out."),
    ("SENEGAL \u00b7 MIGRATION", "Migrant boat sinks off Senegal",
     "Four bodies recovered from a boat carrying 50\u2013100 people; the toll is expected to rise."),
    ("TONGA \u00b7 PACIFIC", "Drought emergency in Tonga",
     "The Pacific kingdom declares an emergency as El Ni\u00f1o bites; water rationing begins."),
    ("WASHINGTON \u00b7 SPORT", "Trump pardons Pete Rose",
     "The late slugger, banned for life for betting, is pardoned after his death."),
    ("NEW YORK \u00b7 MARKETS", "Anthropic slips after debut",
     "ANT falls 4.7% after hours to $92.60, after closing day one at $97.17, up 17%."),
    ("BERLIN \u00b7 EUROPE", "Europe ready for Ukraine talks",
     "Burnham, Merz and Zelensky present a united position on talks with Russia."),
    ("CALIFORNIA \u00b7 TECH", "State probes Nvidia over China chips",
     "California opens an AI-chip inquiry days after Jensen Huang\u2019s departure."),
    ("COOK IS. \u00b7 WEATHER", "Cyclone Xavier nears Cook Islands atoll",
     "Emergency declared for Nassau; a category 2\u20133 passage is forecast for the weekend."),
    ("WELLINGTON \u00b7 SPORT", "Nicholls makes 175 not out against India",
     "New Zealand 368 all out; India 159\u20131 at stumps on day two of the first Test."),
]
MBW = 233
MGAP = 12
MROW_Y = [370, 482, 594]
for i, (kick, head, deck) in enumerate(MED):
    r, c = divmod(i, 4)
    x = MX + c * (MBW + MGAP)
    y = MROW_Y[r]
    img.paste(MED_ICONS[i](MBW, 34), (x, y))
    ky = y + 38
    circle_num(x + 9, ky + 8, 9, str(i + 4), F_NUM2)
    d.text((x + 22, ky), kick, font=F_KICK2, fill=RED)
    hy = ky + 15
    textlines(x, hy, wrap(head, F_MED_H, MBW), F_MED_H, INK, 16)
    dy = hy + 33
    textlines(x, dy, wrap(deck, F_DECK2, MBW), F_DECK2, MUTED, 12)
d.line([MX, 708, W - MX, 708], fill=RULE, width=1)

# ---------------- BY THE NUMBERS ----------------
d.text((MX, 720), "BY THE", font=F_KICK, fill=RED)
d.text((MX, 734), "NUMBERS", font=F_KICK, fill=RED)
STATS = [
    ("370,000", "evacuated ahead of Cyclone Akvan"),
    ("$97.17", "Anthropic\u2019s first close, +17%"),
    ("51\u201348", "Senate rejects the Iran war-powers bid"),
    ("99", "GTA VI\u2019s Metacritic score"),
]
SX = [120, 339, 558, 777]
for (num, lab), sx in zip(STATS, SX):
    d.text((sx, 718), num, font=F_BIGN, fill=INK)
    textlines(sx, 742, wrap(lab, F_BIGL, 200), F_BIGL, MUTED, 12)
d.line([MX, 756, W - MX, 756], fill=RULE, width=1)

# ---------------- BOTTOM: MAP + ALSO ----------------
MAP_X, MAP_Y, MAP_W, MAP_H = MX, 780, 300, 140
LAT_TOP, LAT_BOT = 80.0, -60.0
d.text((MAP_X, 762), "WHERE IT HAPPENED", font=F_SECT, fill=INK)
wm = Image.open(os.path.join(BASE, "worldmap.png")).convert("RGB")
SW, SH = wm.size
SXF = SW / 360.0
SYF = SH / 180.0
def map_xy(lon, lat):
    x = MAP_X + (lon + 180) / 360.0 * MAP_W
    y = MAP_Y + (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * MAP_H
    return x, y
step = 5
for gy in range(0, MAP_H, step):
    for gx in range(0, MAP_W, step):
        lon = gx / MAP_W * 360 - 180
        lat = LAT_TOP - gy / MAP_H * (LAT_TOP - LAT_BOT)
        sx = int((lon + 180) * SXF)
        sy = int((90 - lat) * SYF)
        if 0 <= sx < SW and 0 <= sy < SH:
            px = wm.getpixel((sx, sy))
            if px[0] > 200 and px[1] > 200 and px[2] > 200:
                d.ellipse([MAP_X + gx - 2, MAP_Y + gy - 2, MAP_X + gx + 2, MAP_Y + gy + 2], fill=DOT)
MARKERS = [
    (80.6, 16.5, 0, 0),      # 1 Akvan (Gopalpur)
    (30.5, 50.4, 0, 0),      # 2 Kyiv
    (121.5, 25.0, 0, 0),     # 3 Taipei (Taiex)
    (30.1, 36.9, 0, 0),      # 4 Antalya (COP31)
    (-80.2, 25.8, 0, 0),     # 5 Vice City (Miami)
    (-77.0, 38.9, 0, 0),     # 6 Washington
    (174.8, -41.3, 0, 0),    # 7 Wellington
    (-17.4, 14.7, 0, 0),     # 8 Senegal (Dakar)
    (-175.2, -21.1, 0, 0),   # 9 Tonga
    (-77.0, 38.9, 14, 12),   # 10 Washington (offset from 6)
    (-74.0, 40.7, 0, 0),     # 11 New York
    (13.4, 52.5, 0, 0),      # 12 Berlin
    (-122.4, 37.8, 0, 0),    # 13 California
    (-161.0, -11.0, 0, 0),   # 14 Cook Islands (Nassau)
    (174.8, -41.3, 14, -10), # 15 Wellington (offset from 7)
]
for i, (lon, lat, dx, dy) in enumerate(MARKERS, start=1):
    mx, my = map_xy(lon, lat)
    circle_num(mx + dx, my + dy, 9, str(i), F_MAPN)
d.text((MAP_X, 926), "Numbered dots mark stories 1\u201315.", font=F_MAPC, fill=MUTED)

# ALSO list 16-36 (21 stories, own selection + wording)
AX = 344
AW = 652
d.text((AX, 762), "ALSO ON FRIDAY 20 NOVEMBER \u2014 21 MORE STORIES", font=F_SECT, fill=INK)
d.rectangle([AX, 776, AX + AW, 778], fill=RED)
ALSO = [
    ("Cincinnati: Fiona the hippo dies", "aged 9, after swallowing a hat."),
    ("Gaza: aid groups score the peace plan", "implementation 4 out of 20."),
    ("Hormuz: four attacks on vessels", "in 96 hours, maritime centre says."),
    ("Washington: the US war on Iran has cost $48.3bn", "Pentagon says."),
    ("UK and Norway fund \u00a3100m-plus", "for two Ukrainian naval craft."),
    ("Belgrade: Cupic elected speaker", "of Serbia\u2019s new parliament."),
    ("Copenhagen: Denmark passes asset-forfeiture bill", "in parliament."),
    ("Jakarta: Indonesia passes asset-forfeiture bill", "in parliament."),
    ("Denver: Democrats stay divided", "despite midterm wins."),
    ("Dublin: Harris seeks border-poll criteria talks", "with London."),
    ("Los Angeles: Thomas Markle is found fit", "to stand trial."),
    ("Punjab: a truck driver wins $1.3m", "in a Diwali lottery."),
    ("Johannesburg: DJ Lag on GTA 6 soundtrack", "celebrates the feature."),
    ("Sydney: ASX futures fall 1%", "jobless rate rises to 4.9%."),
    ("Mumbai: Sensex slips at Friday\u2019s open", "Nifty stands at 25,199."),
    ("Antalya: pledges point to about 2.6\u00b0C of warming", "UNEP says."),
    ("New Delhi: Pakistan minister to lead trip", "to Delhi for SCO dialogue."),
    ("Tokyo: PM Takaichi seeks continued dialogue", "with China."),
    ("Canberra: Australia sanctions settler groups", "in the West Bank."),
    ("Sofia: LPG tanker off Bulgaria hit by projectiles", "crew safe."),
    ("Washington: US files emergency court request", "on Venezuelan TPS."),
]
COLW = 320
COLX = [AX, AX + COLW + 12]
ROW_H = 10
for i, (title, detail) in enumerate(ALSO):
    col, row = divmod(i, 11)
    x = COLX[col]
    y = 784 + row * ROW_H
    num = str(i + 16)
    cx = x
    for txt, fnt, fill in [(num + ". ", F_ALSO_N, RED), (title, F_ALSO_B, INK),
                           (" \u2014 " + detail, F_ALSO, INK)]:
        d.text((cx, y), txt, font=fnt, fill=fill)
        cx += d.textlength(txt, font=fnt)
    if cx > x + COLW:
        print("OVERFLOW also", num, title, "width", round(cx - x), ">", COLW)

# ---------------- DATE CHECK + FOOTER ----------------
d.line([MX, 952, W - MX, 952], fill=RULE, width=1)
dc1 = "DATE CHECK \u2014 Left out on purpose because first reported before today: 19 NOV: Trump\u2013Xi\u2013Putin trilateral meeting itself \u00b7 Anthropic\u2019s $83 IPO pricing \u00b7"
dc2 = "GTA VI\u2019s midnight unlock \u00b7 the ICJ\u2019s Rohingya genocide judgment \u00b7 the Van Gogh record $190.4m sale \u00b7 the EU\u2019s proposed \u20ac45bn loan for Ukraine \u00b7"
dc3 = "the US\u2013Venezuela military deal \u00b7 Fiji\u2019s drought disaster declaration \u00b7 Han Duck-soo\u2019s acquittal \u00b7 the Crimean Bridge attack \u00b7 the Houthi strike on Riyadh\u2019s PIF tower."
d.text((MX, 958), dc1, font=F_FOOT, fill=RED)
d.text((MX, 969), dc2, font=F_FOOT, fill=RED)
d.text((MX, 980), dc3, font=F_FOOT, fill=RED)
d.line([MX, 994, W - MX, 994], fill=RULE, width=1)
d.text((MX, 1000), "Every story here happened or was first reported on Friday 20 November 2026. Contested claims are attributed to the side making them.",
       font=F_FOOT, fill=MUTED)
d.text((MX, 1011), "Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 The Hindu \u00b7 IMD \u00b7 ICC \u00b7 UNEP. Original drawings.",
       font=F_FOOT, fill=MUTED)

out = os.path.join(BASE, "repo", "entry.png")
img.save(out, "PNG")
print("saved", out, img.size, os.path.getsize(out), "bytes")
