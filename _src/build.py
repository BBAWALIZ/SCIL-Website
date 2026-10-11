"""Generates the static SCIL Machinery site into the project root.

    python _src/build.py

The output is plain HTML; no build step is needed to host it. Edit data.py
(content) or parts.py (shared header/footer) and re-run to regenerate.
"""
import os, re, sys
from html import escape as e

sys.path.insert(0, os.path.dirname(__file__))
import data as D
from parts import head, gantry, footer, icon, token, mcard, machine_img, enquiry_form

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BY_ID = {m[0]: m for m in D.MACHINES}
ALL_STATIONS = D.STATIONS + [D.WATER]
ST = {s["key"]: s for s in ALL_STATIONS}


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def machines_in(key):
    return [m for m in D.MACHINES if m[2] == key]


# --------------------------------------------------------------------------- home
HERO_PICK = {"blowing": 34, "filling": 33, "labeling": 39, "packaging": 20, "palletizing": 18}
HERO_FIG = {"injection": "Preforms", "blowing": "to 22,000 BPH", "filling": "to 36,000 BPH",
            "labeling": "3 label types", "packaging": "Shrink · case", "palletizing": "15 packs/min"}
WALK_PICK = {"blowing": [34, 48, 42], "filling": [33, 21, 13], "labeling": [39, 40, 16],
             "packaging": [20, 19, 22], "palletizing": [18, 47]}


def home():
    fps = []
    for i, s in enumerate(D.STATIONS):
        if s["key"] in HERO_PICK:
            img = f'<img class="photo-mult" src="assets/img/products/{machine_img(HERO_PICK[s["key"]])}" alt="" width="850" height="690">'
        else:
            img = token("preform")
        fps.append(f"""<a class="station-fp footprint" style="--i:{i}" href="#st-{s['key']}">
      <div class="plate">
        <div class="station-fp__no"><span class="stencil">{s['no']}</span></div>
        <div class="station-fp__img">{img}</div>
        <h2>{e(s['name'])}</h2>
        <p>{e(s['short'])}</p>
        <span class="mcard__fig">{e(HERO_FIG[s['key']])}</span>
      </div>
    </a>""")

    stations = []
    for s in D.STATIONS:
        picks = WALK_PICK.get(s["key"], [])
        if picks:
            cards = '<div class="machines">' + "".join(mcard(BY_ID[i]) for i in picks) + "</div>"
            more = f'<p class="station__more"><a class="link-arrow" href="equipment.html#{s["key"]}">All {len(machines_in(s["key"]))} {e(s["name"].lower())} machines {icon("arrow")}</a></p>'
        else:
            cards = f"""<div class="empty-bay" style="margin-top:28px">{token("preform")}
        <p><strong>Injection machines are specified per project.</strong> Send us your preform weight, neck finish and output, and we will propose the machine and moulds.</p></div>"""
            more = f'<p class="station__more"><a class="link-arrow" href="contact.html">Ask about preform injection {icon("arrow")}</a></p>'
        water = ""
        if s["key"] == "filling":
            water = f'<p class="meta" style="margin-top:18px">Fed by <a href="equipment/water-treatment-equipment.html">00 Water treatment</a>: filtration, RO, ozone and UV.</p>'
        stations.append(f"""<article class="station" id="st-{s['key']}" data-station="{s['no']}" data-token="{s['token']}" data-out="{e(s['out'])}">
      <div class="station__head"><span class="station__no stencil" aria-hidden="true">{s['no']}</span><h3 class="sign-m"><span class="visually-hidden">Station {s['no']}: </span>{e(s['name'])}</h3></div>
      <div class="station__body"><p class="prose">{e(s['text'])}</p>{token(s['token'], 'station__token-inline', 'Leaves as: ' + s['out'])}</div>
      {cards}{water}
      {more}
    </article>""")

    ticks = "".join(f'<li style="top:{(i + 0.5) / 6 * 100:.2f}%" data-tick="{s["no"]}">{s["no"]}</li>' for i, s in enumerate(D.STATIONS))
    tstates = "".join(f'<div class="token__state{" is-on" if i == 0 else ""}" data-state="{s["token"]}">{token(s["token"])}</div>' for i, s in enumerate(D.STATIONS))

    tags = "".join(f"""<article class="tag">
      <div class="tag__band" aria-hidden="true"></div>
      <blockquote><p>“{e(t['short'])}”</p>
        <details><summary>Full words {icon('arrow')}</summary>{''.join(f'<p>{e(p)}</p>' for p in t['full'])}</details>
      </blockquote>
      <footer><b>{e(t['org'])}</b>{e(t['name'])}, {e(t['role'])}</footer>
    </article>""" for t in D.TESTIMONIALS if t["org"] not in ("Safira", "Najd Water"))

    logos = "".join(f'<li><img src="assets/img/clients/{f}" alt="" loading="lazy"></li>' for f in sorted(os.listdir(os.path.join(ROOT, "assets/img/clients"))))

    solo_pick = [D.SOLO[0], D.SOLO[7], D.SOLO[4]]
    solos = "".join(f"""<a class="pricecard footprint" href="solo.html">
      <div class="plate">
        <div class="pricecard__img"><img class="photo-mult" src="assets/img/products/{img}" alt="" loading="lazy" width="409" height="334"></div>
        <h3>{e(name)}</h3>
        <p>{e(desc)}</p>
        <div class="price">{''.join(f'<span><small>{e(k)}</small><b>{e(v)}</b></span>' for k, v in prices[:2])}</div>
      </div></a>""" for img, name, desc, prices, _ in solo_pick)

    html = head("SCIL Machinery · Complete bottling lines, preform to pallet",
                "SCIL Machinery designs and builds complete beverage packaging lines in Suzhou: preform injection, PET blowing, filling, labeling, packaging and palletizing for water, soft drinks, juice, edible oil and homecare.", alt="ar/index.html")
    html += gantry("index.html", alt="ar/index.html")
    html += f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <div class="hero__head">
      <h1 class="hero__title" id="hero-title"><span class="sign-xl">Preform to pallet. <em>One supplier.</em></span></h1>
      <div class="hero__aside">
        <p class="lede">Complete bottling lines for water, soft drinks, juice, edible oil and homecare, installed and serviced by our own engineers.</p>
        <div class="hero__ctas">
          <a class="btn" href="#enquire">Plan my line {icon('arrow')}</a>
          <a class="btn btn--plate" href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} WhatsApp an engineer</a>
        </div>
      </div>
    </div>
  </div>
  <div class="plan">
    <div class="wrap plan__scroller" tabindex="0" aria-label="The six stations of a SCIL line">
      <div class="plan__track">
        <span class="lane" aria-hidden="true"></span><span class="lane lane--edge" aria-hidden="true"></span><span class="lane-chevrons" aria-hidden="true"></span>
        {''.join(fps)}
        <div class="fg-zone">
          <svg viewBox="0 0 64 56" aria-hidden="true"><use href="#tk-pallet-mini"/></svg>
          <span class="sign-s">Finished goods</span>
          <p>Shrink-wrapped, palletized, ready for your trucks.</p>
        </div>
      </div>
    </div>
    <p class="wrap plan__hint">{icon('arrow')} Swipe along the line</p>
  </div>
