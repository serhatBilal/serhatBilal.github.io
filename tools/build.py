# -*- coding: utf-8 -*-
"""Static site generator for Serhat Bilal Studio.

Usage:  python3 tools/build.py
Reads tools/content.py and writes plain HTML into the repo root (GitHub Pages ready).
"""
import html
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (BY_SLUG, EMAIL, GAMES, GITHUB, PRIVACY, SITE, STUDIO, TERMS_INTRO,  # noqa: E402
                     UPDATED_EN, UPDATED_TR, terms_sections)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
esc = html.escape

# ----------------------------------------------------------------------------- helpers


def bi(en, tr, tag="span", cls=""):
    c = ' class="%s"' % cls if cls else ""
    return '<%s data-l="en"%s>%s</%s><%s data-l="tr"%s>%s</%s>' % (tag, c, en, tag, tag, c, tr, tag)


def url(slug=None, page=None):
    if slug is None:
        return "/"
    return "/games/%s/" % slug + ("%s/" % page if page else "")


def full(path):
    return SITE + path


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def icon(slug):
    return "/assets/img/%s/icon.webp" % slug


def status_badge(g):
    cls = {"live": "", "soon": " soon", "dev": " dev"}[g["status"]]
    return '<span class="badge%s"><i></i>%s</span>' % (cls, bi(g["status_en"], g["status_tr"]))


def gname(g):
    return esc(g["name"])


ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
APPLE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.15-2.8.85-3.5.85-.73 0-1.85-.83-3.05-.8-1.57.02-3.02.92-3.83 2.32-1.63 2.83-.42 7.02 1.17 9.32.78 1.12 1.7 2.38 2.9 2.33 1.17-.05 1.6-.75 3.02-.75 1.4 0 1.8.75 3.03.73 1.25-.02 2.05-1.14 2.82-2.27.9-1.3 1.27-2.56 1.28-2.63-.03-.01-2.45-.94-2.47-3.72zM14.1 5.8c.64-.78 1.07-1.86.95-2.94-.92.04-2.04.62-2.7 1.4-.6.69-1.12 1.8-.98 2.85 1.03.08 2.08-.52 2.73-1.31z"/></svg>'
MAILI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 8 8 6 8-6"/></svg>'
GH = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.03 1.76 2.7 1.25 3.35.96.1-.75.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.28 1.18-3.09-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.78 0c2.2-1.49 3.17-1.18 3.17-1.18.62 1.59.23 2.76.11 3.05.74.81 1.18 1.83 1.18 3.09 0 4.42-2.7 5.4-5.27 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>'


def phone(g, idx, eager=False):
    s = g["shots"]
    alt = "%s screenshot %d" % (g["name"], idx)
    ld = "" if eager else ' loading="lazy"'
    return ('<div class="phone"><img data-l="en" src="/assets/img/%s/shot-en-%d.webp" alt="%s"%s decoding="async">'
            '<img data-l="tr" src="/assets/img/%s/shot-tr-%d.webp" alt="%s (TR)"%s decoding="async"></div>') % (
        g["slug"], idx, esc(alt), ld, g["slug"], idx, esc(alt), ld)


# ----------------------------------------------------------------------------- shell

LANG_BOOT = ("<script>(function(){try{var q=new URLSearchParams(location.search).get('lang');"
             "var s=localStorage.getItem('sbs-lang');var l=q||s||((navigator.language||'').toLowerCase().indexOf('tr')===0?'tr':'en');"
             "document.documentElement.lang=(l==='tr'?'tr':'en')}catch(e){}})()</script>")


def head(title_en, title_tr, desc, path, accent=None, og=None, extra=""):
    og = og or "/assets/img/og-default.png"
    return """<!doctype html>
<html lang="en" class="no-js" data-title-en="%(te)s" data-title-tr="%(tt)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(te)s</title>
<meta name="description" content="%(d)s">
<meta name="theme-color" content="#07070d">
<link rel="canonical" href="%(c)s">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%(studio)s">
<meta property="og:title" content="%(te)s">
<meta property="og:description" content="%(d)s">
<meta property="og:url" content="%(c)s">
<meta property="og:image" content="%(og)s">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
%(boot)s
%(extra)s
</head>
""" % dict(te=esc(title_en), tt=esc(title_tr), d=esc(desc), c=full(path), og=full(og), studio=STUDIO,
           boot=LANG_BOOT, extra=extra)


