"""Shared page parts: head, gantry (nav), footer, icons and the container token drawings."""
from html import escape as e
import data as D

ICONS = {
    "arrow": '<path d="M4 12h15M13 6l6 6-6 6"/>',
    "arrow-ur": '<path d="M7 17L17 7M8 7h9v9"/>',
    "arrow-l": '<path d="M20 12H5M11 6l-6 6 6 6"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "chat": '<path d="M4 20l1.6-4.2A8 8 0 1 1 9 19.3L4 20z"/><path d="M9 10.5c.6 2 2.2 3.6 4.5 4.5"/>',
    "mail": '<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>',
    "download": '<path d="M12 3v12M7 10l5 5 5-5M4 20h16"/>',
    "menu": '<path d="M3 7h18M3 12h18M3 17h18"/>',
    "close": '<path d="M5 5l14 14M19 5L5 19"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><path d="M12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z"/>',
    "check": '<path d="M4 12.5l5 5L20 6.5"/>',
    "grid": '<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>',
    "wechat": '<path d="M9.5 4C5.4 4 2 6.8 2 10.2c0 1.9 1 3.6 2.7 4.7L4 17.5l2.9-1.5c.8.2 1.7.4 2.6.4"/><path d="M15.5 9C12 9 9 11.3 9 14.2s3 5.2 6.5 5.2c.7 0 1.4-.1 2-.3l2.5 1.4-.6-2.3c1.6-1 2.6-2.4 2.6-4 0-2.9-3-5.2-6.5-5.2z"/>',
    "linkedin": '<path d="M4 9h3.5v11H4zM5.8 4.2a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6zM10 9h3.3v1.6c.5-1 1.8-1.9 3.6-1.9 3.4 0 4.1 2.2 4.1 5.2V20h-3.5v-5.4c0-1.3 0-3-1.8-3s-2.2 1.4-2.2 2.9V20H10z"/>',
    "youtube": '<path d="M21.5 7.5a2.6 2.6 0 0 0-1.8-1.8C18 5.2 12 5.2 12 5.2s-6 0-7.7.5A2.6 2.6 0 0 0 2.5 7.5 27 27 0 0 0 2 12a27 27 0 0 0 .5 4.5 2.6 2.6 0 0 0 1.8 1.8c1.7.5 7.7.5 7.7.5s6 0 7.7-.5a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.5-4.5z"/><path d="M10 15l5-3-5-3z"/>',
    "facebook": '<path d="M14 21v-8h3l.5-3.5H14V7.6c0-1 .3-1.7 1.8-1.7h1.8V2.8A24 24 0 0 0 15 2.6c-2.6 0-4.4 1.6-4.4 4.5v2.4H7.7V13h2.9v8"/>',
    "instagram": '<path d="M4 4h16v16H4z"/><path d="M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM17 7h.01"/>',
    "x": '<path d="M4 4l16 16M20 4L4 20"/>',
}


def icon(name, cls=""):
    extra = " i-arrow" if name == "arrow" else (" i-dir" if name in ("arrow-l", "arrow-ur") else "")
    return f'<svg class="i{extra} {cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


