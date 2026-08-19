#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web et Go — générateur du site statique.

Assemble les pages HTML à partir de composants partagés (en-tête, pied,
blocs récurrents) afin d'éviter toute duplication et de garder un code
maintenable. Produit du HTML statique pur : aucune dépendance à l'exécution.

    python3 build.py
"""

import os
import re
import datetime

RACINE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.webetgo.fr"
EMAIL = "webetgo022@gmail.com"
AUJOURD_HUI = datetime.date.today().isoformat()

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
NAV = [
    ("index.html", "Accueil"),
    ("creation-de-site.html", "Création de site"),
    ("realisations.html", "Réalisations"),
    ("tarifs.html", "Tarifs"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
]

# ---------------------------------------------------------------------------
# Icônes (traits fins, 1.4px, style unifié)
# ---------------------------------------------------------------------------
def icone(nom, taille=20):
    chemins = {
        "plume": '<path d="M4 20c0-6 4-12 12-14 1.5-.5 3-1 4-2 0 4-.5 8-2 11-2 4-6 6-10 6H4Z"/><path d="M4 20c3-3 6-5 9-6"/>',
        "ecrans": '<rect x="2" y="4" width="14" height="10" rx="1"/><path d="M6 18h6"/><rect x="17" y="9" width="5" height="11" rx="1"/>',
        "loupe": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
        "bouclier": '<path d="M12 3 5 6v5.5c0 4.2 2.9 7.6 7 9.5 4.1-1.9 7-5.3 7-9.5V6l-7-3Z"/><path d="m9 12 2 2 4-4"/>',
        "main": '<path d="M8.5 11V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M11.5 11V4.5a1.5 1.5 0 0 1 3 0V11"/><path d="M14.5 11.5V7a1.5 1.5 0 0 1 3 0v7.5c0 3.6-2.6 6.5-6 6.5-2.3 0-4-1-5.2-2.9L4 14.4a1.6 1.6 0 0 1 2.7-1.7l1.8 2.3"/>',
        "compas": '<circle cx="12" cy="12" r="9"/><path d="m15 9-2.5 6L9 15l2.5-6L15 9Z"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3Z"/>',
        "cadenas": '<rect x="4" y="10" width="16" height="10" rx="1.5"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
        "sauvegarde": '<path d="M4 7c0-1.7 3.6-3 8-3s8 1.3 8 3-3.6 3-8 3-8-1.3-8-3Z"/><path d="M4 7v10c0 1.7 3.6 3 8 3s8-1.3 8-3V7"/><path d="M20 12c0 1.7-3.6 3-8 3s-8-1.3-8-3"/>',
        "domaine": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18"/><path d="M3.5 9h17M3.5 15h17"/>',
        "texte": '<path d="M5 6h14M5 11h14M5 16h9"/>',
        "conforme": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="m9.5 13.5 2 2 3.5-4"/>',
        "livre": '<path d="M4 5.5C4 4.7 4.7 4 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5v-13Z"/><path d="M20 5.5c0-.8-.7-1.5-1.5-1.5H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5v-13Z"/>',
        "coche": '<path d="m4 12.5 5 5L20 6.5"/>',
        "croix": '<path d="M6 6 18 18M18 6 6 18"/>',
        "epingle": '<path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
        "horloge": '<circle cx="12" cy="12" r="9"/><path d="M12 6.5V12l3.5 2.5"/>',
        "enveloppe": '<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
        "fleche": '<path d="M4 12h15"/><path d="m13 6 6 6-6 6"/>',
        "telechargement": '<path d="M12 3.5v11"/><path d="m7.5 10 4.5 4.5 4.5-4.5"/><path d="M4.5 19.5h15"/>',
    }
    d = chemins.get(nom, "")
    return (
        f'<svg width="{taille}" height="{taille}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true" focusable="false">{d}</svg>'
    )


FLECHE = (
    '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
    'focusable="false"><path d="M4 12h14"/><path d="m12 6 6 6-6 6"/></svg>'
)

# ---------------------------------------------------------------------------
# En-tête HTML
# ---------------------------------------------------------------------------
def tete(titre, description, slug, schema="", og_image="assets/img/hero.webp",
         precharger_hero=False, css_extra=""):
    canon = f"{SITE}/{slug}"
    css_sup = f'\n  <link rel="stylesheet" href="{css_extra}">' if css_extra else ""
    precharge = ""
    if precharger_hero:
        precharge = (
            '\n  <link rel="preload" as="image" href="assets/img/hero.webp" '
            'imagesrcset="assets/img/hero-800.webp 900w, assets/img/hero.webp 1800w" '
            'imagesizes="(max-width: 999px) 92vw, 46vw" fetchpriority="high">'
        )
    bloc_schema = f'\n  <script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="fr" class="sans-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>document.documentElement.classList.remove('sans-js');</script>
  <title>{titre}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canon}">
  <meta name="author" content="Gabriel LEGENTIL — Web et Go">
  <meta name="theme-color" content="#14181C">
  <meta name="format-detection" content="telephone=no">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Web et Go">
  <meta property="og:title" content="{titre}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}/{og_image}">
  <meta property="og:image:alt" content="Web et Go — création de sites internet professionnels à Dinan">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{titre}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE}/{og_image}">

  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="favicon-96.png" type="image/png" sizes="96x96">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">

  <link rel="preload" as="font" type="font/woff2" href="assets/fonts/Fraunces-latin.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="assets/fonts/InstrumentSans-latin.woff2" crossorigin>{precharge}
  <link rel="stylesheet" href="assets/css/main.css">{css_sup}{bloc_schema}
</head>
<body>
  <a class="evitement" href="#contenu">Aller au contenu principal</a>
"""


