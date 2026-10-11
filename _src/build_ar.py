"""Arabic (RTL) pages, written to /ar/. Called from build.py; can run alone:

    python _src/build_ar.py
"""
import os, sys
from html import escape as e
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
import data as D
import ar_data as A
from parts import head, gantry, footer, icon, token, mcard, machine_img, enquiry_form
from build import write, machines_in, body_paragraphs, ROOT, HERO_PICK, WALK_PICK

L = "ar"
B = "../"            # asset base for /ar/*.html
ST = {s["key"]: s for s in A.STATIONS + [A.WATER]}
BY_ID = {m[0]: m for m in D.MACHINES}
HERO_FIG = {"injection": "بريفورم", "blowing": "حتى 22,000 عبوة/ساعة", "filling": "حتى 36,000 عبوة/ساعة",
            "labeling": "3 أنواع ملصقات", "packaging": "شرنك · كراتين", "palletizing": "15 حزمة/دقيقة"}


def wa(text):
    return f"https://wa.me/{D.WHATSAPP}?text={quote(text)}"


def direct_links(items):
    return '<div class="zone__direct">' + "".join(items) + "</div>"


DL_WA = f'<a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon("chat")} واتساب <span class="data" dir="ltr">{D.WHATSAPP_DISPLAY}</span></a>'
DL_TEL = f'<a href="{D.PHONE_HREF}">{icon("phone")} اتصل بسوجو <span class="data" dir="ltr">{D.PHONE}</span></a>'
DL_MAIL = f'<a href="mailto:{D.EMAIL}">{icon("mail")} البريد الإلكتروني <span class="data">{D.EMAIL}</span></a>'
DL_CAT = f'<a href="{D.CATALOGUE}" rel="noopener">{icon("download")} الكتالوج <span class="data">PDF</span></a>'


def page(fname, title, desc, body, alt_en, b=B, lb=""):
    html = head(title, desc, b, lang=L, alt=alt_en)
    html += gantry(fname, b, lang=L, alt=alt_en, lb=lb)
    html += body
    html += footer(b, lang=L, lb=lb, stations=A.STATIONS, alt=alt_en)
    return html


# --------------------------------------------------------------------------- home
def home():
    fps = []
    for i, s in enumerate(A.STATIONS):
        if s["key"] in HERO_PICK:
            img = f'<img class="photo-mult" src="{B}assets/img/products/{machine_img(HERO_PICK[s["key"]])}" alt="" width="850" height="690">'
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
    for s in A.STATIONS:
        picks = WALK_PICK.get(s["key"], [])
        if picks:
            cards = '<div class="machines">' + "".join(mcard(BY_ID[i], B, lang=L, lb="") for i in picks) + "</div>"
            n = len(machines_in(s["key"]))
            more = f'<p class="station__more"><a class="link-arrow" href="equipment.html#{s["key"]}">كل ماكينات {e(s["name"])} ({n}) {icon("arrow")}</a></p>'
        else:
            cards = f"""<div class="empty-bay" style="margin-top:28px">{token("preform")}
        <p><strong>ماكينات الحقن تُحدَّد حسب كل مشروع.</strong> أرسل لنا وزن البريفورم ومقاس العنق والطاقة المطلوبة، ونقترح عليك الماكينة والقوالب.</p></div>"""
            more = f'<p class="station__more"><a class="link-arrow" href="contact.html">اسأل عن حقن البريفورم {icon("arrow")}</a></p>'
        water = ""
        if s["key"] == "filling":
            water = '<p class="meta" style="margin-top:18px">تغذيها <a href="equipment/water-treatment-equipment.html">00 معالجة المياه</a>: ترشيح وتناضح عكسي وأوزون وأشعة فوق بنفسجية.</p>'
        stations.append(f"""<article class="station" id="st-{s['key']}" data-station="{s['no']}" data-token="{s['token']}" data-out="{e(s['out'])}">
      <div class="station__head"><span class="station__no stencil" aria-hidden="true">{s['no']}</span><h3 class="sign-m"><span class="visually-hidden">المحطة {s['no']}: </span>{e(s['name'])}</h3></div>
      <div class="station__body"><p class="prose">{e(s['text'])}</p>{token(s['token'], 'station__token-inline', 'تخرج من المحطة: ' + s['out'])}</div>
      {cards}{water}
      {more}
    </article>""")

    ticks = "".join(f'<li style="top:{(i + 0.5) / 6 * 100:.2f}%" data-tick="{s["no"]}">{s["no"]}</li>' for i, s in enumerate(A.STATIONS))
    tstates = "".join(f'<div class="token__state{" is-on" if i == 0 else ""}" data-state="{s["token"]}">{token(s["token"])}</div>' for i, s in enumerate(A.STATIONS))

    tags = "".join(f"""<article class="tag">
      <div class="tag__band" aria-hidden="true"></div>
      <blockquote><p>«{e(t['short'])}»</p>
        <details><summary>الشهادة كاملة {icon('arrow')}</summary>{''.join(f'<p>{e(p)}</p>' for p in t['full'])}</details>
      </blockquote>
      <footer><b>{e(t['org'])}</b>{e(t['name'])}، {e(t['role'])}</footer>
    </article>""" for t in A.TESTIMONIALS if t["org"] not in ("Safira", "Najd Water"))

    logos = "".join(f'<li><img src="{B}assets/img/clients/{f}" alt="" loading="lazy"></li>' for f in sorted(os.listdir(os.path.join(ROOT, "assets/img/clients"))))

    solo_idx = [0, 7, 4]
    solos = "".join(f"""<a class="pricecard footprint" href="solo.html">
      <div class="plate">
        <div class="pricecard__img"><img class="photo-mult" src="{B}assets/img/products/{D.SOLO[i][0]}" alt="" loading="lazy" width="409" height="334"></div>
        <h3>{e(A.SOLO[i][0])}</h3>
        <p>{e(A.SOLO[i][1])}</p>
        <div class="price">{''.join(f'<span><small>{e(k)}</small><b dir="ltr">{e(v)}</b></span>' for k, v in A.SOLO[i][2][:2])}</div>
      </div></a>""" for i in solo_idx)

    body = f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <div class="hero__head">
      <h1 class="hero__title" id="hero-title"><span class="sign-xl">من البريفورم إلى الطبلية. <em>مورّد واحد.</em></span></h1>
      <div class="hero__aside">
        <p class="lede">خطوط تعبئة متكاملة للمياه والمشروبات الغازية والعصائر وزيت الطعام والمنظفات، يركّبها ويخدمها مهندسونا.</p>
        <div class="hero__ctas">
          <a class="btn" href="#enquire">خطّط خط إنتاجك {icon('arrow')}</a>
          <a class="btn btn--plate" href="https://wa.me/{D.WHATSAPP}" rel="noopener">{icon('chat')} تحدّث مع مهندس على واتساب</a>
        </div>
      </div>
    </div>
  </div>
  <div class="plan">
    <div class="wrap plan__scroller" tabindex="0" aria-label="محطات خط SCIL الست">
      <div class="plan__track">
        <span class="lane" aria-hidden="true"></span><span class="lane lane--edge" aria-hidden="true"></span><span class="lane-chevrons" aria-hidden="true"></span>
        {''.join(fps)}
        <div class="fg-zone">
          <svg viewBox="0 0 64 56" aria-hidden="true"><use href="#tk-pallet-mini"/></svg>
          <span class="sign-s">منتج جاهز</span>
          <p>مغلّف بالشرنك، محمّل على الطبليات، وجاهز لشاحناتك.</p>
        </div>
      </div>
    </div>
    <p class="wrap plan__hint">{icon('arrow')} اسحب على طول الخط</p>
  </div>