def body_open(accent=None, nav_active=""):
    style = ""
    if accent:
        style = ' style="--a1:%s;--a2:%s"' % accent

    def cur(k):
        return ' aria-current="page"' if nav_active == k else ""

    return """<body%s>
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="container nav-in">
    <a class="brand" href="/" aria-label="%s"><span class="brand-mark">SB</span><span>Serhat Bilal <span style="color:var(--muted);font-weight:600">Studio</span></span></a>
    <nav class="nav-links" id="navlinks" aria-label="Main">
      <a href="/#games"%s>%s</a>
      <a href="/legal/"%s>%s</a>
      <a href="/#about">%s</a>
      <a href="mailto:%s">%s</a>
    </nav>
    <div class="lang" role="group" aria-label="Language"><button data-set="en" type="button">EN</button><button data-set="tr" type="button">TR</button></div>
    <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="navlinks"><span></span></button>
  </div>
</header>
<main id="main">
""" % (style, STUDIO, cur("games"), bi("Games", "Oyunlar"), cur("legal"), bi("Legal &amp; Support", "Yasal ve Destek"),
       bi("About", "Hakkında"), EMAIL, bi("Contact", "İletişim"))


def footer():
    def col(page):
        return "".join('<li><a href="%s">%s</a></li>' % (url(g["slug"], page), esc(g.get("short") or g["name"])) for g in GAMES)
    games_col = "".join('<li><a href="%s">%s</a></li>' % (url(g["slug"]), gname(g)) for g in GAMES)
    return """</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/"><span class="brand-mark">SB</span><span>Serhat Bilal Studio</span></a>
        <p class="blurb">%(blurb)s</p>
      </div>
      <div><h5>%(h_games)s</h5><ul>%(games)s</ul></div>
      <div><h5>%(h_priv)s</h5><ul>%(priv)s</ul></div>
      <div><h5>%(h_terms)s</h5><ul>%(terms)s</ul></div>
      <div><h5>%(h_sup)s</h5><ul>%(sup)s<li style="margin-top:14px"><a href="/legal/">%(all)s →</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="year">2026</span> Serhat Bilal Studio · Bursa, Türkiye</span>
      <span><a href="%(gh)s" target="_blank" rel="noopener">GitHub</a> · <a href="mailto:%(em)s">%(em)s</a></span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
""" % dict(blurb=bi("Independent mobile games made with Godot. Every game has its own privacy policy, terms and support page.",
                    "Godot ile yapılan bağımsız mobil oyunlar. Her oyunun kendi gizlilik politikası, şartları ve destek sayfası var."),
           h_games=bi("Games", "Oyunlar"), h_priv=bi("Privacy", "Gizlilik"), h_terms=bi("Terms", "Şartlar"), h_sup=bi("Support", "Destek"),
           games=games_col, priv=col("privacy"), terms=col("terms"), sup=col("support"),
           all=bi("All legal links", "Tüm yasal linkler"), gh=GITHUB, em=EMAIL)


# ----------------------------------------------------------------------------- home


def panel(g, i):
    s = g["slug"]
    flip = " flip" if i % 2 else ""
    if g["shots"]:
        visual = '<div class="phones">%s</div>' % "".join(phone(g, n) for n in g["shots"]["home"])
    else:
        visual = '<div class="art"><img src="%s" alt="%s artwork" loading="lazy" width="768" height="768"></div>' % (icon(s), esc(g["name"]))
    if g["store_url"]:
        primary = '<a class="btn primary" href="%s" target="_blank" rel="noopener">%s App Store</a>' % (g["store_url"], APPLE)
    else:
        primary = '<span class="btn primary disabled">%s</span>' % bi(g["status_en"], g["status_tr"])
    tags = "".join('<span class="chip">%s</span>' % bi(*t) for t in g["tags"])
    return """<article class="panel rv%(flip)s" style="--a1:%(a1)s;--a2:%(a2)s" id="%(slug)s">
  <div class="panel-copy">
    %(badge)s
    <h3>%(name)s</h3>
    <p class="tagline">%(tag)s</p>
    <p class="summary">%(sum)s</p>
    <div class="chips">%(tags)s</div>
    <div class="actions">%(primary)s<a class="btn ghost" href="%(page)s">%(details)s %(arrow)s</a></div>
    <div class="legal-links"><a href="%(p)s">%(lp)s</a><a href="%(t)s">%(lt)s</a><a href="%(su)s">%(ls)s</a></div>
  </div>
  <div class="panel-visual">%(visual)s</div>
</article>""" % dict(flip=flip, a1=g["accent"][0], a2=g["accent"][1], slug=s, badge=status_badge(g), name=gname(g),
                     tag=bi(*g["tagline"]), sum=bi(*g["summary"]), tags=tags, primary=primary, page=url(s),
                     details=bi("Game details", "Oyun detayları"), arrow=ARROW,
                     p=url(s, "privacy"), t=url(s, "terms"), su=url(s, "support"),
                     lp=bi("Privacy Policy", "Gizlilik Politikası"), lt=bi("Terms of Use", "Kullanım Şartları"),
                     ls=bi("Support", "Destek"), visual=visual)