</section>

<section class="section section--tight" aria-label="SCIL in figures">
  <div class="wrap">
    <div class="legend">
      <p class="legend__text">Since <span class="stencil">2003</span> we have shipped <span class="stencil">5,200</span> machines to <span class="stencil">840+</span> clients. Their lines have filled more than <span class="stencil">230</span> billion containers.</p>
    </div>
    <p class="legend__foot meta">Figures as published by SCIL Machinery.</p>
  </div>
</section>

<section class="section" id="line" aria-labelledby="line-title" style="padding-top:clamp(40px,5vw,72px)">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="line-title">Walk the line, station by station</h2>
      <p class="lede">Every line follows the container. Here is what each SCIL station does to it, and the machines that do the work.</p>
    </div>
    <div class="walk" data-walk>
      <div class="walk__strip" aria-hidden="true"><svg viewBox="0 0 300 400"><use data-strip-use href="#tk-preform"/></svg><strong data-strip-out>01 · {e(D.STATIONS[0]['out'])}</strong><div class="walk__strip-lane"><span></span></div></div>
      <div class="walk__rail">
        <div class="walk__sticky">
          <div class="walk__lane" aria-hidden="true"><span class="walk__lane-fill" data-lane-fill></span><ol class="walk__ticks">{ticks}</ol></div>
          <div class="walk__ride"><div class="token" aria-hidden="true">
            <div class="token__stage">{tstates}</div>
            <div class="token__cap"><strong data-token-out>{e(D.STATIONS[0]['out'])}</strong><span class="meta" data-token-no>Leaves station 01</span></div>
          </div></div>
        </div>
      </div>
      <div class="stations">{''.join(stations)}</div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="proof-title" style="padding-top:0">
  <div class="wrap">
    <div class="proof">
      <div class="proof__lead"><h2 class="sign-l" id="proof-title"><span>Rated 1,400.</span><span class="go">Running 1,800.</span></h2></div>
      <figure class="proof__quote">
        <blockquote class="quote"><p>“We bought a 5 L line rated at 1,400 BPH. After the engineers finished installing it, the line started giving us 1,800 BPH.”</p></blockquote>
        <figcaption class="quote"><footer><b>Abass Hijazi</b>, CEO, Safira</footer></figcaption>
      </figure>
      <div class="gauge" data-gauge role="img" aria-label="Safira 5 litre line: rated 1,400 bottles per hour, running 1,800 bottles per hour">
        <div class="gauge__row"><span class="gauge__lab">Rated, on contract</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--rated" style="--w:{1400 / 2000 * 100:.1f}%">1,400</div></div></div>
        <div class="gauge__row"><span class="gauge__lab">Running, after start-up</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--run" style="--w:{1800 / 2000 * 100:.1f}%">1,800</div></div></div>
        <div class="gauge__scale"><span></span><div class="gauge__ticks"><span>0</span><span>500</span><span>1,000</span><span>1,500</span><span>2,000 BPH</span></div></div>
      </div>
    </div>

    <div class="returns">
      <div class="returns__txt">
        <h3 class="sign-m">Clients come back for the next line</h3>
        <p class="prose" style="margin-top:14px">Najd Water started with one blowing machine. Four years later they ordered the whole line.</p>
      </div>
      <div class="returns__path">
        <div class="ret-step"><span class="ret-step__yr">2014</span><span class="stencil">12,000 BPH</span><p>First contract: a blowing machine.</p></div>
        <div class="ret-step"><span class="ret-step__yr">Sep 2018</span><span class="stencil">24,000 BPH</span><p>A fully automatic water production line. “Thanks, SCIL family, for always being by our side.”</p></div>
      </div>
    </div>

    <div class="tags">
      <div class="sec-head" style="margin-bottom:24px">
        <h3 class="sign-m">In their own words</h3>
        <div class="tags__ctrl" style="justify-self:end"><button type="button" data-tags="-1" aria-label="Previous">{icon('arrow-l')}</button><button type="button" data-tags="1" aria-label="Next">{icon('arrow')}</button></div>
      </div>
      <div class="tags__row" data-tags-row tabindex="0" aria-label="Client testimonials">{tags}</div>
    </div>
  </div>