</section>

<section class="section section--tight" aria-label="SCIL بالأرقام">
  <div class="wrap">
    <div class="legend">
      <p class="legend__text">منذ <span class="stencil">2003</span> شحنّا <span class="stencil">5,200</span> ماكينة إلى أكثر من <span class="stencil">840</span> عميلًا، وعبّأت خطوطهم أكثر من <span class="stencil">230</span> مليار عبوة.</p>
    </div>
    <p class="legend__foot meta">الأرقام كما تنشرها SCIL Machinery.</p>
  </div>
</section>

<section class="section" id="line" aria-labelledby="line-title" style="padding-top:clamp(40px,5vw,72px)">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="line-title">جولة على الخط، محطة بعد محطة</h2>
      <p class="lede">كل خط يتبع العبوة. هذا ما تفعله كل محطة من محطات SCIL بها، والماكينات التي تؤدي العمل.</p>
    </div>
    <div class="walk" data-walk data-leaves="تخرج من المحطة">
      <div class="walk__strip" aria-hidden="true"><svg viewBox="0 0 300 400"><use data-strip-use href="#tk-preform"/></svg><strong data-strip-out>01 · {e(A.STATIONS[0]['out'])}</strong><div class="walk__strip-lane"><span></span></div></div>
      <div class="walk__rail">
        <div class="walk__sticky">
          <div class="walk__lane" aria-hidden="true"><span class="walk__lane-fill" data-lane-fill></span><ol class="walk__ticks">{ticks}</ol></div>
          <div class="walk__ride"><div class="token" aria-hidden="true">
            <div class="token__stage">{tstates}</div>
            <div class="token__cap"><strong data-token-out>{e(A.STATIONS[0]['out'])}</strong><span class="meta" data-token-no>تخرج من المحطة 01</span></div>
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
      <div class="proof__lead"><h2 class="sign-l" id="proof-title"><span>الطاقة المتعاقد عليها 1,400.</span><span class="go">الإنتاج الفعلي 1,800.</span></h2></div>
      <figure class="proof__quote">
        <blockquote class="quote"><p>«اشترينا خط 5 لترات بطاقة 1,400 عبوة/ساعة. وبعد أن أنهى المهندسون التركيب، صار الخط ينتج 1,800 عبوة/ساعة.»</p></blockquote>
        <figcaption class="quote"><footer><b>عباس حجازي</b>، الرئيس التنفيذي، Safira</footer></figcaption>
      </figure>
      <div class="gauge" data-gauge role="img" aria-label="خط Safira سعة 5 لترات: الطاقة المتعاقد عليها 1,400 عبوة في الساعة، والإنتاج الفعلي 1,800 عبوة في الساعة">
        <div class="gauge__row"><span class="gauge__lab">المتعاقد عليه</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--rated" style="--w:70.0%">1,400</div></div></div>
        <div class="gauge__row"><span class="gauge__lab">الفعلي بعد التشغيل</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--run" style="--w:90.0%">1,800</div></div></div>
        <div class="gauge__scale"><span></span><div class="gauge__ticks"><span>0</span><span>500</span><span>1,000</span><span>1,500</span><span>2,000 عبوة/ساعة</span></div></div>
      </div>
    </div>

    <div class="returns">
      <div class="returns__txt">
        <h3 class="sign-m">عملاؤنا يعودون للخط التالي</h3>
        <p class="prose" style="margin-top:14px">بدأت Najd Water بماكينة نفخ واحدة، وبعد أربع سنوات طلبت الخط كاملًا.</p>
      </div>
      <div class="returns__path">
        <div class="ret-step"><span class="ret-step__yr">2014</span><span class="stencil">12,000 BPH</span><p>العقد الأول: ماكينة نفخ.</p></div>
        <div class="ret-step"><span class="ret-step__yr">سبتمبر 2018</span><span class="stencil">24,000 BPH</span><p>خط إنتاج مياه أوتوماتيكي بالكامل. «شكرًا لعائلة SCIL على وقوفها الدائم إلى جانبنا.»</p></div>
      </div>
    </div>

    <div class="tags">
      <div class="sec-head" style="margin-bottom:24px">
        <h3 class="sign-m">بكلمات عملائنا</h3>
        <div class="tags__ctrl" style="justify-self:end"><button type="button" data-tags="1" aria-label="السابق">{icon('arrow-l')}</button><button type="button" data-tags="-1" aria-label="التالي">{icon('arrow')}</button></div>
      </div>
      <div class="tags__row" data-tags-row tabindex="0" aria-label="شهادات العملاء">{tags}</div>
    </div>
  </div>
