#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

OUT = r'C:\Users\Albert WIB\Desktop\soprocacam-website'

HEADER = """  <header class="site-header inner-mode">
    <div class="header-inner">
      <a href="index.html" class="logo-link"><img src="images/logo.png" alt="Logo SOPROCACAM" class="logo-img" /><div class="logo-text"><span class="logo-name">SOPROCACAM COOP-CA</span><span class="logo-tagline">Terre Généreuse, Coopérative engagée</span></div></a>
      <nav class="main-nav"><ul class="nav-list">
        <li class="nav-item"><a href="index.html" class="nav-link">Accueil</a></li>
        <li class="nav-item"><a href="qui-sommes-nous.html" class="nav-link">Qui sommes-nous</a></li>
        <li class="nav-item"><a href="cooperative.html" class="nav-link">La coopérative</a></li>
        <li class="nav-item"><a href="plantations.html" class="nav-link">Nos plantations</a></li>
        <li class="nav-item nav-dropdown-parent"><a href="#" class="nav-link">Nos produits ▾</a><div class="nav-dropdown"><a href="cacao.html" class="dropdown-link">Le cacao</a><a href="cafe.html" class="dropdown-link">Le café</a><a href="approvisionnement-afrique.html" class="dropdown-link">Cacao d'Afrique</a></div></li>
        <li class="nav-item"><a href="qualite.html" class="nav-link">Qualité</a></li>
        <li class="nav-item"><a href="export.html" class="nav-link">Export</a></li>
        <li class="nav-item nav-dropdown-parent"><a href="#" class="nav-link">Plus ▾</a><div class="nav-dropdown"><a href="engagement.html" class="dropdown-link">Engagement</a><a href="partenaire.html" class="dropdown-link">Devenir partenaire</a><a href="actualites.html" class="dropdown-link">Actualités</a><a href="faq.html" class="dropdown-link">FAQ</a><a href="contact.html" class="dropdown-link">Contact</a></div></li>
      </ul></nav>
      <div class="header-right"><button class="lang-switcher">FR / EN</button><a href="contact.html" class="btn btn-caramel" style="padding:10px 20px;font-size:12px;">Demander un devis</a><button class="burger" aria-label="Menu"><span></span><span></span><span></span></button></div>
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
    <div style="padding:24px 32px;margin-top:16px;"><a href="contact.html" class="btn btn-caramel" style="width:100%;justify-content:center;">Demander un devis</a></div>
  </nav>"""

FOOTER = """  <footer class="site-footer"><div class="container"><div class="footer-grid">
    <div class="footer-brand"><img src="images/logo.png" alt="SOPROCACAM" class="logo-img" /><div class="footer-brand-name">SOPROCACAM COOP-CA</div><div class="footer-brand-tag">Terre Généreuse, Coopérative engagée</div><p class="footer-desc">Producteur, coopérative et exportateur de cacao et de café depuis Douala, Cameroun.</p></div>
    <div><div class="footer-col-title">Navigation</div><div class="footer-links"><a href="index.html">Accueil</a><a href="qui-sommes-nous.html">Qui sommes-nous</a><a href="cooperative.html">La coopérative</a><a href="plantations.html">Nos plantations</a><a href="cacao.html">Le cacao</a><a href="cafe.html">Le café</a></div></div>
    <div><div class="footer-col-title">Services</div><div class="footer-links"><a href="approvisionnement-afrique.html">Cacao d'Afrique</a><a href="qualite.html">Qualité</a><a href="export.html">Export</a><a href="engagement.html">Engagement</a><a href="partenaire.html">Devenir partenaire</a><a href="faq.html">FAQ</a></div></div>
    <div><div class="footer-col-title">Contact</div>
      <div class="footer-contact-item"><span class="footer-contact-label">Siège</span><span class="footer-contact-value">Akwa, rue Franceville, BP 6469, Douala, Cameroun</span></div>
      <div class="footer-contact-item"><span class="footer-contact-label">Tél.</span><span class="footer-contact-value"><a href="tel:+237673330101">+237 673 33 01 01</a></span></div>
      <div class="footer-contact-item"><span class="footer-contact-label">Email</span><span class="footer-contact-value"><a href="mailto:soprocacam@gmail.com">soprocacam@gmail.com</a></span></div>
      <div class="footer-contact-item"><span class="footer-contact-label">NIU</span><span class="footer-contact-value">M052517855075A</span></div>
    </div>
  </div><div class="footer-bottom"><div class="footer-copyright">&copy; 2026 SOPROCACAM COOP-CA. Tous droits réservés.</div><div class="footer-legal"><a href="mentions-legales.html">Mentions légales</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a></div></div></div></footer>
  <a href="https://wa.me/237673330101" target="_blank" rel="noopener" class="whatsapp-btn" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>
  <script src="js/main.js"></script>"""

def make_page(title, desc, body):
    return (
        '<!DOCTYPE html>\n<html lang="fr">\n<head>\n'
        '  <meta charset="UTF-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
        f'  <title>{title}</title>\n'
        f'  <meta name="description" content="{desc}" />\n'
        '  <link rel="icon" type="image/png" href="images/logo.png" />\n'
        '  <link rel="stylesheet" href="css/style.css" />\n'
        '</head>\n<body>\n'
        + HEADER + '\n'
        + body + '\n'
        + FOOTER + '\n'
        '</body>\n</html>\n'
    )

def banner(img, title, sub, alt=''):
    return (
        f'  <section class="page-banner">\n'
        f'    <img src="{img}" alt="{alt}" loading="eager" />\n'
        f'    <div class="page-banner-overlay"></div>\n'
        f'    <div class="container"><div class="page-banner-content"><div class="page-banner-ellipse">\n'
        f'      <h1 class="page-banner-title">{title}</h1>\n'
        f'      <p class="page-banner-sub">{sub}</p>\n'
        f'    </div></div></div>\n'
        f'  </section>\n'
    )

def write(fn, title, desc, body):
    path = os.path.join(OUT, fn)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_page(title, desc, body))
    print(f'  Created: {fn}')

