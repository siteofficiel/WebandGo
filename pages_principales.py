#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Web et Go — pages principales : accueil, création de site, réalisations."""

from build import (
    tete, entete, pied, bandeau, cta_final, reassurance, icone, FLECHE,
    bloc_faq, bloc_inclus, bloc_options, ecrire, schema_faq, schema_fil, ESSENTIEL,
    SCHEMA_ORG, PROJETS, EMAIL, SITE,
)

# ===========================================================================
# ACCUEIL
# ===========================================================================
def page_accueil():
    h = tete(
        "Web et Go — Création de site internet professionnel à Dinan",
        "Web et Go crée des sites internet professionnels pour les entreprises, "
        "indépendants et associations autour de Dinan. Design sur mesure, mise en ligne "
        "et référencement Google. À partir de 420 €, sans abonnement.",
        "index.html",
        schema=SCHEMA_ORG,
        precharger_hero=True,
    )
    h += entete("index.html", clair=True)

    h += f"""  <main id="contenu">

  <!-- ================= HÉROS ================= -->
  <section class="hero">
    <div class="conteneur conteneur--large">
      <div class="hero__grille">

        <div class="hero__texte">
          <p class="surtitre">Création de sites internet · Dinan</p>
          <h1>Votre site internet doit donner envie de <em>vous choisir</em>.</h1>
          <p class="hero__chapo">
            Web et Go crée des sites professionnels, modernes et efficaces pour les
            entreprises, indépendants et associations.
          </p>
          <div class="groupe-btn">
            <a class="btn btn--accent btn--large" href="contact.html">Créer mon site</a>
            <a class="btn btn--fantome btn--large" href="realisations.html">Voir les réalisations</a>
          </div>

          <div class="hero__reperes">
            <div class="hero__repere">
              <strong>420 €</strong>
              <span>Prix de départ, paiement unique</span>
            </div>
            <div class="hero__repere">
              <strong>0 €</strong>
              <span>D'abonnement Web et Go</span>
            </div>
            <div class="hero__repere">
              <strong>24 h</strong>
              <span>De délai de réponse</span>
            </div>
          </div>
        </div>

        <div class="hero__visuel">
          <div class="hero__photo" data-parallaxe="16">
            <img src="assets/img/hero.webp"
                 srcset="assets/img/hero-800.webp 900w, assets/img/hero.webp 1600w"
                 sizes="(max-width: 999px) 92vw, 46vw"
                 width="1600" height="1000" fetchpriority="high" decoding="async"
                 alt="Un site internet vitrine affiché sur un grand écran d'ordinateur et
                      repris sur un téléphone, posés sur un bureau clair.">
          </div>
          <span class="hero__etiquette"><i aria-hidden="true"></i>Sites livrés &amp; en ligne</span>
        </div>

      </div>
    </div>
  </section>

{reassurance()}

  <!-- ================= COMMENT ÇA MARCHE ================= -->
  <section class="section sur-sombre" id="methode">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Comment ça marche</p>
          <h2>Quatre étapes, et vous êtes en ligne.</h2>
        </div>
        <div>
          <p class="chapo">
            Un interlocuteur, un déroulé simple, aucune surprise. Vous savez à chaque
            moment où en est votre projet.
          </p>
        </div>
      </div>

      <div class="etapes reveler" style="--retard:60ms">
        <article class="etape">
          <span class="etape__num">01</span>
          <h3>On échange</h3>
          <p>Comprendre votre activité, vos objectifs et vos besoins réels avant d'ouvrir le moindre outil.</p>
        </article>
        <article class="etape">
          <span class="etape__num">02</span>
          <h3>Je conçois</h3>
          <p>Création de la structure et du design du site, adaptés à votre métier et à votre image.</p>
        </article>
        <article class="etape">
          <span class="etape__num">03</span>
          <h3>Vous validez</h3>
          <p>Présentation du site, relecture ensemble et ajustements jusqu'à ce que le résultat vous convienne.</p>
        </article>
        <article class="etape">
          <span class="etape__num">04</span>
          <h3>Je mets en ligne</h3>
          <p>Configuration technique, mise en ligne, formation à la prise en main et tutoriel PDF.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ================= TARIFS ================= -->
  <section class="section sur-ivoire" id="tarifs">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Tarifs</p>
          <h2>Un prix de base fixe. Des options selon vos besoins.</h2>
        </div>
        <div>
          <p class="chapo">
            Devis gratuit, zéro abonnement Web et Go : vous ne payez que ce que vous
            choisissez, et vous le savez avant de commencer.
          </p>
        </div>
      </div>

      <div class="tarif-principal reveler" style="--retard:60ms">
        <div class="tarif-principal__prix">
          <p class="etiquette">Forfait Basic</p>
          <h3>Création de votre site internet</h3>
          <p class="montant">
            <small>À partir de</small>
            <strong>420 €</strong>
          </p>
          <p style="color:rgba(247,244,238,.72);font-size:.95rem;margin:0">
            Paiement unique, sans abonnement.
          </p>
          <p class="mention">
            TVA non applicable, art. 293 B du CGI.<br>
            Prix fixe de départ + options sur mesure, détaillées dans le devis.
          </p>
        </div>
        <div class="tarif-principal__detail">
          <h4>Ce que couvre le forfait</h4>
          <p>
            Le design, la rédaction, la mise en ligne et la formation : tout est compris
            dans les 420 €, détaillés juste au-dessus. Les options éventuelles sont
            chiffrées à l'avance, ligne par ligne, dans un devis gratuit.
          </p>
          <div class="groupe-btn">
            <a class="btn btn--accent" href="contact.html">Obtenir mon devis gratuit</a>
            <a class="btn btn--fantome" href="tarifs.html">Voir toutes les options</a>
          </div>
        </div>
      </div>

      <div class="encadre reveler" style="--retard:80ms; margin-top:2rem">
        <h4>Zéro abonnement Web et Go</h4>
        <p>
          L'hébergement et le nom de domaine sont souscrits au nom du client et restent à
          sa charge (environ <strong>50 à 100 €/an</strong> selon l'hébergeur) — la
          configuration est incluse dans le forfait. Avantage : vous êtes 100 %
          propriétaire, sans intermédiaire.
        </p>
      </div>
    </div>
  </section>

{cta_final()}
  </main>

"""
    h += pied()
    ecrire("index.html", h)