</section>

<section class="section asphalt" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="svc-title">نبقى معك بعد التشغيل</h2>
      <p class="lede">يختار العملاء SCIL لما يحدث بعد وصول الماكينات. مسار الخدمة يرافق خطك طوال عمره.</p>
    </div>
    <ol class="loop" style="padding:0;list-style:none">
      <li class="loop__step"><span class="chip">1</span><h3>التركيب</h3><p>يركّب مهندسونا الخط في مصنعك ويشغّلونه.</p></li>
      <li class="loop__step"><span class="chip">2</span><h3>رفع الطاقة</h3><p>نوصل الخط إلى طاقته المقررة، وندرّب مشغليك عليه.</p></li>
      <li class="loop__step"><span class="chip">3</span><h3>تدقيق الكفاءة</h3><p>فحص دوري لماكينة واحدة أو للخط كاملًا، مع خطة عمل وتقدير للعائد.</p></li>
      <li class="loop__step"><span class="chip">4</span><h3>العَمرة</h3><p>استبدال الأجزاء المستهلكة في موقعك، ليعمل الخط كأول يوم.</p></li>
      <li class="loop__step loop__step--stop"><span class="chip">!</span><h3>الأعطال</h3><p>إذا توقف الخط، يساعدك فريق الخدمة على تحديد السبب وإعادة التشغيل.</p></li>
    </ol>
    <div class="bays">
      <div class="bay"><div><h3>قطع الغيار</h3><p>قسم مخصص لقطع الغيار، وقطع دقيقة الصنع تُفحص قبل التسليم، وشفافية في التكلفة والتوفر.</p><a class="link-arrow" href="services.html#spare-parts">قطع الغيار {icon('arrow')}</a></div><img src="{B}assets/img/products/svc1.jpg" alt="" loading="lazy"></div>
      <div class="bay"><div><h3>التدريب</h3><p>دورات في موقعك ليعرف فريقك الخط كاملًا: الأداء والجودة وتقليل استهلاك الموارد.</p><a class="link-arrow" href="services.html#training">الدورات التدريبية {icon('arrow')}</a></div><img src="{B}assets/img/products/svc3.jpg" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="clients-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="clients-title">أكثر من 840 عميلًا. هذه بعض علاماتهم.</h2>
      <p class="lede">منتجو مياه ومشروبات غازية وعصائر وزيوت يعملون اليوم بماكينات SCIL.</p>
    </div>
    <ul class="dock" aria-label="شعارات العملاء">{logos}</ul>
  </div>
</section>

