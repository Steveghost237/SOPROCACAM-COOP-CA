/* ==========================================================================
   SOPROCACAM COOP-CA – Main JavaScript
   ========================================================================== */

'use strict';

/* ==========================================================================
   HEADER SCROLL BEHAVIOR
   ========================================================================== */
function initHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  function updateHeader() {
    if (window.scrollY > 80) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', updateHeader, { passive: true });
  updateHeader();
}

/* ==========================================================================
   MOBILE MENU
   ========================================================================== */
function initMobileMenu() {
  const burger = document.querySelector('.burger');
  const menu = document.querySelector('.mobile-menu');
  const overlay = document.querySelector('.mobile-menu-overlay');

  if (!burger || !menu) return;

  function openMenu() {
    burger.classList.add('open');
    menu.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    burger.classList.remove('open');
    menu.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  burger.addEventListener('click', () => {
    if (menu.classList.contains('open')) closeMenu();
    else openMenu();
  });

  if (overlay) overlay.addEventListener('click', closeMenu);

  // Close on ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

/* ==========================================================================
   HERO CAROUSEL
   ========================================================================== */
function initCarousel() {
  const carousel = document.querySelector('.carousel');
  if (!carousel) return;

  const slides = carousel.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  const prevBtn = document.querySelector('.carousel-chevron.prev');
  const nextBtn = document.querySelector('.carousel-chevron.next');

  if (!slides.length) return;

  let current = 0;
  let timer = null;
  let paused = false;

  function goTo(index) {
    const prev = current;
    slides[prev].classList.remove('active');
    if (dots[prev]) {
      dots[prev].classList.remove('active');
      dots[prev].setAttribute('aria-selected', 'false');
    }

    current = (index + slides.length) % slides.length;

    // Re-trigger animations by briefly removing then re-adding active
    slides[current].classList.add('active');
    if (dots[current]) {
      dots[current].classList.add('active');
      dots[current].setAttribute('aria-selected', 'true');
    }
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
      if (!paused) next();
    }, 6000);
  }

  // Init first slide
  slides[0].classList.add('active');
  if (dots[0]) dots[0].classList.add('active');

  // Dot click
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      goTo(i);
      startTimer();
    });
  });

  // Chevron click
  if (prevBtn) prevBtn.addEventListener('click', () => { prev(); startTimer(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { next(); startTimer(); });

  // Keyboard
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') { prev(); startTimer(); }
    if (e.key === 'ArrowRight') { next(); startTimer(); }
  });

  // Touch / swipe
  let touchStartX = 0;
  carousel.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });
  carousel.addEventListener('touchend', (e) => {
    const diff = touchStartX - e.changedTouches[0].screenX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) next(); else prev();
      startTimer();
    }
  }, { passive: true });

  // Pause on hover
  carousel.addEventListener('mouseenter', () => { paused = true; });
  carousel.addEventListener('mouseleave', () => { paused = false; });

  startTimer();
}

/* ==========================================================================
   PRODUCTS CAROUSEL (circular thumbnails)
   ========================================================================== */