def home():
    title_en = "Serhat Bilal Studio — Indie Mobile Games"
    title_tr = "Serhat Bilal Studio — Bağımsız Mobil Oyunlar"
    desc = "Independent mobile games by Serhat Bilal: The Flipside, Merge Survivors: Dark Dungeon and Tiny Mage. Privacy policies, terms and support for every game."
    out = head(title_en, title_tr, desc, "/")
    out += body_open(nav_active="")
    stack = ""
    for cls, g, label in (("s1", BY_SLUG["the-flipside"], "The Flipside"), ("s2", BY_SLUG["merge-survivors"], "Merge Survivors"),
                          ("s3", BY_SLUG["tiny-mage"], "Tiny Mage")):
        stack += '<a class="%s" href="%s" aria-label="%s"><img src="%s" alt="%s icon" width="768" height="768"><span class="tag">%s</span></a>' % (
            cls, url(g["slug"]), esc(g["name"]), icon(g["slug"]), esc(g["name"]), label)
    out += """<section class="hero"><div class="container hero-grid">
  <div>
    <span class="eyebrow">%(eb)s</span>
    <h1>%(h1)s</h1>
    <p class="lead">%(lead)s</p>
    <div class="hero-cta">
      <a class="btn primary" href="#games">%(c1)s %(arrow)s</a>
      <a class="btn ghost" href="/legal/">%(c2)s</a>
    </div>
    <div class="hero-stats">
      <div><strong>3</strong><span>%(s1)s</span></div>
      <div><strong>EN · TR</strong><span>%(s2)s</span></div>
      <div><strong>Godot</strong><span>%(s3)s</span></div>
    </div>
  </div>
  <div class="stack" aria-label="%(al)s">%(stack)s</div>
</div></section>
""" % dict(eb=bi("Indie game studio · Bursa", "Bağımsız oyun stüdyosu · Bursa"),
           h1=bi('Mobile games<br>forged in the <span class="grad">dark.</span>', 'Karanlıkta<br><span class="grad">dövülen</span> mobil oyunlar.', tag="span"),
           lead=bi("Three games, one small studio: a neon-soaked endless runner, a dark-fantasy survivors-like and a tiny wizard with a very big wand.",
                   "Üç oyun, tek küçük stüdyo: neon bir sonsuz koşu, karanlık fantezi bir survivors oyunu ve kocaman asası olan minicik bir büyücü."),
           c1=bi("Explore games", "Oyunları keşfet"), c2=bi("Privacy, terms &amp; support", "Gizlilik, şartlar ve destek"), arrow=ARROW,
           s1=bi("games", "oyun"), s2=bi("languages", "dil"), s3=bi("engine", "motor"), al="Game icons", stack=stack)

    out += """<section class="section" id="games"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p></div>
%s
</div></section>
""" % (bi("The games", "Oyunlar"), bi("Pick your descent.", "Yolculuğunu seç."),
       bi("Each game has its own page, privacy policy, terms of use and support — with a dedicated link for every one.",
          "Her oyunun kendi sayfası, gizlilik politikası, kullanım şartları ve destek sayfası var — hepsi için ayrı bir link."),
       "\n".join(panel(g, i) for i, g in enumerate(GAMES)))

    out += """<section class="section" style="padding-top:20px"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2></div>
  <div class="cards">
    <div class="card rv"><div class="ico">🎮</div><h4>%s</h4><p>%s</p></div>
    <div class="card rv"><div class="ico">🔒</div><h4>%s</h4><p>%s</p></div>
    <div class="card rv"><div class="ico">🌍</div><h4>%s</h4><p>%s</p></div>
  </div>
</div></section>
""" % (bi("How I build", "Nasıl geliştiriyorum"), bi("Small games, no tricks.", "Küçük oyunlar, numarasız."),
       bi("Player first", "Oyuncu önce"), bi("Short sessions, fast restarts and no forced accounts. Ads, where they exist, are optional.",
                                            "Kısa oturumlar, hızlı yeniden denemeler ve zorunlu hesap yok. Reklamlar varsa isteğe bağlıdır."),
       bi("Clear about data", "Veride net"), bi("Every game has a plain-language privacy policy that matches what the game really does.",
                                              "Her oyunun, oyunun gerçekte yaptığıyla uyumlu, sade dilde bir gizlilik politikası var."),
       bi("English &amp; Türkçe", "English ve Türkçe"), bi("Games and every page on this site are available in both languages.",
                                                          "Oyunlar ve bu sitedeki her sayfa iki dilde de mevcut."))

    # legal matrix
    rows = ""
    for g in GAMES:
        rows += '<div class="matrix-row"><div class="g"><img src="%s" alt="" width="38" height="38"><span>%s</span></div><a class="l" href="%s">%s</a><a class="l" href="%s">%s</a><a class="l" href="%s">%s</a></div>' % (
            icon(g["slug"]), gname(g), url(g["slug"], "privacy"), bi("Privacy", "Gizlilik"), url(g["slug"], "terms"), bi("Terms", "Şartlar"),
            url(g["slug"], "support"), bi("Support", "Destek"))
    out += """<section class="section" style="padding-top:20px"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p></div>
  <div class="matrix rv"><div class="matrix-row head"><span>%s</span><span>%s</span><span>%s</span><span>%s</span></div>%s</div>
  <p class="rv" style="margin-top:18px"><a class="btn ghost sm" href="/legal/">%s %s</a></p>
</div></section>
""" % (bi("Legal &amp; support", "Yasal ve destek"), bi("Everything in one place.", "Her şey tek yerde."),
       bi("Copy the exact URL you need for App Store Connect or Google Play Console from the legal hub.",
          "App Store Connect veya Google Play Console için ihtiyacın olan linki yasal merkezden kopyala."),
       bi("Game", "Oyun"), bi("Privacy Policy", "Gizlilik Politikası"), bi("Terms of Use", "Kullanım Şartları"), bi("Support", "Destek"),
       rows, bi("Open the legal hub", "Yasal merkezi aç"), ARROW)

    out += """<section class="section" id="about" style="padding-top:20px"><div class="container">
  <div class="about rv">
    <img class="avatar" src="https://github.com/serhatBilal.png?size=400" alt="Serhat Bilal" width="280" height="280" loading="lazy">
    <div>
      <span class="eyebrow">%s</span>
      <h2>Serhat Bilal</h2>
      <p>%s</p>
      <div class="actions"><a class="btn primary" href="mailto:%s">%s %s</a><a class="btn ghost" href="%s" target="_blank" rel="noopener">%s GitHub</a></div>
    </div>
  </div>
</div></section>
""" % (bi("About", "Hakkında"),
       bi("Software developer from Bursa, Türkiye, building games and apps across mobile, back-end and tools. This studio is the public home of my games — if something is broken, unclear or just cool, write to me.",
          "Bursa'dan yazılım geliştirici; mobil, back-end ve araçlar alanında oyun ve uygulamalar yapıyorum. Bu stüdyo, oyunlarımın herkese açık evi — bir şey bozuksa, belirsizse ya da sadece harikaysa bana yaz."),
       EMAIL, MAILI, bi("Get in touch", "İletişime geç"), GITHUB, GH)
    out += footer()
    write("index.html", out)