# ===========================================================================
# CRÉATION DE SITE
# ===========================================================================
def page_creation():
    fil = schema_fil([("Accueil", "index.html"), ("Création de site", "creation-de-site.html")])
    h = tete(
        "Création de site internet — ce qui est compris | Web et Go",
        "Le détail de la création d'un site internet par Web et Go : design sur mesure, "
        "responsive, mise en ligne, nom de domaine, HTTPS, SEO de base, RGPD, formation. "
        "Forfait Basic à 420 €, options à la carte.",
        "creation-de-site.html",
        schema=fil,
        og_image="assets/img/craft.webp",
    )
    h += entete("creation-de-site.html", clair=True)
    h += bandeau(
        [("index.html", "Accueil"), (None, "Création de site")],
        "Ce que comprend votre site.",
        "Le Forfait Basic à 420 € inclut tout l'essentiel, de la conception à la mise en "
        "ligne. Pour aller plus loin, vous ajoutez uniquement les options qui vous "
        "servent — zéro abonnement, dans tous les cas.",
        boutons="""<div class="groupe-btn" style="margin-top:2rem">
        <a class="btn" href="contact.html">Demander mon devis</a>
        <a class="btn btn--fantome" href="tarifs.html">Voir les tarifs</a>
      </div>""",
    )
    h += reassurance()

    h += f"""  <main id="contenu">

  <section class="section">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Forfait Basic — 420 €</p>
          <h2>Ce qui est inclus, point par point.</h2>
        </div>
        <div>
          <p class="chapo">
            Un paiement unique, sans abonnement Web et Go. Tout ce qui suit est compris
            dans le prix de base.
          </p>
        </div>
      </div>
      <div class="inclus reveler" style="--retard:60ms">
{bloc_inclus()}
      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur">
      <div class="duo reveler">
        <div class="duo__media">
          <img src="assets/img/craft.webp" width="1600" height="893" loading="lazy"
               decoding="async"
               alt="Schéma d'une page de site internet et de sa version mobile, avec les
                    repères d'alignement de la mise en page.">
        </div>
        <div>
          <p class="surtitre">La méthode</p>
          <h2>Un site utile avant d'être joli.</h2>
          <p>
            Un joli site qui n'apporte aucun contact est un joli site raté. Avant de
            choisir une couleur ou une police, je regarde qui sont vos clients, ce qu'ils
            cherchent, et ce qui va les décider à vous écrire plutôt qu'à fermer l'onglet.
          </p>
          <p>Trois exigences guident chaque page&nbsp;:</p>
          <ul class="liste-check">
            <li><strong>Clarté</strong> — en deux secondes, vos visiteurs comprennent qui
                vous êtes et comment vous joindre.</li>
            <li><strong>Crédibilité</strong> — un design soigné et des contenus sérieux
                inspirent confiance dès la première visite.</li>
            <li><strong>Conversion</strong> — boutons, formulaire, carte et horaires :
                tout facilite la prise de contact.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= AVANT / APRÈS ================= -->
  <section class="section sur-ivoire" id="avant-apres">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Avant / après</p>
          <h2>La différence se voit en trois secondes.</h2>
        </div>
        <div>
          <p class="chapo">
            Beaucoup d'activités sérieuses sont desservies par un site vieillissant.
            Voici, concrètement, ce qui change.
          </p>
        </div>
      </div>

      <div class="avant-apres reveler" style="--retard:60ms">
        <article class="aa-carte aa-carte--avant">
          <span class="aa-carte__label">Avant</span>
          <div class="maquette">
            <svg viewBox="0 0 400 240" role="img"
                 aria-label="Schéma d'un site vieillissant : texte dense, contenus mal alignés, navigation surchargée.">
              <rect width="400" height="240" fill="#FFFFFF"/>
              <rect x="0" y="0" width="400" height="26" fill="#DDD8D0"/>
              <rect x="10" y="9" width="46" height="8" fill="#A9A49B"/>
              <g fill="#BDB8B0">
                <rect x="150" y="10" width="26" height="6"/><rect x="182" y="10" width="30" height="6"/>
                <rect x="218" y="10" width="22" height="6"/><rect x="246" y="10" width="34" height="6"/>
                <rect x="286" y="10" width="26" height="6"/><rect x="318" y="10" width="30" height="6"/>
                <rect x="354" y="10" width="20" height="6"/>
              </g>
              <rect x="12" y="38" width="180" height="12" fill="#8F8A82"/>
              <g fill="#CFC9C0">
                <rect x="12" y="60" width="376" height="5"/><rect x="12" y="70" width="376" height="5"/>
                <rect x="12" y="80" width="376" height="5"/><rect x="12" y="90" width="340" height="5"/>
                <rect x="12" y="100" width="376" height="5"/><rect x="12" y="110" width="300" height="5"/>
              </g>
              <rect x="12" y="126" width="110" height="70" fill="#E3DED6"/>
              <path d="M12 126h110v70H12z M12 126l110 70 M122 126l-110 70" stroke="#CFC9C0" fill="none" stroke-width="1"/>
              <g fill="#CFC9C0">
                <rect x="134" y="126" width="254" height="5"/><rect x="134" y="136" width="254" height="5"/>
                <rect x="134" y="146" width="230" height="5"/><rect x="134" y="156" width="254" height="5"/>
                <rect x="134" y="166" width="200" height="5"/><rect x="134" y="176" width="254" height="5"/>
                <rect x="134" y="186" width="170" height="5"/>
              </g>
              <rect x="12" y="208" width="376" height="20" fill="#EDE9E2"/>
              <rect x="20" y="215" width="120" height="5" fill="#CFC9C0"/>
            </svg>
          </div>
          <h3>Un site qui dessert votre travail</h3>
          <ul class="aa-liste">
            <li>{icone('croix', 14)}<span>Illisible sur téléphone, il faut zoomer</span></li>
            <li>{icone('croix', 14)}<span>On ne comprend pas tout de suite ce que vous faites</span></li>
            <li>{icone('croix', 14)}<span>Le contact est enterré au fond d'une page</span></li>
            <li>{icone('croix', 14)}<span>Absent ou mal placé dans les résultats Google</span></li>
            <li>{icone('croix', 14)}<span>Une image qui ne reflète pas la qualité de votre travail</span></li>
          </ul>
        </article>

        <article class="aa-carte aa-carte--apres">
          <span class="aa-carte__label">Après</span>
          <div class="maquette">
            <svg viewBox="0 0 400 240" role="img"
                 aria-label="Schéma d'un site moderne Web et Go : hiérarchie claire, grande image, appel à l'action visible.">
              <rect width="400" height="240" fill="#FCFAF6"/>
              <rect x="0" y="0" width="400" height="28" fill="#14181C"/>
              <circle cx="24" cy="14" r="7" fill="none" stroke="#8FC0CD" stroke-width="1.2"/>
              <rect x="38" y="11" width="40" height="6" rx="1" fill="#F7F4EE"/>
              <g fill="#8B8F94">
                <rect x="250" y="11" width="24" height="5" rx="1"/>
                <rect x="282" y="11" width="24" height="5" rx="1"/>
                <rect x="314" y="11" width="24" height="5" rx="1"/>
              </g>
              <rect x="348" y="7" width="42" height="14" rx="2" fill="#2E7387"/>
              <rect x="24" y="52" width="150" height="13" rx="2" fill="#14181C"/>
              <rect x="24" y="72" width="120" height="13" rx="2" fill="#14181C"/>
              <g fill="#C9C4BC">
                <rect x="24" y="96" width="150" height="5" rx="1"/>
                <rect x="24" y="106" width="130" height="5" rx="1"/>
              </g>
              <rect x="24" y="124" width="74" height="20" rx="2" fill="#1B4B5A"/>
              <rect x="106" y="124" width="66" height="20" rx="2" fill="none" stroke="#C9C4BC" stroke-width="1"/>
              <rect x="200" y="52" width="176" height="112" rx="3" fill="#DDE6E8"/>
              <path d="M200 140l40-30 34 24 30-22 72 40v10a3 3 0 0 1-3 3H203a3 3 0 0 1-3-3z" fill="#B7CBD1"/>
              <circle cx="248" cy="80" r="11" fill="#CBD9DD"/>
              <rect x="24" y="182" width="110" height="42" rx="3" fill="#F0EBE3"/>
              <rect x="145" y="182" width="110" height="42" rx="3" fill="#F0EBE3"/>
              <rect x="266" y="182" width="110" height="42" rx="3" fill="#F0EBE3"/>
              <g fill="#B0AAA1">
                <rect x="34" y="194" width="54" height="5" rx="1"/><rect x="34" y="205" width="80" height="4" rx="1"/>
                <rect x="155" y="194" width="54" height="5" rx="1"/><rect x="155" y="205" width="80" height="4" rx="1"/>
                <rect x="276" y="194" width="54" height="5" rx="1"/><rect x="276" y="205" width="80" height="4" rx="1"/>
              </g>
            </svg>
          </div>
          <h3>Un site qui travaille pour vous</h3>
          <ul class="aa-liste">
            <li>{icone('coche', 14)}<span>Parfaitement lisible sur téléphone, sans zoomer</span></li>
            <li>{icone('coche', 14)}<span>Votre métier compris en moins de dix secondes</span></li>
            <li>{icone('coche', 14)}<span>Un contact accessible depuis n'importe quelle page</span></li>
            <li>{icone('coche', 14)}<span>Une structure propre, pensée pour Google</span></li>
            <li>{icone('coche', 14)}<span>Une image à la hauteur de votre travail</span></li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section sur-sombre">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Comment ça marche</p>
          <h2>Le déroulé d'un projet.</h2>
        </div>
        <div>
          <p class="chapo">
            De la première discussion à la mise en ligne, vous savez toujours où en est
            votre site et ce qu'on attend de vous.
          </p>
        </div>
      </div>
      <div class="etapes reveler" style="--retard:60ms">
        <article class="etape">
          <span class="etape__num">01</span>
          <h3>On échange</h3>
          <p>Analyse de vos besoins, de votre secteur et de vos objectifs avant toute chose.
             Un devis gratuit et détaillé vous est remis à l'issue de cet échange.</p>
        </article>
        <article class="etape">
          <span class="etape__num">02</span>
          <h3>Je conçois</h3>
          <p>Création de la structure et du design du site, adaptés à votre activité.
             Je vous aide aussi à rédiger les textes si besoin.</p>
        </article>
        <article class="etape">
          <span class="etape__num">03</span>
          <h3>Vous validez</h3>
          <p>Présentation du site, relecture ensemble et ajustements. Rien n'est mis en
             ligne tant que le résultat ne vous convient pas.</p>
        </article>
        <article class="etape">
          <span class="etape__num">04</span>
          <h3>Je mets en ligne</h3>
          <p>Configuration du domaine, de l'hébergement et du HTTPS, mise en ligne,
             puis formation à la prise en main avec tutoriel PDF.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Contrat sur mesure</p>
          <h2>Les options, si vous en avez besoin.</h2>
        </div>
        <div>
          <p class="chapo">
            On part du Forfait Basic à 420 €, puis vous ajoutez uniquement ce qui vous
            sert. Les options marquées <strong>Tuto inclus</strong> sont livrées avec un
            tutoriel pour être 100 % autonome.
          </p>
        </div>
      </div>
      <div class="options reveler" style="--retard:60ms">
{bloc_options()}
      </div>
      <div class="duo-encadres reveler" style="--retard:80ms;margin-top:2.5rem">
        <div class="encadre">
          <h4>Après la mise en ligne</h4>
          <p>
            Les modifications sont facturées <strong>40 € de l'heure</strong>, sur devis
            gratuit préalable (1 h minimum). Besoin régulier ? Le carnet de
            <strong>5 h prépayées à 180 €</strong> est plus avantageux, sans limite de durée.
          </p>
        </div>
        <div class="encadre">
          <h4>Hébergement et nom de domaine</h4>
          <p>
            Ils sont souscrits <strong>à votre nom</strong>, directement chez l'hébergeur :
            vous êtes 100 % propriétaire, sans intermédiaire. Comptez en général
            <strong>50 à 100 € par an</strong>. La configuration est incluse dans le forfait.
          </p>
        </div>
      </div>
      <div class="groupe-btn reveler" style="margin-top:2.5rem">
        <a class="btn btn--accent" href="contact.html">Composer mon contrat (devis gratuit)</a>
        <a class="btn btn--fantome" href="documents/grille-tarifaire-webetgo.pdf">
          {icone('telechargement', 17)} Télécharger la grille tarifaire (PDF)
        </a>
      </div>
    </div>
  </section>

{cta_final("Un site complet, sans y passer vos soirées.",
           "Expliquez-moi votre projet et recevez un devis gratuit et détaillé, "
           "ligne par ligne.")}
  </main>

"""
    h += pied()
    ecrire("creation-de-site.html", h)