# ---- Container token drawings. One sprite per page, referenced with <use>. ----
SPRITE = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
 <defs>
  <clipPath id="clip-bottle"><path d="M134 80C134 112 92 130 92 166v62q8 10 0 20v92c0 30 8 44 26 44h64c18 0 26-14 26-44v-92q-8-10 0-20v-62c0-36-42-54-42-86z"/></clipPath>
  <symbol id="tk-preform" viewBox="0 0 300 400">
    <path d="M122 124l2 216c0 30 10 44 26 44s26-14 26-44l2-216z" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M140 140v190" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
    <rect x="104" y="112" width="92" height="12" fill="#1d58a6" stroke="#141716" stroke-width="3"/>
    <rect x="114" y="98" width="72" height="12" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <rect x="118" y="44" width="64" height="54" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M118 58l64 6M118 72l64 6M118 86l64 6" stroke="#141716" stroke-width="2.5"/>
    <path d="M70 392h160" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-bottle-shape" viewBox="0 0 300 400">
    <path d="M134 80C134 112 92 130 92 166v62q8 10 0 20v92c0 30 8 44 26 44h64c18 0 26-14 26-44v-92q-8-10 0-20v-62c0-36-42-54-42-86z" fill="rgba(201,217,238,.45)" stroke="#141716" stroke-width="3"/>
    <rect x="124" y="70" width="52" height="10" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <rect x="132" y="34" width="36" height="36" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M132 46l36 4M132 58l36 4" stroke="#141716" stroke-width="2.5"/>
    <path d="M110 176v150" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".9"/>
    <path d="M92 228q8 10 0 20M208 228q-8 10 0 20" fill="none" stroke="#141716" stroke-width="3"/>
    <path d="M70 392h160" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-bottle" viewBox="0 0 300 400"><use href="#tk-bottle-shape"/></symbol>
  <symbol id="tk-filled" viewBox="0 0 300 400">
    <g clip-path="url(#clip-bottle)"><path d="M60 150q30-10 60 0t60 0 60 0V400H60z" fill="#7fb0e6"/></g>
    <use href="#tk-bottle-shape"/>
    <rect x="128" y="22" width="44" height="50" fill="#1d58a6" stroke="#141716" stroke-width="3"/>
    <path d="M136 22v50M146 22v50M156 22v50M164 22v50" stroke="#141716" stroke-width="1.5" opacity=".55"/>
  </symbol>
  <symbol id="tk-labelled" viewBox="0 0 300 400">
    <use href="#tk-filled"/>
    <rect x="92" y="258" width="116" height="74" fill="#f4f5f1" stroke="#141716" stroke-width="3"/>
    <path d="M106 278h60M106 292h88M106 306h44" stroke="#1d58a6" stroke-width="5"/>
  </symbol>
  <symbol id="tk-mini" viewBox="0 0 120 220">
    <g transform="scale(.4) translate(0 150)"><use href="#tk-labelled" width="300" height="400"/></g>
  </symbol>
  <symbol id="tk-pack" viewBox="0 0 300 400">
    <g transform="translate(36 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(86 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(136 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(14 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(64 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(114 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <path d="M40 176c0-14 8-18 20-18h170c14 0 24 4 24 18v190c0 12-8 18-20 18H60c-12 0-20-6-20-18z" fill="rgba(255,255,255,.28)" stroke="#141716" stroke-width="3"/>
    <path d="M58 200c40 10 140 10 180 0M58 360c40 8 140 8 180 0" stroke="#fff" stroke-width="4" opacity=".7" fill="none"/>
    <path d="M30 392h240" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-pallet" viewBox="0 0 300 400">
    <g stroke="#141716" stroke-width="3">
      <rect x="34" y="350" width="232" height="12" fill="#f4f5f1"/>
      <rect x="40" y="362" width="28" height="18" fill="#f4f5f1"/><rect x="136" y="362" width="28" height="18" fill="#f4f5f1"/><rect x="232" y="362" width="28" height="18" fill="#f4f5f1"/>
      <rect x="34" y="380" width="232" height="10" fill="#f4f5f1"/>
      <g fill="#cfe5d6">
        <rect x="40" y="280" width="72" height="70"/><rect x="112" y="280" width="76" height="70"/><rect x="188" y="280" width="72" height="70"/>
        <rect x="40" y="210" width="72" height="70"/><rect x="112" y="210" width="76" height="70"/><rect x="188" y="210" width="72" height="70"/>
        <rect x="40" y="140" width="72" height="70"/><rect x="112" y="140" width="76" height="70"/><rect x="188" y="140" width="72" height="70"/>
      </g>
    </g>
    <path d="M40 140h220v210H40z" fill="none" stroke="#11784a" stroke-width="5"/>
    <path d="M40 186l220-34M40 246l220-34M40 306l220-34M40 346l220-34" stroke="#11784a" stroke-width="2" opacity=".55"/>
    <path d="M62 300h28M134 300h32M210 300h28M62 230h28M134 230h32M210 230h28M62 160h28M134 160h32M210 160h28" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-water" viewBox="0 0 300 400">
    <g stroke="#141716" stroke-width="3">
      <rect x="40" y="150" width="56" height="230" rx="28" fill="#c9d9ee"/>
      <rect x="122" y="110" width="56" height="270" rx="28" fill="#c9d9ee"/>
      <rect x="204" y="190" width="56" height="190" rx="28" fill="#7fb0e6"/>
      <path d="M96 200h26M178 240h26" fill="none"/>
    </g>
    <path d="M30 392h240" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-pallet-mini" viewBox="0 0 64 56">
    <g fill="none" stroke="currentColor" stroke-width="3"><path d="M4 44h56M8 52h48M10 44v8M32 44v8M54 44v8"/><path d="M8 8h48v36H8zM8 26h48M32 8v36"/></g>
  </symbol>
 </defs>
