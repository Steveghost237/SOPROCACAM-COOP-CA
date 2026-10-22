#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de génération des pages HTML de SOPROCACAM COOP-CA"""

import os

OUT_DIR = r'C:\Users\Albert WIB\Desktop\soprocacam-website'

HEADER = '''  <header class="site-header inner-mode" role="banner">
    <div class="header-inner">
      <a href="index.html" class="logo-link">
        <img src="images/logo.png" alt="Logo SOPROCACAM COOP-CA" class="logo-img" />
        <div class="logo-text">
          <span class="logo-name">SOPROCACAM COOP-CA</span>
          <span class="logo-tagline">Terre Généreuse, Coopérative engagée</span>
        </div>
      </a>
      <nav class="main-nav">
        <ul class="nav-list">
          <li class="nav-item"><a href="index.html" class="nav-link">Accueil</a></li>
          <li class="nav-item"><a href="qui-sommes-nous.html" class="nav-link">Qui sommes-nous</a></li>
          <li class="nav-item"><a href="cooperative.html" class="nav-link">La coopérative</a></li>
          <li class="nav-item"><a href="plantations.html" class="nav-link">Nos plantations</a></li>
          <li class="nav-item nav-dropdown-parent">
            <a href="#" class="nav-link">Nos produits ▾</a>
            <div class="nav-dropdown">
              <a href="cacao.html" class="dropdown-link">Le cacao</a>
              <a href="cafe.html" class="dropdown-link">Le café</a>
              <a href="approvisionnement-afrique.html" class="dropdown-link">Cacao d'Afrique</a>
            </div>
          </li>
          <li class="nav-item"><a href="qualite.html" class="nav-link">Qualité</a></li>
          <li class="nav-item"><a href="export.html" class="nav-link">Export</a></li>
          <li class="nav-item nav-dropdown-parent">
            <a href="#" class="nav-link">Plus ▾</a>
            <div class="nav-dropdown">
              <a href="engagement.html" class="dropdown-link">Engagement</a>
              <a href="partenaire.html" class="dropdown-link">Devenir partenaire</a>
              <a href="actualites.html" class="dropdown-link">Actualités</a>
              <a href="faq.html" class="dropdown-link">FAQ</a>
              <a href="contact.html" class="dropdown-link">Contact</a>
            </div>
          </li>
        </ul>
      </nav>
      <div class="header-right">
        <button class="lang-switcher">FR / EN</button>
        <a href="contact.html" class="btn btn-caramel" style="padding:10px 20px;font-size:12px;">Demander un devis</a>
        <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <div class="mobile-menu-overlay"></div>
  <nav class="mobile-menu">
    <a href="index.html" class="mobile-nav-link">Accueil</a>
    <a href="qui-sommes-nous.html" class="mobile-nav-link">Qui sommes-nous</a>
    <a href="cooperative.html" class="mobile-nav-link">La coopérative</a>
    <a href="plantations.html" class="mobile-nav-link">Nos plantations</a>
    <a href="cacao.html" class="mobile-nav-sub">→ Le cacao</a>
    <a href="cafe.html" class="mobile-nav-sub">→ Le café</a>
    <a href="approvisionnement-afrique.html" class="mobile-nav-sub">→ Cacao d'Afrique</a>
    <a href="qualite.html" class="mobile-nav-link">Qualité</a>
    <a href="export.html" class="mobile-nav-link">Export</a>
    <a href="engagement.html" class="mobile-nav-link">Engagement</a>
    <a href="partenaire.html" class="mobile-nav-link">Devenir partenaire</a>
    <a href="actualites.html" class="mobile-nav-link">Actualités</a>
    <a href="faq.html" class="mobile-nav-link">FAQ</a>
    <a href="contact.html" class="mobile-nav-link">Contact</a>
    <div style="padding:24px 32px;margin-top:16px;">
      <a href="contact.html" class="btn btn-caramel" style="width:100%;justify-content:center;">Demander un devis</a>
    </div>
  </nav>'''