<section class="section" aria-labelledby="solo-title" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="solo-title">تبدأ مصنعك الأول؟ سولو</h2>
      <p class="lede">سولو هي مجموعة SCIL للمشاريع الناشئة: ماكينات منفردة بأسعار ثابتة ومعلنة، ودون وسيط.</p>
    </div>
    <div class="solo-row">{solos}</div>
    <p class="fineprint">أسعار الوحدة بالدولار الأمريكي كما تعلنها SCIL SOLO. تأكد من السعر الحالي وشروط التسليم مع فريق المبيعات.</p>
    <p style="margin-top:24px"><a class="link-arrow" href="solo.html">كل ماكينات سولو الـ17 {icon('arrow')}</a></p>
  </div>
</section>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt">
      <h2 class="sign-l" id="enq-title">أخبرنا ماذا تعبّئ، ونرسم لك الخط.</h2>
      <p class="lede" style="margin-top:20px">المنتج وحجم العبوة والطاقة المطلوبة تكفي للبدء. يرد عليك مهندس بمخطط مقترح للخط وقائمة بالماكينات.</p>
      {direct_links([DL_WA, DL_TEL, DL_MAIL, DL_CAT])}
    </div>
    <div class="zone__form">{enquiry_form(lang=L)}</div>
  </div>
</section>
"""
    write("ar/index.html", page("index.html", "SCIL Machinery · خطوط تعبئة متكاملة من البريفورم إلى الطبلية",
                                "تصمم SCIL Machinery في سوجو خطوط تعبئة وتغليف المشروبات وتصنعها: حقن البريفورم ونفخ PET والتعبئة والملصقات والتغليف والطبليات، للمياه والمشروبات الغازية والعصائر وزيت الطعام والمنظفات.",
                                body, "../index.html"))


# ---------------------------------------------------------------------- catalogue
def equipment():
    sel = "".join(f'<a href="#{s["key"]}" data-sel="{s["key"]}"><span class="stencil">{s["no"]}</span>{e(s["name"])} <span class="data">{len(machines_in(s["key"]))}</span></a>' for s in A.STATIONS)
    sel += '<a href="#water-treatment" data-sel="water-treatment"><span class="stencil">00</span>معالجة المياه <span class="data">1</span></a>'
    blocks = []
    for s in A.STATIONS + [A.WATER]:
        ms = machines_in(s["key"])
        if ms:
            grid = '<div class="cat-grid">' + "".join(mcard(m, B, heading="h3", lang=L, lb="") for m in ms) + "</div>"
        else:
            grid = f"""<div class="empty-bay">{token('preform')}<p><strong>ماكينات الحقن تُحدَّد حسب كل مشروع.</strong> أرسل لنا وزن البريفورم ومقاس العنق والطاقة المطلوبة، ونقترح عليك الماكينة والقوالب. <a href="contact.html">اسأل عن الحقن</a>.</p></div>"""
        blocks.append(f"""<section class="cat-station" id="{s['key']}" data-cat="{s['key']}" aria-labelledby="h-{s['key']}">
    <div class="cat-station__head"><span class="stencil" aria-hidden="true">{s['no']}</span><h2 class="sign-l" id="h-{s['key']}">{e(s['name'])}</h2><p class="prose">{e(s['text'])} <span class="meta" style="display:block;margin-top:8px">تخرج من المحطة: {e(s['out'])}</span></p></div>
    {grid}
  </section>""")
    body = f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">الرئيسية</a></li><li>الماكينات</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">الماكينات، محطة بعد محطة</h1>
      <p class="lede">{len(D.MACHINES)} ماكينة مرتبة بالترتيب الذي تمر به عبوتك. اختر المحطة، أو اطلب منا تحديد الخط كاملًا.</p>
    </div>
  </div>
</section>
<nav class="selector" aria-label="المحطات"><div class="wrap selector__in" data-selector>{sel}</div></nav>
<div class="wrap">{''.join(blocks)}</div>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">لست متأكدًا أي ماكينة تناسبك؟</h2><p class="lede" style="margin-top:20px">أخبرنا بالمنتج وحجم العبوة والطاقة، ونختار لك الماكينات ونرسم الخط.</p>
      {direct_links([DL_WA, DL_CAT])}</div>
    <div class="zone__form">{enquiry_form(lang=L)}</div>
  </div>
</section>
"""
    write("ar/equipment.html", page("equipment.html", "الماكينات · SCIL Machinery",
                                    "ماكينات SCIL Machinery حسب محطات الخط: ماكينات نفخ PET، وتعبئة المياه والمشروبات الغازية والعصائر والزيوت، والملصقات، والتغليف، والطبليات، ومعالجة المياه.",
                                    body, "../equipment.html"))


def render_body_ar(paras):
    out, in_list = [], False
    for t in paras:
        if t.startswith("-"):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{e(t[1:])}</li>")
            continue
        if in_list:
            out.append("</ul>"); in_list = False
        out.append(f"<h3>{e(t[1:])}</h3>" if t.startswith("#") else f"<p>{e(t)}</p>")
    if in_list:
        out.append("</ul>")
    return "".join(out)