</svg>
"""


def token(name, cls="", label=None):
    lab = f' role="img" aria-label="{e(label)}"' if label else ' aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="0 0 300 400"{lab}><use href="#tk-{name}"/></svg>'


NAV_KEYS = ["index.html", "equipment.html", "services.html", "solo.html", "about.html", "contact.html"]

UI = {
    "en": dict(
        nav=["The line", "Equipment", "Services", "SOLO", "About", "Contact"],
        skip="Skip to content", home_label="SCIL Machinery, home", brand_txt="Beverage packaging lines<br>Suzhou · since 2003",
        cta="Plan my line", menu="Menu", lang_name="English", other_lang="العربية", other_code="ar",
        footer_big="Preform to pallet.<br>One supplier.", hq="SCIL Machinery Headquarters",
        qr_alt="WeChat QR code for SCIL Machinery", qr_txt="Scan to add us<br>on WeChat",
        talk="Talk to us", whatsapp="WhatsApp", agent="Agent · Algeria", agent_txt="Solution Plus<br>Mekacher Abderrahmane",
        the_line="The line", water="00 Water treatment", company="Company",
        f_links=["Services &amp; spare parts", "SOLO start-up machines", "About SCIL", "Contact", "Download catalogue (PDF)"],
        rights="© 2026 SCIL Machinery. All rights reserved.", language="Language",
        # form
        f_product="What do you bottle?", f_products=["Water", "Carbonated drinks", "Juice / tea", "Edible oil", "Homecare / chemicals", "5-gallon water", "Other"],
        f_product_err="Choose a product so we can size the line.",
        f_size="Container size", f_size_ph="e.g. 330 ml, 1.5 L, 5 gal", f_out="Target output", f_out_ph="e.g. 6,000 BPH",
        f_machine="Machine or stage you need", f_machine_ph="Complete line, or e.g. blowing + filling",
        f_name="Your name", f_name_err="Tell us who to reply to.", f_country="Country",
        f_reply="Email or WhatsApp number", f_reply_err="Add an email address or phone number so we can answer.",
        f_notes="Anything else", f_notes_ph="New plant or expansion? Timeline? Existing machines?",
        f_send_email="Send by email", f_send_wa="Send on WhatsApp",
        f_note="Opens your email app or WhatsApp with the enquiry written out, ready to send. Nothing is stored on this site.",
        js=dict(title="Line enquiry from scil-machinery.com", product="Product", size="Container size", output="Target output",
                machine="Machine / stage", country="Country", name="Name", reply="Reply to", subject="Line enquiry",
                wa_done="WhatsApp opened with your enquiry written out. Press send there and an engineer will reply.",
                email_done="Your email app should open with the enquiry ready to send. If nothing opened, write to {email} or use WhatsApp."),
    ),
    "ar": dict(
        nav=["خط الإنتاج", "الماكينات", "الخدمات", "سولو", "عن الشركة", "تواصل معنا"],
        skip="انتقل إلى المحتوى", home_label="SCIL Machinery، الصفحة الرئيسية", brand_txt="خطوط تعبئة وتغليف المشروبات<br>سوجو · منذ 2003",
        cta="خطّط خط إنتاجك", menu="القائمة", lang_name="العربية", other_lang="English", other_code="en",
        footer_big="من البريفورم إلى الطبلية.<br>مورّد واحد.", hq="المقر الرئيسي لشركة SCIL Machinery",
        qr_alt="رمز QR لإضافة SCIL Machinery على وي تشات", qr_txt="امسح الرمز لإضافتنا<br>على وي تشات",
        talk="تواصل معنا", whatsapp="واتساب", agent="الوكيل في الجزائر", agent_txt="Solution Plus<br>Mekacher Abderrahmane",
        the_line="خط الإنتاج", water="00 معالجة المياه", company="الشركة",
        f_links=["الخدمات وقطع الغيار", "ماكينات سولو للمشاريع الناشئة", "عن SCIL", "تواصل معنا", "تحميل الكتالوج (PDF)"],
        rights="© 2026 SCIL Machinery. جميع الحقوق محفوظة.", language="اللغة",
        f_product="ماذا تعبّئ؟", f_products=["مياه", "مشروبات غازية", "عصائر / شاي", "زيت طعام", "منظفات / كيماويات", "مياه 5 جالون", "أخرى"],
        f_product_err="اختر المنتج لنحدد حجم الخط المناسب.",
        f_size="حجم العبوة", f_size_ph="مثل 330 مل، 1.5 لتر، 5 جالون", f_out="الطاقة الإنتاجية المطلوبة", f_out_ph="مثل 6,000 عبوة/ساعة",
        f_machine="الماكينة أو المرحلة المطلوبة", f_machine_ph="خط كامل، أو مثلًا: نفخ + تعبئة",
        f_name="الاسم", f_name_err="أخبرنا باسمك لنرد عليك.", f_country="الدولة",
        f_reply="البريد الإلكتروني أو رقم واتساب", f_reply_err="أضف بريدًا إلكترونيًا أو رقم هاتف لنتمكن من الرد.",
        f_notes="ملاحظات أخرى", f_notes_ph="مصنع جديد أم توسعة؟ متى تريد البدء؟ ما الماكينات الموجودة لديك؟",
        f_send_email="أرسل بالبريد", f_send_wa="أرسل عبر واتساب",
        f_note="يفتح تطبيق البريد أو واتساب وفيه طلبك مكتوبًا وجاهزًا للإرسال. لا يحفظ الموقع أي بيانات.",
        js=dict(title="طلب خط إنتاج من موقع scil-machinery.com", product="المنتج", size="حجم العبوة", output="الطاقة المطلوبة",
                machine="الماكينة / المرحلة", country="الدولة", name="الاسم", reply="للرد", subject="طلب خط إنتاج",
                wa_done="فُتح واتساب وفيه طلبك مكتوبًا. اضغط إرسال، وسيرد عليك أحد مهندسينا.",
                email_done="سيفتح تطبيق البريد وفيه طلبك جاهزًا للإرسال. إن لم يُفتح، راسلنا على {email} أو عبر واتساب."),
    ),
}

FONTS = ("https://fonts.googleapis.com/css2?family=Big+Shoulders:opsz,wght@10..72,600..900"
         "&family=Big+Shoulders+Stencil:opsz,wght@10..72,800"
         "&family=Overpass:ital,wght@0,400..800;1,400"
         "&family=Overpass+Mono:wght@400;600&display=swap")
FONTS_AR = ("https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@600..900"
            "&family=Readex+Pro:wght@300..700&display=swap")


def head(title, desc, b="", lang="en", alt=None):
    u = UI[lang]
    rtl = ' dir="rtl"' if lang == "ar" else ' dir="ltr"'
    alt_link = f'<link rel="alternate" hreflang="{u["other_code"]}" href="{alt}">\n' if alt else ""
    fonts_ar = f'<link rel="stylesheet" href="{FONTS_AR}">\n' if lang == "ar" else ""
    return f"""<!doctype html>