</section>

<section class="section asphalt" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="svc-title">We stay after the start-up</h2>
      <p class="lede">Clients choose SCIL for what happens once the machines arrive. The service lane runs for the life of your line.</p>
    </div>
    <ol class="loop" style="padding:0;list-style:none">
      <li class="loop__step"><span class="chip">1</span><h3>Installation</h3><p>Our engineers install and commission the line in your plant.</p></li>
      <li class="loop__step"><span class="chip">2</span><h3>Ramp-up</h3><p>We run the line up to its rated output, and train your operators on it.</p></li>
      <li class="loop__step"><span class="chip">3</span><h3>Efficiency audit</h3><p>A periodic health check of single machines or the whole line, with an action plan and ROI estimate.</p></li>
      <li class="loop__step"><span class="chip">4</span><h3>Overhaul</h3><p>Worn parts and assemblies replaced on site, so the line runs as on day one.</p></li>
      <li class="loop__step loop__step--stop"><span class="chip">!</span><h3>Breakdown</h3><p>When a line stops, our service team helps you find the cause and get it running.</p></li>
    </ol>
    <div class="bays">
      <div class="bay"><div><h3>Spare parts</h3><p>A dedicated spare-parts department, precision-made parts checked before delivery, transparent cost and availability.</p><a class="link-arrow" href="services.html#spare-parts">Spare parts {icon('arrow')}</a></div><img src="assets/img/products/svc1.jpg" alt="" loading="lazy"></div>
      <div class="bay"><div><h3>Training</h3><p>On-site courses so your team knows the whole line: performance, quality, and lower resource use.</p><a class="link-arrow" href="services.html#training">Training courses {icon('arrow')}</a></div><img src="assets/img/products/svc3.jpg" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="clients-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="clients-title">840+ clients. Some of their marks.</h2>
      <p class="lede">Water, soft-drink, juice and oil producers who run SCIL machines today.</p>
    </div>
    <ul class="dock" aria-label="Client logos">{logos}</ul>
  </div>
</section>

<section class="section" aria-labelledby="solo-title" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="solo-title">Starting your first plant? SOLO</h2>
      <p class="lede">SOLO is SCIL's start-up range: single machines with fixed, published prices and no intermediary.</p>
    </div>
    <div class="solo-row">{solos}</div>
    <p class="fineprint">USD unit prices as listed on SCIL SOLO. Confirm the current price and delivery terms with our sales team.</p>
    <p style="margin-top:24px"><a class="link-arrow" href="solo.html">See all 17 SOLO machines {icon('arrow')}</a></p>
  </div>