# ----------------------------------------------------------------------------- game page


def jsonld(g):
    import json
    d = {"@context": "https://schema.org", "@type": "MobileApplication", "name": g["name"],
         "applicationCategory": "GameApplication", "operatingSystem": "iOS" if "iOS" in g["platform"][0] else "iOS, Android",
         "description": g["summary"][0], "image": full(icon(g["slug"])),
         "author": {"@type": "Person", "name": "Serhat Bilal"}, "inLanguage": ["en", "tr"],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    if g["store_url"]:
        d["url"] = g["store_url"]
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)


def crumbs(g, leaf=None):
    parts = '<a href="/">%s</a><span class="sep">/</span><a href="/#games">%s</a><span class="sep">/</span>' % (bi("Home", "Ana sayfa"), bi("Games", "Oyunlar"))
    if leaf:
        parts += '<a href="%s">%s</a><span class="sep">/</span><span>%s</span>' % (url(g["slug"]), esc(g.get("short") or g["name"]), leaf)
    else:
        parts += "<span>%s</span>" % esc(g.get("short") or g["name"])
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % parts


def game_page(g):
    s = g["slug"]
    title_en = "%s — %s" % (g["name"], STUDIO)
    title_tr = title_en
    out = head(title_en, title_tr, g["meta_desc"][0], url(s), og=icon(s), extra=jsonld(g))
    out += body_open(accent=g["accent"], nav_active="games")
    if g["store_url"]:
        primary = '<a class="btn primary" href="%s" target="_blank" rel="noopener">%s %s</a>' % (g["store_url"], APPLE, bi("Download on the App Store", "App Store'dan indir"))
    else:
        primary = '<span class="btn primary disabled">%s</span>' % bi(g["status_en"], g["status_tr"])
    out += """<section class="ghero"><div class="container">
  %(crumbs)s
  <div class="ghero-grid">
    <div class="icon"><img src="%(icon)s" alt="%(nm)s icon" width="768" height="768"></div>
    <div>
      %(badge)s
      <h1>%(nm)s</h1>
      <p class="tagline">%(tag)s</p>
      <p class="summary">%(sum)s</p>
      <div class="actions">%(primary)s<a class="btn ghost" href="%(sup)s">%(support)s</a></div>
    </div>
  </div>
</div></section>
""" % dict(crumbs=crumbs(g), icon=icon(s), nm=gname(g), badge=status_badge(g), tag=bi(*g["tagline"]), sum=bi(*g["summary"]),
           primary=primary, sup=url(s, "support"), support=bi("Get support", "Destek al"))

    # facts
    facts = [(bi("Platform", "Platform"), bi(*g["platform"])), (bi("Price", "Fiyat"), bi(*g["price"])),
             (bi("Genre", "Tür"), bi(*g["kind"])), (bi("Version", "Sürüm"), bi(g["version"], g["version"]) if g["version"][0].isdigit() else bi("In development", "Geliştiriliyor"))]
    out += '<section class="container rv"><div class="facts">%s</div></section>' % "".join('<div class="fact"><span>%s</span><strong>%s</strong></div>' % f for f in facts)

    if g["shots"]:
        out += """<section class="section" style="padding-bottom:0"><div class="container"><div class="section-head rv" style="margin-bottom:8px"><span class="eyebrow">%s</span></div></div>
<div class="shots rv">%s</div></section>""" % (bi("Screenshots", "Ekran görüntüleri"), "".join(phone(g, n) for n in range(1, g["shots"]["count"] + 1)))

    cards = "".join('<div class="card rv"><div class="ico">%s</div><h4>%s</h4><p>%s</p></div>' % (ico, bi(*t), bi(*b)) for ico, t, b in g["features"])
    out += """<section class="section"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2></div>
  <div class="features">%s</div>
</div></section>
""" % (bi("Features", "Özellikler"), bi("What to expect", "Seni neler bekliyor"), cards)

    glance = "".join('<span class="chip">%s</span>' % bi(*x) for x in g["glance"])
    out += """<section class="section" style="padding-top:0"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p></div>
  <div class="glance rv">%s</div>
</div></section>
""" % (bi("Privacy at a glance", "Bir bakışta gizlilik"), bi("Your data, plainly.", "Verilerin, sade bir dille."),
       bi("The short version. The full documents are linked below.", "Kısa özet. Tam belgeler aşağıda."), glance)

    out += """<section class="section" style="padding-top:0"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2></div>
  <div class="docs-links">
    <a class="doc-link rv" href="%s"><strong>%s</strong><span>%s</span></a>
    <a class="doc-link rv" href="%s"><strong>%s</strong><span>%s</span></a>
    <a class="doc-link rv" href="%s"><strong>%s</strong><span>%s</span></a>
  </div>
</div></section>
""" % (bi("Legal &amp; support", "Yasal ve destek"), bi("Documents for this game", "Bu oyunun belgeleri"),
       url(s, "privacy"), bi("Privacy Policy", "Gizlilik Politikası"), bi("What the game collects and why.", "Oyunun ne topladığı ve nedeni."),
       url(s, "terms"), bi("Terms of Use", "Kullanım Şartları"), bi("The rules for playing.", "Oynamanın kuralları."),
       url(s, "support"), bi("Support &amp; FAQ", "Destek ve SSS"), bi("Answers and how to reach me.", "Cevaplar ve bana nasıl ulaşacağın."))

    others = "".join('<a class="mini rv" href="%s" style="--a1:%s;--a2:%s"><img src="%s" alt="" width="72" height="72"><div><strong>%s</strong><span>%s</span></div></a>' % (
        url(o["slug"]), o["accent"][0], o["accent"][1], icon(o["slug"]), gname(o), bi(*o["tagline"])) for o in GAMES if o["slug"] != s)
    out += """<section class="section" style="padding-top:0"><div class="container">
  <div class="section-head rv"><span class="eyebrow">%s</span><h2>%s</h2></div>
  <div class="more-games">%s</div>
</div></section>
""" % (bi("More games", "Diğer oyunlar"), bi("From the same studio", "Aynı stüdyodan"), others)
    out += footer()
    write("games/%s/index.html" % s, out)