<html lang="{lang}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#cfd3cd">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'ar_AR' if lang == 'ar' else 'en_US'}">
<meta property="og:image" content="{b}assets/img/products/m34.jpg">
{alt_link}<link rel="icon" href="{b}assets/img/brand/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
{fonts_ar}<link rel="stylesheet" href="{b}assets/css/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">{u['skip']}</a>
{SPRITE}"""


def gantry(active, b="", lang="en", alt="", lb=None):
    u = UI[lang]
    lb = b if lb is None else lb
    items = "".join(
        f'<li><a href="{lb}{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in zip(NAV_KEYS, u["nav"]))
    other_attr = f'lang="{u["other_code"]}" hreflang="{u["other_code"]}"'
    items += f'<li class="lang-li"><a href="{alt}" {other_attr}>{u["other_lang"]}</a></li>'
    return f"""
<header class="gantry" data-gantry>
  <div class="wrap gantry__in">
    <a class="brand" href="{lb}index.html" aria-label="{u['home_label']}">
      <span class="brand__plate"><img src="{b}assets/img/brand/logo350.png" alt="SCIL" width="77" height="34"></span>
      <span class="brand__txt">{u['brand_txt']}</span>
    </a>
    <nav aria-label="{u['menu']}"><ul class="zones" id="zones">{items}</ul></nav>
    <div class="gantry__call">
      <a class="lang-switch" href="{alt}" {other_attr}>{u['other_lang']}</a>
      <a class="gantry__tel" href="{D.PHONE_HREF}" dir="ltr">{D.PHONE}</a>
      <a class="btn btn--small" href="{lb}contact.html">{u['cta']} {icon("arrow")}</a>
    </div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="zones" data-menu>
      <span class="visually-hidden">{u['menu']}</span>{icon("menu", "i-open")}
    </button>
  </div>