# ===========================================================================
# RÉALISATIONS
# ===========================================================================
def page_realisations():
    fil = schema_fil([("Accueil", "index.html"), ("Réalisations", "realisations.html")])
    h = tete(
        "Réalisations — sites internet créés par Web et Go",
        "Découvrez les sites internet réalisés par Web et Go : Rance Rénovation (artisan "
        "du bâtiment à Dinan) et Crème Anglaise (chorale associative Évran–Dinan), plus "
        "une démonstration des options sur mesure.",
        "realisations.html",
        schema=fil,
        og_image="assets/img/proj-rance.webp",
    )
    h += entete("realisations.html", clair=True)
    h += bandeau(
        [("index.html", "Accueil"), (None, "Réalisations")],
        "Des sites conçus pour être remarqués.",
        "Deux sites livrés et en ligne pour des activités bien réelles, plus une "
        "démonstration qui présente toutes les options du contrat sur mesure.",
    )

    h += """  <main id="contenu">
  <section class="section">
    <div class="conteneur">
      <div class="projets">
"""
    for i, p in enumerate(PROJETS):
        points = "".join(f"<li>{pt}</li>" for pt in p["points"])
        h += f"""        <article class="projet reveler" style="--retard:{i * 70}ms">
          <a class="projet__media" href="{p['lien']}" target="_blank" rel="noopener"
             aria-label="Découvrir le site {p['nom']} (nouvelle fenêtre)">
            <img src="{p['img']}" width="1400" height="875" loading="lazy" decoding="async"
                 alt="{p['alt']}">
            <span class="projet__voile" aria-hidden="true"><span>Découvrir</span></span>
          </a>
          <div class="projet__contenu">
            <p class="projet__meta">{p['secteur']}<i aria-hidden="true"></i><em>{p['domaine']}</em></p>
            <h2 style="font-size:clamp(1.5rem,1.2rem+1vw,2.1rem)">{p['nom']}</h2>
            <p>{p['texte']}</p>
            <ul class="liste-check">{points}</ul>
            <p style="margin-top:1.4rem">
              <a class="lien-fleche" href="{p['lien']}" target="_blank" rel="noopener">
                {p['cta']} {FLECHE}
              </a>
            </p>
          </div>
        </article>
"""

    h += f"""        <article class="projet projet--demo reveler">
          <div class="projet__media" style="display:grid;place-items:center;
               background:var(--ivoire);aspect-ratio:16/10;box-shadow:none;
               border:1px solid var(--trait)">
            <svg viewBox="0 0 400 250" width="100%" style="max-width:340px" role="img"
                 aria-label="Illustration schématique du site de démonstration L'Atelier du Bois,
                             présentant les options du contrat sur mesure.">
              <rect x="14" y="18" width="372" height="214" rx="4" fill="#FCFAF6"
                    stroke="#E0DAD0"/>
              <rect x="14" y="18" width="372" height="26" rx="4" fill="#14181C"/>
              <circle cx="34" cy="31" r="6" fill="none" stroke="#8FC0CD" stroke-width="1.2"/>
              <g fill="#8B8F94">
                <rect x="250" y="28" width="26" height="5" rx="1"/>
                <rect x="284" y="28" width="26" height="5" rx="1"/>
                <rect x="318" y="28" width="26" height="5" rx="1"/>
              </g>
              <rect x="352" y="24" width="26" height="13" rx="2" fill="#B4863F"/>
              <rect x="34" y="62" width="150" height="10" rx="2" fill="#14181C"/>
              <rect x="34" y="80" width="110" height="10" rx="2" fill="#14181C"/>
              <rect x="34" y="102" width="130" height="4" rx="1" fill="#C9C4BC"/>
              <rect x="34" y="112" width="100" height="4" rx="1" fill="#C9C4BC"/>
              <rect x="34" y="128" width="66" height="18" rx="2" fill="#1B4B5A"/>
              <rect x="204" y="62" width="152" height="84" rx="3" fill="#EDE7DC"/>
              <path d="M204 132l32-24 28 19 26-18 62 33v6a3 3 0 0 1-3 3H207a3 3 0 0 1-3-3z"
                    fill="#DCD2C2"/>
              <circle cx="242" cy="86" r="9" fill="#E5DDD0"/>
              <rect x="34" y="164" width="100" height="52" rx="3" fill="#F2EDE5"/>
              <rect x="144" y="164" width="100" height="52" rx="3" fill="#F2EDE5"/>
              <rect x="254" y="164" width="102" height="52" rx="3" fill="#F2EDE5"/>
              <g fill="#BEB7AC">
                <rect x="44" y="176" width="48" height="5" rx="1"/><rect x="44" y="188" width="72" height="4" rx="1"/>
                <rect x="154" y="176" width="48" height="5" rx="1"/><rect x="154" y="188" width="72" height="4" rx="1"/>
                <rect x="264" y="176" width="48" height="5" rx="1"/><rect x="264" y="188" width="74" height="4" rx="1"/>
              </g>
            </svg>
          </div>
          <div class="projet__contenu">
            <span class="badge-demo">Démonstration</span>
            <p class="projet__meta">Exemple — contrat sur mesure<i aria-hidden="true"></i>
              <em>atelier-du-bois.fr</em></p>
            <h2 style="font-size:clamp(1.5rem,1.2rem+1vw,2.1rem)">L'Atelier du Bois</h2>
            <p>
              Menuiserie artisanale — site de démonstration créé pour présenter toutes les
              options du contrat sur mesure, réunies au même endroit : espace
              administrateur, blog, galerie filtrable, formulaire de devis avancé et avis
              Google intégrés.
            </p>
            <ul class="liste-check">
              <li>Espace administrateur et blog en autonomie</li>
              <li>Galerie filtrable et formulaire de devis avancé</li>
              <li>Avis Google intégrés</li>
            </ul>
            <p style="margin-top:1.4rem">
              <a class="lien-fleche" href="contact.html">Demander la démo {FLECHE}</a>
            </p>
          </div>
        </article>
      </div>

      <div class="encadre reveler" style="margin-top:clamp(2.5rem,5vw,3.5rem)">
        <h4>Une précision honnête</h4>
        <p>
          La carte « Démonstration » est un exemple créé pour présenter les options du
          contrat sur mesure. <strong>Rance Rénovation</strong> et
          <strong>Crème Anglaise</strong> sont, elles, des réalisations livrées et
          réellement en ligne.
        </p>
      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur conteneur--etroit reveler" style="text-align:center">
      <p class="surtitre surtitre--centre">Votre projet</p>
      <h2>Vous avez un projet différent ?</h2>
      <p class="chapo" style="margin-inline:auto;text-align:center">
        Chaque site est adapté à votre activité, à vos contenus et à votre identité.
        Artisan, commerçant, profession libérale, TPE, association : le point de départ
        est toujours le même — une discussion.
      </p>
      <div class="groupe-btn" style="justify-content:center;margin-top:2rem">
        <a class="btn btn--accent" href="contact.html">Parler de mon projet</a>
        <a class="btn btn--fantome" href="tarifs.html">Voir les tarifs</a>
      </div>
    </div>
  </section>

{cta_final()}
  </main>

"""
    h += pied()
    ecrire("realisations.html", h)