FOOTER = '''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="images/logo.png" alt="SOPROCACAM COOP-CA" class="logo-img" />
          <div class="footer-brand-name">SOPROCACAM COOP-CA</div>
          <div class="footer-brand-tag">Terre Généreuse, Coopérative engagée</div>
          <p class="footer-desc">Producteur, coopérative et exportateur de cacao et de café depuis Douala, Cameroun.</p>
          <div class="footer-socials">
            <a href="#" class="social-btn"><svg viewBox="0 0 24 24" fill="currentColor" width="16"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#" class="social-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/></svg></a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Navigation</div>
          <div class="footer-links">
            <a href="index.html">Accueil</a>
            <a href="qui-sommes-nous.html">Qui sommes-nous</a>
            <a href="cooperative.html">La coopérative</a>
            <a href="plantations.html">Nos plantations</a>
            <a href="cacao.html">Le cacao</a>
            <a href="cafe.html">Le café</a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Services</div>
          <div class="footer-links">
            <a href="approvisionnement-afrique.html">Cacao d'Afrique</a>
            <a href="qualite.html">Qualité</a>
            <a href="export.html">Export</a>
            <a href="engagement.html">Engagement</a>
            <a href="partenaire.html">Devenir partenaire</a>
            <a href="faq.html">FAQ</a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Contact</div>
          <div class="footer-contact-item">
            <span class="footer-contact-label">Siège</span>
            <span class="footer-contact-value">Akwa, rue Franceville, BP 6469, Douala, Cameroun</span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-label">Tél.</span>
            <span class="footer-contact-value"><a href="tel:+237673330101">+237 673 33 01 01</a></span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-label">Email</span>
            <span class="footer-contact-value"><a href="mailto:soprocacam@gmail.com">soprocacam@gmail.com</a></span>
          </div>
          <div class="footer-contact-item">
            <span class="footer-contact-label">NIU</span>
            <span class="footer-contact-value">M052517855075A</span>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-copyright">&copy; 2026 SOPROCACAM COOP-CA. Tous droits réservés.</div>
        <div class="footer-legal">
          <a href="mentions-legales.html">Mentions légales</a>
          <a href="faq.html">FAQ</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>
    </div>
  </footer>
  <a href="https://wa.me/237673330101" target="_blank" rel="noopener" class="whatsapp-btn">
    <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>
  <script src="js/main.js"></script>'''

WHATSAPP_ICON = '''<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'''