</header>
<main id="main">"""


def footer(b="", lang="en", lb=None, stations=None, alt=""):
    u = UI[lang]
    lb = b if lb is None else lb
    stations = stations or D.STATIONS
    soc = "".join(f'<a href="{url}" rel="noopener" target="_blank" aria-label="{e(n)}">{icon(k)}</a>' for n, url, k in D.SOCIAL)
    fl = u["f_links"]
    other_attr = f'lang="{u["other_code"]}" hreflang="{u["other_code"]}"'
    return f"""
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <p class="footer__big">{u['footer_big']}</p>
        <address>{u['hq']}<br>{"<br>".join(D.ADDRESS)}</address>
        <div class="footer__qr">
          <img src="{b}assets/img/brand/wechat-qr.jpg" alt="{u['qr_alt']}" width="92" height="92" loading="lazy">
          <p class="meta" style="margin:0">{u['qr_txt']}</p>
        </div>
      </div>
      <div>
        <h2>{u['talk']}</h2>
        <ul>
          <li><a href="{D.PHONE_HREF}" dir="ltr">{D.PHONE}</a></li>
          <li><a href="https://wa.me/{D.WHATSAPP}" rel="noopener">{u['whatsapp']} <span dir="ltr">{D.WHATSAPP_DISPLAY}</span></a></li>
          <li><a href="mailto:{D.EMAIL}">{D.EMAIL}</a></li>
          <li><a href="mailto:{D.EMAIL_SALES}">{D.EMAIL_SALES}</a></li>
        </ul>
        <h2 style="margin-top:28px">{u['agent']}</h2>
        <p style="margin:0">{u['agent_txt']}</p>
      </div>
      <div>
        <h2>{u['the_line']}</h2>
        <ul>
          {"".join(f'<li><a href="{lb}equipment.html#{s["key"]}">{s["no"]} {e(s["name"])}</a></li>' for s in stations)}
          <li><a href="{lb}equipment.html#water-treatment">{u['water']}</a></li>
        </ul>
      </div>
      <div>
        <h2>{u['company']}</h2>
        <ul>
          <li><a href="{lb}services.html">{fl[0]}</a></li>
          <li><a href="{lb}solo.html">{fl[1]}</a></li>
          <li><a href="{lb}about.html">{fl[2]}</a></li>
          <li><a href="{lb}contact.html">{fl[3]}</a></li>
          <li><a href="{D.CATALOGUE}" rel="noopener">{fl[4]}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__base">
      <span>{u['rights']}</span>
      <nav aria-label="{u['language']}"><a href="{alt}" {other_attr}>{u['other_lang']}</a><a href="https://scil-machinery.com/cn/site/index" lang="zh" hreflang="zh">中文</a></nav>
      <div class="social">{soc}</div>
    </div>
  </div>