function initProductsCarousel() {
  const wrap = document.querySelector('.products-carousel-wrap');
  if (!wrap) return;

  const track = wrap.querySelector('.products-carousel');
  const cards = track ? track.querySelectorAll('.product-card') : [];
  const prevBtn = wrap.parentElement.querySelector('.products-nav .prev');
  const nextBtn = wrap.parentElement.querySelector('.products-nav .next');

  if (!cards.length) return;

  let offset = 0;
  const cardWidth = 228; // 200 + 28 gap

  function getVisible() {
    return Math.floor(wrap.offsetWidth / cardWidth);
  }

  function update() {
    const maxOffset = Math.max(0, (cards.length - getVisible()) * cardWidth);
    offset = Math.max(0, Math.min(offset, maxOffset));
    track.style.transform = `translateX(-${offset}px)`;
  }

  if (prevBtn) prevBtn.addEventListener('click', () => { offset -= cardWidth; update(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { offset += cardWidth; update(); });

  // Auto-scroll
  setInterval(() => {
    const maxOffset = Math.max(0, (cards.length - getVisible()) * cardWidth);
    if (offset >= maxOffset) offset = 0;
    else offset += cardWidth;
    update();
  }, 4000);
}

/* ==========================================================================
   ANIMATED COUNTERS
   ========================================================================== */
function initCounters() {
  const counters = document.querySelectorAll('.stat-count');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.animated) {
        entry.target.dataset.animated = 'true';
        animateCounter(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

function animateCounter(el) {
  const target = parseInt(el.dataset.target || el.textContent, 10);
  const duration = 1800;
  const start = performance.now();

  function step(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = Math.round(eased * target);
    el.textContent = value;
    if (progress < 1) requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
}

/* ==========================================================================
   SCROLL ANIMATIONS
   ========================================================================== */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  elements.forEach(el => observer.observe(el));
}

/* ==========================================================================
   FAQ ACCORDION
   ========================================================================== */
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (!question || !answer) return;

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all
      faqItems.forEach(i => {
        i.classList.remove('open');
        const a = i.querySelector('.faq-answer');
        if (a) a.style.maxHeight = '0';
      });

      // Open clicked if was closed
      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
}

/* ==========================================================================
   FORM HANDLING — CodingMailer (codingmailer.onrender.com)
   Aucun compte requis. Envoie vers info@soprocacam.com.
   ========================================================================== */
function initForms() {
  document.querySelectorAll('form[data-sopro]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const success  = form.querySelector('.form-success');
      const errorDiv = form.querySelector('.form-error');
      const btn      = form.querySelector('[type="submit"]');

      // Validation des champs requis
      let valid = true;
      form.querySelectorAll('[required]').forEach(field => {
        if (!field.value.trim()) {
          field.style.borderColor = '#cc0000';
          valid = false;
        } else {
          field.style.borderColor = '';
        }
      });
      if (!valid) return;

      // État chargement
      const btnText = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Envoi en cours…'; }
      if (success)  success.style.display  = 'none';
      if (errorDiv) errorDiv.style.display = 'none';

      // Lecture des champs
      const g = n => form.querySelector(`[name="${n}"]`)?.value?.trim() || '';
      const formType = g('_form_type') || 'contact';
      const dateFr = new Date().toLocaleString('fr-FR');

      /* ---- Construction des données selon le type ---- */
      let subject, rows, nomExp;

      if (formType === 'partenaire') {
        nomExp  = g('nom_complet');
        subject = `Demande de partenariat — ${nomExp} | SOPROCACAM`;
        rows = [
          ['Nom et prénom',     g('nom_complet')   || '—'],
          ['Téléphone',         g('telephone')      || '—'],
          ['E-mail',            g('email')],
          ['Localité / Région', g('localite')       || '—'],
          ['Profil',            g('vous_etes')      || '—'],
          ['Message',           (g('message')       || '(aucun message)').replace(/\n/g, '<br>')],
        ];
      } else {
        nomExp  = g('prenom') + ' ' + g('nom');
        subject = `Demande de devis — ${nomExp} | SOPROCACAM`;
        rows = [
          ['Prénom',            g('prenom')],
          ['Nom',               g('nom')],
          ['Entreprise',        g('entreprise')     || '—'],
          ['Pays',              g('pays')           || '—'],
          ['E-mail',            g('email')],
          ['Téléphone',         g('telephone')      || '—'],
          ['Produit souhaité',  g('produit')        || '—'],
          ['Quantité',          g('quantite')       || '—'],
          ['Destination',       g('destination')    || '—'],
          ['Message',           (g('message')       || '(aucun message)').replace(/\n/g, '<br>')],
        ];
      }

      /* ---- Couleurs SOPROCACAM ---- */
      const C = { choc:'#512616', gold:'#C8953A', cream:'#fdf6ef', border:'#f0e0cc', dark:'#3a1a0a', text:'#2d2d2d' };
      const badge = formType === 'partenaire' ? '#2E7D32' : C.choc;
      const typeLabel = formType === 'partenaire' ? 'Demande de partenariat' : 'Demande de devis / Contact';

      /* ---- Lignes du tableau ---- */
      const rowsHtml = rows.map(([label, val]) => `
        <tr>
          <td style="padding:10px 16px;background:${C.cream};color:${C.gold};font-weight:700;font-size:11px;
                     text-transform:uppercase;letter-spacing:.6px;border-bottom:1px solid ${C.border};
                     white-space:nowrap;width:170px;font-family:Arial,sans-serif;">${label}</td>
          <td style="padding:10px 16px;color:${C.text};font-size:14px;border-bottom:1px solid ${C.border};
                     line-height:1.6;font-family:Arial,sans-serif;">${val}</td>
        </tr>`).join('');

      /* ---- Template HTML email ---- */
      const html = `<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f4f1ee;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f4f1ee;padding:32px 16px;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" border="0"
       style="max-width:600px;width:100%;border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);">

  <!-- EN-TÊTE CHOCOLAT -->
  <tr><td style="background:${C.choc};padding:32px 40px;text-align:center;">
    <div style="width:64px;height:64px;background:rgba(255,255,255,.15);border-radius:50%;
                border:3px solid rgba(255,255,255,.3);margin:0 auto 14px;display:flex;
                align-items:center;justify-content:center;">
      <span style="color:${C.gold};font-size:28px;font-weight:900;letter-spacing:-1px;">S</span>
    </div>
    <h1 style="margin:0;color:#fff;font-size:22px;font-weight:700;letter-spacing:.5px;
               font-family:Arial,sans-serif;">SOPROCACAM COOP-CA</h1>
    <p style="margin:6px 0 0;color:rgba(255,255,255,.75);font-size:12px;font-family:Arial,sans-serif;">
      Trader &amp; Exportateur agr&eacute;&eacute; &mdash; Membre du GEX &mdash; Douala, Cameroun
    </p>
  </td></tr>

  <!-- BADGE TYPE -->
  <tr><td style="background:#fff;padding:20px 40px 0;text-align:center;">
    <span style="display:inline-block;background:${badge};color:#fff;font-size:11px;font-weight:700;
                 text-transform:uppercase;letter-spacing:1px;padding:6px 20px;border-radius:20px;
                 font-family:Arial,sans-serif;">${typeLabel}</span>
  </td></tr>

  <!-- DATE -->
  <tr><td style="background:#fff;padding:14px 40px 20px;">
    <p style="margin:0;font-size:13px;color:#777;border-left:3px solid ${C.gold};padding-left:12px;
              line-height:1.7;font-family:Arial,sans-serif;">
      Re&ccedil;u le <strong>${dateFr}</strong> via
      <a href="https://www.soprocacam.com" style="color:${C.choc};text-decoration:none;">www.soprocacam.com</a>
    </p>
  </td></tr>

  <!-- TABLEAU DES DONNÉES -->
  <tr><td style="background:#fff;padding:0 40px 32px;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="border-radius:8px;overflow:hidden;border:1px solid ${C.border};">
      ${rowsHtml}
    </table>
  </td></tr>

  <!-- BOUTON RÉPONDRE -->
  <tr><td style="background:${C.cream};padding:24px 40px;text-align:center;border-top:2px solid ${C.border};">
    <p style="margin:0 0 14px;color:${C.choc};font-size:14px;font-weight:700;font-family:Arial,sans-serif;">
      R&eacute;pondre &agrave; cette demande&nbsp;:
    </p>
    <a href="mailto:${g('email')}"
       style="display:inline-block;background:${C.choc};color:#fff;text-decoration:none;
              font-size:13px;font-weight:700;padding:13px 30px;border-radius:6px;
              letter-spacing:.5px;font-family:Arial,sans-serif;">
      &#9993;&nbsp; R&eacute;pondre &agrave; ${nomExp.trim()}
    </a>
  </td></tr>

  <!-- PIED DE PAGE -->
  <tr><td style="background:${C.dark};padding:22px 40px;text-align:center;">
    <p style="margin:0 0 6px;color:rgba(255,255,255,.8);font-size:12px;font-family:Arial,sans-serif;">
      <strong style="color:${C.gold};">SOPROCACAM COOP-CA</strong> &mdash;
      Immeuble AXA, rue 309 (rue Franqueville), Akwa, BP&nbsp;6469, Douala, Cameroun
    </p>
    <p style="margin:0;color:rgba(255,255,255,.55);font-size:11px;font-family:Arial,sans-serif;">
      +237&nbsp;673&nbsp;33&nbsp;01&nbsp;01 &nbsp;|&nbsp;
      <a href="mailto:info@soprocacam.com" style="color:${C.gold};">info@soprocacam.com</a>
      &nbsp;|&nbsp;
      <a href="https://www.soprocacam.com" style="color:${C.gold};">www.soprocacam.com</a>
    </p>
    <p style="margin:10px 0 0;color:rgba(255,255,255,.3);font-size:10px;font-family:Arial,sans-serif;">
      Message g&eacute;n&eacute;r&eacute; automatiquement par le formulaire du site web SOPROCACAM.
    </p>
  </td></tr>

</table>
</td></tr></table>
</body></html>`;

      /* ---- Texte brut (fallback) ---- */
      const body = rows.map(([l, v]) => `${l.padEnd(20)}: ${v.replace(/<br>/g,'\n')}`).join('\n')
        + `\n\nReçu depuis : www.soprocacam.com\nDate : ${dateFr}`;

      const payload = JSON.stringify({ to: 'info@soprocacam.com', subject, message: body });
      const sendMail = () => fetch('https://codingmailer.onrender.com/send-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload
      });

      try {
        let response = await sendMail();

        // Render.com free tier : réveil du serveur → réessai automatique après 6s
        if (!response.ok) {
          if (btn) btn.textContent = 'Connexion en cours…';
          await new Promise(r => setTimeout(r, 6000));
          response = await sendMail();
        }

        if (response.ok) {
          if (success) success.style.display = 'block';
          form.reset();
          setTimeout(() => { if (success) success.style.display = 'none'; }, 7000);
        } else {
          if (errorDiv) errorDiv.style.display = 'block';
        }
      } catch (_err) {
        if (errorDiv) errorDiv.style.display = 'block';
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = btnText; }
      }
    });
  });

  // Newsletter
  document.querySelectorAll('.newsletter-form').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('button');
      const prev = btn ? btn.textContent : '';
      if (btn) {
        btn.textContent = 'Envoyé !';
        setTimeout(() => { btn.textContent = prev; form.reset(); }, 3000);
      }
    });
  });
}

