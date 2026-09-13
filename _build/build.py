#!/usr/bin/env python3
"""Genera las paginas del sitio a partir de los parciales de _build/parts.
Uso:  python3 _build/build.py     (desde la carpeta new/)
Cambiar el header, el footer o el <head> aca y regenerar mantiene las 9 paginas
sincronizadas sin tener que editarlas una por una."""
import os, re, datetime

SITE = "https://ernestoocampo.github.io/ROCKEAR_TV/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, "_build", "parts")

def part(name):
    with open(os.path.join(PARTS, name + ".html"), encoding="utf-8") as f:
        return f.read()

# ---------------------------------------------------------------- navegacion
NAV = [
    ("el-medio/",  "El medio"),
    ("agenda/",    "Agenda"),
    ("produce/",   "Produce"),
    ("ernesto/",   "El creador"),
    ("libro/",     "Libro"),
    ("contacto/",  "Contacto"),
]
FOOT_SECC = [("el-medio/","El medio"),("agenda/","Agenda"),("produce/","Rockeart.produce"),
             ("ernesto/","El creador"),("libro/","El libro"),("sponsors/","Sponsors")]
REDES = [("https://youtube.com/@rockear_tv","YouTube"),
         ("https://www.tiktok.com/@rockear_tv","TikTok"),
         ("https://www.instagram.com/rockear_tv/","Instagram"),
         ("https://www.facebook.com/ernesto.ocampo.52","Facebook"),
         ("https://www.instagram.com/rockeart.produce/","Rockeart.produce")]

def head(page):
    b = page["base"]
    extra = page.get("schema", "")
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{page["title"]}</title>
<meta name="description" content="{page["desc"]}">
<meta name="author" content="Ernesto Daniel Ocampo">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#050505">
<link rel="canonical" href="{SITE}{page["url"]}">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["desc"]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:url" content="{SITE}{page["url"]}">
<meta property="og:image" content="{SITE}assets/og-rockear-tv.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23050505'/><path d='M56 12 L30 56 H46 L40 90 L70 44 H54 Z' fill='%23e0201b'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Special+Elite&display=swap" rel="stylesheet">
<script>document.documentElement.className+=" js"</script>
<link rel="stylesheet" href="{b}assets/css/main.css">
{extra}</head>
<body>
<div id="bar"></div>
<div id="glow" aria-hidden="true"></div>
<div class="page-frame" aria-hidden="true">
  <i class="c tl"></i><i class="c tr"></i><i class="c bl"></i><i class="c br"></i>
  <i class="ex et"></i><i class="ex eb"></i><i class="ey el"></i><i class="ey er"></i>
</div>
'''

def header(page):
    b = page["base"]
    def link(u, t):
        act = ' class="act"' if page["url"] == u else ''
        return '<a href="%s%s"%s>%s</a>' % (b, u, act, t)
    links = "\n      ".join(link(u, t) for u, t in NAV)
    return f'''<header id="hdr">
  <div class="wrap bar">
    <a class="brand" href="{b}" aria-label="ROCKEAR TV — inicio">
      <img src="{b}assets/logo-rockear-tv-sm.webp" alt="ROCKEAR TV" width="420" height="135">
      <i>Rockeart.produce</i>
    </a>
    <nav class="main" id="nav">
      {links}
    </nav>
    <div style="display:flex;gap:12px;align-items:center">
      <a class="live" href="https://youtube.com/@rockear_tv" target="_blank" rel="noopener"><i class="d"></i>YouTube</a>
      <button class="burger" id="burger" aria-label="Menú" aria-expanded="false" aria-controls="nav">
        <span></span><span></span><span></span></button>
    </div>
  </div>
</header>
'''

def footer(page):
    b = page["base"]
    secc = "\n        ".join(f'<a class="fl" href="{b}{u}">{t}</a>' for u, t in FOOT_SECC)
    redes = "\n        ".join(f'<a class="fl" href="{u}" target="_blank" rel="noopener">{t}</a>' for u, t in REDES)
    return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img class="fwordmark" src="{b}assets/logo-rockear-tv.webp" alt="ROCKEAR TV" width="1200" height="385" loading="lazy">
        <p>Rock, entrevistas, música y comunicación. Creado por Ernesto Daniel Ocampo · Producido por Rockeart.produce.</p>
      </div>
      <div>
        <h4>Secciones</h4>
        {secc}
      </div>
      <div>
        <h4>Redes</h4>
        {redes}
      </div>
      <div>
        <h4>Contacto</h4>
        <a class="fl" href="mailto:rockeart.produce@gmail.com">rockeart.produce@gmail.com</a>
        <a class="fl" href="https://wa.me/5491173681292" target="_blank" rel="noopener">WhatsApp +54 9 11 7368-1292</a>
        <a class="fl" href="{b}legal/">Aviso legal</a>
      </div>
    </div>
  </div>
  <div class="copy"><div class="wrap" style="display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;width:100%">
    <span>© <span id="year">{datetime.date.today().year}</span> Ernesto Daniel Ocampo · Rockeart.produce</span>
    <span>Todos los derechos reservados</span>
  </div></div>
</footer>

<button id="top" aria-label="Volver arriba">↑</button>
<script src="{b}assets/js/main.js"></script>
</body>
</html>
'''