</footer>
<script src="{b}assets/js/site.js" defer></script>
</body>
</html>
"""


def mcard(m, b="", heading="h4", lang="en", lb=None):
    mid, slug, st, name, fig, summ = m
    lb = b if lb is None else lb
    if lang == "ar":
        import ar_data as A
        name, fig, summ = A.MACHINES[mid][:3]
    img = machine_img(mid)
    return f"""<a class="mcard footprint" href="{lb}equipment/{slug}.html">
  <div class="plate">
    <div class="mcard__img"><img class="photo-mult" src="{b}assets/img/products/{img}" alt="" loading="lazy" width="850" height="690"></div>
    <span class="mcard__fig">{e(fig)}</span>
    <{heading}>{e(name)}</{heading}>
    <p>{e(summ)}</p>
  </div>
</a>"""


import os, json
_IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "img", "products")


def machine_img(mid):
    for ext in (".jpg", ".jpeg", ".png"):
        if os.path.exists(os.path.join(_IMG_DIR, f"m{mid}{ext}")):
            return f"m{mid}{ext}"
    return "m34.jpg"


def enquiry_form(machine_name="", lang="en"):
    u = UI[lang]
    chips = "".join(
        f'<label><input type="radio" name="product" value="{e(lbl)}"{" required" if i == 0 else ""}><span>{e(lbl)}</span></label>'
        for i, lbl in enumerate(u["f_products"]))
    js = e(json.dumps(dict(u["js"], email=D.EMAIL, wa=D.WHATSAPP), ensure_ascii=False))
    return f"""<form class="form" data-enquiry data-i18n="{js}" action="mailto:{D.EMAIL}" method="post" enctype="text/plain" novalidate>
  <fieldset class="field full chips" data-field="product">
    <legend>{u['f_product']}</legend>
    {chips}
    <span class="err">{u['f_product_err']}</span>
  </fieldset>
  <div class="field">
    <label for="f-size">{u['f_size']}</label>
    <input id="f-size" name="size" placeholder="{u['f_size_ph']}" autocomplete="off">
  </div>
  <div class="field">
    <label for="f-out">{u['f_out']}</label>
    <input id="f-out" name="output" inputmode="numeric" placeholder="{u['f_out_ph']}">
  </div>
  <div class="field full">
    <label for="f-machine">{u['f_machine']}</label>
    <input id="f-machine" name="machine" value="{e(machine_name)}" placeholder="{u['f_machine_ph']}">
  </div>
  <div class="field" data-field="name">
    <label for="f-name">{u['f_name']}</label>
    <input id="f-name" name="name" autocomplete="name" required>
    <span class="err">{u['f_name_err']}</span>
  </div>
  <div class="field">
    <label for="f-country">{u['f_country']}</label>
    <input id="f-country" name="country" autocomplete="country-name">
  </div>
  <div class="field full" data-field="reply">
    <label for="f-reply">{u['f_reply']}</label>
    <input id="f-reply" name="reply" autocomplete="email" required dir="auto">
    <span class="err">{u['f_reply_err']}</span>
  </div>
  <div class="field full">
    <label for="f-notes">{u['f_notes']}</label>
    <textarea id="f-notes" name="notes" placeholder="{u['f_notes_ph']}"></textarea>
  </div>
  <div class="full form__actions">
    <button class="btn" type="submit" data-via="email">{u['f_send_email']} {icon("mail")}</button>
    <button class="btn btn--ink" type="submit" data-via="whatsapp">{u['f_send_wa']} {icon("chat")}</button>
  </div>
  <p class="full form__note">{u['f_note']}</p>
  <p class="form__status" role="status" aria-live="polite"></p>
</form>"""