# ----------------------------------------------------------------------------- doc pages


def tabs(g, active):
    s = g["slug"]
    items = (("privacy", bi("Privacy Policy", "Gizlilik Politikası")), ("terms", bi("Terms of Use", "Kullanım Şartları")), ("support", bi("Support", "Destek")))
    t = "".join('<a href="%s"%s>%s</a>' % (url(s, k), ' aria-current="page"' if k == active else "", label) for k, label in items)
    return '<div class="tabs">%s</div>' % t


def doc_head(g, kind, title, subtitle):
    s = g["slug"]
    leaf = title
    return """<section class="doc-head"><div class="container">
  %s
  <div class="doc-title"><img src="%s" alt="" width="84" height="84"><div><h1>%s</h1><p>%s</p></div></div>
  %s
</div></section>
""" % (crumbs(g, leaf), icon(s), title, subtitle, tabs(g, kind))


def legal_doc(g, kind):
    s = g["slug"]
    if kind == "privacy":
        P = PRIVACY[s]
        sections = P["sections"]
        intro = P["intro"]
        callout = P["callout"]
        t_en, t_tr = "Privacy Policy", "Gizlilik Politikası"
    else:
        sections = terms_sections(s)
        intro = TERMS_INTRO
        callout = None
        t_en, t_tr = "Terms of Use", "Kullanım Şartları"
    title_en = "%s · %s — %s" % (t_en, g["name"], STUDIO)
    title_tr = "%s · %s — %s" % (t_tr, g["name"], STUDIO)
    desc = "%s for %s by Serhat Bilal." % (t_en, g["name"])
    out = head(title_en, title_tr, desc, url(s, kind), og=icon(s))
    out += body_open(accent=g["accent"], nav_active="")
    out += doc_head(g, kind, bi(t_en, t_tr), esc(g["name"]))
    toc = "".join('<a href="#%s">%s</a>' % (sid, bi(he, ht)) for sid, he, ht, _, _ in sections)
    body = "".join('<section id="%s"><h2>%s</h2>%s</section>' % (sid, bi(he, ht), bi(be, bt, tag="div")) for sid, he, ht, be, bt in sections)
    co = ""
    if callout:
        co = '<div class="callout"><strong>%s</strong>%s</div>' % (bi(callout[0], callout[1]), bi(callout[2], callout[3], tag="p"))
    out += """<div class="container doc-wrap">
  <aside class="toc" aria-label="Contents"><h4>%s</h4>%s</aside>
  <article class="doc">
    <div class="meta"><span>%s: %s</span><span>%s</span></div>
    <p class="intro">%s</p>
    %s
    %s
  </article>
</div>
""" % (bi("Contents", "İçindekiler"), toc, bi("Last updated", "Son güncelleme"), bi(UPDATED_EN, UPDATED_TR), esc(g["name"]),
       bi(*intro), co, body)
    out += footer()
    write("games/%s/%s/index.html" % (s, kind), out)