# =========================================================
# COOPERATIVE
# =========================================================
write('cooperative.html',
    'La coopérative SOPROCACAM COOP-CA – +13 producteurs camerounais',
    'La coopérative SOPROCACAM COOP-CA réunit plus de 13 producteurs industriels dans toutes les régions de culture du Cameroun.',
    banner('images/cooperative.jpg', 'Une coopérative engagée', 'Ensemble, nous produisons mieux et nous vendons plus juste.', 'Membres SOPROCACAM') +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Définition</span>
      <h2 class="section-title">Qu'est-ce qu'une COOP-CA ?</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:20px;line-height:1.8;">Une COOP-CA est une société coopérative dotée d'un conseil d'administration. Ses membres s'unissent pour partager leurs moyens, leurs connaissances et leurs marchés. Chaque producteur garde son exploitation, mais profite de la force du groupe : meilleure organisation, meilleur accès aux débouchés et meilleur prix.</p>
      <div class="tech-table-wrap"><table class="data-table"><thead><tr><th colspan="2">La coopérative en bref</th></tr></thead><tbody>
        <tr><td>Nom</td><td>SOPROCACAM COOP-CA</td></tr>
        <tr><td>Type</td><td>Société coopérative avec conseil d'administration</td></tr>
        <tr><td>Siège</td><td>Akwa, Douala, Cameroun</td></tr>
        <tr><td>Producteurs membres</td><td>+13 producteurs industriels</td></tr>
        <tr><td>Couverture</td><td>Toutes les régions de culture du Cameroun</td></tr>
        <tr><td>Port d'export</td><td>Douala</td></tr>
        <tr><td>NIU</td><td>M052517855075A</td></tr>
        <tr><td>RCCM</td><td>25/066/CMR/CE/10/051/CCA/032004/032004000</td></tr>
      </tbody></table></div>
    </div>
    <div class="fade-in-right"><img src="images/plantation.jpg" alt="Plantation membre" style="width:100%;height:480px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Présence nationale</span><h2 class="section-title">Une présence dans toutes les régions de culture</h2><div class="divider centered"></div></div>
    <div class="grid-2">
      <div class="fade-in-left">
        <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Nos membres sont répartis dans les grandes zones de production du pays :</p>
        <ul class="checklist">
          <li>Régions du <strong>Centre, du Sud, de l'Est, du Littoral et du Sud-Ouest</strong> pour le cacao et le café Robusta</li>
          <li>Hauts plateaux de <strong>l'Ouest et du Nord-Ouest</strong> pour l'Arabica</li>
        </ul>
        <p style="color:var(--text-mid);margin-top:20px;line-height:1.8;">Cette couverture nationale nous permet de réunir des volumes importants et de répondre aux commandes de grande taille.</p>
      </div>
      <div class="fade-in-right"><img src="images/afrique.jpg" alt="Régions de production Cameroun" style="width:100%;height:360px;object-fit:cover;" loading="lazy" /></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Avantages</span><h2 class="section-title">Ce que la coopérative apporte</h2><div class="divider centered"></div></div>
    <div class="benefit-grid">
      <div><div class="benefit-col-title">Aux producteurs</div><ul class="checklist">
        <li>Un débouché sûr pour leur récolte, à des conditions connues d'avance.</li>
        <li>Un accompagnement technique : bonnes pratiques de culture, de récolte et de séchage.</li>
        <li>Un meilleur pouvoir de négociation grâce à la vente groupée.</li>
        <li>L'accès aux marchés internationaux via notre activité d'exportation.</li>
      </ul></div>
      <div><div class="benefit-col-title">Aux acheteurs</div><ul class="checklist">
        <li>Des volumes importants et réguliers, impossibles à atteindre pour un producteur isolé.</li>
        <li>Une qualité homogène grâce à des pratiques et des contrôles communs.</li>
        <li>Une traçabilité claire : on sait de quelle zone et de quel producteur vient le lot.</li>
        <li>Un interlocuteur unique pour toute la chaîne.</li>
      </ul></div>
    </div>
  </div></section>

  <section class="steps-section"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Méthode</span><h2 class="section-title">Comment nous travaillons ensemble</h2><div class="divider centered"></div></div>
    <div class="steps-grid">
      <div class="step-item fade-in"><div class="step-num">1</div><div class="step-title">Collecte</div><p class="step-text">Achat des fèves et du café auprès des membres, à des prix transparents.</p></div>
      <div class="step-item fade-in delay-1"><div class="step-num">2</div><div class="step-title">Appui</div><p class="step-text">Conseils de culture et de traitement après récolte.</p></div>
      <div class="step-item fade-in delay-2"><div class="step-num">3</div><div class="step-title">Contrôle</div><p class="step-text">Tri et vérification de la qualité avant regroupement des lots.</p></div>
      <div class="step-item fade-in delay-3"><div class="step-num">4</div><div class="step-title">Exportation</div><p class="step-text">SOPROCACAM COOP-CA assure la vente et l'expédition internationales.</p></div>
    </div>
  </div></section>

  <section class="cta-section"><div class="container-md" style="text-align:center;">
    <h2 class="section-title fade-in" style="color:white;">Rejoignez notre réseau</h2>
    <p class="section-sub fade-in delay-1">Vous êtes producteur de cacao ou de café et souhaitez rejoindre notre réseau ou vendre votre récolte ?</p>
    <div class="cta-btns fade-in delay-2">
      <a href="partenaire.html" class="btn btn-caramel">Devenir producteur partenaire</a>
      <a href="contact.html" class="btn btn-secondary">Nous contacter</a>
    </div>
  </div></section>"""
)

# =========================================================
# PLANTATIONS
# =========================================================
write('plantations.html',
    'Nos plantations – SOPROCACAM COOP-CA',
    'SOPROCACAM COOP-CA exploite ses propres plantations de cacao et café au Cameroun. Découvrez nos cultures et pratiques respectueuses.',
    banner('images/plantation.jpg', 'Nos plantations, notre fierté', 'Une partie de ce que nous exportons pousse sur nos propres terres.', 'Plantation SOPROCACAM') +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Présentation</span>
      <h2 class="section-title">Nous cultivons nous-mêmes</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">SOPROCACAM COOP-CA n'est pas seulement un négociant : nous cultivons. Nos plantations de cacao et de café nous donnent une connaissance directe de la terre, des variétés et des saisons. Cette expérience guide ensuite nos choix auprès des producteurs de la coopérative et dans nos achats à l'étranger.</p>
      <a href="contact.html" class="btn btn-primary">Demander une visite de nos plantations</a>
    </div>
    <div class="fade-in-right"><img src="images/hero4.jpg" alt="Cabosses de cacao mûres" style="width:100%;height:420px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Ce que nous produisons</span><h2 class="section-title">Nos cultures</h2><div class="divider centered"></div></div>
    <div class="cards-grid-3">
      <div class="card fade-in"><img src="images/cacao.jpg" alt="Cacao" style="width:100%;height:160px;object-fit:cover;margin-bottom:20px;" /><div class="card-title">Cacao (Theobroma cacao)</div><p class="card-text">Des fèves fermentées et séchées issues de nos propres parcelles, dans les grandes régions cacaoyères du Cameroun.</p><a href="cacao.html" class="read-more" style="margin-top:16px;">Voir le cacao</a></div>
      <div class="card fade-in delay-1"><img src="images/cafe.jpg" alt="Café Robusta" style="width:100%;height:160px;object-fit:cover;margin-bottom:20px;" /><div class="card-title">Café Robusta</div><p class="card-text">Principalement cultivé dans les régions du Littoral, du Centre, du Sud et de l'Est. Caractère fort, idéal pour les mélanges.</p><a href="cafe.html" class="read-more" style="margin-top:16px;">Voir le café</a></div>
      <div class="card fade-in delay-2"><img src="images/beans.jpg" alt="Café Arabica" style="width:100%;height:160px;object-fit:cover;margin-bottom:20px;" /><div class="card-title">Café Arabica</div><p class="card-text">Cultivé en altitude sur les hauts plateaux de l'Ouest et du Nord-Ouest. Arômes délicats et complexes.</p><a href="cafe.html" class="read-more" style="margin-top:16px;">Voir le café</a></div>
    </div>
  </div></section>

  <section class="steps-section"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Saisons</span><h2 class="section-title">Le calendrier de la culture</h2><div class="divider centered"></div></div>
    <div class="steps-grid">
      <div class="step-item fade-in"><div class="step-num">1</div><div class="step-title">Entretien des parcelles</div><p class="step-text">Désherbage, taille, gestion de l'ombrage pour préserver la fertilité du sol.</p></div>
      <div class="step-item fade-in delay-1"><div class="step-num">2</div><div class="step-title">Floraison et fructification</div><p class="step-text">Suivi sanitaire des arbres pour garantir un bon développement des cabosses.</p></div>
      <div class="step-item fade-in delay-2"><div class="step-num">3</div><div class="step-title">Récolte</div><p class="step-text">Cueillette à maturité pour garantir la qualité des fèves et des cerises.</p></div>
      <div class="step-item fade-in delay-3"><div class="step-num">4</div><div class="step-title">Après-récolte</div><p class="step-text">Fermentation et séchage du cacao ; séchage et préparation du café.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Responsabilité</span><h2 class="section-title">Des pratiques respectueuses</h2><div class="divider centered"></div></div>
    <div class="grid-2">
      <div class="fade-in-left">
        <ul class="checklist">
          <li>Arbres d'ombrage pour préserver la biodiversité</li>
          <li>Gestion raisonnée des intrants et des engrais</li>
          <li>Entretien régulier et renouvellement progressif des vieux plants</li>
          <li>Préservation de la fertilité des sols</li>
          <li>Formation continue des travailleurs agricoles</li>
        </ul>
        <div style="margin-top:32px;"><a href="engagement.html" class="btn btn-primary">Notre engagement</a></div>
      </div>
      <div class="fade-in-right"><img src="images/engagement.jpg" alt="Agriculture durable" style="width:100%;height:360px;object-fit:cover;" loading="lazy" /></div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Galerie photos</span><h2 class="section-title">Dans nos plantations</h2><div class="divider centered"></div></div>
    <div class="gallery-grid">
      <div class="gallery-item"><img src="images/plantation.jpg" alt="Parcelle de cacao" loading="lazy" /></div>
      <div class="gallery-item"><img src="images/cacao.jpg" alt="Cabosses de cacao" loading="lazy" /></div>
      <div class="gallery-item"><img src="images/cafe.jpg" alt="Cerises de café" loading="lazy" /></div>
      <div class="gallery-item"><img src="images/workers.jpg" alt="Ouvriers au travail" loading="lazy" /></div>
      <div class="gallery-item"><img src="images/about.jpg" alt="Séchage au soleil" loading="lazy" /></div>
      <div class="gallery-item"><img src="images/engagement.jpg" alt="Pratiques durables" loading="lazy" /></div>
    </div>
    <div style="text-align:center;margin-top:40px;"><p style="color:var(--text-mid);font-style:italic;margin-bottom:20px;">Photos réelles de l'entreprise à intégrer dès disponibilité.</p><a href="contact.html" class="btn btn-primary">Demander une visite de nos plantations</a></div>
  </div></section>"""
)