def wrap_page(title, desc, body_content):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" type="image/png" href="images/logo.png" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{HEADER}
{body_content}
{FOOTER}
</body>
</html>'''

def banner(img, title, sub, alt=''):
    return f'''  <section class="page-banner">
    <img src="{img}" alt="{alt}" loading="eager" />
    <div class="page-banner-overlay"></div>
    <div class="container">
      <div class="page-banner-content">
        <div class="page-banner-ellipse">
          <h1 class="page-banner-title">{title}</h1>
          <p class="page-banner-sub">{sub}</p>
        </div>
      </div>
    </div>
  </section>'''


# ============================================================
# PAGE: QUI SOMMES-NOUS
# ============================================================
qui = banner('images/about.jpg', 'Qui sommes-nous ?', 'Une coopérative ancrée dans la terre, tournée vers le monde.', 'Plantation SOPROCACAM') + '''

  <section class="section bg-white">
    <div class="container">
      <div class="section-header fade-in">
        <span class="section-label">Notre histoire</span>
        <h2 class="section-title">SOPROCACAM COOP-CA</h2>
        <div class="divider"></div>
      </div>
      <div class="grid-2">
        <div class="fade-in-left">
          <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">SOPROCACAM COOP-CA est une société coopérative camerounaise dont le siège se trouve à Akwa, au cœur de Douala, capitale économique du pays et principal port d'exportation. Notre métier est l'achat et la vente de produits agricoles, avec une spécialité : le cacao et le café.</p>
          <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Notre force vient de notre organisation. Nous sommes planteurs, car nous exploitons nos propres plantations. Nous sommes coopérative, car nous réunissons plus de 13 producteurs industriels de cacao présents dans toutes les régions du Cameroun où l'on cultive le cacao et le café.</p>
          <p style="color:var(--text-mid);margin-bottom:24px;line-height:1.8;">Nous sommes enfin exportateurs et acheteurs, car nous achetons également du cacao dans d'autres pays africains producteurs avant de l'expédier vers les marchés internationaux.</p>
          <a href="cooperative.html" class="btn btn-primary">Découvrir notre coopérative</a>
        </div>
        <div class="fade-in-right">
          <img src="images/workers.jpg" alt="Producteurs membres de SOPROCACAM" style="width:100%;height:420px;object-fit:cover;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <!-- Damier Mission / Vision -->
  <section class="section bg-cream">
    <div class="container">
      <div class="checker-grid">
        <div class="checker-item text-block">
          <span class="section-label">Notre mission</span>
          <h2 class="section-title">Valoriser le cacao et le café d'Afrique</h2>
          <div class="divider"></div>
          <p style="color:var(--text-mid);line-height:1.8;">Valoriser le cacao et le café d'Afrique sur les marchés internationaux, en offrant aux acheteurs des volumes fiables, une qualité contrôlée et une transparence totale sur l'origine, tout en assurant aux producteurs un revenu juste et durable.</p>
        </div>
        <div class="checker-item img-block">
          <img src="images/workers.jpg" alt="Mains d'un planteur camerounais" loading="lazy" />
        </div>
        <div class="checker-item img-block">
          <img src="images/plantation.jpg" alt="Paysage de plantation" loading="lazy" />
        </div>
        <div class="checker-item text-block" style="text-align:right;">
          <span class="section-label">Notre vision</span>
          <h2 class="section-title">Un partenaire de référence en Afrique</h2>
          <div class="divider" style="margin-left:auto;"></div>
          <p style="color:var(--text-mid);line-height:1.8;">Devenir un partenaire de référence en Afrique centrale pour les chocolatiers, torréfacteurs et négociants qui recherchent un cacao et un café produits et exportés de manière responsable.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Valeurs -->
  <section class="section bg-white">
    <div class="container">
      <div class="section-header centered fade-in">
        <span class="section-label">Ce qui nous guide</span>
        <h2 class="section-title">Nos valeurs</h2>
        <div class="divider centered"></div>
      </div>
      <div class="values-grid">
        <div class="value-card fade-in">
          <svg class="value-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <div class="value-title">Honnêteté</div>
          <p class="value-text">Transparence envers nos membres, nos acheteurs et nos partenaires à chaque étape.</p>
        </div>
        <div class="value-card fade-in delay-1">
          <svg class="value-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          <div class="value-title">Qualité</div>
          <p class="value-text">Exigence à chaque étape, du champ au conteneur, sans compromis.</p>
        </div>
        <div class="value-card fade-in delay-2">
          <svg class="value-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <div class="value-title">Solidarité</div>
          <p class="value-text">La force du groupe au service de chaque producteur membre.</p>
        </div>
        <div class="value-card fade-in delay-3">
          <svg class="value-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          <div class="value-title">Ancrage local</div>
          <p class="value-text">Fiers de nos terres camerounaises et de nos producteurs africains.</p>
        </div>
        <div class="value-card fade-in delay-4">
          <svg class="value-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <div class="value-title">Ouverture internationale</div>
          <p class="value-text">Tourner nos productions vers les marchés internationaux avec professionnalisme.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Organisation -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header centered fade-in">
        <span class="section-label">Notre structure</span>
        <h2 class="section-title">Notre organisation</h2>
        <div class="divider centered"></div>
        <p class="section-sub" style="max-width:600px;margin:0 auto;">Une équipe structurée autour de cinq pôles pour garantir efficacité et réactivité.</p>
      </div>
      <div class="poles-grid" style="margin-top:48px;">
        <div class="pole-item fade-in"><strong>Direction générale</strong><span>Orientation stratégique, relations avec les membres</span></div>
        <div class="pole-item fade-in delay-1"><strong>Production & Producteurs</strong><span>Suivi des plantations et accompagnement des membres</span></div>
        <div class="pole-item fade-in delay-2"><strong>Achats & Approvisionnement</strong><span>Collecte au Cameroun et achats africains</span></div>
        <div class="pole-item fade-in delay-3"><strong>Qualité</strong><span>Contrôle, tri, traçabilité</span></div>
        <div class="pole-item fade-in delay-4"><strong>Export & Logistique</strong><span>Documents, transport, chargement à Douala</span></div>
      </div>
    </div>
  </section>

  <section class="cta-section">
    <div class="container-md" style="text-align:center;">
      <h2 class="section-title fade-in" style="color:white;">Prêt à travailler ensemble ?</h2>
      <div class="cta-btns fade-in delay-1">
        <a href="cooperative.html" class="btn btn-caramel">Découvrir notre coopérative</a>
        <a href="contact.html" class="btn btn-secondary">Nous contacter</a>
      </div>
    </div>
  </section>'''

write_file('qui-sommes-nous.html', wrap_page(
    'Qui sommes-nous ? – SOPROCACAM COOP-CA',
    'Découvrez SOPROCACAM COOP-CA, coopérative camerounaise de cacao et café, planteurs, coopérative et exportateurs depuis Douala.',
    qui
))


# ============================================================
# PAGE: COOPÉRATIVE
# ============================================================
coop = banner('images/cooperative.jpg', 'Une coopérative engagée', 'Ensemble, nous produisons mieux et nous vendons plus juste.', 'Membres de la coopérative SOPROCACAM') + '''

  <section class="section bg-white">
    <div class="container">
      <div class="grid-2">
        <div class="fade-in-left">
          <span class="section-label">Définition</span>
          <h2 class="section-title">Qu'est-ce qu'une COOP-CA ?</h2>
          <div class="divider"></div>
          <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Une COOP-CA est une société coopérative dotée d'un conseil d'administration. Ses membres s'unissent pour partager leurs moyens, leurs connaissances et leurs marchés. Chaque producteur garde son exploitation, mais profite de la force du groupe : meilleure organisation, meilleur accès aux débouchés et meilleur prix.</p>
          <table class="data-table" style="margin-top:28px;">
            <thead><tr><th colspan="2">La coopérative en bref</th></tr></thead>
            <tbody>
              <tr><td><strong>Nom</strong></td><td>SOPROCACAM COOP-CA</td></tr>
              <tr><td><strong>Type</strong></td><td>Société coopérative avec conseil d'administration</td></tr>
              <tr><td><strong>Siège</strong></td><td>Akwa, Douala, Cameroun</td></tr>
              <tr><td><strong>Producteurs membres</strong></td><td>+13 producteurs industriels</td></tr>
              <tr><td><strong>Couverture</strong></td><td>Toutes les régions de culture du Cameroun</td></tr>
              <tr><td><strong>Port d'export</strong></td><td>Douala</td></tr>
              <tr><td><strong>NIU</strong></td><td>M052517855075A</td></tr>
              <tr><td><strong>RCCM</strong></td><td>25/066/CMR/CE/10/051/CCA/032004/032004000</td></tr>
            </tbody>
          </table>
        </div>
        <div class="fade-in-right">
          <img src="images/plantation.jpg" alt="Plantation membre de la coopérative" style="width:100%;height:480px;object-fit:cover;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-cream">
    <div class="container">
      <div class="section-header centered fade-in">
        <span class="section-label">Présence nationale</span>
        <h2 class="section-title">Une présence dans toutes les régions de culture</h2>
        <div class="divider centered"></div>
      </div>
      <div class="grid-2">
        <div class="fade-in-left">
          <p class="zones-text">Nos membres sont répartis dans les grandes zones de production du pays :</p>
          <ul class="checklist" style="margin-top:20px;">
            <li>Régions du <strong>Centre, du Sud, de l'Est, du Littoral et du Sud-Ouest</strong> pour le cacao et le café Robusta</li>
            <li>Hauts plateaux de <strong>l'Ouest et du Nord-Ouest</strong> pour l'Arabica</li>
          </ul>
          <p class="zones-text" style="margin-top:20px;">Cette couverture nationale nous permet de réunir des volumes importants et de répondre aux commandes de grande taille.</p>
        </div>
        <div class="fade-in-right">
          <img src="images/afrique.jpg" alt="Carte des régions de production au Cameroun" style="width:100%;height:380px;object-fit:cover;" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white">
    <div class="container">
      <div class="section-header centered fade-in">
        <span class="section-label">Avantages</span>
        <h2 class="section-title">Ce que la coopérative apporte</h2>
        <div class="divider centered"></div>
      </div>
      <div class="benefit-grid">
        <div>
          <div class="benefit-col-title">Aux producteurs</div>
          <ul class="checklist">
            <li>Un débouché sûr pour leur récolte, à des conditions connues d'avance.</li>
            <li>Un accompagnement technique : bonnes pratiques de culture, de récolte et de séchage.</li>
            <li>Un meilleur pouvoir de négociation grâce à la vente groupée.</li>
            <li>L'accès aux marchés internationaux via notre activité d'exportation.</li>
          </ul>
        </div>
        <div>
          <div class="benefit-col-title">Aux acheteurs</div>
          <ul class="checklist">
            <li>Des volumes importants et réguliers, impossibles à atteindre pour un producteur isolé.</li>
            <li>Une qualité homogène grâce à des pratiques et des contrôles communs.</li>
            <li>Une traçabilité claire : on sait de quelle zone et de quel producteur vient le lot.</li>
            <li>Un interlocuteur unique pour toute la chaîne.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="steps-section">
    <div class="container">
      <div class="section-header centered fade-in">
        <span class="section-label">Méthode de travail</span>
        <h2 class="section-title">Comment nous travaillons ensemble</h2>
        <div class="divider centered"></div>
      </div>
      <div class="steps-grid">
        <div class="step-item fade-in"><div class="step-num">1</div><div class="step-title">Collecte</div><p class="step-text">Achat des fèves et du café auprès des membres, à des prix transparents.</p></div>
        <div class="step-item fade-in delay-1"><div class="step-num">2</div><div class="step-title">Appui</div><p class="step-text">Conseils de culture et de traitement après récolte.</p></div>
        <div class="step-item fade-in delay-2"><div class="step-num">3</div><div class="step-title">Contrôle</div><p class="step-text">Tri et vérification de la qualité avant regroupement des lots.</p></div>
        <div class="step-item fade-in delay-3"><div class="step-num">4</div><div class="step-title">Exportation</div><p class="step-text">SOPROCACAM COOP-CA assure la vente et l'expédition internationales.</p></div>
      </div>
    </div>
  </section>

  <section class="cta-section">
    <div class="container-md" style="text-align:center;">
      <h2 class="section-title fade-in" style="color:white;">Rejoignez notre réseau</h2>
      <p class="section-sub fade-in delay-1">Vous êtes producteur de cacao ou de café et souhaitez rejoindre notre réseau ou vendre votre récolte ?</p>
      <div class="cta-btns fade-in delay-2">
        <a href="partenaire.html" class="btn btn-caramel">Devenir producteur partenaire</a>
        <a href="contact.html" class="btn btn-secondary">Nous contacter</a>
      </div>
    </div>
  </section>'''

write_file('cooperative.html', wrap_page(
    'La coopérative SOPROCACAM COOP-CA – Producteurs camerounais unis',
    'Découvrez la coopérative SOPROCACAM COOP-CA : +13 producteurs industriels, présence dans toutes les régions de culture du Cameroun.',
    coop
))

print('Pages generated.')