# ---------------------------------------------------------------------------
# Marque, en-tête, menu
# ---------------------------------------------------------------------------
def marque(lien="index.html"):
    """Monogramme officiel Web et Go : deux fichiers superposés, l'un clair
    (en-tête transparent / pied sombre), l'autre encre (en-tête accroché)."""
    return f"""<a class="marque" href="{lien}" aria-label="Web et Go — retour à l'accueil">
        <span class="marque__sigle">
          <img class="marque__logo marque__logo--sombre" src="assets/img/logo-mono.png"
               width="123" height="96" alt="" aria-hidden="true" decoding="async">
          <img class="marque__logo marque__logo--clair" src="assets/img/logo-mono-clair.png"
               width="123" height="96" alt="" aria-hidden="true" decoding="async">
        </span>
        <span class="marque__texte">Web <em>et</em> Go</span>
      </a>"""


def entete(actif, clair=False):
    """clair = héros sombre en haut de page → en-tête transparent au repos."""
    attr = ' data-entete-clair' if clair else ""
    classe = "entete entete--transparent" if clair else "entete"
    liens = []
    for href, label in NAV:
        courant = ' aria-current="page"' if href == actif else ""
        liens.append(f'<a class="nav__lien" href="{href}"{courant}>{label}</a>')
    nav = "\n          ".join(liens)

    liens_m = []
    for i, (href, label) in enumerate(NAV):
        courant = ' aria-current="page"' if href == actif else ""
        liens_m.append(
            f'<a class="panneau__lien" href="{href}" style="--i:{i}"{courant}>'
            f'<span>0{i + 1}</span>{label}</a>'
        )
    nav_m = "\n        ".join(liens_m)

    return f"""  <header class="{classe}" data-entete{attr}>
    <div class="entete__interieur">
      {marque()}
      <nav class="nav" aria-label="Navigation principale">
          {nav}
      </nav>
      <div class="entete__actions">
        <a class="btn btn--fantome" href="contact.html">Parlons de votre projet</a>
        <button class="hamburger" type="button" data-menu-bouton
                aria-expanded="false" aria-controls="menu-mobile" aria-label="Ouvrir le menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <div class="panneau" id="menu-mobile" data-menu-panneau>
    <nav class="panneau__nav" aria-label="Navigation mobile">
        {nav_m}
    </nav>
    <div class="panneau__pied">
      <a class="btn btn--accent" href="contact.html">Parlons de votre projet</a>
      <p class="panneau__contact">
        Écrivez directement à <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        Réponse sous 24&nbsp;h · Dinan, Évran et alentours
      </p>
    </div>
  </div>
"""


