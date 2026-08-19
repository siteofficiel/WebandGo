#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web et Go — générateur du site statique.

    python3 generer.py

Écrit les 9 pages HTML, le sitemap, le robots.txt, le manifeste et le favicon
à la racine du dossier. Le livrable final est du HTML/CSS/JS pur : aucune
dépendance n'est nécessaire pour héberger le site.
"""

import os

from build import RACINE, SITE, AUJOURD_HUI, ecrire
from pages_principales import page_accueil, page_creation, page_realisations
from pages_secondaires import (
    page_tarifs, page_apropos, page_contact,
    page_mentions, page_cgv, page_confidentialite,
)

# Priorités et fréquences de mise à jour du sitemap
URLS = [
    ("index.html", "1.0", "monthly"),
    ("creation-de-site.html", "0.9", "monthly"),
    ("tarifs.html", "0.9", "monthly"),
    ("realisations.html", "0.8", "monthly"),
    ("a-propos.html", "0.7", "yearly"),
    ("contact.html", "0.8", "yearly"),
    ("cgv.html", "0.3", "yearly"),
    ("mentions-legales.html", "0.2", "yearly"),
    ("confidentialite.html", "0.2", "yearly"),
]


def sitemap():
    lignes = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for slug, prio, freq in URLS:
        loc = f"{SITE}/" if slug == "index.html" else f"{SITE}/{slug}"
        lignes += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{AUJOURD_HUI}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{prio}</priority>",
            "  </url>",
        ]
    lignes.append("</urlset>")
    ecrire("sitemap.xml", "\n".join(lignes) + "\n")


def robots():
    ecrire("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
""")


def manifeste():
    ecrire("site.webmanifest", """{
  "name": "Web et Go — Création de sites internet",
  "short_name": "Web et Go",
  "description": "Création de sites internet professionnels à Dinan et en Bretagne.",
  "lang": "fr",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "background_color": "#F7F4EE",
  "theme_color": "#14181C",
  "icons": [
    { "src": "assets/img/icone-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
    { "src": "assets/img/icone-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }
  ]
}
""")


def main():
    print("\n  Web et Go — génération du site\n" + "  " + "─" * 44)
    page_accueil()
    page_creation()
    page_realisations()
    page_tarifs()
    page_apropos()
    page_contact()
    page_mentions()
    page_cgv()
    page_confidentialite()
    print("  " + "─" * 44)
    sitemap()
    robots()
    manifeste()
    print("  " + "─" * 44)

    total = 0
    for dossier, _, fichiers in os.walk(RACINE):
        if "__pycache__" in dossier:
            continue
        for f in fichiers:
            if not f.endswith(".py"):
                total += os.path.getsize(os.path.join(dossier, f))
    print(f"  Poids total du site livrable : {total / 1024:.0f} Ko\n")


if __name__ == "__main__":
    main()