</section>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt">
      <h2 class="sign-l" id="enq-title">Tell us what you bottle. We'll draw the line.</h2>
      <p class="lede" style="margin-top:20px">Product, container and output are enough to start. An engineer replies with a proposed line layout and machine list.</p>
      <div class="zone__direct">
        <a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} WhatsApp <span class="data">{D.WHATSAPP_DISPLAY}</span></a>
        <a href="{D.PHONE_HREF}">{icon('phone')} Call Suzhou <span class="data">{D.PHONE}</span></a>
        <a href="mailto:{D.EMAIL}">{icon('mail')} Email <span class="data">{D.EMAIL}</span></a>
        <a href="{D.CATALOGUE}" rel="noopener">{icon('download')} Catalogue <span class="data">PDF</span></a>
      </div>
    </div>
    <div class="zone__form">{enquiry_form()}</div>
  </div>
</section>
"""
    html += footer(alt="ar/index.html")
    write("index.html", html)


# ---------------------------------------------------------------------- catalogue
def equipment():
    order = [D.WATER] + D.STATIONS
    sel = "".join(f'<a href="#{s["key"]}" data-sel="{s["key"]}"><span class="stencil">{s["no"]}</span>{e(s["name"])} <span class="data">{len(machines_in(s["key"]))}</span></a>' for s in D.STATIONS)
    sel += f'<a href="#water-treatment" data-sel="water-treatment"><span class="stencil">00</span>Water treatment <span class="data">1</span></a>'
    blocks = []
    for s in D.STATIONS + [D.WATER]:
        ms = machines_in(s["key"])
        if ms:
            grid = '<div class="cat-grid">' + "".join(mcard(m, heading="h3") for m in ms) + "</div>"
        else:
            grid = f"""<div class="empty-bay">{token('preform')}<p><strong>Injection machines are specified per project.</strong> Send us your preform weight, neck finish and target output and we will propose the machine and moulds. <a href="contact.html">Ask about injection</a>.</p></div>"""
        blocks.append(f"""<section class="cat-station" id="{s['key']}" data-cat="{s['key']}" aria-labelledby="h-{s['key']}">
    <div class="cat-station__head"><span class="stencil" aria-hidden="true">{s['no']}</span><h2 class="sign-l" id="h-{s['key']}">{e(s['name'])}</h2><p class="prose">{e(s['text'])} <span class="meta" style="display:block;margin-top:8px">Leaves as: {e(s['out'])}</span></p></div>
    {grid}
  </section>""")
    html = head("Equipment · SCIL Machinery", "SCIL Machinery equipment by line station: PET blowing machines, water, CSD, juice and oil fillers, labelers, shrink and case packers, palletizers and water treatment.", alt="ar/equipment.html")
    html += gantry("equipment.html", alt="ar/equipment.html")
    html += f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li>Equipment</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">Equipment, station by station</h1>
      <p class="lede">{len(D.MACHINES)} machines, arranged in the order your container meets them. Pick a station, or ask us to specify the whole line.</p>
    </div>
  </div>
</section>
<nav class="selector" aria-label="Stations"><div class="wrap selector__in" data-selector>{sel}</div></nav>
<div class="wrap">{''.join(blocks)}</div>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">Not sure which machine fits?</h2><p class="lede" style="margin-top:20px">Tell us the product, container and output. We'll match the machines and draw the line.</p>
      <div class="zone__direct"><a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} WhatsApp <span class="data">{D.WHATSAPP_DISPLAY}</span></a><a href="{D.CATALOGUE}" rel="noopener">{icon('download')} Catalogue <span class="data">PDF</span></a></div></div>
    <div class="zone__form">{enquiry_form()}</div>
  </div>
</section>
"""
    html += footer(alt="ar/equipment.html")
    write("equipment.html", html)


def body_paragraphs(mid):
    src = open(os.path.join(os.path.dirname(__file__), "machines_source.txt"), encoding="utf-8").read()
    m = re.search(rf"===== eq\\{mid}\.html\n(.*?)(?=\n===== |\Z)", src, re.S)
    if not m:
        return []
    lines = m.group(1).split("\n")
    skip = {"Equipments Categories", "Blowing", "Filling", "Labeling", "Packaging", "Palletizing & Smart Warehouse",
            "Water Treatment", "Injection", "Home", "Our Equipments", "Machine", "Description", "PRODUCT DESCRIPTION", ""}
    out, started = [], False
    for ln in lines:
        ln = ln.strip()
        if ln.startswith("[IMG"):
            started = True
            continue
        if not started or ln in skip:
            continue
        if mid == 48 and ln.startswith("设备参数"):
            break
        if mid == 34 and ln.startswith("The production capacity of the bottles"):
            break
        if mid == 42:
            break
        if mid == 45 and ln.startswith("The machine has 4 cavities"):
            break
        out.append(ln)
    # merge the HSP TS fragments and numbered "1" / "text" pairs
    merged, i = [], 0
    while i < len(out):
        ln = out[i]
        if re.fullmatch(r"\d+", ln) and i + 1 < len(out):
            merged.append(("li", out[i + 1])); i += 2; continue
        m2 = re.match(r"^\d+[\.\-]\s*(.+)$", ln)
        if m2:
            merged.append(("li", m2.group(1))); i += 1; continue
        merged.append(("p", ln)); i += 1
    if mid == 49:
        merged = [("p", " ".join(t for _, t in merged))]
    fixes = {"prefrom": "preform", " perform": " preform", "pressuer": "pressure", "The water treatment system in Toppling": "The water treatment system",
             "ling label": "long label", "Liner": "Linear", "  ": " "}
    res = []
    for kind, t in merged:
        for a, b2 in fixes.items():
            t = t.replace(a, b2)
        res.append((kind, t))
    return res