# ---------------------------------------------------------------------------
# Blocs partagés
# ---------------------------------------------------------------------------
def bandeau(fil, titre, chapo, boutons=""):
    items = []
    for i, (href, label) in enumerate(fil):
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li><span aria-current="page">{label}</span></li>')
    return f"""  <section class="bandeau">
    <div class="conteneur bandeau__contenu">
      <ol class="fil" aria-label="Fil d'Ariane">
        {''.join(items)}
      </ol>
      <h1>{titre}</h1>
      <p class="chapo">{chapo}</p>
      {boutons}
    </div>
  </section>
"""


def cta_final(titre="Prêt à donner une vraie présence en ligne à votre activité ?",
              texte="Expliquez-moi votre projet en quelques lignes. Je vous réponds sous 24&nbsp;h, "
                    "avec un devis gratuit et détaillé ligne par ligne."):
    return f"""  <section class="section sur-sombre cta-final">
    <div class="conteneur conteneur--etroit reveler">
      <p class="surtitre surtitre--centre">Prendre contact</p>
      <h2>{titre}</h2>
      <p class="chapo">{texte}</p>
      <div class="groupe-btn">
        <a class="btn btn--large" href="contact.html">Parlons de votre projet</a>
        <a class="btn btn--fantome btn--large" href="tarifs.html">Voir les tarifs</a>
      </div>
      <p class="cta-final__mail">
        Ou écrivez-moi directement : <a href="mailto:{EMAIL}">{EMAIL}</a>
      </p>
    </div>
  </section>
"""


