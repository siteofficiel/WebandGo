# Web et Go — site vitrine

Site statique de **Web et Go** (Gabriel LEGENTIL) — création de sites internet
professionnels, secteur de Dinan et Évran (Côtes-d'Armor).

Aucun framework, aucune dépendance à installer pour le consulter : HTML, CSS et
JavaScript natif. Les polices, les images et la bibliothèque de carte sont
hébergées dans le dépôt.

---

## Publier sur GitHub Pages

1. Créer un dépôt et y pousser le contenu de cette archive (les fichiers doivent
   être à la **racine** du dépôt, `index.html` compris).
2. Dépôt → **Settings** → **Pages**.
3. *Source* : **Deploy from a branch** — branche `main`, dossier `/ (root)`.
4. Enregistrer. La mise en ligne prend une à deux minutes.

### Nom de domaine

Le fichier `CNAME` contient `www.webetgo.fr`. GitHub Pages servira donc le site
sur ce domaine, à condition de créer chez le registraire un enregistrement DNS
`CNAME` pour `www` pointant vers `<utilisateur>.github.io`.

> **Important — à lire si vous n'utilisez pas le domaine webetgo.fr.**
> Les balises `canonical`, les `og:url`, le `sitemap.xml` et le `robots.txt`
> désignent tous `https://www.webetgo.fr`. Si le site est publié sur une adresse
> différente (par exemple `utilisateur.github.io/webetgo`), ces balises
> indiqueront à Google que la version « officielle » est ailleurs, et les pages
> publiées risquent de ne pas être indexées.
>
> Dans ce cas : supprimer le fichier `CNAME`, ouvrir `build.py`, remplacer la
> valeur de `SITE` par l'adresse réelle, puis régénérer (voir plus bas).

---

## Modifier le site

Les pages HTML sont **générées** : il ne faut pas les modifier directement, sinon
les changements seront écrasés à la génération suivante. Les textes et la
structure vivent dans les fichiers Python.

| Fichier | Contenu |
|---|---|
| `build.py` | Constantes (`SITE`, `EMAIL`), en-tête, pied de page, bandeau, tarifs, FAQ, options |
| `pages_principales.py` | Accueil, Création de site, Réalisations |
| `pages_secondaires.py` | Tarifs, À propos, Contact, Mentions légales, CGV, Confidentialité |
| `generer.py` | Point d'entrée : écrit les 9 pages + `sitemap.xml`, `robots.txt`, `site.webmanifest` |

Régénérer après modification (Python 3, aucune dépendance externe) :

```bash
python3 generer.py
```

Prévisualiser en local :

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

---

## Structure

```
index.html, creation-de-site.html, realisations.html, tarifs.html,
a-propos.html, contact.html, mentions-legales.html, cgv.html,
confidentialite.html      les 9 pages générées
assets/css/               main.css (feuille principale) + carte.css
assets/js/                site.js, bandeau.js, carte.js
assets/fonts/             Fraunces + Instrument Sans (woff2)
assets/img/               visuels WebP, logos et icônes
assets/vendor/            Leaflet 1.9.4 (auto-hébergé)
documents/                grille tarifaire (PDF)
sitemap.xml, robots.txt, site.webmanifest
```

## Données personnelles

Le site **ne dépose aucun cookie** et n'utilise aucun traceur. Le seul appel à un
service extérieur est le fond de carte de la page À propos (OpenStreetMap /
CARTO), qui reçoit l'adresse IP du visiteur. Un bandeau l'annonce et permet de le
refuser ; le choix est conservé dans le `localStorage` du navigateur. Voir
`confidentialite.html`.

## Formulaire de contact

L'hébergement GitHub Pages est purement statique : il ne peut pas envoyer
d'e-mail. Le formulaire de la page Contact ouvre donc la messagerie du visiteur
avec le message pré-rempli (`mailto:` vers webetgo022@gmail.com), comme sur le
site actuel. Pour une réception directe en boîte mail, il faudrait un service
tiers de traitement de formulaire.

## Crédits

- [Leaflet](https://leafletjs.com/) 1.9.4 — BSD-2-Clause
- Fonds de carte © [OpenStreetMap](https://www.openstreetmap.org/copyright), tuiles © [CARTO](https://carto.com/attributions)
- Polices [Fraunces](https://fonts.google.com/specimen/Fraunces) et [Instrument Sans](https://fonts.google.com/specimen/Instrument+Sans) — SIL Open Font License 1.1