def pagehead(page):
    """Encabezado de pagina interior (las que no son la home)."""
    lead = f'<p class="lead rv d1">{page["lead"]}</p>' if page.get("lead") else ""
    return f'''<section class="pagehead">
  <div class="wrap">
    <div class="head">
      <div>
        <h1 class="line"><span>{page["h1"]}</span></h1>
        {lead}
      </div>
    </div>
  </div>
</section>
'''

def build(page):
    out = head(page) + header(page) + "<main>\n"
    if not page.get("home"):
        out += pagehead(page)
    out += page["body"](page["base"]) + "\n</main>\n" + footer(page)
    path = os.path.join(ROOT, page["url"], "index.html") if page["url"] else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    return path, len(out)

# -------------------------------------------------------------------- schema
def ld(obj):
    import json
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False) + '\n</script>\n'

PERSONA = {"@type":"Person","@id":SITE+"#persona","name":"Ernesto Daniel Ocampo",
  "description":"Manager, productor y referente del rock independiente argentino. Creador de ROCKEAR TV y fundador de Rockeart.produce.",
  "jobTitle":"Manager y productor","image":SITE+"assets/ernesto-ocampo.webp","url":SITE+"ernesto/",
  "sameAs":["https://www.instagram.com/ernesto.d.ocampo/","https://www.facebook.com/ernesto.ocampo.52"]}
ORG = {"@type":"Organization","@id":SITE+"#org","name":"ROCKEAR TV",
  "description":"Canal de rock en español: entrevistas reales, sesiones en vivo y coberturas sin filtro. Desde Argentina al mundo.",
  "url":SITE,"logo":SITE+"assets/logo-rockear-tv.webp","founder":{"@id":SITE+"#persona"},
  "email":"rockeart.produce@gmail.com",
  "sameAs":["https://youtube.com/@rockear_tv","https://www.tiktok.com/@rockear_tv",
            "https://www.instagram.com/rockear_tv/","https://www.facebook.com/ernesto.ocampo.52",
            "https://www.instagram.com/rockeart.produce/"]}
PRODUCE = {"@type":"Organization","name":"Rockeart.produce",
  "description":"Productora creada por Ernesto Daniel Ocampo, responsable de producir ROCKEAR TV.",
  "founder":{"@id":SITE+"#persona"},"sameAs":["https://www.instagram.com/rockeart.produce/"]}
EVENTO = {"@type":"Event","name":"Los Gladiolos RNR en Carnal","startDate":"2026-09-25T22:00-03:00",
  "eventStatus":"https://schema.org/EventScheduled",
  "eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode",
  "location":{"@type":"Place","name":"Carnal","address":{"@type":"PostalAddress",
     "streetAddress":"Niceto Vega 5511","addressLocality":"Buenos Aires","addressCountry":"AR"}},
  "performer":{"@type":"MusicGroup","name":"Los Gladiolos RNR","sameAs":"https://www.instagram.com/losgladiolosok"},
  "organizer":{"@id":SITE+"#org"},
  "image":SITE+"assets/eventos/gladiolos-25sep.webp",
  "offers":{"@type":"Offer","price":"0","priceCurrency":"ARS","availability":"https://schema.org/InStock",
            "description":"Entrada sin cargo hasta las 23 hs","url":SITE+"agenda/"}}

def graph(*items):
    return ld({"@context":"https://schema.org","@graph":list(items)})

def breadcrumb(url, name):
    return {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Inicio","item":SITE},
      {"@type":"ListItem","position":2,"name":name,"item":SITE+url}]}

# ------------------------------------------------------------------- helpers
def clean(name, base, drop_head=True):
    """Toma un parcial, le saca el encabezado de seccion y arregla las rutas."""
    html = part(name)
    if drop_head:
        html = re.sub(r'<div class="head">.*?</div>\n    </div>\n', '', html, count=1, flags=re.S)
        html = re.sub(r'<div class="head">.*?\n    </div>\n', '', html, count=1, flags=re.S)
    html = html.replace('src="assets/', f'src="{base}assets/')
    html = html.replace('href="#contacto"', f'href="{base}contacto/"')
    html = html.replace('href="#medios"', f'href="{base}el-medio/"')
    html = re.sub(r'^\s*<div class="wrap">\n', '', html)
    html = re.sub(r'\n\s*</div>\s*$', '', html)
    return html