def support_page(g):
    s = g["slug"]
    title_en = "Support · %s — %s" % (g["name"], STUDIO)
    title_tr = "Destek · %s — %s" % (g["name"], STUDIO)
    out = head(title_en, title_tr, "Support and FAQ for %s." % g["name"], url(s, "support"), og=icon(s))
    out += body_open(accent=g["accent"])
    out += doc_head(g, "support", bi("Support", "Destek"), esc(g["name"]))
    subj = "Support: %s" % g["name"]
    mailto = "mailto:%s?subject=%s" % (EMAIL, subj.replace(" ", "%20").replace(":", "%3A"))
    inc = "".join("<li>%s</li>" % bi(*x) for x in g["support_include"])
    faq = "".join('<details><summary>%s</summary><div class="ans">%s</div></details>' % (bi(*q), bi(*a, tag="p")) for q, a in g["faq"])
    out += """<div class="container" style="padding-bottom:80px">
  <div class="support-grid">
    <div class="support-card"><h2>%s</h2><p>%s</p><a class="btn primary" href="%s">%s %s</a></div>
    <div class="support-card"><h2>%s</h2><ul>%s</ul></div>
  </div>
  <div class="section-head" style="margin:48px 0 20px"><h2 style="font-size:1.7rem">%s</h2></div>
  <div class="faq">%s</div>
  <p style="margin-top:34px;color:var(--muted)">%s <a href="%s" style="text-decoration:underline">%s</a> · <a href="%s" style="text-decoration:underline">%s</a></p>
</div>
""" % (bi("Email support", "E-posta desteği"),
       bi("Write to <strong>%s</strong>. I read every message and reply as soon as I can." % EMAIL,
          "<strong>%s</strong> adresine yaz. Her mesajı okurum ve en kısa sürede yanıtlarım." % EMAIL),
       mailto, MAILI, bi("Send an email", "E-posta gönder"),
       bi("Please include", "Lütfen şunları ekle"), inc,
       bi("Frequently asked questions", "Sık sorulan sorular"), faq,
       bi("Also see:", "Ayrıca bak:"), url(s, "privacy"), bi("Privacy Policy", "Gizlilik Politikası"), url(s, "terms"), bi("Terms of Use", "Kullanım Şartları"))
    out += footer()
    write("games/%s/support/index.html" % s, out)