# =========================================================
# CACAO D'AFRIQUE
# =========================================================
write('approvisionnement-afrique.html',
    "Cacao d'Afrique – SOPROCACAM COOP-CA",
    "SOPROCACAM COOP-CA achète du cacao dans plusieurs pays africains producteurs pour offrir volumes importants et origines variées.",
    banner('images/afrique.jpg', "Du cacao de toute l'Afrique", 'Rassemblé à Douala pour vos marchés.', "Cacao d'Afrique") +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Pourquoi cet approvisionnement</span>
      <h2 class="section-title">Un approvisionnement africain pour répondre à vos volumes</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Les acheteurs internationaux ont souvent besoin de grandes quantités régulières que nos seules plantations et notre seule coopérative ne peuvent pas toujours couvrir. Pour répondre à cette demande, nous achetons également du cacao dans d'autres pays africains producteurs.</p>
      <p style="color:var(--text-mid);line-height:1.8;">Cet approvisionnement africain complémentaire nous permet de vous proposer des volumes importants, un seul point de contact et une même exigence de qualité, quelle que soit l'origine du lot.</p>
    </div>
    <div class="fade-in-right"><img src="images/hero1.jpg" alt="Cacao d'Afrique" style="width:100%;height:420px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Processus</span><h2 class="section-title">Comment cela fonctionne</h2><div class="divider centered"></div></div>
    <div class="steps-h">
      <div class="step-h-item"><div class="step-h-num">1</div><div class="step-h-title">Sélection des sources</div><p class="step-h-text">Nous travaillons avec des producteurs et fournisseurs reconnus dans les pays d'origine.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">2</div><div class="step-h-title">Achat</div><p class="step-h-text">Négociation transparente, prix et quantités confirmés par contrat.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">3</div><div class="step-h-title">Contrôle qualité</div><p class="step-h-text">Vérification de l'humidité, du tri et de l'aspect des fèves avant acceptation.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">4</div><div class="step-h-title">Regroupement</div><p class="step-h-text">Acheminement des lots vers notre point de regroupement ou directement vers le port.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">5</div><div class="step-h-title">Exportation</div><p class="step-h-text">Documents, conditionnement et expédition vers votre destination.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Avantages</span><h2 class="section-title">Ce que cela vous apporte</h2><div class="divider centered"></div></div>
    <div class="cards-grid-4">
      <div class="card fade-in"><div class="card-title">Volumes plus importants</div><p class="card-text">Des volumes plus importants et plus réguliers pour satisfaire vos besoins les plus exigeants.</p></div>
      <div class="card fade-in delay-1"><div class="card-title">Choix des origines</div><p class="card-text">Le choix entre plusieurs origines africaines selon vos exigences de profil et de goût.</p></div>
      <div class="card fade-in delay-2"><div class="card-title">Interlocuteur unique</div><p class="card-text">Un seul fournisseur, un seul contrat, un seul interlocuteur pour simplifier votre chaîne.</p></div>
      <div class="card fade-in delay-3"><div class="card-title">Même exigence qualité</div><p class="card-text">La même exigence de qualité que pour nos propres produits, à chaque étape.</p></div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container"><div class="container-md">
    <div class="section-header centered fade-in"><span class="section-label">Transparence</span><h2 class="section-title">Une origine toujours indiquée</h2><div class="divider centered"></div></div>
    <p style="color:var(--text-mid);text-align:center;font-size:17px;line-height:1.8;margin-bottom:32px;">Nous indiquons toujours clairement l'origine de chaque lot, qu'il vienne du Cameroun ou d'un autre pays africain, afin que vous sachiez exactement ce que vous achetez.</p>
    <div style="text-align:center;"><a href="contact.html" class="btn btn-primary">Demander une offre selon l'origine</a></div>
  </div></div></section>"""
)

# =========================================================
# CACAO
# =========================================================
write('cacao.html',
    'Le cacao – SOPROCACAM COOP-CA | Fèves fermentées et séchées',
    'SOPROCACAM COOP-CA exporte des fèves de cacao du Cameroun et d\'autres origines africaines. Qualité suivie, volumes fiables.',
    banner('images/cacao.jpg', 'Le cacao', "Des fèves riches en arômes, de nos plantations et de toute l'Afrique à votre chocolaterie.", 'Fèves de cacao camerounaises') +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Présentation</span>
      <h2 class="section-title">Un cacao d'exception</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Le Cameroun est l'un des pays producteurs de cacao d'Afrique, avec une culture présente notamment dans les régions du Centre, du Sud, de l'Est, du Sud-Ouest et du Littoral. SOPROCACAM COOP-CA exporte des fèves issues de ses plantations, de ses producteurs membres et de pays africains partenaires.</p>
      <p style="color:var(--text-mid);line-height:1.8;">Chaque lot est fermenté, séché puis trié afin de répondre aux exigences des transformateurs et des chocolatiers.</p>
    </div>
    <div class="fade-in-right"><img src="images/hero1.jpg" alt="Cabosses de cacao du Cameroun" style="width:100%;height:420px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header fade-in"><span class="section-label">Fiche technique</span><h2 class="section-title">Caractéristiques du cacao</h2><div class="divider"></div></div>
    <div class="tech-table-wrap"><table class="data-table">
      <thead><tr><th>Caractéristique</th><th>Détail</th></tr></thead>
      <tbody>
        <tr><td>Produit</td><td>Fèves de cacao fermentées et séchées</td></tr>
        <tr><td>Origines</td><td>Cameroun (Centre, Sud, Est, Littoral, Sud-Ouest) et autres pays africains</td></tr>
        <tr><td>Conditionnement</td><td>Sacs de jute de 60 à 65 kg</td></tr>
        <tr><td>Humidité</td><td>Conforme aux normes d'exportation (≤ 8 %)</td></tr>
        <tr><td>Commande minimale</td><td>1 conteneur de 20 pieds</td></tr>
        <tr><td>Port d'expédition</td><td>Douala, Cameroun</td></tr>
        <tr><td>Documents</td><td>Facture commerciale, liste de colisage, certificat d'origine, certificat phytosanitaire</td></tr>
        <tr><td>Traçabilité</td><td>Origine indiquée par lot</td></tr>
      </tbody>
    </table></div>
  </div></section>

  <section class="steps-section"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Processus</span><h2 class="section-title">Du champ au sac</h2><div class="divider centered"></div></div>
    <div class="steps-h">
      <div class="step-h-item"><div class="step-h-num">1</div><div class="step-h-title">Récolte des cabosses</div><p class="step-h-text">À pleine maturité.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">2</div><div class="step-h-title">Écabossage</div><p class="step-h-text">Mise en fermentation des fèves.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">3</div><div class="step-h-title">Séchage au soleil</div><p class="step-h-text">Jusqu'au taux d'humidité requis.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">4</div><div class="step-h-title">Tri et contrôle</div><p class="step-h-text">Élimination des fèves défectueuses, vérification de la qualité.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">5</div><div class="step-h-title">Ensachage</div><p class="step-h-text">Stockage dans un entrepôt sain et ventilé.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Pourquoi nous choisir</span><h2 class="section-title">4 raisons de choisir notre cacao</h2><div class="divider centered"></div></div>
    <div class="cards-grid-4">
      <div class="card fade-in"><div class="card-title">Origine indiquée</div><p class="card-text">Chaque lot est traçable : plantation, producteur membre, région ou pays d'achat.</p></div>
      <div class="card fade-in delay-1"><div class="card-title">Qualité suivie</div><p class="card-text">Contrôle rigoureux à chaque étape, de la récolte au chargement à Douala.</p></div>
      <div class="card fade-in delay-2"><div class="card-title">Volumes importants</div><p class="card-text">Grâce à nos plantations, à la coopérative et à nos achats africains.</p></div>
      <div class="card fade-in delay-3"><div class="card-title">Export complet</div><p class="card-text">Accompagnement export de A à Z : documents, logistique, livraison.</p></div>
    </div>
    <div style="text-align:center;margin-top:48px;display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="contact.html" class="btn btn-primary fade-in">Demander un devis cacao</a>
      <a href="contact.html" class="btn btn-outline fade-in delay-1">Demander un échantillon</a>
    </div>
  </div></section>"""
)