/* ==========================================================================
   SMOOTH ACTIVE NAV
   ========================================================================== */
function initActiveNav() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link, .dropdown-link, .mobile-nav-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (href === path || (path === 'index.html' && href === '/') || href.includes(path.replace('.html', ''))) {
      link.classList.add('active');
    }
  });
}

/* ==========================================================================
   LIGHTBOX (gallery)
   ========================================================================== */
function initLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  if (!galleryItems.length) return;

  const lb = document.createElement('div');
  lb.style.cssText = `
    display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.92);
    align-items:center;justify-content:center;cursor:pointer;
  `;
  lb.innerHTML = '<img style="max-width:90vw;max-height:90vh;object-fit:contain;" />';
  document.body.appendChild(lb);

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const src = item.querySelector('img')?.src;
      if (!src) return;
      lb.querySelector('img').src = src;
      lb.style.display = 'flex';
    });
  });

  lb.addEventListener('click', () => { lb.style.display = 'none'; });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') lb.style.display = 'none';
  });
}

/* ==========================================================================
   LANGUAGE SWITCHER (FR / EN) – global, persistent via localStorage
   Two layers:
   1. [data-i18n] elements -> translations.fr / translations.en (nav, footer)
   2. Full-text dict (SOPRO.dict) -> every other text node, alt, placeholder,
      title and <title> translated FR -> EN. Originals are kept so switching
      back to FR restores the page exactly.
   ========================================================================== */
