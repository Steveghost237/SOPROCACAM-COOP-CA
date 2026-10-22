# -*- coding: utf-8 -*-
"""
update_i18n.py
Adds data-i18n attributes and injects translations.js into all HTML pages
of the SOPROCACAM website.
"""
import os, re

ROOT = r'C:\Users\Albert WIB\Desktop\soprocacam-website'
HTML_FILES = [f for f in os.listdir(ROOT) if f.endswith('.html')]

# Mapping page -> (banner_title_key, banner_sub_key)
PAGE_BANNER = {
    'qui-sommes-nous.html':          ('page.about.title',      'page.about.sub'),
    'cooperative.html':              ('page.coop.title',       'page.coop.sub'),
    'plantations.html':              ('page.plant.title',      'page.plant.sub'),
    'cacao.html':                    ('page.cacao.title',      'page.cacao.sub'),
    'cafe.html':                     ('page.cafe.title',       'page.cafe.sub'),
    'approvisionnement-afrique.html':('page.afrique.title',    'page.afrique.sub'),
    'qualite.html':                  ('page.qualite.title',    'page.qualite.sub'),
    'export.html':                   ('page.export.title',     'page.export.sub'),
    'partenaire.html':               ('page.partner.title',    'page.partner.sub'),
    'engagement.html':               ('page.engagement.title', 'page.engagement.sub'),
    'actualites.html':               ('page.news.title',       'page.news.sub'),
    'faq.html':                      ('page.faq.title',        'page.faq.sub'),
    'contact.html':                  ('page.contact.title',    'page.contact.sub'),
    'mentions-legales.html':         ('page.legal.title',      'page.legal.sub'),
}