def render_body(parts):
    html, in_list = [], False
    headings = {"Key Advantages", "FEATURES", "Features", "Your advantages:", "Preform loader system", "Heating system", "Servo System Transmission",
                "Mould Clamping System", "Change moulds", "Human-machine Interface", "Easy maintenance", "Accurate Filling Control",
                "Stainless-Steel Construction", "Touch Screen Operation", "Multi-Size Compatibility", "Weighted Filling Heads", "Flexible Production Use"}
    for kind, t in parts:
        if kind == "li":
            if not in_list:
                html.append("<ul>"); in_list = True
            html.append(f"<li>{e(t)}</li>")
            continue
        if in_list:
            html.append("</ul>"); in_list = False
        if t in headings:
            html.append(f"<h3>{e(t.rstrip(':').title() if t.isupper() else t.rstrip(':'))}</h3>")
        else:
            html.append(f"<p>{e(t)}</p>")
    if in_list:
        html.append("</ul>")
    return "".join(html)


def spec_table(mid):
    s = D.SPECS.get(mid)
    if not s:
        return ""
    if "head" in s:
        th = "".join(f'<th scope="col">{e(h)}</th>' for h in s["head"])
        rows = "".join("<tr>" + f'<th scope="row">{e(r[0])}</th>' + "".join(f"<td>{e(c)}</td>" for c in r[1:]) + "</tr>" for r in s["rows"])
        return f'<table class="specs specs--series"><caption>{e(s["caption"])}</caption><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>'
    rows = "".join(f'<tr><th scope="row">{e(k)}</th><td>{e(v)}</td></tr>' for k, v in s["rows"])
    return f'<table class="specs"><caption>{e(s["caption"])}</caption><tbody>{rows}</tbody></table>'


def machine_page(m):
    mid, slug, key, name, fig, summ = m
    s = ST[key]
    b = "../"
    idx = next((i for i, x in enumerate(D.STATIONS) if x["key"] == key), -1)
    mini = "".join(
        f'<a href="{b}equipment.html#{x["key"]}" title="{e(x["name"])}" class="{"is-on" if i == idx else ("is-past" if i < idx else "")}">{x["no"]}<span> {e(x["name"])}</span></a>'
        for i, x in enumerate(D.STATIONS))
    siblings = [x for x in machines_in(key) if x[0] != mid][:4]
    sib = "".join(mcard(x, b, heading="h3") for x in siblings)
    body = render_body(body_paragraphs(mid))
    alt = f"../ar/equipment/{slug}.html"
    html = head(f"{name} · SCIL Machinery", f"{name}: {summ} {fig}.", b, alt=alt)
    html += gantry("equipment.html", b, alt=alt)
    html += f"""
<section class="page-head" style="padding-bottom:24px">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{b}index.html">Home</a></li><li><a href="{b}equipment.html">Equipment</a></li><li><a href="{b}equipment.html#{key}">{s['no']} {e(s['name'])}</a></li></ol>
  </div>
</section>
<section class="wrap" style="padding-bottom:var(--space-section)">
  <div class="mdetail">
    <div class="mdetail__media"><div class="footprint"><div class="plate"><img class="photo-mult" src="{b}assets/img/products/{machine_img(mid)}" alt="{e(name)}" width="850" height="690"></div></div></div>
    <div class="mdetail__info">
      {'<nav class="lane-mini" aria-label="Position on the line">' + mini + '</nav>' if idx >= 0 else '<p class="meta" style="margin:0 0 24px">00 Water treatment · feeds station 03 Filling</p>'}
      <h1 class="sign-l">{e(name)}</h1>
      <span class="mdetail__fig">{e(fig)}</span>
      <p class="lede">{e(summ)}</p>
      <div class="mdetail__actions">
        <a class="btn" href="{b}contact.html?machine={slug}">Request a quote {icon('arrow')}</a>
        <a class="btn btn--plate" href="https://wa.me/{D.WHATSAPP}?text={e('Hello SCIL, I am interested in the ' + name + '.').replace(' ', '%20')}" rel="noopener">{icon('chat')} WhatsApp</a>
      </div>
      <div class="body-copy prose" style="margin-top:36px">{body}</div>
      {spec_table(mid)}
      <p class="meta" style="margin-top:22px">Full technical data is in the <a href="{D.CATALOGUE}" rel="noopener">SCIL catalogue (PDF)</a> or on request.</p>
    </div>
  </div>
</section>
{f'''<section class="section" style="padding-top:0" aria-labelledby="sib"><div class="wrap"><div class="sec-head" style="margin-bottom:32px"><h2 class="sign-m" id="sib">More at station {s['no']} · {e(s['name'])}</h2></div><div class="cat-grid">{sib}</div></div></section>''' if sib else ''}
"""
    html += footer(b, alt=alt)
    write(f"equipment/{slug}.html", html)