def spec_table_ar(mid):
    s = D.SPECS.get(mid)
    if not s:
        return ""
    T = A.SPEC_LABELS
    cap = T.get(s["caption"], s["caption"])
    if "head" in s:
        th = "".join(f'<th scope="col">{e(T.get(h, h))}</th>' for h in s["head"])
        rows = "".join("<tr>" + f'<th scope="row">{e(r[0])}</th>' + "".join(f"<td>{e(c)}</td>" for c in r[1:]) + "</tr>" for r in s["rows"])
        return f'<table class="specs specs--series"><caption>{e(cap)}</caption><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>'
    rows = "".join(f'<tr><th scope="row">{e(T.get(k, k))}</th><td>{e(v)}</td></tr>' for k, v in s["rows"])
    return f'<table class="specs"><caption>{e(cap)}</caption><tbody>{rows}</tbody></table>'


def machine_page(m):
    mid, slug, key, _, _, _ = m
    name, fig, summ, paras = A.MACHINES[mid]
    s = ST[key]
    b, lb = "../../", "../"
    idx = next((i for i, x in enumerate(A.STATIONS) if x["key"] == key), -1)
    mini = "".join(
        f'<a href="{lb}equipment.html#{x["key"]}" title="{e(x["name"])}" class="{"is-on" if i == idx else ("is-past" if i < idx else "")}">{x["no"]}<span> {e(x["name"])}</span></a>'
        for i, x in enumerate(A.STATIONS))
    sib = "".join(mcard(x, b, heading="h3", lang=L, lb=lb) for x in [x for x in machines_in(key) if x[0] != mid][:4])
    pos = ('<nav class="lane-mini" aria-label="موقعها على الخط">' + mini + '</nav>') if idx >= 0 else '<p class="meta" style="margin:0 0 24px">00 معالجة المياه · تغذي المحطة 03 التعبئة</p>'
    body = f"""
<section class="page-head" style="padding-bottom:24px">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{lb}index.html">الرئيسية</a></li><li><a href="{lb}equipment.html">الماكينات</a></li><li><a href="{lb}equipment.html#{key}">{s['no']} {e(s['name'])}</a></li></ol>
  </div>
</section>
<section class="wrap" style="padding-bottom:var(--space-section)">
  <div class="mdetail">
    <div class="mdetail__media"><div class="footprint"><div class="plate"><img class="photo-mult" src="{b}assets/img/products/{machine_img(mid)}" alt="{e(name)}" width="850" height="690"></div></div></div>
    <div class="mdetail__info">
      {pos}
      <h1 class="sign-l">{e(name)}</h1>
      <span class="mdetail__fig">{e(fig)}</span>
      <p class="lede">{e(summ)}</p>
      <div class="mdetail__actions">
        <a class="btn" href="{lb}contact.html?machine={quote(name)}">اطلب عرض سعر {icon('arrow')}</a>
        <a class="btn btn--plate" href="{wa('مرحبًا SCIL، أرغب في الاستفسار عن ' + name + '.')}" rel="noopener">{icon('chat')} واتساب</a>
      </div>
      <div class="body-copy prose" style="margin-top:36px">{render_body_ar(paras)}</div>
      {spec_table_ar(mid)}
      <p class="meta" style="margin-top:22px">البيانات الفنية الكاملة في <a href="{D.CATALOGUE}" rel="noopener">كتالوج SCIL (PDF)</a> أو عند الطلب.</p>
    </div>
  </div>
</section>
{f'''<section class="section" style="padding-top:0" aria-labelledby="sib"><div class="wrap"><div class="sec-head" style="margin-bottom:32px"><h2 class="sign-m" id="sib">ماكينات أخرى في المحطة {s['no']} · {e(s['name'])}</h2></div><div class="cat-grid">{sib}</div></div></section>''' if sib else ''}
"""
    write(f"ar/equipment/{slug}.html", page("equipment.html", f"{name} · SCIL Machinery", f"{name}: {summ}", body,
                                            f"../../equipment/{slug}.html", b=b, lb=lb))