def add_i18n(html, filename):
    # ---- Inject translations.js ----------------------------------------
    if 'translations.js' not in html:
        html = html.replace(
            '<script src="js/main.js"></script>',
            '<script src="js/translations.js"></script>\n  <script src="js/main.js"></script>'
        )

    # ---- Logo tagline -----------------------------------------------------
    html = html.replace(
        'class="logo-tagline">Terre G\u00e9n\u00e9reuse',
        'class="logo-tagline" data-i18n="logo.tagline">Terre G\u00e9n\u00e9reuse'
    )
    html = html.replace(
        'class="footer-brand-tag">Terre G\u00e9n\u00e9reuse',
        'class="footer-brand-tag" data-i18n="logo.tagline">Terre G\u00e9n\u00e9reuse'
    )

    # ---- Desktop nav links ------------------------------------------------
    nav_replacements = [
        ('href="index.html" class="nav-link"',
         'href="index.html" class="nav-link" data-i18n="nav.home"'),
        ('href="qui-sommes-nous.html" class="nav-link"',
         'href="qui-sommes-nous.html" class="nav-link" data-i18n="nav.about"'),
        ('href="cooperative.html" class="nav-link"',
         'href="cooperative.html" class="nav-link" data-i18n="nav.cooperative"'),
        ('href="plantations.html" class="nav-link"',
         'href="plantations.html" class="nav-link" data-i18n="nav.plantations"'),
        ('href="qualite.html" class="nav-link"',
         'href="qualite.html" class="nav-link" data-i18n="nav.qualite"'),
        ('href="export.html" class="nav-link"',
         'href="export.html" class="nav-link" data-i18n="nav.export"'),
        # dropdown items
        ('href="cacao.html" class="dropdown-link"',
         'href="cacao.html" class="dropdown-link" data-i18n="nav.cacao"'),
        ('href="cafe.html" class="dropdown-link"',
         'href="cafe.html" class="dropdown-link" data-i18n="nav.cafe"'),
        ('href="approvisionnement-afrique.html" class="dropdown-link"',
         'href="approvisionnement-afrique.html" class="dropdown-link" data-i18n="nav.afrique"'),
        ('href="engagement.html" class="dropdown-link"',
         'href="engagement.html" class="dropdown-link" data-i18n="nav.engagement"'),
        ('href="partenaire.html" class="dropdown-link"',
         'href="partenaire.html" class="dropdown-link" data-i18n="nav.partner"'),
        ('href="actualites.html" class="dropdown-link"',
         'href="actualites.html" class="dropdown-link" data-i18n="nav.news"'),
        ('href="faq.html" class="dropdown-link"',
         'href="faq.html" class="dropdown-link" data-i18n="nav.faq"'),
        ('href="contact.html" class="dropdown-link"',
         'href="contact.html" class="dropdown-link" data-i18n="nav.contact"'),
    ]
    for old, new in nav_replacements:
        html = html.replace(old, new)

    # Dropdown parent labels (Nos produits \u25be / Plus \u25be)
    html = re.sub(
        r'class="nav-link">Nos produits \u25be<',
        'class="nav-link" data-i18n="nav.products">Nos produits \u25be<',
        html
    )
    html = re.sub(
        r'class="nav-link">Plus \u25be<',
        'class="nav-link" data-i18n="nav.more">Plus \u25be<',
        html
    )

    # ---- Mobile nav links -------------------------------------------------
    mobile_replacements = [
        ('href="index.html" class="mobile-nav-link"',
         'href="index.html" class="mobile-nav-link" data-i18n="nav.home"'),
        ('href="qui-sommes-nous.html" class="mobile-nav-link"',
         'href="qui-sommes-nous.html" class="mobile-nav-link" data-i18n="nav.about"'),
        ('href="cooperative.html" class="mobile-nav-link"',
         'href="cooperative.html" class="mobile-nav-link" data-i18n="nav.cooperative"'),
        ('href="plantations.html" class="mobile-nav-link"',
         'href="plantations.html" class="mobile-nav-link" data-i18n="nav.plantations"'),
        ('href="qualite.html" class="mobile-nav-link"',
         'href="qualite.html" class="mobile-nav-link" data-i18n="nav.qualite"'),
        ('href="export.html" class="mobile-nav-link"',
         'href="export.html" class="mobile-nav-link" data-i18n="nav.export"'),
        ('href="engagement.html" class="mobile-nav-link"',
         'href="engagement.html" class="mobile-nav-link" data-i18n="nav.engagement"'),
        ('href="partenaire.html" class="mobile-nav-link"',
         'href="partenaire.html" class="mobile-nav-link" data-i18n="nav.partner"'),
        ('href="actualites.html" class="mobile-nav-link"',
         'href="actualites.html" class="mobile-nav-link" data-i18n="nav.news"'),
        ('href="faq.html" class="mobile-nav-link"',
         'href="faq.html" class="mobile-nav-link" data-i18n="nav.faq"'),
        ('href="contact.html" class="mobile-nav-link"',
         'href="contact.html" class="mobile-nav-link" data-i18n="nav.contact"'),
        ('href="cacao.html" class="mobile-nav-sub"',
         'href="cacao.html" class="mobile-nav-sub" data-i18n="nav.cacao"'),
        ('href="cafe.html" class="mobile-nav-sub"',
         'href="cafe.html" class="mobile-nav-sub" data-i18n="nav.cafe"'),
        ('href="approvisionnement-afrique.html" class="mobile-nav-sub"',
         'href="approvisionnement-afrique.html" class="mobile-nav-sub" data-i18n="nav.afrique"'),
    ]
    for old, new in mobile_replacements:
        html = html.replace(old, new)

    # ---- CTA header button ------------------------------------------------
    html = re.sub(
        r'class="btn btn-caramel" (style="padding:10px 20px[^"]*")>Demander un devis',
        r'class="btn btn-caramel" data-i18n="cta.quote" \1>Demander un devis',
        html
    )

    # ---- Footer -----------------------------------------------------------
    footer_replacements = [
        ('class="footer-col-title">Navigation<',
         'class="footer-col-title" data-i18n="footer.nav">Navigation<'),
        ('class="footer-col-title">Services<',
         'class="footer-col-title" data-i18n="footer.services">Services<'),
        ('class="footer-col-title">Contact<',
         'class="footer-col-title" data-i18n="footer.contact_col">Contact<'),
        ('class="footer-desc">Producteur',
         'class="footer-desc" data-i18n="footer.desc">Producteur'),
        ('class="footer-contact-label">Si\u00e8ge<',
         'class="footer-contact-label" data-i18n="footer.siege">Si\u00e8ge<'),
        ('class="footer-contact-label">T\u00e9l.<',
         'class="footer-contact-label" data-i18n="footer.tel">T\u00e9l.<'),
        ('class="footer-contact-label">Email<',
         'class="footer-contact-label" data-i18n="footer.email_lbl">Email<'),
        ('class="footer-contact-label">NIU<',
         'class="footer-contact-label" data-i18n="footer.niu">NIU<'),
        ('class="footer-copyright">&copy; 2026',
         'class="footer-copyright" data-i18n="footer.copyright">&copy; 2026'),
        ('href="mentions-legales.html">Mentions l\u00e9gales</a>',
         'href="mentions-legales.html" data-i18n="footer.legal">Mentions l\u00e9gales</a>'),
        ('class="useful-links-title">Liens utiles',
         'class="useful-links-title" data-i18n="footer.useful">Liens utiles'),
        # footer nav links (plain <a> without class)
        ('href="index.html">Accueil</a>',
         'href="index.html" data-i18n="nav.home">Accueil</a>'),
        ('href="qui-sommes-nous.html">Qui sommes-nous</a>',
         'href="qui-sommes-nous.html" data-i18n="nav.about">Qui sommes-nous</a>'),
        ('href="cooperative.html">La coop\u00e9rative</a>',
         'href="cooperative.html" data-i18n="nav.cooperative">La coop\u00e9rative</a>'),
        ('href="plantations.html">Nos plantations</a>',
         'href="plantations.html" data-i18n="nav.plantations">Nos plantations</a>'),
        ('href="cacao.html">Le cacao</a>',
         'href="cacao.html" data-i18n="footer.cacao_link">Le cacao</a>'),
        ('href="cafe.html">Le caf\u00e9</a>',
         'href="cafe.html" data-i18n="footer.cafe_link">Le caf\u00e9</a>'),
        ('href="qualite.html">Qualit\u00e9 &amp; tra\u00e7abilit\u00e9</a>',
         'href="qualite.html" data-i18n="nav.qualite">Qualit\u00e9 &amp; tra\u00e7abilit\u00e9</a>'),
        ('href="export.html">Export</a>',
         'href="export.html" data-i18n="nav.export">Export</a>'),
        ('href="engagement.html">Engagement</a>',
         'href="engagement.html" data-i18n="nav.engagement">Engagement</a>'),
        ('href="partenaire.html">Devenir partenaire</a>',
         'href="partenaire.html" data-i18n="nav.partner">Devenir partenaire</a>'),
        ('href="actualites.html">Actualit\u00e9s</a>',
         'href="actualites.html" data-i18n="nav.news">Actualit\u00e9s</a>'),
        ('href="faq.html">FAQ</a>',
         'href="faq.html" data-i18n="nav.faq">FAQ</a>'),
        ('href="contact.html">Contact</a>',
         'href="contact.html" data-i18n="nav.contact">Contact</a>'),
        ('href="qui-sommes-nous.html">\u00c0 propos de SOPROCACAM</a>',
         'href="qui-sommes-nous.html" data-i18n="footer.about_link">\u00c0 propos de SOPROCACAM</a>'),
        ("href=\"approvisionnement-afrique.html\">Cacao d'Afrique</a>",
         'href="approvisionnement-afrique.html" data-i18n="nav.afrique">Cacao d\'Afrique</a>'),
    ]
    for old, new in footer_replacements:
        html = html.replace(old, new)

    # ---- Page banner (per-page) -------------------------------------------
    if filename in PAGE_BANNER:
        title_key, sub_key = PAGE_BANNER[filename]
        html = re.sub(
            r'class="page-banner-title">([^<]+)<',
            'class="page-banner-title" data-i18n="' + title_key + r'">\1<',
            html, count=1
        )
        html = re.sub(
            r'class="page-banner-sub">([^<]+)<',
            'class="page-banner-sub" data-i18n="' + sub_key + r'">\1<',
            html, count=1
        )

    return html


# Run
updated = 0
for filename in HTML_FILES:
    path = os.path.join(ROOT, filename)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    modified = add_i18n(original, filename)
    if modified != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(modified)
        updated += 1
        print('  Updated:', filename)
    else:
        print('  Unchanged:', filename)

print('Done:', updated, '/', len(HTML_FILES), 'files updated.')