# ----------------------------------------------------------------------------- hub / misc


def legal_hub():
    out = head("Legal & Support — %s" % STUDIO, "Yasal ve Destek — %s" % STUDIO,
               "Privacy policy, terms of use and support links for every game by Serhat Bilal Studio.", "/legal/")
    out += body_open(nav_active="legal")
    cards = ""
    for g in GAMES:
        rows = ""
        for kind, lbl in (("privacy", bi("Privacy Policy", "Gizlilik Politikası")), ("terms", bi("Terms of Use", "Kullanım Şartları")), ("support", bi("Support URL", "Destek URL'si"))):
            u = full(url(g["slug"], kind))
            rows += '<div class="url-row"><div class="lbl"><span>%s</span><a href="%s">%s ↗</a></div><div class="url-box"><code>%s</code><button class="copy" type="button" data-copy="%s" aria-label="Copy">%s</button></div></div>' % (
                lbl, url(g["slug"], kind), bi("Open", "Aç"), u, u, bi("Copy", "Kopyala"))
        cards += '<div class="hub-card rv" style="--a1:%s;--a2:%s"><header><img src="%s" alt="" width="52" height="52"><div><strong>%s</strong><span>%s</span></div></header>%s</div>' % (
            g["accent"][0], g["accent"][1], icon(g["slug"]), gname(g), bi(g["status_en"], g["status_tr"]), rows)
    out += """<section class="doc-head"><div class="container">
  <nav class="crumbs"><a href="/">%s</a><span class="sep">/</span><span>%s</span></nav>
  <span class="eyebrow">%s</span>
  <h1 style="font-size:clamp(2rem,5vw,3.6rem);font-weight:800;letter-spacing:-0.04em">%s</h1>
  <p style="margin-top:14px;color:var(--muted);max-width:640px">%s</p>
</div></section>
<section class="container" style="padding-bottom:90px"><div class="hub">%s</div></section>
""" % (bi("Home", "Ana sayfa"), bi("Legal &amp; Support", "Yasal ve Destek"), bi("Legal hub", "Yasal merkez"),
       bi("One link per document, per game.", "Her oyun için, her belge için ayrı link."),
       bi("Paste these URLs into App Store Connect (Privacy Policy URL, Support URL) and Google Play Console. Every page is available in English and Turkish with the language switch.",
          "Bu URL'leri App Store Connect (Gizlilik Politikası URL'si, Destek URL'si) ve Google Play Console'a yapıştır. Her sayfa dil değiştirici ile İngilizce ve Türkçe olarak mevcuttur."),
       cards)
    out += footer()
    write("legal/index.html", out)