def pied(js_extra=""):
    js_sup = f'\n  <script src="{js_extra}" defer></script>' if js_extra else ""
    return f"""  <footer class="pied">
    <div class="conteneur">
      <div class="pied__haut">
        <div>
          <h4>Informations</h4>
          <ul>
            <li><a href="tarifs.html#faq">Questions fréquentes</a></li>
            <li><a href="documents/grille-tarifaire-webetgo.pdf">Grille tarifaire (PDF)</a></li>
            <li><a href="mentions-legales.html">Mentions légales</a></li>
            <li><a href="confidentialite.html#cookies" data-bandeau-rouvrir>Cookies &amp; données</a></li>
            <li><a href="cgv.html">Conditions générales de vente</a></li>
            <li><a href="confidentialite.html">Confidentialité &amp; cookies</a></li>
          </ul>
        </div>
      </div>
      <div class="pied__bas">
        <p>© <span data-annee>2026</span> Web et Go — Gabriel LEGENTIL. Tous droits réservés.</p>
        <div class="pied__legal">
          <span>SIRET 106&nbsp;879&nbsp;794&nbsp;00019</span>
          <span>TVA non applicable, art.&nbsp;293&nbsp;B du CGI</span>
        </div>
      </div>
    </div>
  </footer>

  <div class="aviscook" data-bandeau hidden role="dialog" aria-modal="false"
       aria-labelledby="aviscook-titre" aria-describedby="aviscook-texte">
    <div class="aviscook__boite">
      <div>
        <p class="aviscook__titre" id="aviscook-titre">Cookies &amp; données</p>
        <p class="aviscook__texte" id="aviscook-texte">
          Ce site ne dépose <strong>aucun cookie</strong> et n'utilise aucun traceur.
          Seule la carte du secteur (page À propos) fait appel à OpenStreetMap, qui
          reçoit votre adresse IP pour afficher les images.
          <a href="confidentialite.html">En savoir plus</a>
        </p>
      </div>
      <div class="aviscook__actions">
        <button type="button" class="btn btn--accent" data-bandeau-accepter>
          J'ai compris
        </button>
        <button type="button" class="btn btn--fantome" data-bandeau-refuser
                aria-label="Rejeter l'affichage de la carte">
          Rejeter
        </button>
      </div>
    </div>
  </div>

  <script src="assets/js/site.js" defer></script>{js_sup}
  <script src="assets/js/bandeau.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Données réelles (issues du site actuel webetgo.fr)
# ---------------------------------------------------------------------------
OPTIONS = [
    ("Espace administrateur", "Gérez vos documents en autonomie", "+320 €", True),
    ("Blog", "Publiez vos actualités vous-même", "+250 €", True),
    ("Création de logo", "Fichiers haute définition", "+150 €", False),
    ("Formulaire avancé", "Devis en ligne, pièces jointes", "+120 €", False),
    ("Galerie / portfolio avancé", "", "+80 €", False),
    ("Avis Google intégrés", "", "+70 €", False),
    ("Rédaction des textes des pages supplémentaires", "", "+60 €/page", False),
    ("Page supplémentaire", "", "+50 €/page", False),
    ("Retouche / optimisation photos", "", "+50 €", False),
]

INCLUS = [
    ("plume", "Un design créé sur mesure",
     "Des pages pensées pour votre métier, vos couleurs et vos clients."),
    ("ecrans", "Parfait sur téléphone et ordinateur",
     "Un affichage vérifié sur mobile, tablette et ordinateur avant la livraison."),
    ("texte", "Aide à la rédaction",
     "Des textes clairs qui présentent vos services et donnent envie de vous écrire."),
    ("loupe", "Trouvable sur Google",
     "Une structure propre pour être bien présent dès la mise en ligne."),
    ("domaine", "Adresse web à votre nom",
     "Votre nom de domaine (ex. : monentreprise.fr) configuré à votre nom."),
    ("globe", "Mise en ligne complète",
     "Hébergement et configuration technique pris en charge de bout en bout."),
    ("cadenas", "HTTPS et site sécurisé",
     "Connexion sécurisée, un signal de confiance pour vos visiteurs."),
    ("conforme", "Livré en règle (RGPD)",
     "Cookies et mentions légales : votre site est conforme dès le départ."),
    ("epingle", "Formulaire, carte et galerie",
     "Formulaire de contact, carte Google Maps et galerie photos inclus."),
    ("livre", "Formation et tutoriel PDF",
     "Une prise en main expliquée simplement, tutoriel PDF inclus."),
    ("sauvegarde", "Sauvegarde de votre site",
     "Une copie de vos fichiers conservée, pour repartir vite en cas de problème."),
    ("main", "Disponibilité après la mise en ligne",
     "Je reste joignable une fois le site publié : vous n'êtes pas laissé seul."),
]

# Sous-ensemble affiché sur l'accueil : l'essentiel, sans dérouler les 12 items
# détaillés qui sont la matière de la page « Création de site ».
ESSENTIEL = [INCLUS[i] for i in (0, 1, 3, 5, 7, 11)]

FAQ = [
    ("Combien coûte un site internet ?",
     "La création d'un site commence à <strong>420 €</strong> avec le Forfait Basic : "
     "un paiement unique, sans abonnement Web et Go. Des options peuvent s'ajouter selon "
     "vos besoins (espace administrateur, blog, pages supplémentaires…). Le devis est "
     "gratuit et détaillé ligne par ligne avant de commencer."),
    ("Combien de temps faut-il pour créer un site ?",
     "En général, quelques semaines suffisent. Un délai précis vous est communiqué dès "
     "le premier échange, une fois votre projet et vos contenus connus."),
    ("Est-ce que le site fonctionne sur téléphone ?",
     "Oui. Votre site est conçu pour être beau et facile à lire sur téléphone, tablette "
     "et ordinateur. C'est systématiquement vérifié avant la livraison."),
    ("Est-ce que le référencement Google est inclus ?",
     "Votre site est construit avec une structure propre pour être bien présent sur "
     "Google dès le départ : titres cohérents, pages lisibles, temps de chargement "
     "maîtrisé. C'est compris dans le Forfait Basic à 420 €."),
    ("Dois-je m'occuper de l'hébergement ?",
     "Non, je m'occupe de toute la configuration. En revanche, l'hébergement et le nom "
     "de domaine sont souscrits <strong>à votre nom</strong>, directement chez "
     "l'hébergeur : comptez en général 50 à 100 € par an selon le prestataire. "
     "La configuration, elle, est incluse dans le forfait."),
    ("Est-ce que je suis propriétaire de mon nom de domaine ?",
     "Oui, à 100 %. L'hébergement et le nom de domaine sont pris à votre nom, sans "
     "intermédiaire. Vous en restez pleinement propriétaire, quoi qu'il arrive."),
    ("Est-ce qu'il y a un abonnement mensuel ?",
     "Aucun abonnement chez Web et Go. Vous payez la création une seule fois et vous "
     "êtes propriétaire de votre site. Seuls l'hébergement et le nom de domaine, "
     "souscrits à votre nom, restent à votre charge (environ 50 à 100 €/an)."),
    ("Peut-on modifier le site après la livraison ?",
     "Oui. Toute modification après la mise en ligne est facturée <strong>40 € de "
     "l'heure</strong>, sur devis gratuit préalable (1 h minimum). Si vous prévoyez des "
     "retouches régulières, le carnet de 5 h prépayées à <strong>180 €</strong> est plus "
     "avantageux, à consommer quand vous voulez."),
    ("Pourrai-je gérer mon site moi-même ?",
     "Oui, c'est le principe. La formation à la mise en ligne et un tutoriel PDF sont "
     "inclus dans le Forfait Basic. Les options comme l'espace administrateur ou le blog "
     "sont livrées avec leur propre tutoriel : vous ajoutez vos documents ou publiez vos "
     "actualités sans toucher au code."),
    ("Pour qui travaille Web et Go ?",
     "Pour les entreprises et les associations : artisans, commerçants, professions "
     "libérales, TPE/PME, auto-entrepreneurs, clubs et collectifs. Tous ceux qui veulent "
     "un beau site sans avoir besoin de s'y connaître en informatique."),
]

PROJETS = [
    {
        "nom": "Rance Rénovation",
        "secteur": "Artisan du bâtiment",
        "domaine": "rancerenovation.fr",
        "img": "assets/img/proj-rance.webp",
        "alt": "Page d'accueil du site Rance Rénovation, artisan du bâtiment à Dinan, "
               "réalisé par Web et Go",
        "texte": "Travaux du bâtiment dans le secteur de Dinan. Le site présente les "
                 "prestations et les chantiers réalisés — extensions, façades, terrasses "
                 "et rénovation — avec de vraies photos de réalisations et un contact "
                 "accessible depuis chaque page.",
        "points": ["Présentation claire des prestations", "Galerie de chantiers réalisés",
                   "Contact visible sur toutes les pages"],
        "lien": "https://rancerenovation.fr/index.html",
        "cta": "Découvrir le site",
    },
    {
        "nom": "Crème Anglaise",
        "secteur": "Association — chorale",
        "domaine": "Chorale d'Évran &amp; Dinan",
        "img": "assets/img/proj-creme.webp",
        "alt": "Page d'accueil du site de la chorale associative Crème Anglaise, "
               "secteur Évran et Dinan, réalisé par Web et Go",
        "texte": "Chorale associative du secteur Évran–Dinan. Un site chaleureux qui "
                 "présente le groupe, son répertoire et ses concerts, et qui explique "
                 "simplement comment rejoindre la chorale — l'essentiel pour une "
                 "association qui recrute ses membres.",
        "points": ["Identité chaleureuse et vivante", "Répertoire et concerts à jour",
                   "Parcours pensé pour recruter des choristes"],
        "lien": "https://siteofficiel.github.io/creme-anglaise-/fr.html",
        "cta": "Découvrir le site",
    },
]


def bloc_faq(limite=None, titre_id="faq"):
    items = []
    donnees = FAQ if limite is None else FAQ[:limite]
    for i, (q, r) in enumerate(donnees):
        items.append(f"""        <div class="faq__item">
          <h3 style="margin:0">
            <button class="faq__question" type="button" data-faq-question
                    aria-expanded="false" aria-controls="{titre_id}-r{i}" id="{titre_id}-q{i}">
              <span>{q}</span>
              <span class="faq__icone" aria-hidden="true"></span>
            </button>
          </h3>
          <div class="faq__reponse" id="{titre_id}-r{i}" role="region"
               aria-labelledby="{titre_id}-q{i}" data-ouvert="false">
            <div><p>{r}</p></div>
          </div>
        </div>""")
    return "\n".join(items)


def bloc_options():
    lignes = []
    for nom, note, prix, tuto in OPTIONS:
        puce = '<span class="puce-tuto">Tuto inclus</span>' if tuto else ""
        note_html = f'<span class="options__note">{note}</span>' if note else ""
        lignes.append(f"""        <div class="options__ligne">
          <span class="options__nom">{nom}{puce}{note_html}</span>
          <span class="options__pointille" aria-hidden="true"></span>
          <span class="options__prix">{prix}</span>
        </div>""")
    return "\n".join(lignes)


def bloc_inclus(items=None):
    items = items or INCLUS
    out = []
    for ico, titre, texte in items:
        out.append(f"""        <div class="inclus__item">
          {icone(ico)}
          <div>
            <h4>{titre}</h4>
            <p>{texte}</p>
          </div>
        </div>""")
    return "\n".join(out)


def reassurance():
    items = [
        ("compas", "Création sur mesure"),
        ("ecrans", "Design responsive"),
        ("loupe", "Optimisé pour Google"),
        ("cadenas", "Site sécurisé"),
        ("main", "Accompagnement humain"),
    ]
    lis = "\n        ".join(
        f'<li class="reassurance__item">{icone(ico)}<span>{txt}</span></li>'
        for ico, txt in items
    )
    return f"""  <section class="reassurance" aria-label="Ce qui est compris dans chaque site">
    <div class="conteneur conteneur--large">
      <ul class="reassurance__liste">
        {lis}
      </ul>
    </div>
  </section>