# =========================================================
# CAFÉ
# =========================================================
write('cafe.html',
    'Le café du Cameroun – SOPROCACAM COOP-CA | Robusta & Arabica',
    'SOPROCACAM COOP-CA exporte du café Robusta et Arabica camerounais sélectionné, trié et conditionné pour l\'export.',
    banner('images/cafe.jpg', 'Le café du Cameroun', 'Un café de caractère, cultivé avec soin et préparé pour l\'export.', 'Café Robusta et Arabica camerounais') +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Présentation</span>
      <h2 class="section-title">Un café de caractère</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Le Cameroun produit du café Robusta, principalement dans les régions du Littoral, du Centre, du Sud et de l'Est, et de l'Arabica, cultivé en altitude sur les hauts plateaux de l'Ouest et du Nord-Ouest. SOPROCACAM COOP-CA propose ces deux types de café, issus de ses plantations et de son réseau de producteurs membres.</p>
      <p style="color:var(--text-mid);line-height:1.8;">Les cerises sont récoltées à maturité, puis séchées et préparées avec attention pour conserver tout leur potentiel aromatique.</p>
    </div>
    <div class="fade-in-right"><img src="images/beans.jpg" alt="Grains de café camerounais" style="width:100%;height:420px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header fade-in"><span class="section-label">Fiche technique</span><h2 class="section-title">Nos cafés</h2><div class="divider"></div></div>
    <div class="tech-table-wrap"><table class="data-table">
      <thead><tr><th>Caractéristique</th><th>Robusta</th><th>Arabica</th></tr></thead>
      <tbody>
        <tr><td>Régions</td><td>Littoral, Centre, Sud, Est</td><td>Ouest, Nord-Ouest (hauts plateaux)</td></tr>
        <tr><td>Profil aromatique</td><td>Fort, terreux, faible acidité</td><td>Délicat, fruité, acidité modérée</td></tr>
        <tr><td>Humidité</td><td>≤ 12,5 %</td><td>≤ 12,5 %</td></tr>
        <tr><td>Conditionnement</td><td>Sacs de jute de 60 kg</td><td>Sacs de jute de 60 kg</td></tr>
        <tr><td>Commande minimale</td><td>1 conteneur de 20 pieds</td><td>1 conteneur de 20 pieds</td></tr>
        <tr><td>Port d'expédition</td><td>Douala, Cameroun</td><td>Douala, Cameroun</td></tr>
      </tbody>
    </table></div>
  </div></section>

  <section class="steps-section"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Processus</span><h2 class="section-title">Du champ au sac</h2><div class="divider centered"></div></div>
    <div class="steps-h">
      <div class="step-h-item"><div class="step-h-num">1</div><div class="step-h-title">Récolte des cerises</div><p class="step-h-text">À maturité.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">2</div><div class="step-h-title">Séchage</div><p class="step-h-text">Sur aires ou claies jusqu'au taux d'humidité cible.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">3</div><div class="step-h-title">Déparchage & Triage</div><p class="step-h-text">Pour retirer les grains défectueux.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">4</div><div class="step-h-title">Contrôle qualité</div><p class="step-h-text">Humidité, calibre, aspect.</p><div class="step-h-arrow"></div></div>
      <div class="step-h-item"><div class="step-h-num">5</div><div class="step-h-title">Ensachage</div><p class="step-h-text">Stockage avant expédition.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Pourquoi nous choisir</span><h2 class="section-title">4 raisons de choisir notre café</h2><div class="divider centered"></div></div>
    <div class="cards-grid-4">
      <div class="card fade-in"><div class="card-title">Origine camerounaise</div><p class="card-text">Authentique, du Robusta à l'Arabica, traçable jusqu'au producteur.</p></div>
      <div class="card fade-in delay-1"><div class="card-title">Préparation soignée</div><p class="card-text">Un tri rigoureux pour ne conserver que les grains de qualité.</p></div>
      <div class="card fade-in delay-2"><div class="card-title">Approvisionnement fiable</div><p class="card-text">Un réseau coopératif solide pour des volumes réguliers.</p></div>
      <div class="card fade-in delay-3"><div class="card-title">Interlocuteur unique</div><p class="card-text">Du champ au port, un seul contact pour simplifier vos achats.</p></div>
    </div>
    <div style="text-align:center;margin-top:48px;display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="contact.html" class="btn btn-primary fade-in">Demander un devis café</a>
      <a href="contact.html" class="btn btn-outline fade-in delay-1">Demander un échantillon</a>
    </div>
  </div></section>"""
)

# =========================================================
# QUALITÉ
# =========================================================
write('qualite.html',
    'Qualité & traçabilité – SOPROCACAM COOP-CA',
    'SOPROCACAM COOP-CA contrôle la qualité à chaque étape, de la plantation au conteneur. Traçabilité complète et conformité aux normes d\'export.',
    banner('images/qualite.jpg', 'La qualité, de la parcelle au conteneur', 'Chaque lot est suivi, contrôlé et documenté.', 'Contrôle qualité cacao') +
    """
  <section class="section bg-white"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Notre engagement</span>
      <h2 class="section-title">La qualité, un suivi permanent</h2>
      <div class="divider"></div>
      <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Un acheteur exigeant a besoin de certitudes : d'où vient le produit, comment il a été traité, et s'il correspond à ce qui a été convenu. Chez SOPROCACAM COOP-CA, la qualité n'est pas un contrôle final, c'est un suivi permanent, que le produit vienne de nos plantations, de nos membres ou d'un pays africain partenaire.</p>
    </div>
    <div class="fade-in-right"><img src="images/workers.jpg" alt="Contrôle qualité" style="width:100%;height:380px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Processus</span><h2 class="section-title">Les étapes du contrôle</h2><div class="divider centered"></div></div>
    <div class="quality-steps">
      <div class="quality-step fade-in"><div class="quality-step-num">01</div><div class="step-title">Contrôle à la récolte</div><p class="step-text">Sélection des cabosses et cerises à maturité optimale.</p></div>
      <div class="quality-step fade-in delay-1"><div class="quality-step-num">02</div><div class="step-title">Fermentation maîtrisée</div><p class="step-text">Durée et conditions de fermentation surveillées pour développer les arômes.</p></div>
      <div class="quality-step fade-in delay-2"><div class="quality-step-num">03</div><div class="step-title">Séchage contrôlé</div><p class="step-text">Taux d'humidité vérifié régulièrement jusqu'à atteindre les normes d'export.</p></div>
      <div class="quality-step fade-in delay-3"><div class="quality-step-num">04</div><div class="step-title">Tri et inspection</div><p class="step-text">Élimination des fèves défectueuses, inspection visuelle et physique du lot.</p></div>
      <div class="quality-step fade-in delay-4"><div class="quality-step-num">05</div><div class="step-title">Regroupement et pesée</div><p class="step-text">Constitution des lots avec identification de l'origine.</p></div>
      <div class="quality-step fade-in"><div class="quality-step-num">06</div><div class="step-title">Inspection avant chargement</div><p class="step-text">Vérification finale avant ensachage et chargement au port de Douala.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Traçabilité</span><h2 class="section-title">Un lot, une origine</h2><div class="divider centered"></div></div>
    <div class="grid-2">
      <div class="fade-in-left">
        <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Chaque lot est identifié par son origine : plantation, producteur membre, région ou pays d'achat. Cette identification nous permet de répondre précisément aux questions de nos acheteurs et aux exigences de traçabilité de leurs marchés.</p>
        <ul class="checklist" style="margin-top:20px;">
          <li>Identification par plantation ou producteur</li>
          <li>Identification par région de culture</li>
          <li>Identification par pays d'origine (pour les achats africains)</li>
          <li>Documentation complète à chaque transfert</li>
        </ul>
      </div>
      <div class="fade-in-right">
        <h3 style="font-family:var(--font-sans);font-size:18px;font-weight:600;color:var(--chocolate);margin-bottom:16px;">Conformité</h3>
        <p style="color:var(--text-mid);margin-bottom:16px;line-height:1.8;">Nous respectons les règles d'exportation en vigueur et préparons les documents demandés par nos clients :</p>
        <ul class="checklist">
          <li>Certificat d'origine</li>
          <li>Certificat phytosanitaire</li>
          <li>Facture commerciale</li>
          <li>Liste de colisage</li>
          <li>Autres pièces selon le pays de destination</li>
        </ul>
      </div>
    </div>
    <div style="text-align:center;margin-top:48px;"><a href="contact.html" class="btn btn-primary fade-in">Demander notre fiche qualité</a></div>
  </div></section>"""
)

# =========================================================
# EXPORT
# =========================================================
write('export.html',
    'Export – SOPROCACAM COOP-CA | Partenaire export depuis Douala',
    'SOPROCACAM COOP-CA gère l\'export de cacao et café depuis Douala. Chocolatiers, torréfacteurs, négociants : nous nous occupons de tout.',
    banner('images/export.jpg', 'Exporter avec SOPROCACAM COOP-CA', 'Un partenaire à Douala qui s\'occupe de tout, jusqu\'au port.', 'Port de Douala export') +
    """
  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">À qui nous nous adressons</span><h2 class="section-title">Nos clients à l'international</h2><div class="divider centered"></div></div>
    <div class="cards-grid-4">
      <div class="card fade-in"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg><div class="card-title">Chocolatiers</div><p class="card-text">Industriels du chocolat à la recherche de fèves de qualité et de volumes réguliers.</p></div>
      <div class="card fade-in delay-1"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg><div class="card-title">Torréfacteurs</div><p class="card-text">Marques de café et torréfacteurs en quête d'origines africaines authentiques.</p></div>
      <div class="card fade-in delay-2"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg><div class="card-title">Négociants</div><p class="card-text">Importateurs et négociants en matières premières agricoles cherchant un partenaire fiable.</p></div>
      <div class="card fade-in delay-3"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg><div class="card-title">Traders</div><p class="card-text">Courtiers en matières premières agricoles à la recherche d'origines africaines.</p></div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Services</span><h2 class="section-title">Nos services</h2><div class="divider centered"></div></div>
    <div class="cards-grid-3" style="margin-bottom:48px;">
      <div class="card fade-in"><div class="card-title">Approvisionnement sur mesure</div><p class="card-text">Cacao du Cameroun, cacao d'autres origines africaines, café Robusta et Arabica. Nous adaptons les volumes et les origines à vos besoins.</p></div>
      <div class="card fade-in delay-1"><div class="card-title">Contrôle qualité</div><p class="card-text">Inspection et tri avant chargement. Chaque lot est identifié et documenté pour répondre à vos exigences de traçabilité.</p></div>
      <div class="card fade-in delay-2"><div class="card-title">Logistique et documents</div><p class="card-text">Préparation des documents d'export (certificat d'origine, phytosanitaire, facture commerciale) et coordination du chargement à Douala.</p></div>
      <div class="card fade-in delay-3"><div class="card-title">Échantillons</div><p class="card-text">Envoi d'échantillons avant toute commande ferme pour validation de la qualité.</p></div>
      <div class="card fade-in delay-4"><div class="card-title">Interlocuteur unique</div><p class="card-text">Un seul contact de votre demande jusqu'à la livraison, sans intermédiaire superflu.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Processus de commande</span><h2 class="section-title">Comment commander</h2><div class="divider centered"></div></div>
    <div class="process-steps">
      <div class="process-step fade-in"><div class="step-title">Contact</div><p class="step-text">Vous nous indiquez produit, origine, quantité et destination.</p></div>
      <div class="process-step fade-in delay-1"><div class="step-title">Offre</div><p class="step-text">Nous vous envoyons prix et conditions dans les meilleurs délais.</p></div>
      <div class="process-step fade-in delay-2"><div class="step-title">Échantillon</div><p class="step-text">Validation de la qualité avant toute commande ferme.</p></div>
      <div class="process-step fade-in delay-3"><div class="step-title">Contrat</div><p class="step-text">Signature et modalités de paiement convenus entre les parties.</p></div>
      <div class="process-step fade-in delay-4"><div class="step-title">Préparation & Expédition</div><p class="step-text">Contrôle, chargement, documents d'export depuis Douala.</p></div>
      <div class="process-step fade-in"><div class="step-title">Livraison</div><p class="step-text">Suivi jusqu'à la destination convenue.</p></div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header fade-in"><span class="section-label">Conditions commerciales</span><h2 class="section-title">Nos conditions</h2><div class="divider"></div></div>
    <div class="tech-table-wrap"><table class="data-table">
      <thead><tr><th>Élément</th><th>Conditions</th></tr></thead>
      <tbody>
        <tr><td>Commande minimale</td><td>1 conteneur de 20 pieds</td></tr>
        <tr><td>Conditionnement cacao</td><td>Sacs de jute de 60 à 65 kg</td></tr>
        <tr><td>Conditionnement café</td><td>Sacs de jute de 60 kg</td></tr>
        <tr><td>Port de chargement</td><td>Douala, Cameroun</td></tr>
        <tr><td>Modes de paiement</td><td>Lettre de crédit, virement bancaire selon termes du contrat</td></tr>
        <tr><td>Délai de réponse</td><td>Sous 48 heures</td></tr>
      </tbody>
    </table></div>
    <div style="text-align:center;margin-top:48px;"><a href="contact.html" class="btn btn-primary fade-in">Demander un devis export</a></div>
  </div></section>"""
)

# =========================================================
# PARTENAIRE
# =========================================================
write('partenaire.html',
    'Devenir producteur partenaire – SOPROCACAM COOP-CA',
    'Rejoignez le réseau SOPROCACAM COOP-CA. Un débouché fiable, un accompagnement technique et l\'accès aux marchés internationaux.',
    banner('images/partenaire.jpg', 'Rejoignez notre réseau', 'SOPROCACAM COOP-CA accueille des producteurs de cacao et de café motivés, soucieux de qualité et prêts à travailler en réseau.', 'Planteur camerounais') +
    """
  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Un processus simple et transparent</span><h2 class="section-title">Comment rejoindre la coopérative</h2><div class="divider centered"></div></div>
    <div class="partner-steps">
      <div class="partner-step fade-in">
        <div class="partner-step-num">1</div>
        <div><h3 style="font-family:var(--font-sans);font-size:18px;font-weight:600;color:var(--chocolate);margin-bottom:8px;">Premier contact</h3><p style="color:var(--text-mid);line-height:1.7;">Présentation de votre exploitation : localisation, culture pratiquée (cacao, café ou les deux), volumes habituels.</p></div>
      </div>
      <div class="partner-step fade-in delay-1">
        <div class="partner-step-num">2</div>
        <div><h3 style="font-family:var(--font-sans);font-size:18px;font-weight:600;color:var(--chocolate);margin-bottom:8px;">Visite et évaluation</h3><p style="color:var(--text-mid);line-height:1.7;">Échange sur vos pratiques, visite de votre exploitation et contrôle de la qualité de votre production.</p></div>
      </div>
      <div class="partner-step fade-in delay-2">
        <div class="partner-step-num">3</div>
        <div><h3 style="font-family:var(--font-sans);font-size:18px;font-weight:600;color:var(--chocolate);margin-bottom:8px;">Accord et intégration</h3><p style="color:var(--text-mid);line-height:1.7;">Définition des conditions de collecte, accompagnement technique et début de la collaboration.</p></div>
      </div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Ce que vous gagnez</span><h2 class="section-title">Les avantages du réseau</h2><div class="divider centered"></div></div>
    <div class="cards-grid-3">
      <div class="card fade-in"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><div class="card-title">Débouché fiable</div><p class="card-text">Un acheteur régulier pour votre récolte, à des prix annoncés clairement et à l'avance.</p></div>
      <div class="card fade-in delay-1"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg><div class="card-title">Accompagnement technique</div><p class="card-text">Formations aux bonnes pratiques de culture, de fermentation et de séchage.</p></div>
      <div class="card fade-in delay-2"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg><div class="card-title">Accès aux marchés internationaux</div><p class="card-text">Vos produits exportés vers les marchés internationaux grâce à notre réseau.</p></div>
    </div>
  </div></section>

  <section class="section bg-white"><div class="container"><div class="container-md">
    <div class="section-header centered fade-in"><span class="section-label">Formulaire d'inscription</span><h2 class="section-title">Rejoignez notre réseau</h2><div class="divider centered"></div></div>
    <div class="form-wrap">
      <div class="form-title">Devenir producteur partenaire</div>
      <form data-sopro>
        <div class="form-row">
          <div class="form-group"><label>Nom et prénom <span class="required">*</span></label><input type="text" required placeholder="Votre nom complet" /></div>
          <div class="form-group"><label>Téléphone <span class="required">*</span></label><input type="tel" required placeholder="+237 6XX XX XX XX" /></div>
        </div>
        <div class="form-group"><label>E-mail</label><input type="email" placeholder="votre@email.com" /></div>
        <div class="form-group"><label>Localité / Région <span class="required">*</span></label><input type="text" required placeholder="Ex: Mbalmayo, région Centre" /></div>
        <div class="form-group"><label>Vous êtes <span class="required">*</span></label>
          <select required>
            <option value="">Sélectionner...</option>
            <option>Producteur de cacao</option>
            <option>Producteur de café</option>
            <option>Producteur de cacao et de café</option>
            <option>Fournisseur de cacao d'un autre pays africain</option>
            <option>Autre</option>
          </select>
        </div>
        <div class="form-group"><label>Message</label><textarea placeholder="Décrivez votre exploitation : superficie, volumes habituels, pratiques..."></textarea></div>
        <input type="text" style="display:none;" tabindex="-1" name="_trap" />
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Envoyer ma demande</button>
        <div class="form-success">Merci pour votre envoi ! Notre équipe vous contacte rapidement.</div>
      </form>
    </div>
  </div></div></section>

  <section class="cta-section" style="position:relative;overflow:hidden;">
    <img src="images/plantation.jpg" alt="Plantation" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.15;" />
    <div class="container-md" style="text-align:center;position:relative;">
      <h2 class="section-title fade-in" style="color:white;">Vous cultivez du cacao ou du café ?</h2>
      <p class="section-sub fade-in delay-1">Alors n'hésitez plus. Rejoignez SOPROCACAM COOP-CA et accédez à un débouché fiable et aux marchés internationaux.</p>
      <div class="cta-btns fade-in delay-2"><a href="tel:+237673330101" class="btn btn-caramel">Nous appeler</a><a href="https://wa.me/237673330101" target="_blank" class="btn btn-secondary">WhatsApp</a></div>
    </div>
  </section>"""
)

# =========================================================
# ENGAGEMENT
# =========================================================
write('engagement.html',
    'Engagement & Durabilité – SOPROCACAM COOP-CA',
    'SOPROCACAM COOP-CA s\'engage pour ses producteurs, la terre, les communautés et ses clients. Découvrez nos actions concrètes.',
    banner('images/engagement.jpg', 'Terre généreuse, coopérative engagée', 'Notre réussite se mesure aussi à celle des familles qui cultivent.', 'Agriculture durable Cameroun') +
    """
  <section class="section bg-white"><div class="container">
    <div class="section-header centered fade-in"><span class="section-label">Nos engagements</span><h2 class="section-title">Ce qui nous guide</h2><div class="divider centered"></div></div>
    <div class="cards-grid-4">
      <div class="card fade-in" style="border-top:3px solid var(--chocolate);">
        <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        <div class="card-title">Pour les producteurs</div>
        <p class="card-text">Un débouché fiable, des prix annoncés clairement, un accompagnement technique et la volonté d'améliorer durablement les revenus de nos membres et de leurs équipes.</p>
      </div>
      <div class="card fade-in delay-1" style="border-top:3px solid var(--green);">
        <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22V12M12 12C12 6.48 7.52 2 2 2"/><path d="M12 12c0-5.52 4.48-10 10-10"/></svg>
        <div class="card-title">Pour la terre</div>
        <p class="card-text">Des pratiques qui protègent les sols, l'eau et la biodiversité : culture sous ombrage, gestion raisonnée des intrants, respect des forêts.</p>
      </div>
      <div class="card fade-in delay-2" style="border-top:3px solid var(--caramel);">
        <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
        <div class="card-title">Pour les communautés</div>
        <p class="card-text">Création d'emplois locaux, soutien aux zones de production et formation des travailleurs agricoles aux bonnes pratiques.</p>
      </div>
      <div class="card fade-in delay-3" style="border-top:3px solid var(--gold);">
        <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <div class="card-title">Pour nos clients</div>
        <p class="card-text">Transparence, éthique des affaires, respect des lois et des engagements pris. Une relation de confiance durable.</p>
      </div>
    </div>
  </div></section>

  <section class="section bg-cream"><div class="container"><div class="grid-2">
    <div class="fade-in-left">
      <span class="section-label">Nos actions</span>
      <h2 class="section-title">Ce que nous faisons concrètement</h2>
      <div class="divider"></div>
      <ul class="checklist">
        <li>Formations aux bonnes pratiques de culture, de fermentation et de séchage.</li>
        <li>Renouvellement progressif des plantations vieillissantes.</li>
        <li>Encouragement des jeunes et des femmes à s'impliquer dans la filière.</li>
        <li>Dialogue régulier avec les producteurs membres au sein du conseil d'administration.</li>
        <li>Partage des connaissances et des savoir-faire entre membres.</li>
        <li>Investissement dans la qualité pour accéder aux meilleurs marchés.</li>
      </ul>
      <div style="margin-top:32px;"><a href="partenaire.html" class="btn btn-primary">Devenir partenaire</a></div>
    </div>
    <div class="fade-in-right"><img src="images/workers.jpg" alt="Travailleurs agricoles camerounais" style="width:100%;height:420px;object-fit:cover;" loading="lazy" /></div>
  </div></div></section>

  <section class="cta-section"><div class="container-md" style="text-align:center;">
    <h2 class="section-title fade-in" style="color:white;">Ensemble, nous allons plus loin</h2>
    <p class="section-sub fade-in delay-1">Rejoignez une coopérative qui place les producteurs, la terre et les clients au cœur de son action.</p>
    <div class="cta-btns fade-in delay-2">
      <a href="partenaire.html" class="btn btn-caramel">Devenir partenaire</a>
      <a href="contact.html" class="btn btn-secondary">Nous contacter</a>
    </div>
  </div></section>"""
)

# =========================================================
# ACTUALITÉS
# =========================================================
write('actualites.html',
    'Actualités – SOPROCACAM COOP-CA',
    'Suivez les actualités de SOPROCACAM COOP-CA : vie des plantations, coopérative, marché du cacao et du café africain.',
    banner('images/plantation.jpg', 'Actualités', 'La vie de nos plantations, de notre coopérative et du marché.', 'Actualités SOPROCACAM') +
    """
  <section class="news-section"><div class="container">
    <div class="section-header fade-in"><span class="section-label">Dernières nouvelles</span><h2 class="section-title">Nos articles</h2><div class="divider"></div></div>
    <div class="news-grid">
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/cooperative.jpg" alt="Bienvenue sur notre site" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Octobre 2026</div><div class="news-card-title">Bienvenue sur le site de SOPROCACAM COOP-CA : qui nous sommes</div><p class="news-card-excerpt">SOPROCACAM COOP-CA lance son site web. Découvrez notre histoire, nos produits et notre coopérative.</p></div>
      </a>
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/cacao.jpg" alt="Fermentation cacao" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Septembre 2026</div><div class="news-card-title">Comment le cacao devient chocolat : le rôle de la fermentation</div><p class="news-card-excerpt">La fermentation est l'étape clé qui développe les arômes du cacao. Découvrez comment nous maîtrisons ce processus.</p></div>
      </a>
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/cafe.jpg" alt="Café Robusta Arabica" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Août 2026</div><div class="news-card-title">Café Robusta et Arabica : quelles différences pour l'acheteur ?</div><p class="news-card-excerpt">Profil aromatique, acidité, corps : comprendre les différences entre nos deux types de café pour faire le bon choix.</p></div>
      </a>
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/workers.jpg" alt="Coopérative producteurs" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Juillet 2026</div><div class="news-card-title">Pourquoi la coopérative change la vie des producteurs</div><p class="news-card-excerpt">Grâce à la force du groupe, nos membres accèdent à des marchés autrefois inaccessibles pour un producteur isolé.</p></div>
      </a>
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/afrique.jpg" alt="Cacao africain" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Juin 2026</div><div class="news-card-title">Pourquoi acheter du cacao africain auprès d'un seul fournisseur</div><p class="news-card-excerpt">Un interlocuteur unique pour plusieurs origines africaines : simplicité, qualité homogène et traçabilité.</p></div>
      </a>
      <a href="#" class="news-card">
        <div class="news-card-img"><img src="images/export.jpg" alt="Import cacao Douala" loading="lazy" /></div>
        <div class="news-card-body"><div class="news-date">Mai 2026</div><div class="news-card-title">Ce qu'il faut savoir avant d'importer du cacao depuis Douala</div><p class="news-card-excerpt">Documents d'export, Incoterms, conditions de paiement : notre guide pratique pour vos premiers achats.</p></div>
      </a>
    </div>
  </div></section>

  <section class="newsletter-section"><div class="container-md" style="text-align:center;">
    <span class="section-label">Newsletter</span>
    <h2 class="section-title" style="color:var(--chocolate);">Recevez nos actualités</h2>
    <p style="color:var(--text-mid);">Disponibilités de récolte, actualités du marché et vie de la coopérative directement dans votre boîte mail.</p>
    <form class="newsletter-form" onsubmit="return false;">
      <input type="email" placeholder="Votre adresse e-mail" required />
      <button type="submit">S'abonner</button>
    </form>
  </div></section>"""
)

# =========================================================
# FAQ
# =========================================================
write('faq.html',
    'FAQ – Questions fréquentes – SOPROCACAM COOP-CA',
    'Trouvez les réponses à vos questions sur SOPROCACAM COOP-CA : produits, volumes, export, qualité, paiement et plus.',
    banner('images/about.jpg', 'Questions fréquentes', 'Toutes les réponses à vos questions sur nos produits et services.', 'FAQ SOPROCACAM') +
    """
  <section class="faq-section"><div class="container">
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-question">Qui est SOPROCACAM COOP-CA ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Une société coopérative basée à Douala qui réunit plus de 13 producteurs industriels de cacao, exploite ses propres plantations de cacao et de café et achète aussi du cacao dans d'autres pays africains producteurs avant de l'exporter.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Quels produits exportez-vous ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Principalement des fèves de cacao et du café vert (Robusta et Arabica). Nous exportons depuis le port de Douala vers les marchés internationaux.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">D'où viennent vos produits ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">De nos plantations et de celles de nos membres dans les régions de culture du Cameroun, ainsi que, pour le cacao, de pays africains partenaires. L'origine de chaque lot est toujours précisée.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Que signifie COOP-CA ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Société coopérative avec conseil d'administration : une organisation de producteurs dirigée par un conseil élu par ses membres.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Quel volume minimum puis-je commander ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Un conteneur de 20 pieds. Contactez-nous pour discuter de vos besoins spécifiques en volume et en calendrier.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Pouvez-vous m'envoyer un échantillon ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Oui, nous proposons des échantillons pour valider la qualité avant toute commande ferme. Contactez-nous pour en faire la demande.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Comment le produit est-il conditionné ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">En sacs de jute de 60 à 65 kg pour le cacao et de 60 kg pour le café, étiquetés par lot avec indication de l'origine.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Quels documents fournissez-vous ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Facture commerciale, liste de colisage, certificat d'origine, certificat phytosanitaire et autres pièces selon la destination et les exigences de l'acheteur.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Depuis quel port expédiez-vous ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Depuis le port de Douala, principal port d'exportation du Cameroun.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Quels modes de paiement acceptez-vous ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Lettre de crédit et virement bancaire, selon les termes du contrat convenu entre les parties.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Pouvez-vous visiter vos plantations ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Oui, sur demande. Écrivez-nous pour organiser une visite de nos plantations et rencontrer nos équipes.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Comment devenir producteur partenaire ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Contactez-nous via la page <a href="partenaire.html" style="color:var(--caramel);">Devenir partenaire</a> en précisant votre localisation, votre culture et vos volumes habituels. Notre équipe vous contacte rapidement.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-question">Quelles langues parlez-vous ? <span class="faq-icon">+</span></button>
        <div class="faq-answer"><div class="faq-answer-inner">Français et anglais. Nous pouvons communiquer dans les deux langues pour répondre à vos besoins.</div></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:56px;">
      <p style="color:var(--text-mid);margin-bottom:20px;">Une autre question ?</p>
      <a href="contact.html" class="btn btn-primary">Contactez-nous</a>
    </div>
  </div></section>"""
)

# =========================================================
# CONTACT
# =========================================================
write('contact.html',
    'Contact – Demande de devis – SOPROCACAM COOP-CA',
    'Contactez SOPROCACAM COOP-CA pour une demande de devis, un échantillon ou toute question sur nos produits cacao et café.',
    banner('images/export.jpg', 'Parlons de votre projet', 'Une question, un besoin, une demande de prix ? Nous vous répondons rapidement.', 'Contact SOPROCACAM') +
    """
  <section class="section bg-white" style="padding-top:0;">
    <div class="map-wrap">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=9.677%2C4.040%2C9.750%2C4.090&amp;layer=mapnik&amp;marker=4.0603%2C9.7077" title="Siège SOPROCACAM COOP-CA – Akwa, Douala" loading="lazy" allowfullscreen></iframe>
    </div>
    <div class="container">
      <div class="contact-grid">
        <div>
          <h2 class="contact-info-title">SOPROCACAM COOP-CA</h2>
          <span class="contact-info-label">Siège social</span>
          <div class="contact-info-value">Akwa, rue Franceville, BP 6469<br>Douala, Cameroun</div>
          <span class="contact-info-label">Téléphone</span>
          <div class="contact-info-value"><a href="tel:+237673330101">+237 673 33 01 01</a></div>
          <span class="contact-info-label">E-mail</span>
          <div class="contact-info-value"><a href="mailto:soprocacam@gmail.com">soprocacam@gmail.com</a><br><a href="mailto:info@onetradecomodity.com">info@onetradecomodity.com</a></div>
          <span class="contact-info-label">NIU</span>
          <div class="contact-info-value">M052517855075A</div>
          <span class="contact-info-label">RCCM</span>
          <div class="contact-info-value" style="font-size:12px;">25/066/CMR/CE/10/051/CCA/032004/032004000</div>
          <div style="margin-top:28px;display:flex;flex-direction:column;gap:12px;">
            <a href="https://wa.me/237673330101" target="_blank" rel="noopener" class="btn btn-green" style="justify-content:center;">
              <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
              Écrire sur WhatsApp
            </a>
            <a href="tel:+237673330101" class="btn btn-outline" style="justify-content:center;">Appeler le +237 673 33 01 01</a>
          </div>
        </div>
        <div class="form-wrap">
          <div class="form-title">Demande de devis / Contact</div>
          <form data-sopro>
            <div class="form-row">
              <div class="form-group"><label>Prénom <span class="required">*</span></label><input type="text" required placeholder="Jean" /></div>
              <div class="form-group"><label>Nom <span class="required">*</span></label><input type="text" required placeholder="Dupont" /></div>
            </div>
            <div class="form-group"><label>Entreprise <span class="required">*</span></label><input type="text" required placeholder="Votre entreprise" /></div>
            <div class="form-row">
              <div class="form-group"><label>Pays <span class="required">*</span></label><input type="text" required placeholder="France" /></div>
              <div class="form-group"><label>E-mail <span class="required">*</span></label><input type="email" required placeholder="jean@exemple.com" /></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Téléphone</label><input type="tel" placeholder="+33 1 23 45 67 89" /></div>
              <div class="form-group"><label>Produit souhaité</label><select><option value="">Sélectionner...</option><option>Cacao du Cameroun</option><option>Cacao d'autres origines africaines</option><option>Café</option></select></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Quantité souhaitée</label><input type="text" placeholder="Ex: 1 conteneur 20 pieds" /></div>
              <div class="form-group"><label>Destination</label><input type="text" placeholder="Ex: Rotterdam, Anvers..." /></div>
            </div>
            <div class="form-group"><label>Message</label><textarea placeholder="Précisez votre besoin : volumes, qualité, calendrier, questions..."></textarea></div>
            <div class="form-consent"><input type="checkbox" required /><label style="text-transform:none;font-size:13px;letter-spacing:0;">J'accepte que mes informations soient utilisées pour répondre à ma demande.</label></div>
            <input type="text" style="display:none;" name="_trap" tabindex="-1" />
            <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Envoyer ma demande</button>
            <div class="form-success">Merci ! Votre demande a bien été envoyée. Notre équipe vous répond sous 48 heures.</div>
          </form>
        </div>
        <div>
          <div class="useful-links-title">Liens utiles</div>
          <div class="useful-links">
            <a href="qui-sommes-nous.html">À propos de SOPROCACAM</a>
            <a href="cooperative.html">La coopérative</a>
            <a href="cacao.html">Le cacao</a>
            <a href="cafe.html">Le café</a>
            <a href="export.html">Export</a>
            <a href="partenaire.html">Devenir partenaire</a>
            <a href="faq.html">FAQ</a>
            <a href="mentions-legales.html">Mentions légales</a>
          </div>
        </div>
      </div>
    </div>
  </section>"""
)

# =========================================================
# MENTIONS LÉGALES
# =========================================================
write('mentions-legales.html',
    'Mentions légales – SOPROCACAM COOP-CA',
    'Mentions légales du site SOPROCACAM COOP-CA. Éditeur, hébergeur, propriété intellectuelle, données personnelles.',
    banner('images/about.jpg', 'Mentions légales', 'Informations légales du site SOPROCACAM COOP-CA.', 'Mentions légales') +
    """
  <section class="section bg-white"><div class="container"><div style="max-width:800px;margin:0 auto;font-family:var(--font-body);color:var(--text-mid);line-height:1.8;">
    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Éditeur du site</h2>
    <p>Le présent site est édité par <strong>SOPROCACAM COOP-CA</strong>, société coopérative avec conseil d'administration.</p>
    <p>Siège social : Akwa, rue Franceville, BP 6469, Douala, Cameroun.</p>
    <p>NIU : M052517855075A</p>
    <p>RCCM : 25/066/CMR/CE/10/051/CCA/032004/032004000</p>
    <p>Téléphone : <a href="tel:+237673330101" style="color:var(--caramel);">+237 673 33 01 01</a></p>
    <p>E-mail : <a href="mailto:soprocacam@gmail.com" style="color:var(--caramel);">soprocacam@gmail.com</a></p>
    <p>Directeur de la publication : le Président du conseil d'administration de SOPROCACAM COOP-CA.</p>

    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Hébergement</h2>
    <p>[Nom et adresse de l'hébergeur – à compléter par l'équipe technique lors de la mise en ligne]</p>

    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Propriété intellectuelle</h2>
    <p>L'ensemble des contenus du site (textes, images, logo) est la propriété de SOPROCACAM COOP-CA ou utilisé avec autorisation. Les images libres de droits proviennent de Unsplash (voir fichier credits.txt). Toute reproduction sans accord écrit est interdite.</p>

    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Données personnelles</h2>
    <p>Les informations transmises via les formulaires servent uniquement à répondre à vos demandes. Elles ne sont ni vendues ni cédées à des tiers. Vous pouvez demander leur modification ou leur suppression en écrivant à <a href="mailto:soprocacam@gmail.com" style="color:var(--caramel);">soprocacam@gmail.com</a>.</p>

    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Responsabilité</h2>
    <p>SOPROCACAM COOP-CA s'efforce de fournir des informations exactes mais ne peut garantir l'absence d'erreurs. Les fiches produits sont données à titre indicatif ; les caractéristiques contractuelles sont celles du contrat de vente.</p>

    <h2 style="font-family:var(--font-sans);font-size:22px;font-weight:600;color:var(--chocolate);margin:40px 0 12px;">Cookies</h2>
    <p>Ce site n'utilise pas de cookies de traçage. Seules des données techniques nécessaires au bon fonctionnement du site peuvent être enregistrées temporairement.</p>

    <div style="margin-top:48px;padding-top:32px;border-top:1px solid rgba(81,38,22,.1);">
      <a href="index.html" class="btn btn-outline">Retour à l'accueil</a>
    </div>
  </div></div></section>"""
)

print("\nAll pages generated successfully!")
print("Files created in:", OUT)