def not_found():
    out = head("Page not found — %s" % STUDIO, "Sayfa bulunamadı — %s" % STUDIO, "Page not found.", "/404.html")
    out += body_open()
    out += '<section class="container center-page"><div><h1 class="grad">404</h1><p>%s</p><a class="btn primary" href="/">%s</a></div></section>' % (
        bi("This page wandered off into the dark. Let's get you back.", "Bu sayfa karanlığa karıştı. Seni geri götürelim."), bi("Back to home", "Ana sayfaya dön"))
    out += footer()
    write("404.html", out)


REDIRECT_MAP = '{"the-flipside-run":"the-flipside","the-flipside":"the-flipside","flipside":"the-flipside","merge-survivors":"merge-survivors","merge-survivors-dark-dungeon":"merge-survivors","tiny-mage":"tiny-mage","tinymage":"tiny-mage"}'


def redirect_page(rel, page, fallback):
    """Old URLs (privacy.html?app=the-flipside-run, support.html, apps.html) keep working."""
    target_default = fallback
    out = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Redirecting… — %(studio)s</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="2;url=%(fb)s">
<link rel="canonical" href="%(canon)s">
<link rel="stylesheet" href="/assets/style.css">
<script>
(function(){
  var map=%(map)s, p=new URLSearchParams(location.search), app=map[(p.get('app')||'').toLowerCase()];
  var page=%(page)s, dest;
  if(page==='apps'){dest='/#games'}
  else{dest='/games/'+(app||'the-flipside')+'/'+page+'/'}
  var l=p.get('lang'); if(l==='en'||l==='tr'){dest+=(dest.indexOf('?')<0?'?':'&')+'lang='+l}
  location.replace(dest);
})();
</script>
</head>
<body>
<main class="container center-page"><div class="redirect-card">
<h1>This page has moved</h1>
<p>Policies, terms and support now have their own page for every game.</p>
%(links)s
</div></main>
</body>
</html>
""" % dict(studio=STUDIO, fb=target_default, canon=full(target_default), map=REDIRECT_MAP, page='"%s"' % page,
           links="".join('<a class="btn ghost sm" href="%s">%s</a>' % (url(g["slug"], page if page != "apps" else None), esc(g["name"])) for g in GAMES)
           if page != "apps" else '<a class="btn primary" href="/#games">Games</a>')
    write(rel, out)


def sitemap():
    urls = ["/", "/legal/"]
    for g in GAMES:
        urls += [url(g["slug"]), url(g["slug"], "privacy"), url(g["slug"], "terms"), url(g["slug"], "support")]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    x += "".join("  <url><loc>%s</loc></url>\n" % full(u) for u in urls)
    x += "</urlset>\n"
    write("sitemap.xml", x)
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)


def favicon():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#ff7a3d"/></linearGradient></defs><rect width="64" height="64" rx="18" fill="url(#g)"/><text x="32" y="42" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="800" font-size="27" fill="#fff">SB</text></svg>"""
    write("assets/img/favicon.svg", svg)


def main():
    favicon()
    home()
    legal_hub()
    not_found()
    for g in GAMES:
        game_page(g)
        legal_doc(g, "privacy")
        legal_doc(g, "terms")
        support_page(g)
    redirect_page("privacy.html", "privacy", "/games/the-flipside/privacy/")
    redirect_page("support.html", "support", "/games/the-flipside/support/")
    redirect_page("apps.html", "apps", "/#games")
    sitemap()
    print("built %d games" % len(GAMES))


if __name__ == "__main__":
    main()