def sec(inner, extra=""):
    return f'<section{extra}>\n  <div class="wrap">\n{inner}\n  </div>\n</section>\n'

# --------------------------------------------------------------------- home
def home_body(b):
    hero = part("inicio").replace('src="assets/', f'src="{b}assets/')
    hero = hero.replace('href="#medios"', f'href="{b}el-medio/"')
    hero = f'<section id="inicio" class="hero">\n{hero}\n</section>\n'  
    ticker = '''<div class="ticker" aria-hidden="true">
  <div class="ticker-t">
    <b>Entrevistas reales</b><b>Sesiones en vivo</b><b>Coberturas sin filtro</b><b>Rock en español</b><b>Desde Argentina al mundo</b>
    <b>Entrevistas reales</b><b>Sesiones en vivo</b><b>Coberturas sin filtro</b><b>Rock en español</b><b>Desde Argentina al mundo</b>
  </div>
</div>
'''
    mapa = f'''    <div class="head">
      <div>
        <h2 class="line"><span>El canal del <em>rock en español</em></span></h2>
        <p class="lead rv d1">Entrevistas reales, sesiones en vivo y coberturas sin filtro. Creado por Ernesto Ocampo y producido por <strong>Rockeart.produce</strong>.</p>
      </div>
    </div>
    <div class="bento rv d1">
      <a class="cel big" href="{b}el-medio/"><span class="k">El medio</span><h3>Qué es ROCKEAR TV</h3>
        <p>Entrevistas, sesiones en vivo y coberturas. La escena contada por los que la hacen.</p></a>
      <a class="cel" href="{b}agenda/"><span class="k">Agenda</span><h3>Próximas fechas</h3>
        <p>Dónde estamos filmando y cubriendo.</p></a>
      <a class="cel" href="{b}produce/"><span class="k">Productora</span><h3>Rockeart<br>.produce</h3>
        <p>La estructura que produce el canal.</p></a>
      <a class="cel big" href="{b}ernesto/"><span class="k">El creador</span><h3>Ernesto Daniel Ocampo</h3>
        <p>Manager, productor y referente del rock independiente argentino.</p></a>
    </div>
'''
    gig = re.search(r'(<div class="gig rv">.*?</div>\n    </div>)', part("fechas"), re.S).group(1)
    gig = gig.replace('src="assets/', f'src="{b}assets/')
    agenda = f'''    <div class="head">
      <div>
        <h2 class="line"><span>Próxima <em>fecha</em></span></h2>
      </div>
    </div>
{gig}
    <div class="notice rv d2" style="margin-top:34px">
      <a class="btn" href="{b}agenda/"><span>Ver toda la agenda</span></a>
    </div>
'''
    redes = clean("medios", b)
    redes = f'''    <div class="head">
      <div>
        <h2 class="line"><span>Nuestros <span class="out">medios</span></span></h2>
        <p class="lead rv d1">Todos los canales oficiales de ROCKEAR TV, reunidos en un solo lugar.</p>
      </div>
    </div>
{redes}'''
    sp = clean("sponsors", b)
    sp = sp.replace('<p class="sp-note rv d2">¿Querés acompañar a ROCKEAR TV? Escribinos.</p>',
                    f'<p class="sp-note rv d2"><a href="{b}sponsors/">Conocé a las marcas que nos acompañan →</a></p>')
    sponsors = f'''    <div class="head">
      <div>
        <h2 class="line"><span>Nos <em>acompañan</em></span></h2>
        <p class="lead rv d1">Las marcas que hacen posible que ROCKEAR TV siga saliendo al aire.</p>
      </div>
    </div>
{sp}'''
    cta = f'''    <div class="contact rv">
      <h2>¿Tenés una historia <em>para contar?</em></h2>
      <p class="lead">Si sos artista, banda o productor y querés ser parte de la escena, escribinos.</p>
      <div class="cta" style="margin-top:34px"><a class="btn red" href="{b}contacto/"><span>Contacto</span></a></div>
    </div>
'''
    return hero + ticker + sec(mapa) + sec(agenda) + sec(redes) + sec(sponsors) + sec(cta)