# ----------------------------------------------------------------------- services
def services():
    html = head("Services · SCIL Machinery", "Installation, commissioning, line ramp-up, technical audits, overhauls, spare parts and operator training from SCIL Machinery.", alt="ar/services.html")
    html += gantry("services.html", alt="ar/services.html")
    html += f"""
<section class="page-head asphalt" style="padding-bottom:var(--space-section)">
  <div class="wrap">
    <ol class="crumbs" style="color:var(--on-asphalt-2)"><li><a href="index.html" style="color:var(--on-asphalt)">Home</a></li><li>Services</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl" style="color:var(--plate)">The service lane runs for the life of your line</h1>
      <p class="lede">Installation and commissioning, line ramp-up, efficiency audits and breakdown support, with spare parts and training behind them.</p>
    </div>
    <ol class="loop" style="padding:0;list-style:none;margin-top:clamp(56px,7vw,96px)">
      <li class="loop__step"><span class="chip">1</span><h2>Installation</h2><p>Line installation and commissioning in your plant.</p></li>
      <li class="loop__step"><span class="chip">2</span><h2>Ramp-up</h2><p>Running the line up to its rated output.</p></li>
      <li class="loop__step"><span class="chip">3</span><h2>Audit</h2><p>Periodic technical audit and inspection.</p></li>
      <li class="loop__step"><span class="chip">4</span><h2>Overhaul</h2><p>Worn parts replaced on site.</p></li>
      <li class="loop__step loop__step--stop"><span class="chip">!</span><h2>Breakdown</h2><p>Support when a line stops.</p></li>
    </ol>
  </div>
</section>
<div class="wrap">
  <section class="svc-block" id="service-packages" aria-labelledby="h-pk">
    <div class="svc-block__head"><h2 class="sign-l" id="h-pk">Technical audit &amp; inspection</h2><img src="assets/img/products/svc2.jpg" alt="SCIL engineers on a service visit" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>With a technical audit, SCIL gives your equipment a periodic health check and performance assessment. We analyse single machines or complete lines under production conditions, identify technical and organisational stoppers, and help you improve your packaging processes.</p>
      <p>We help you implement quick wins, tune your equipment, and put the measures from our action plan into operation. A full cost estimate lets you calculate your return on investment, and the optimisation proposals help lower overall costs and raise the efficiency of your packaging machines.</p>
      <h3 class="sign-s" style="margin-top:36px;margin-bottom:12px">Machine overhaul: just like on the first day</h3>
      <p>When a machine has clocked up long hours and starts to show its age, it is time to overhaul. A technical audit first establishes its condition and the spare parts needed. Then our technicians come to your facility, replace all worn parts and assemblies, and carry out minor repairs on site.</p>
      <ul class="checks">
        <li>{icon('check')}<span>Fast, targeted replacement of all worn parts and assemblies</span></li>
        <li>{icon('check')}<span>Inspections and overhauls planned and carried out by one supplier</span></li>
        <li>{icon('check')}<span>Lasting technical availability of your line</span></li>
      </ul>
    </div>
  </section>
  <section class="svc-block" id="spare-parts" aria-labelledby="h-sp">
    <div class="svc-block__head"><h2 class="sign-l" id="h-sp">Spare parts</h2><img src="assets/img/products/svc1.jpg" alt="SCIL spare parts" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>Our spare-parts supply meets the strict expectations of our clients. All spares are manufactured to a high level of precision and pass strict quality checks before delivery. You get competent, friendly advice, high availability and short delivery times. In short: you no longer have to worry about spare parts.</p>
      <ul class="checks">
        <li>{icon('check')}<span>A dedicated spare-parts department: <a href="mailto:{D.EMAIL_PARTS}">{D.EMAIL_PARTS}</a></span></li>
        <li>{icon('check')}<span>Transparent cost and availability</span></li>
        <li>{icon('check')}<span>Optimised logistics and delivery</span></li>
      </ul>
    </div>
  </section>
  <section class="svc-block" id="training" aria-labelledby="h-tr">
    <div class="svc-block__head"><h2 class="sign-l" id="h-tr">Training courses</h2><img src="assets/img/products/svc3.jpg" alt="SCIL training session" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>Equipment effectiveness is not only about the machine; it is also about the operator. SCIL training courses help you get the most out of your equipment. On-site training gives your team a complete understanding of all the machinery SCIL supplied, and answers three questions:</p>
      <ol class="qlist"><li>How can the line's performance be improved?</li><li>How can quality be improved?</li><li>How can resource consumption in the plant be reduced?</li></ol>
      <blockquote class="quote" style="margin-top:36px"><p>“The training provided by SCIL was first class. They tailored the sessions to our business needs.”</p><footer><b>Carlos Manuel</b>, General manager, Coca-Cola Bolivia</footer></blockquote>
    </div>
  </section>
</div>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">Line down, or due for an audit?</h2><p class="lede" style="margin-top:20px">Reach the service team directly.</p>
      <div class="zone__direct"><a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} WhatsApp <span class="data">{D.WHATSAPP_DISPLAY}</span></a><a href="{D.PHONE_HREF}">{icon('phone')} Call <span class="data">{D.PHONE}</span></a><a href="mailto:{D.EMAIL_PARTS}">{icon('mail')} Spare parts <span class="data">{D.EMAIL_PARTS}</span></a></div></div>
    <div class="zone__form">{enquiry_form('Service / spare parts')}</div>
  </div>
</section>
"""
    html += footer(alt="ar/services.html")
    write("services.html", html)