# ----------------------------------------------------------------------- services
def services():
    loop = """<ol class="loop" style="padding:0;list-style:none;margin-top:clamp(56px,7vw,96px)">
      <li class="loop__step"><span class="chip">1</span><h2>التركيب</h2><p>تركيب الخط وتشغيله في مصنعك.</p></li>
      <li class="loop__step"><span class="chip">2</span><h2>رفع الطاقة</h2><p>إيصال الخط إلى طاقته المقررة.</p></li>
      <li class="loop__step"><span class="chip">3</span><h2>التدقيق</h2><p>تدقيق فني وفحص دوري.</p></li>
      <li class="loop__step"><span class="chip">4</span><h2>العَمرة</h2><p>استبدال الأجزاء المستهلكة في موقعك.</p></li>
      <li class="loop__step loop__step--stop"><span class="chip">!</span><h2>الأعطال</h2><p>دعم عند توقف الخط.</p></li>
    </ol>"""
    body = f"""
<section class="page-head asphalt" style="padding-bottom:var(--space-section)">
  <div class="wrap">
    <ol class="crumbs" style="color:var(--on-asphalt-2)"><li><a href="index.html" style="color:var(--on-asphalt)">الرئيسية</a></li><li>الخدمات</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl" style="color:var(--plate)">مسار الخدمة يرافق خطك طوال عمره</h1>
      <p class="lede">التركيب والتشغيل، ورفع الطاقة، وتدقيق الكفاءة، ودعم الأعطال، ومن ورائها قطع الغيار والتدريب.</p>
    </div>
    {loop}
  </div>
</section>
<div class="wrap">
  <section class="svc-block" id="service-packages" aria-labelledby="h-pk">
    <div class="svc-block__head"><h2 class="sign-l" id="h-pk">التدقيق الفني والفحص</h2><img src="{B}assets/img/products/svc2.jpg" alt="مهندسو SCIL في زيارة خدمة" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>التدقيق الفني من SCIL فحص دوري لحالة معداتك وتقييم لأدائها. نحلل ماكينة واحدة أو الخط كاملًا أثناء الإنتاج، ونحدد العوائق الفنية والتنظيمية، ونساعدك على تحسين عمليات التعبئة والتغليف.</p>
      <p>نساعدك على تنفيذ المكاسب السريعة، وضبط معداتك، وتطبيق خطة العمل. ونقدم تقديرًا كاملًا للتكلفة لتحسب العائد على الاستثمار، ومقترحات تخفض تكاليفك وترفع كفاءة ماكينات التغليف.</p>
      <h3 class="sign-s" style="margin-top:36px;margin-bottom:12px">عَمرة الماكينة: كأنها في يومها الأول</h3>
      <p>حين تقضي الماكينة ساعات تشغيل طويلة وتظهر عليها علامات التقادم، يحين وقت العَمرة. يحدد التدقيق الفني أولًا حالتها وقطع الغيار المطلوبة، ثم يأتي فنيونا إلى مصنعك، ويستبدلون كل الأجزاء والمجموعات المستهلكة، ويجرون الإصلاحات البسيطة في الموقع.</p>
      <ul class="checks">
        <li>{icon('check')}<span>استبدال سريع ومركّز لكل الأجزاء والمجموعات المستهلكة</span></li>
        <li>{icon('check')}<span>تخطيط الفحوص والعَمرات وتنفيذها من مورّد واحد</span></li>
        <li>{icon('check')}<span>جاهزية فنية مستمرة لخطك</span></li>
      </ul>
    </div>
  </section>
  <section class="svc-block" id="spare-parts" aria-labelledby="h-sp">
    <div class="svc-block__head"><h2 class="sign-l" id="h-sp">قطع الغيار</h2><img src="{B}assets/img/products/svc1.jpg" alt="قطع غيار SCIL" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>توريد قطع الغيار لدينا يلبي توقعات عملائنا الصارمة. تُصنع كل القطع بدقة عالية وتخضع لفحص جودة صارم قبل التسليم. تحصل على مشورة متخصصة، وتوفر عالٍ، ومدة تسليم قصيرة. باختصار: لن تقلق بشأن قطع الغيار بعد اليوم.</p>
      <ul class="checks">
        <li>{icon('check')}<span>قسم مخصص لقطع الغيار: <a href="mailto:{D.EMAIL_PARTS}">{D.EMAIL_PARTS}</a></span></li>
        <li>{icon('check')}<span>شفافية في التكلفة والتوفر</span></li>
        <li>{icon('check')}<span>لوجستيات وتسليم أكثر كفاءة</span></li>
      </ul>
    </div>
  </section>
  <section class="svc-block" id="training" aria-labelledby="h-tr">
    <div class="svc-block__head"><h2 class="sign-l" id="h-tr">الدورات التدريبية</h2><img src="{B}assets/img/products/svc3.jpg" alt="جلسة تدريب من SCIL" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>كفاءة المعدات لا تتعلق بالماكينة وحدها، بل بالمشغّل أيضًا. دورات SCIL تساعدك على الاستفادة القصوى من معداتك. يمنح التدريب في موقعك فريقك فهمًا كاملًا لكل الماكينات التي ورّدتها SCIL، ويجيب عن ثلاثة أسئلة:</p>
      <ol class="qlist"><li>كيف نرفع أداء الخط؟</li><li>كيف نحسّن الجودة؟</li><li>كيف نخفض استهلاك الموارد في المصنع؟</li></ol>
      <blockquote class="quote" style="margin-top:36px"><p>«كان التدريب الذي قدمته SCIL من الطراز الأول، وصمموا الجلسات حسب احتياجات عملنا.»</p><footer><b>كارلوس مانويل</b>، المدير العام، Coca-Cola Bolivia</footer></blockquote>
    </div>
  </section>
</div>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">توقف الخط، أو حان موعد التدقيق؟</h2><p class="lede" style="margin-top:20px">تواصل مباشرة مع فريق الخدمة.</p>
      {direct_links([DL_WA, DL_TEL, f'<a href="mailto:{D.EMAIL_PARTS}">{icon("mail")} قطع الغيار <span class="data">{D.EMAIL_PARTS}</span></a>'])}</div>
    <div class="zone__form">{enquiry_form('خدمة / قطع غيار', lang=L)}</div>
  </div>
</section>
"""
    write("ar/services.html", page("services.html", "الخدمات · SCIL Machinery",
                                   "التركيب والتشغيل ورفع الطاقة والتدقيق الفني والعَمرة وقطع الغيار وتدريب المشغلين من SCIL Machinery.",
                                   body, "../services.html"))


