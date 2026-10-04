# -*- coding: utf-8 -*-
"""Generates assets/img/og-default.png (1200x630) and apple-touch-icon.png from the game icons."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")


def font(size, bold=True):
    for p in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Helvetica.ttc",
              "/Library/Fonts/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def rounded(im, r):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.size[0], im.size[1]), r, fill=255)
    im.putalpha(m)
    return im


W, H = 1200, 630
bg = Image.new("RGB", (W, H), (7, 7, 13))
glow = Image.new("RGB", (W, H), (7, 7, 13))
d = ImageDraw.Draw(glow)
d.ellipse((-200, -250, 600, 450), fill=(76, 40, 160))
d.ellipse((650, -200, 1400, 500), fill=(150, 70, 30))
glow = glow.filter(ImageFilter.GaussianBlur(120))
bg = Image.blend(bg, glow, 0.85)
d = ImageDraw.Draw(bg)
for x in range(0, W, 60):
    d.line((x, 0, x, H), fill=(255, 255, 255, 14), width=1)
for y in range(0, H, 60):
    d.line((0, y, W, y), fill=(255, 255, 255, 14), width=1)

specs = [("the-flipside", (640, 90), -7), ("merge-survivors", (830, 40), 6), ("tiny-mage", (740, 250), -2)]
for slug, (x, y), rot in specs:
    ic = Image.open(os.path.join(IMG, slug, "icon-512.png")).convert("RGBA").resize((300, 300), Image.LANCZOS)
    ic = rounded(ic, 78)
    pad = Image.new("RGBA", (360, 360), (0, 0, 0, 0))
    sh = Image.new("RGBA", (300, 300), (0, 0, 0, 160)).filter(ImageFilter.GaussianBlur(14))
    pad.paste(sh, (30, 44), rounded(sh.copy(), 78))
    pad.paste(ic, (30, 30), ic)
    pad = pad.rotate(rot, resample=Image.BICUBIC, expand=True)
    bg.paste(pad, (x - 20, y), pad)

d = ImageDraw.Draw(bg)
d.rounded_rectangle((70, 90, 134, 154), 18, fill=(139, 92, 246))
d.text((102, 122), "SB", font=font(26), fill="white", anchor="mm")
d.text((70, 250), "Mobile games", font=font(74), fill="white")
d.text((70, 336), "forged in the dark.", font=font(74), fill=(255, 150, 90))
d.text((70, 470), "Serhat Bilal Studio", font=font(34), fill=(200, 198, 220))
d.text((70, 520), "The Flipside  ·  Merge Survivors  ·  Tiny Mage", font=font(26), fill=(140, 138, 165))
bg.save(os.path.join(IMG, "og-default.png"), optimize=True)

t = Image.new("RGB", (180, 180))
px = t.load()
for yy in range(180):
    for xx in range(180):
        k = (xx + yy) / 358.0
        px[xx, yy] = (int(139 + (255 - 139) * k), int(92 + (122 - 92) * k), int(246 + (61 - 246) * k))
ImageDraw.Draw(t).text((90, 92), "SB", font=font(76), fill="white", anchor="mm")
t.save(os.path.join(IMG, "apple-touch-icon.png"), optimize=True)
print("ok")