# -------------------------------------------------------------------------- about
def about():
    team = "".join(f"""<li class="badge"><div class="badge__top" aria-hidden="true"></div><img src="assets/img/team/{img}" alt="" loading="lazy" width="260" height="285"><div class="badge__txt"><b>{e(n)}{f' <span lang="zh">{e(zh)}</span>' if zh else ''}</b><span>{e(r)}</span></div></li>""" for img, n, zh, r in D.TEAM)
    html = head("About · SCIL Machinery", "SCIL Machinery is a Taiwanese-standard manufacturer of beverage packaging machinery in Suzhou, China, supplying complete lines since 2003.", alt="ar/about.html")
    html += gantry("about.html", alt="ar/about.html")
    html += f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li>About</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">Built in Suzhou to Taiwanese standards</h1>
      <p class="lede">SCIL Machinery is a large independent manufacturer of beverage packaging machinery, supplying complete lines since 2003.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="legend"><p class="legend__text"><span class="stencil">23+</span> years. <span class="stencil">840+</span> clients. <span class="stencil">5,200</span> machines. <span class="stencil">230B+</span> containers.</p></div>
    <div class="sec-head" style="margin-top:clamp(56px,7vw,96px)">
      <div class="prose">
        <p>Our commitment is to clients looking for the best packaging solution, built on our own research, development and production. We always strive to provide better quality and better service.</p>
        <p>SCIL offers complete beverage filling and packaging solutions covering every step: blow moulding, filling, labelling and packaging, for water, soft drinks, juices and homecare products. Our line services include installation and commissioning, line ramp-up, efficiency audits and breakdown support.</p>
      </div>
      <div class="footprint"><div class="plate" style="padding:18px"><img class="photo-mult" src="assets/img/brand/prod-line.png" alt="Illustration of a complete SCIL line from preform injection to palletizing" loading="lazy"></div></div>
    </div>
    <div class="vm">
      <div><h2>Vision</h2><p>To become the benchmark for beverage packaging solutions.</p></div>
      <div><h2>Mission</h2><p>To give our customers real value in every dealing with us: understand their requirements precisely, and supply economically manufactured machines of superior quality that meet or exceed their expectations.</p></div>
      <div><h2>Responsibility</h2><p>SCIL promotes, at every level and in all its business, sustainability, environmental care, fair labour standards and the safety and health of workers, in full compliance with applicable law and guided by integrity and honesty.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="team-title">
  <div class="wrap">
    <div class="sec-head"><h2 class="sign-l" id="team-title">The people on your project</h2><p class="lede">From the first offer to the service visit, these are the managers who run SCIL.</p></div>
    <ul class="team" style="padding:0;margin:0">{team}</ul>
  </div>
</section>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">Visit Suzhou, or let us come to you</h2><address class="lede" style="margin-top:20px;font-style:normal">{'<br>'.join(D.ADDRESS)}</address>
      <div class="zone__direct"><a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} WhatsApp <span class="data">{D.WHATSAPP_DISPLAY}</span></a><a href="{D.PHONE_HREF}">{icon('phone')} Call <span class="data">{D.PHONE}</span></a></div></div>
    <div class="zone__form">{enquiry_form()}</div>
  </div>