# -------------------------------------------------------------------------- about
def about():
    team = "".join(f"""<li class="badge"><div class="badge__top" aria-hidden="true"></div><img src="{B}assets/img/team/{img}" alt="" loading="lazy" width="260" height="285"><div class="badge__txt"><b>{e(A.TEAM_NAMES_AR.get(n, n))}{f' <span lang="zh">{e(zh)}</span>' if zh else ''}</b><span>{e(A.TEAM_ROLES[r])}</span></div></li>""" for img, n, zh, r in D.TEAM)
    body = f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">الرئيسية</a></li><li>عن الشركة</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">صناعة في سوجو بمعايير تايوانية</h1>
      <p class="lede">SCIL Machinery مصنّع مستقل كبير لماكينات تعبئة وتغليف المشروبات، يورّد خطوطًا متكاملة منذ 2003.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="legend"><p class="legend__text"><span class="stencil">+23</span> عامًا. <span class="stencil">+840</span> عميلًا. <span class="stencil">5,200</span> ماكينة. <span class="stencil">+230</span> مليار عبوة.</p></div>
    <div class="sec-head" style="margin-top:clamp(56px,7vw,96px)">
      <div class="prose">
        <p>التزامنا موجّه للعملاء الباحثين عن أفضل حل للتعبئة والتغليف، ويقوم على البحث والتطوير والتصنيع في مصانعنا. نسعى دائمًا إلى جودة أعلى وخدمة أفضل.</p>
        <p>تقدم SCIL حلولًا متكاملة لتعبئة المشروبات وتغليفها تغطي كل المراحل: النفخ والتعبئة والملصقات والتغليف، للمياه والمشروبات الغازية والعصائر والمنظفات. وتشمل خدماتنا التركيب والتشغيل، ورفع طاقة الخط، وتدقيق الكفاءة، ودعم الأعطال.</p>
      </div>
      <div class="footprint"><div class="plate" style="padding:18px"><img class="photo-mult" src="{B}assets/img/brand/prod-line.png" alt="رسم توضيحي لخط SCIL كامل من حقن البريفورم إلى الطبليات" loading="lazy"></div></div>
    </div>
    <div class="vm">
      <div><h2>رؤيتنا</h2><p>أن نكون المرجع في حلول تعبئة المشروبات وتغليفها.</p></div>
      <div><h2>رسالتنا</h2><p>أن نقدم لعملائنا قيمة حقيقية في كل تعامل: نفهم متطلباتهم بدقة، ونورّد ماكينات بتكلفة تصنيع اقتصادية وجودة عالية تلبي توقعاتهم أو تتجاوزها.</p></div>
      <div><h2>مسؤوليتنا</h2><p>تعزز SCIL على كل المستويات وفي كل أعمالها الاستدامة وحماية البيئة ومعايير العمل العادلة وسلامة العاملين وصحتهم، ملتزمةً بالقوانين ومسترشدةً بالنزاهة والأمانة.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="team-title">
  <div class="wrap">
    <div class="sec-head"><h2 class="sign-l" id="team-title">الفريق الذي يتابع مشروعك</h2><p class="lede">من العرض الأول إلى زيارة الخدمة، هؤلاء المديرون يديرون SCIL.</p></div>
    <ul class="team" style="padding:0;margin:0">{team}</ul>
  </div>
</section>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">زُرنا في سوجو، أو نأتي إليك</h2><address class="lede" style="margin-top:20px;font-style:normal" dir="ltr">{'<br>'.join(D.ADDRESS)}</address>
      {direct_links([DL_WA, DL_TEL])}</div>
    <div class="zone__form">{enquiry_form(lang=L)}</div>
  </div>