"""


# ---------------------------------------------------------------------------
# Données structurées
# ---------------------------------------------------------------------------
SCHEMA_ORG = """{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": "%(site)s/#entreprise",
    "name": "Web et Go",
    "alternateName": "WebetGo",
    "description": "Création de sites internet professionnels pour les entreprises, indépendants et associations. Design sur mesure, mise en ligne, référencement Google. À partir de 420 €, sans abonnement.",
    "url": "%(site)s/",
    "email": "%(email)s",
    "image": "%(site)s/assets/img/hero.webp",
    "priceRange": "À partir de 420 €",
    "vatID": "TVA non applicable, art. 293 B du CGI",
    "founder": { "@type": "Person", "name": "Gabriel LEGENTIL" },
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "38 Le Hambout",
      "postalCode": "22630",
      "addressLocality": "Saint-André-des-Eaux",
      "addressRegion": "Côtes-d'Armor",
      "addressCountry": "FR"
    },
    "areaServed": [
      { "@type": "City", "name": "Dinan" },
      { "@type": "City", "name": "Évran" },
      { "@type": "AdministrativeArea", "name": "Côtes-d'Armor" },
      { "@type": "AdministrativeArea", "name": "Bretagne" }
    ],
    "knowsLanguage": "fr",
    "makesOffer": {
      "@type": "Offer",
      "name": "Création de site internet — Forfait Basic",
      "description": "Site vitrine professionnel : design sur mesure, responsive, mise en ligne, configuration du nom de domaine et de l'hébergement, structure optimisée pour Google, conformité RGPD, formation et tutoriel PDF inclus.",
      "price": "420",
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock"
    }
  }""" % {"site": SITE, "email": EMAIL}


def schema_faq():
    import json
    entrees = []
    for q, r in FAQ:
        texte = re.sub(r"<[^>]+>", "", r).replace("&nbsp;", " ")
        entrees.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": texte},
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entrees,
    }, ensure_ascii=False, indent=2)


def schema_fil(elements):
    import json
    items = []
    for i, (nom, url) in enumerate(elements, start=1):
        items.append({"@type": "ListItem", "position": i, "name": nom,
                      "item": f"{SITE}/{url}"})
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }, ensure_ascii=False, indent=2)


def ecrire(nom, contenu):
    chemin = os.path.join(RACINE, nom)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    print(f"  ✓ {nom:<28} {len(contenu.encode('utf-8')) / 1024:6.1f} Ko")