</section>
"""
    html += footer(alt="ar/about.html")
    write("about.html", html)


# --------------------------------------------------------------------------- SOLO
def solo():
    cards = "".join(f"""<article class="pricecard footprint" id="solo-{i + 1}">
      <div class="plate">
        <div class="pricecard__img"><img class="photo-mult" src="assets/img/products/{img}" alt="" loading="lazy" width="409" height="334"></div>
        <h2>{e(name)}</h2>
        <p>{e(desc)}</p>
        <div class="price">{''.join(f'<span><small>{e(k)}</small><b>{e(v)}</b></span>' for k, v in prices)}</div>
        <p style="margin:16px 0 0;flex:0"><a class="link-arrow" href="https://wa.me/{D.WHATSAPP}?text={('Hello SCIL, I am interested in the SOLO ' + name).replace(' ', '%20')}" rel="noopener">Order on WhatsApp {icon('arrow')}</a></p>
      </div></article>""" for i, (img, name, desc, prices, st) in enumerate(D.SOLO))
    html = head("SOLO start-up machines · SCIL Machinery", "SOLO by SCIL: fixed-price blowing, filling, labeling, packaging and palletizing machines for start-up bottling plants.", alt="ar/solo.html")
    html += gantry("solo.html", alt="ar/solo.html")
    html += f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li>SOLO</li></ol>
    <div class="solo-hero">
      <div><img src="assets/img/brand/solo-logo.png" alt="SOLO" style="height:64px;width:auto;margin-bottom:28px;mix-blend-mode:multiply"><h1 class="sign-xl">Your first plant, priced up front</h1></div>
      <p class="lede">SOLO is SCIL's platform for start-up packaging businesses: single machines with published prices, sold without an intermediary.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="solo-grid">{cards}</div>
    <p class="fineprint">USD unit prices as listed on SCIL SOLO. Prices, configuration and delivery terms are confirmed by SCIL sales with your order.</p>
  </div>
</section>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">Combine SOLO machines into a starter line</h2><p class="lede" style="margin-top:20px">Tell us your product and output and we'll suggest the SOLO machines that work together.</p></div>
    <div class="zone__form">{enquiry_form('SOLO start-up line')}</div>
  </div>
</section>
"""
    html += footer(alt="ar/solo.html")
    write("solo.html", html)


# ------------------------------------------------------------------------ contact
def contact():
    html = head("Contact · SCIL Machinery", "Contact SCIL Machinery in Suzhou: line enquiries, quotes, service and spare parts by WhatsApp, phone, WeChat or email.", alt="ar/contact.html")
    html += gantry("contact.html", alt="ar/contact.html")
    html += f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">Home</a></li><li>Contact</li></ol>
    <div class="page-head__grid"><h1 class="sign-xl">Plan your line with an engineer</h1><p class="lede">Product, container and output are enough to start. We reply with a proposed layout and machine list.</p></div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap hq">
    <div class="hq__main">{enquiry_form()}</div>
    <aside class="hq__side" aria-label="Direct contact">
      <a class="channel" href="https://wa.me/{D.WHATSAPP}" rel="noopener"><span class="channel__ic">{icon('chat')}</span><span><b>WhatsApp</b><span>{D.WHATSAPP_DISPLAY}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="{D.PHONE_HREF}"><span class="channel__ic">{icon('phone')}</span><span><b>Call Suzhou</b><span>{D.PHONE}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="mailto:{D.EMAIL}"><span class="channel__ic">{icon('mail')}</span><span><b>Email</b><span>{D.EMAIL}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="mailto:{D.EMAIL_PARTS}"><span class="channel__ic">{icon('grid')}</span><span><b>Spare parts</b><span>{D.EMAIL_PARTS}</span></span>{icon('arrow-ur')}</a>
      <div class="channel" style="grid-template-columns:96px 1fr"><img src="assets/img/brand/wechat-qr.jpg" alt="WeChat QR code" width="96" height="96" style="width:96px;height:96px;object-fit:cover;object-position:center 38%;background:#fff;padding:4px"><span><b>WeChat</b><span>Scan to add us</span></span></div>
      <div style="margin-top:36px">
        <h2 class="sign-s" style="margin-bottom:10px">Headquarters</h2>
        <address class="prose" style="font-style:normal">SCIL Machinery<br>{'<br>'.join(D.ADDRESS)}</address>
        <p><a class="link-arrow" href="https://www.openstreetmap.org/search?query=FengHuang%20Town%20Zhangjiagang%20Suzhou" rel="noopener">Open map {icon('arrow-ur')}</a></p>
        <h2 class="sign-s" style="margin:32px 0 10px">Agent · Algeria</h2>
        <p class="prose">Solution Plus<br>Mekacher Abderrahmane</p>
      </div>
    </aside>
  </div>
</section>
"""
    html += footer(alt="ar/contact.html")
    write("contact.html", html)


if __name__ == "__main__":
    home(); equipment(); services(); about(); solo(); contact()
    for m in D.MACHINES:
        machine_page(m)
    print("built", 6 + len(D.MACHINES), "English pages")
    import build_ar
    build_ar.build_all()