function initLanguage() {
  const btn = document.querySelector('.lang-switcher');
  const T = window.SOPRO && window.SOPRO.translations;
  const dict = (window.SOPRO && window.SOPRO.dict) || {};
  if (!T) return;

  const origNodes = new WeakMap();  /* Text node -> original FR value   */
  const origAttrs = new WeakMap();  /* element   -> {attr: original FR} */
  let origTitle = null;
  let captured = false;

  function getLang() {
    return localStorage.getItem('sopro-lang') || 'fr';
  }

  /* Capture originals once, before any translation */
  function captureOriginals() {
    if (captured) return;
    captured = true;
    origTitle = document.title;

    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) origNodes.set(n, n.nodeValue);

    document.querySelectorAll('[placeholder],[alt],[title]').forEach(el => {
      const m = {};
      ['placeholder', 'alt', 'title'].forEach(a => {
        if (el.hasAttribute(a)) m[a] = el.getAttribute(a);
      });
      origAttrs.set(el, m);
    });

    /* keep the original label of every data-i18n element (for → / ▾) */
    document.querySelectorAll('[data-i18n]').forEach(el => {
      el.dataset.origI18n = el.textContent;
    });
  }

  function norm(s) { return s.replace(/\s+/g, ' ').trim(); }

  function applyLang(lang) {
    captureOriginals();
    const d = T[lang] || {};
    document.documentElement.lang = lang;

    /* Language button label */
    if (btn) {
      btn.textContent = lang === 'fr' ? 'EN' : 'FR';
      btn.setAttribute('aria-label',
        lang === 'fr' ? 'Switch to English' : 'Passer en français');
    }

    /* 1) data-i18n elements (preserves → prefix and ▾ suffix) */
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (d[key] === undefined || el.children.length !== 0) return;
      let v = d[key];
      const orig = el.dataset.origI18n || '';
      if (/^\s*→\s*/.test(orig)) v = '→ ' + v;
      if (/▾\s*$/.test(orig))     v = v + ' ▾';
      el.textContent = v;
    });

    /* 2) Full-text translation of every other text node */
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) {
      const parent = n.parentElement;
      if (!parent) continue;
      if (parent.closest('script,style,[data-i18n]')) continue;
      const orig = origNodes.get(n);
      if (orig === undefined) continue;
      if (lang === 'fr') { n.nodeValue = orig; continue; }
      const tr = dict[norm(orig)];
      if (tr !== undefined) {
        const lead = orig.match(/^\s*/)[0];
        const tail = orig.match(/\s*$/)[0];
        n.nodeValue = lead + tr + tail;
      }
    }

    /* 3) Attributes: placeholder, alt, title */
    document.querySelectorAll('[placeholder],[alt],[title]').forEach(el => {
      const orig = origAttrs.get(el);
      if (!orig) return;
      ['placeholder', 'alt', 'title'].forEach(a => {
        const o = orig[a];
        if (o === undefined) return;
        if (lang === 'fr') { el.setAttribute(a, o); return; }
        const tr = dict[norm(o)];
        if (tr !== undefined) el.setAttribute(a, tr);
      });
    });

    /* 4) <title> */
    if (origTitle !== null) {
      if (lang === 'fr') document.title = origTitle;
      else if (dict[norm(origTitle)]) document.title = dict[norm(origTitle)];
    }

    document.dispatchEvent(new CustomEvent('langChanged', { detail: { lang } }));
  }

  function setLang(lang) {
    localStorage.setItem('sopro-lang', lang);
    applyLang(lang);
  }

  /* Apply saved language immediately */
  applyLang(getLang());

  /* Toggle on click */
  if (btn) {
    btn.addEventListener('click', () => {
      setLang(getLang() === 'fr' ? 'en' : 'fr');
    });
  }
}

/* ==========================================================================
   INIT
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  initLanguage();   /* run first so translations apply as early as possible */
  initHeader();
  initMobileMenu();
  initCarousel();
  initProductsCarousel();
  initCounters();
  initScrollAnimations();
  initFAQ();
  initForms();
  initActiveNav();
  initLightbox();
});