PAGES = [
  dict(url="", home=True, base="", title="ROCKEAR TV | El canal del rock en español",
       desc="ROCKEAR TV: el canal que muestra la verdadera cara del rock en español. Entrevistas reales, sesiones en vivo y coberturas sin filtro. Creado por Ernesto Ocampo, producido por Rockeart.produce.",
       schema=graph(ORG, PERSONA, PRODUCE, EVENTO,
                    {"@type":"WebSite","name":"ROCKEAR TV","url":SITE,"publisher":{"@id":SITE+"#org"}}),
       body=home_body),
  dict(url="el-medio/", base="../", num="01", h1="Rockear <em>TV</em>", schema=graph(ORG, breadcrumb("el-medio/","El medio")),
       title="El medio | ROCKEAR TV",
       desc="Qué es ROCKEAR TV: entrevistas reales, sesiones en vivo y coberturas sin filtro del rock en español.",
       lead="El canal de YouTube que te muestra <strong>la verdadera cara del rock en español</strong>. Creado por Ernesto Ocampo y producido por <strong>Rockeart.produce</strong>.",
       body=lambda b: sec(clean("medio", b)) + sec(f'''    <div class="head">
      <div><h2 class="line"><span>Nuestros <span class="out">medios</span></span></h2>
        <p class="lead rv d1">Todos los canales oficiales, reunidos en un solo lugar.</p></div>
    </div>
{clean("medios", b)}''')),
  dict(url="agenda/", base="../", num="02", h1="Próximas <em>fechas</em>", schema=graph(EVENTO, breadcrumb("agenda/","Agenda")),
       title="Agenda | ROCKEAR TV",
       desc="Próximas fechas de ROCKEAR TV y Rockeart.produce: shows, coberturas y producciones en vivo.",
       lead="Dónde estamos filmando, cubriendo y produciendo. Las fechas se anuncian acá y en nuestras redes.",
       body=lambda b: sec(clean("fechas", b))),
  dict(url="produce/", base="../", num="03", h1="Rockeart<em>.produce</em>", schema=graph(PRODUCE, breadcrumb("produce/","Rockeart.produce")),
       title="Rockeart.produce | ROCKEAR TV",
       desc="La productora desde la que se crea y produce ROCKEAR TV, y desde donde nacen nuevos eventos y producciones.",
       lead="La productora desde la que se crea y produce ROCKEAR TV, y desde donde nacen nuevos eventos y producciones.",
       body=lambda b: sec(clean("produce", b))),
  dict(url="ernesto/", base="../", num="04", h1="El <span class=\"out\">creador</span>", schema=graph(PERSONA, breadcrumb("ernesto/","El creador")),
       title="Ernesto Daniel Ocampo | ROCKEAR TV",
       desc="Ernesto Ocampo: manager, productor y referente del rock independiente argentino. Creador de ROCKEAR TV y fundador de Rockeart.produce.",
       body=lambda b: sec(clean("creador", b))),
  dict(url="libro/", base="../", num="05", h1="La música, <em>mi religión</em>",
       schema=graph({"@type":"Book","name":"La música, mi religión","author":{"@id":SITE+"#persona"},"genre":"Autobiografía","inLanguage":"es"}, breadcrumb("libro/","El libro")),
       title="La música, mi religión | ROCKEAR TV",
       desc="Obra autobiográfica de Ernesto Daniel Ocampo: un relato personal escrito desde la memoria y la pasión por la música.",
       body=lambda b: sec(clean("libro", b))),
  dict(url="sponsors/", base="../", num="06", h1="Nos <em>acompañan</em>", schema=graph(breadcrumb("sponsors/","Sponsors")),
       title="Sponsors | ROCKEAR TV",
       desc="Las marcas que hacen posible que ROCKEAR TV siga saliendo al aire.",
       lead="Las marcas que hacen posible que ROCKEAR TV siga saliendo al aire.",
       body=lambda b: sec(clean("sponsors", b))),
  dict(url="contacto/", base="../", num="07", h1="Contacto",
       schema=graph({"@type":"ContactPage","name":"Contacto — ROCKEAR TV","url":SITE+"contacto/"}, breadcrumb("contacto/","Contacto")),
       title="Contacto | ROCKEAR TV",
       desc="Entrevistas, sesiones en vivo, coberturas y producciones. Escribinos a ROCKEAR TV.",
       body=lambda b: sec(clean("contacto", b, drop_head=False))),
  dict(url="legal/", base="../", num="08", h1="Aviso legal", schema=graph(breadcrumb("legal/","Aviso legal")),
       title="Aviso legal | ROCKEAR TV",
       desc="Propiedad intelectual, uso no autorizado y control administrativo del sitio de ROCKEAR TV.",
       body=lambda b: sec(clean("legal", b))),
]

if __name__ == "__main__":
    for p in PAGES:
        path, n = build(p)
        print("%6.1f KB  %s" % (n/1024, os.path.relpath(path, ROOT)))
