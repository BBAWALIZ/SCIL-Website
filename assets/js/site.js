/* SCIL Machinery — site behaviour. No dependencies. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- mobile menu ---- */
  const gantry = $('[data-gantry]');
  const menuBtn = $('[data-menu]');
  if (gantry && menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = gantry.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('keydown', (ev) => {
      if (ev.key === 'Escape' && gantry.classList.contains('is-open')) {
        gantry.classList.remove('is-open');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.focus();
      }
    });
  }

  /* ---- walk the line: lane fill + container token ---- */
  const walk = $('[data-walk]');
  if (walk) {
    const stations = $$('.station', walk);
    const fill = $('[data-lane-fill]', walk);
    const states = $$('.token__state', walk);
    const ticks = $$('[data-tick]', walk);
    const outEl = $('[data-token-out]', walk);
    const noEl = $('[data-token-no]', walk);
    const stripUse = $('[data-strip-use]', walk);
    const stripOut = $('[data-strip-out]', walk);
    let current = -1;

    const setStation = (i) => {
      if (i === current || i < 0) return;
      current = i;
      const st = stations[i];
      stations.forEach((s, k) => s.classList.toggle('is-on', k === i));
      ticks.forEach((t, k) => t.classList.toggle('is-on', k <= i));
      states.forEach((s) => s.classList.toggle('is-on', s.dataset.state === st.dataset.token));
      if (outEl) outEl.textContent = st.dataset.out;
      if (noEl) noEl.textContent = `${walk.dataset.leaves || 'Leaves station'} ${st.dataset.station}`;
      if (stripUse) stripUse.setAttribute('href', `#tk-${st.dataset.token}`);
      if (stripOut) stripOut.textContent = `${st.dataset.station} · ${st.dataset.out}`;
    };

    let ticking = false;
    const update = () => {
      ticking = false;
      const r = walk.getBoundingClientRect();
      const vh = innerHeight;
      const p = Math.min(1, Math.max(0, (vh * 0.5 - r.top) / r.height));
      walk.style.setProperty('--p', p.toFixed(4));
      let idx = 0;
      stations.forEach((s, k) => { if (s.getBoundingClientRect().top < vh * 0.55) idx = k; });
      setStation(idx);
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    addEventListener('resize', update);
    update();
  }

  /* ---- gauge (Safira proof): bars fill once they reach the viewport ---- */
  const gauge = $('[data-gauge]');
  if (gauge && !reduce && gauge.getBoundingClientRect().top > innerHeight) {
    gauge.classList.add('is-armed');
    const done = () => {
      gauge.classList.add('is-in');
      removeEventListener('scroll', check);
      removeEventListener('resize', check);
      if (io) io.disconnect();
    };
    const check = () => { if (gauge.getBoundingClientRect().top < innerHeight * 0.9) done(); };
    const io = 'IntersectionObserver' in window
      ? new IntersectionObserver((es) => { if (es.some((en) => en.isIntersecting)) done(); }, { threshold: 0.1 })
      : null;
    if (io) io.observe(gauge);
    addEventListener('scroll', check, { passive: true });
    addEventListener('resize', check);
    addEventListener('load', check);
  }

  /* ---- testimonial tags scroller ---- */
  const row = $('[data-tags-row]');
  $$('[data-tags]').forEach((b) => b.addEventListener('click', () => {
    if (!row) return;
    const card = row.firstElementChild;
    const step = card ? card.getBoundingClientRect().width + 22 : 360;
    row.scrollBy({ left: step * Number(b.dataset.tags), behavior: reduce ? 'auto' : 'smooth' });
  }));

  /* ---- catalogue station selector ---- */
  const selector = $('[data-selector]');
  if (selector && 'IntersectionObserver' in window) {
    const links = $$('a', selector);
    const byKey = Object.fromEntries(links.map((a) => [a.dataset.sel, a]));
    const io = new IntersectionObserver((es) => {
      es.forEach((en) => {
        if (!en.isIntersecting) return;
        links.forEach((a) => a.classList.remove('is-on'));
        const a = byKey[en.target.dataset.cat];
        if (a) {
          a.classList.add('is-on');
          const L = a.offsetLeft - 16;
          selector.scrollTo({ left: L, behavior: reduce ? 'auto' : 'smooth' });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    $$('[data-cat]').forEach((s) => io.observe(s));
  }

  /* ---- enquiry form: compose an email or WhatsApp message ---- */
  const params = new URLSearchParams(location.search);
  const machineSlug = params.get('machine');

  $$('form[data-enquiry]').forEach((form) => {
    let T = {};
    try { T = JSON.parse(form.dataset.i18n || '{}'); } catch (err) { T = {}; }
    const EMAIL = T.email || 'info@scil-machinery.com';
    const WA = T.wa || '8613221284949';
    if (machineSlug) {
      const m = form.querySelector('[name="machine"]');
      if (m && !m.value) {
        m.value = /^[a-z0-9-]+$/.test(machineSlug)
          ? machineSlug.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())
          : machineSlug;
      }
    }
    let via = 'email';
    $$('button[data-via]', form).forEach((b) => b.addEventListener('click', () => { via = b.dataset.via; }));

    const fieldOk = (name) => {
      const wrap = form.querySelector(`[data-field="${name}"]`);
      let ok;
      if (name === 'product') ok = !!form.querySelector('input[name="product"]:checked');
      else ok = (form.elements[name].value || '').trim().length > 1;
      if (wrap) wrap.toggleAttribute('data-invalid', !ok);
      return ok;
    };
    ['name', 'reply'].forEach((n) => form.elements[n].addEventListener('input', () => {
      const w = form.querySelector(`[data-field="${n}"]`);
      if (w && w.hasAttribute('data-invalid')) fieldOk(n);
    }));
    $$('input[name="product"]', form).forEach((r) => r.addEventListener('change', () => fieldOk('product')));

    form.addEventListener('submit', (ev) => {
      ev.preventDefault();
      const ok = ['product', 'name', 'reply'].map(fieldOk).every(Boolean);
      if (!ok) {
        const first = form.querySelector('[data-invalid] input');
        if (first) first.focus();
        return;
      }
      const v = (n) => (form.elements[n] && form.elements[n].value || '').trim();
      const product = (form.querySelector('input[name="product"]:checked') || {}).value || '';
      const opt = (label, n) => (v(n) ? `${label}: ${v(n)}` : null);
      const lines = [
        T.title || 'Line enquiry from scil-machinery.com', '',
        `${T.product || 'Product'}: ${product}`,
        opt(T.size || 'Container size', 'size'), opt(T.output || 'Target output', 'output'),
        opt(T.machine || 'Machine / stage', 'machine'), opt(T.country || 'Country', 'country'), '',
        `${T.name || 'Name'}: ${v('name')}`, `${T.reply || 'Reply to'}: ${v('reply')}`,
        v('notes') ? `\n${v('notes')}` : null,
      ].filter((l) => l !== null);
      const text = lines.join('\n');
      const status = form.querySelector('.form__status');
      if (via === 'whatsapp') {
        window.open(`https://wa.me/${WA}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
        status.textContent = T.wa_done || 'WhatsApp opened with your enquiry written out. Press send there and an engineer will reply.';
      } else {
        const subject = `${T.subject || 'Line enquiry'}: ${product}${v('output') ? ', ' + v('output') : ''}`;
        location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`;
        status.textContent = (T.email_done || 'Your email app should open with the enquiry ready to send. If nothing opened, write to {email} or use WhatsApp.').replace('{email}', EMAIL);
      }
      status.classList.add('is-on');
    });
  });
})();