</section>
"""
    write("ar/about.html", page("about.html", "عن الشركة · SCIL Machinery",
                                "SCIL Machinery مصنّع لماكينات تعبئة وتغليف المشروبات بمعايير تايوانية في سوجو بالصين، يورّد خطوطًا متكاملة منذ 2003.",
                                body, "../about.html"))


# --------------------------------------------------------------------------- SOLO
def solo():
    cards = "".join(f"""<article class="pricecard footprint" id="solo-{i + 1}">
      <div class="plate">
        <div class="pricecard__img"><img class="photo-mult" src="{B}assets/img/products/{D.SOLO[i][0]}" alt="" loading="lazy" width="409" height="334"></div>
        <h2>{e(name)}</h2>
        <p>{e(desc)}</p>
        <div class="price">{''.join(f'<span><small>{e(k)}</small><b dir="ltr">{e(v)}</b></span>' for k, v in prices)}</div>
        <p style="margin:16px 0 0;flex:0"><a class="link-arrow" href="{wa('مرحبًا SCIL، أرغب في طلب ماكينة سولو: ' + name)}" rel="noopener">اطلبها عبر واتساب {icon('arrow')}</a></p>
      </div></article>""" for i, (name, desc, prices) in enumerate(A.SOLO))
    body = f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">الرئيسية</a></li><li>سولو</li></ol>
    <div class="solo-hero">
      <div><img src="{B}assets/img/brand/solo-logo.png" alt="SOLO" style="height:64px;width:auto;margin-bottom:28px;mix-blend-mode:multiply"><h1 class="sign-xl">مصنعك الأول، بسعر معروف مسبقًا</h1></div>
      <p class="lede">سولو منصة SCIL للمشاريع الناشئة في التعبئة والتغليف: ماكينات منفردة بأسعار معلنة، تُباع دون وسيط.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="solo-grid">{cards}</div>
    <p class="fineprint">أسعار الوحدة بالدولار الأمريكي كما تعلنها SCIL SOLO. يؤكد فريق مبيعات SCIL السعر والمواصفات وشروط التسليم مع طلبك.</p>
  </div>
</section>
<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">اجمع ماكينات سولو في خط مبتدئ</h2><p class="lede" style="margin-top:20px">أخبرنا بمنتجك والطاقة المطلوبة، ونقترح ماكينات سولو التي تعمل معًا.</p></div>
    <div class="zone__form">{enquiry_form('خط مبتدئ من سولو', lang=L)}</div>
  </div>
</section>
"""
    write("ar/solo.html", page("solo.html", "ماكينات سولو للمشاريع الناشئة · SCIL Machinery",
                               "سولو من SCIL: ماكينات نفخ وتعبئة وملصقات وتغليف وطبليات بأسعار ثابتة للمصانع الناشئة.",
                               body, "../solo.html"))


# ------------------------------------------------------------------------ contact
def contact():
    body = f"""
<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="index.html">الرئيسية</a></li><li>تواصل معنا</li></ol>
    <div class="page-head__grid"><h1 class="sign-xl">خطّط خط إنتاجك مع مهندس</h1><p class="lede">المنتج وحجم العبوة والطاقة المطلوبة تكفي للبدء. نرد عليك بمخطط مقترح وقائمة بالماكينات.</p></div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap hq">
    <div class="hq__main">{enquiry_form(lang=L)}</div>
    <aside class="hq__side" aria-label="تواصل مباشر">
      <a class="channel" href="https://wa.me/{D.WHATSAPP}" rel="noopener"><span class="channel__ic">{icon('chat')}</span><span><b>واتساب</b><span dir="ltr">{D.WHATSAPP_DISPLAY}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="{D.PHONE_HREF}"><span class="channel__ic">{icon('phone')}</span><span><b>اتصل بسوجو</b><span dir="ltr">{D.PHONE}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="mailto:{D.EMAIL}"><span class="channel__ic">{icon('mail')}</span><span><b>البريد الإلكتروني</b><span>{D.EMAIL}</span></span>{icon('arrow-ur')}</a>
      <a class="channel" href="mailto:{D.EMAIL_PARTS}"><span class="channel__ic">{icon('grid')}</span><span><b>قطع الغيار</b><span>{D.EMAIL_PARTS}</span></span>{icon('arrow-ur')}</a>
      <div class="channel" style="grid-template-columns:96px 1fr"><img src="{B}assets/img/brand/wechat-qr.jpg" alt="رمز QR على وي تشات" width="96" height="96" style="width:96px;height:96px;object-fit:cover;object-position:center 38%;background:#fff;padding:4px"><span><b>وي تشات</b><span>امسح الرمز لإضافتنا</span></span></div>
      <div style="margin-top:36px">
        <h2 class="sign-s" style="margin-bottom:10px">المقر الرئيسي</h2>
        <address class="prose" style="font-style:normal" dir="ltr">SCIL Machinery<br>{'<br>'.join(D.ADDRESS)}</address>
        <p><a class="link-arrow" href="https://www.openstreetmap.org/search?query=FengHuang%20Town%20Zhangjiagang%20Suzhou" rel="noopener">افتح الخريطة {icon('arrow-ur')}</a></p>
        <h2 class="sign-s" style="margin:32px 0 10px">الوكيل في الجزائر</h2>
        <p class="prose">Solution Plus<br>Mekacher Abderrahmane</p>
      </div>
    </aside>
  </div>
</section>
"""
    write("ar/contact.html", page("contact.html", "تواصل معنا · SCIL Machinery",
                                  "تواصل مع SCIL Machinery في سوجو: طلبات خطوط الإنتاج وعروض الأسعار والخدمة وقطع الغيار عبر واتساب أو الهاتف أو وي تشات أو البريد.",
                                  body, "../contact.html"))


def build_all():
    home(); equipment(); services(); about(); solo(); contact()
    for m in D.MACHINES:
        machine_page(m)
    print("built", 6 + len(D.MACHINES), "Arabic pages")


if __name__ == "__main__":
    build_all()
