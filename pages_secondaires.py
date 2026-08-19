#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Web et Go — tarifs, à propos, contact et pages légales."""

from build import (
    tete, entete, pied, bandeau, cta_final, reassurance, icone, FLECHE,
    bloc_faq, bloc_inclus, bloc_options, ecrire, schema_faq, schema_fil,
    EMAIL, SITE,
)

# ===========================================================================
# TARIFS
# ===========================================================================
def page_tarifs():
    import json
    schemas = [
        json.loads(schema_fil([("Accueil", "index.html"), ("Tarifs", "tarifs.html")])),
        json.loads(schema_faq()),
    ]
    h = tete(
        "Tarifs — création de site internet à partir de 420 € | Web et Go",
        "Tarifs Web et Go : Forfait Basic à 420 €, paiement unique, sans abonnement. "
        "Options sur mesure (espace administrateur, blog, logo…), modifications à 40 €/h. "
        "Devis gratuit et détaillé.",
        "tarifs.html",
        schema=json.dumps(schemas, ensure_ascii=False, indent=2),
    )
    h += entete("tarifs.html", clair=True)
    h += bandeau(
        [("index.html", "Accueil"), (None, "Tarifs")],
        "Un prix clair, annoncé avant de commencer.",
        "Un prix de base fixe, des options que vous choisissez, et zéro abonnement Web et "
        "Go. Le devis détaille chaque ligne : vous savez exactement ce que vous payez.",
    )

    h += f"""  <main id="contenu">

  <section class="section">
    <div class="conteneur">
      <div class="tarif-principal reveler">
        <div class="tarif-principal__prix">
          <p class="etiquette">Forfait Basic</p>
          <h2 style="color:inherit">Création de votre site internet</h2>
          <p class="montant">
            <small>À partir de</small>
            <strong>420 €</strong>
          </p>
          <p style="color:rgba(247,244,238,.72);font-size:.95rem;margin:0">
            Paiement unique, sans abonnement.
          </p>
          <p class="mention">
            TVA non applicable, art. 293 B du CGI.<br>
            Le prix final dépend des options retenues ; il est fixé dans le devis, avant
            le début du projet.
          </p>
        </div>
        <div class="tarif-principal__detail">
          <h3 style="font-size:1.15rem">Ce que comprennent les 420 €</h3>
          <ul class="liste-check">
            <li>Un design créé sur mesure, parfait sur téléphone et ordinateur</li>
            <li>Mise en ligne complète : hébergement et adresse web configurés à votre nom</li>
            <li>Votre site trouvable sur Google dès le départ</li>
            <li>Formulaire de contact, carte Google Maps et galerie photos</li>
            <li>Conformité RGPD incluse (cookies, mentions légales)</li>
            <li>Formation à la mise en ligne + tutoriel PDF</li>
            <li>Disponibilité après la mise en ligne</li>
          </ul>
          <div class="groupe-btn">
            <a class="btn btn--accent" href="contact.html">Demander mon devis gratuit</a>
            <a class="btn btn--fantome" href="documents/grille-tarifaire-webetgo.pdf">
              {icone('telechargement', 17)} Grille tarifaire (PDF)
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Contrat sur mesure</p>
          <h2>Les options, à la carte.</h2>
        </div>
        <div>
          <p class="chapo">
            Ajoutées au Forfait Basic uniquement si elles vous servent. Les options
            marquées <strong>Tuto inclus</strong> sont livrées avec un tutoriel pour être
            autonome.
          </p>
        </div>
      </div>
      <div class="options reveler" style="--retard:60ms">
{bloc_options()}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Après la livraison</p>
          <h2>Et ensuite, combien ça coûte ?</h2>
        </div>
        <div>
          <p class="chapo">
            Rien d'obligatoire, rien d'automatique. Vous ne payez que si vous demandez
            quelque chose.
          </p>
        </div>
      </div>

      <div class="duo-encadres reveler" style="--retard:60ms">
        <div class="encadre">
          <h4>Modifications ponctuelles</h4>
          <p>
            <strong>40 € de l'heure</strong>, avec un devis gratuit avant toute
            intervention. Facturation à l'heure entamée, 1 h minimum.
          </p>
        </div>
        <div class="encadre">
          <h4>Carnet d'heures</h4>
          <p>
            <strong>5 h prépayées pour 180 €</strong> (au lieu de 200 €), à utiliser quand
            vous voulez, <strong>sans limite de durée</strong>. Idéal si votre site évolue
            régulièrement.
          </p>
        </div>
        <div class="encadre encadre--sombre">
          <h4>Hébergement et nom de domaine</h4>
          <p>
            Souscrits <strong>à votre nom</strong>, ils restent à votre charge : comptez en
            général <strong>50 à 100 € par an</strong> selon l'hébergeur. La configuration
            initiale est incluse dans le forfait, et vous restez propriétaire à 100 %.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section sur-sombre">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Pour qui</p>
          <h2>Des sites pour les professionnels et les associations.</h2>
        </div>
        <div>
          <p class="chapo">
            Le Forfait Basic est pensé pour les structures qui ont besoin d'une présence
            en ligne sérieuse, sans budget d'agence.
          </p>
        </div>
      </div>
      <ul class="villes reveler" style="--retard:60ms">
        <li>Artisans</li>
        <li>Commerçants</li>
        <li>Professions libérales</li>
        <li>TPE / PME</li>
        <li>Auto-entrepreneurs</li>
        <li>Associations, clubs et collectifs</li>
      </ul>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="conteneur conteneur--etroit">
      <div class="reveler" style="text-align:center;margin-bottom:clamp(2rem,4vw,3rem)">
        <p class="surtitre surtitre--centre">Questions fréquentes</p>
        <h2>Vos questions sur les tarifs et le déroulé</h2>
      </div>
      <div class="faq reveler" style="--retard:60ms">
{bloc_faq(titre_id='tarifs')}
      </div>
    </div>
  </section>

{cta_final("Un devis gratuit, détaillé ligne par ligne.",
           "Décrivez votre projet en quelques phrases : je vous réponds sous 24&nbsp;h "
           "avec un chiffrage précis, sans engagement.")}
  </main>

"""
    h += pied()
    ecrire("tarifs.html", h)


# ===========================================================================
# À PROPOS
# ===========================================================================
def page_apropos():
    fil = schema_fil([("Accueil", "index.html"), ("À propos", "a-propos.html")])
    h = tete(
        "À propos — Gabriel Legentil, créateur de sites internet à Dinan | Web et Go",
        "Web et Go, c'est Gabriel Legentil : un interlocuteur unique, du premier échange à "
        "la mise en ligne. Création de sites internet professionnels autour de Dinan et "
        "Évran, en Côtes-d'Armor.",
        "a-propos.html",
        schema=fil,
        og_image="assets/img/atelier.webp",
        css_extra="assets/css/carte.css",
    )
    h += entete("a-propos.html", clair=True)
    h += bandeau(
        [("index.html", "Accueil"), (None, "À propos")],
        "Un interlocuteur unique, du premier échange à la mise en ligne.",
        "Web et Go, ce n'est pas un service client à numéro. C'est Gabriel Legentil, "
        "installé à Saint-André-des-Eaux, qui conçoit, rédige, met en ligne — et reste "
        "joignable après.",
    )

    h += f"""  <main id="contenu">

  <section class="section">
    <div class="conteneur">
      <div class="portrait reveler">
        <div class="portrait__media">
          <img src="assets/img/atelier.webp" width="1000" height="1241" loading="lazy"
               decoding="async"
               alt="Schéma reliant la maquette d'une page de site à sa déclinaison sur
                    téléphone, étape par étape.">
        </div>
        <div>
          <p class="surtitre">Qui je suis</p>
          <h2>Bonjour, je m'appelle Gabriel.</h2>
          <p>
            Je crée des sites internet pour les professionnels et les associations du
            secteur de Dinan, en Côtes-d'Armor. Pas de grande structure derrière : quand
            vous m'écrivez, c'est moi qui vous réponds, et c'est encore moi qui mettrai
            votre site en ligne.
          </p>
          <p>
            J'ai monté Web et Go avec une idée simple : beaucoup d'entreprises sérieuses
            n'ont pas de site, ou en ont un qui leur fait du tort. Souvent parce qu'on leur
            a proposé des devis à plusieurs milliers d'euros, des abonnements sans fin, ou
            des interlocuteurs qui parlent une langue qu'elles ne comprennent pas.
          </p>
          <p>
            Mon travail consiste à retirer cette barrière. Vous parlez de votre métier ;
            je m'occupe de la technique. Vous n'avez rien à installer, rien à
            paramétrer, rien à apprendre — sauf si vous le souhaitez, et dans ce cas je
            vous forme.
          </p>
          <div class="signature">
            <strong>Gabriel LEGENTIL</strong>
            <span>Fondateur de Web et Go — Saint-André-des-Eaux, Côtes-d'Armor</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Ma façon de travailler</p>
          <h2>Trois principes, tenus sur chaque projet.</h2>
        </div>
        <div>
          <p class="chapo">
            Ce ne sont pas des slogans : ce sont les règles auxquelles vous pouvez me
            tenir, du devis à la mise en ligne.
          </p>
        </div>
      </div>

      <div class="piliers reveler" style="--retard:60ms">
        <article class="pilier">
          <span class="pilier__num">01</span>
          <h3>Parler clairement</h3>
          <p>
            Pas de jargon, pas de mots compliqués pour impressionner. Si une chose est
            techniquement nécessaire, je vous explique pourquoi, en français.
          </p>
        </article>
        <article class="pilier">
          <span class="pilier__num">02</span>
          <h3>Annoncer le prix avant</h3>
          <p>
            Le devis est gratuit et détaillé ligne par ligne. Vous savez ce que vous payez,
            et ce que vous ne payez pas. Aucune facture ne tombe par surprise.
          </p>
        </article>
        <article class="pilier">
          <span class="pilier__num">03</span>
          <h3>Rester joignable</h3>
          <p>
            La mise en ligne n'est pas une porte qui se ferme. Une question six mois plus
            tard trouve encore une réponse — c'est le minimum quand on travaille près de
            chez ses clients.
          </p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="conteneur">
      <div class="duo duo--inverse reveler">
        <div class="duo__media">
          <img src="assets/img/craft.webp" width="1600" height="893" loading="lazy"
               decoding="async"
               alt="Schéma d'une page de site internet et de sa version mobile, avec les
                    repères d'alignement de la mise en page.">
        </div>
        <div>
          <p class="surtitre">Ce que vous n'aurez pas à faire</p>
          <h2>La technique, c'est mon métier. Pas le vôtre.</h2>
          <p>
            Un site internet demande une quinzaine de compétences différentes. Vous n'avez
            à en maîtriser aucune. Voici ce dont je m'occupe intégralement&nbsp;:
          </p>
          <ul class="non-liste">
            <li>Le code</li>
            <li>L'hébergement</li>
            <li>Les DNS</li>
            <li>Le HTTPS</li>
            <li>Le référencement</li>
            <li>Les sauvegardes</li>
            <li>La conformité RGPD</li>
            <li>L'affichage mobile</li>
            <li>Les performances</li>
          </ul>
          <p style="margin-top:1.8rem">
            <a class="lien-fleche" href="creation-de-site.html">
              Voir le détail de ce qui est compris {FLECHE}</a>
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section sur-sombre" id="zone">
    <div class="conteneur">
      <div class="zone reveler">
        <div>
          <p class="surtitre">Zone d'intervention</p>
          <h2>Web et Go, au service des professionnels de votre région.</h2>
          <p>
            J'interviens principalement autour de <strong>Dinan</strong> et
            <strong>Évran</strong>, dans les <strong>Côtes-d'Armor</strong>. Dans ce
            secteur, un rendez-vous en personne est possible : c'est souvent la meilleure
            façon de bien comprendre un projet.
          </p>
          <p>
            Ailleurs en Bretagne ou en France, un projet se mène très bien à distance, par
            e-mail. Dans tous les cas, la réponse arrive sous 24 h, week-end compris, et le
            devis est gratuit.
          </p>
          <ul class="villes">
            <li>Dinan</li>
            <li>Évran</li>
            <li>Côtes-d'Armor (22)</li>
            <li>Bretagne</li>
            <li>Reste de la France, à distance</li>
          </ul>
          <p style="margin-top:1.8rem">
            <a class="lien-fleche" href="https://maps.google.com/?q=Dinan,Cotes-d-Armor,France"
               target="_blank" rel="noopener">Voir Dinan sur Google Maps {FLECHE}</a>
          </p>
        </div>
        <div class="duo__media">
          <div class="carte" data-carte>
            <div class="carte__ecran" data-carte-ecran>
              <p class="carte__titre">Le secteur de Dinan et d'Évran</p>
              <p class="carte__note">
                L'affichage de la carte est désactivé. Elle est fournie par OpenStreetMap
                et ne dépose aucun cookie.
              </p>
              <button type="button" class="btn btn--accent"
                      data-carte-activer>Afficher la carte</button>
              <p class="carte__repli">
                <a class="lien-fleche"
                   href="https://maps.google.com/?q=Dinan,Cotes-d-Armor,France"
                   target="_blank" rel="noopener">Voir le secteur sur une carte {FLECHE}</a>
              </p>
              <p class="carte__erreur" data-carte-erreur hidden>
                La carte n'a pas pu être chargée. Vous pouvez consulter le secteur sur
                Google&nbsp;Maps avec le lien ci-contre.
              </p>
            </div>
            <div class="carte__toile" data-carte-toile hidden role="application"
                 aria-label="Carte du secteur d'intervention autour de Dinan et Évran,
                             dans les Côtes-d'Armor"></div>
          </div>
          <p class="duo__legende">Dinan, Côtes-d'Armor — le secteur où j'interviens.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur conteneur--etroit reveler">
      <div style="text-align:center;margin-bottom:2.5rem">
        <p class="surtitre surtitre--centre">Informations</p>
        <h2>L'entreprise en clair</h2>
      </div>
      <dl class="fiche">
        <div><dt class="cle">Nom commercial</dt><dd class="val">WebetGo</dd></div>
        <div><dt class="cle">Responsable</dt><dd class="val">Gabriel LEGENTIL</dd></div>
        <div><dt class="cle">Statut</dt><dd class="val">Entrepreneur individuel</dd></div>
        <div><dt class="cle">SIRET</dt><dd class="val">106 879 794 00019</dd></div>
        <div><dt class="cle">Adresse</dt>
             <dd class="val">38 Le Hambout, 22630 Saint-André-des-Eaux</dd></div>
        <div><dt class="cle">TVA</dt>
             <dd class="val">Non applicable, art. 293 B du CGI</dd></div>
        <div><dt class="cle">Contact</dt>
             <dd class="val"><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      </dl>
    </div>
  </section>

{cta_final("Envie d'en parler de vive voix ?",
           "Écrivez-moi en quelques lignes. Si vous êtes dans le secteur de Dinan, "
           "on peut aussi se rencontrer.")}
  </main>

"""
    h += pied(js_extra="assets/js/carte.js")
    ecrire("a-propos.html", h)


# ===========================================================================
# CONTACT
# ===========================================================================
def page_contact():
    fil = schema_fil([("Accueil", "index.html"), ("Contact", "contact.html")])
    h = tete(
        "Contact — parlons de votre projet de site internet | Web et Go",
        "Contactez Web et Go pour votre projet de site internet à Dinan, Évran et "
        "alentours. Réponse sous 24 h, week-end compris. Devis gratuit et sans "
        "engagement.",
        "contact.html",
        schema=fil,
    )
    h += entete("contact.html", clair=True)
    h += bandeau(
        [("index.html", "Accueil"), (None, "Contact")],
        "Parlons de votre projet.",
        "Décrivez votre activité et ce que vous attendez de votre site. Je vous réponds "
        "sous 24 h, week-end compris, avec un devis gratuit et détaillé ligne par ligne.",
    )

    h += f"""  <main id="contenu">

  <section class="section">
    <div class="conteneur">
      <div class="contact-grille">

        <aside class="coordonnees reveler">
          <h2 style="font-size:clamp(1.4rem,1.2rem+.6vw,1.8rem);margin-top:0">
            Écrire à Web et Go
          </h2>

          <div class="coordonnees__item">
            {icone('enveloppe', 19)}
            <div>
              <p class="coordonnees__label">E-mail</p>
              <p class="coordonnees__valeur"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
              <p class="coordonnees__note">Le moyen le plus direct de me joindre.</p>
            </div>
          </div>

          <div class="coordonnees__item">
            {icone('horloge', 19)}
            <div>
              <p class="coordonnees__label">Délai de réponse</p>
              <p class="coordonnees__valeur">Moins de 24 h</p>
              <p class="coordonnees__note">Week-end compris.</p>
            </div>
          </div>

          <div class="coordonnees__item">
            {icone('epingle', 19)}
            <div>
              <p class="coordonnees__label">Zone d'intervention</p>
              <p class="coordonnees__valeur">Dinan, Évran et alentours</p>
              <p class="coordonnees__note">
                Côtes-d'Armor (22) — rendez-vous possible sur place.<br>
                <a class="lien-fleche" style="margin-top:.5rem"
                   href="https://maps.google.com/?q=Dinan,Cotes-d-Armor,France"
                   target="_blank" rel="noopener">Voir sur Google Maps {FLECHE}</a>
              </p>
            </div>
          </div>

          <div class="coordonnees__item">
            {icone('conforme', 19)}
            <div>
              <p class="coordonnees__label">Devis</p>
              <p class="coordonnees__valeur">Gratuit et sans engagement</p>
              <p class="coordonnees__note">Détaillé ligne par ligne, avant tout démarrage.</p>
            </div>
          </div>

          <p class="coordonnees__note" style="margin-top:2rem;padding-top:1.4rem;
             border-top:1px solid var(--trait)">
            Web et Go — Gabriel LEGENTIL, entrepreneur individuel.<br>
            38 Le Hambout, 22630 Saint-André-des-Eaux.<br>
            SIRET 106 879 794 00019.
          </p>
        </aside>

        <div class="reveler" style="--retard:60ms">
          <!-- Pas d'attribut action : une cible "mailto:" n'étant pas sécurisée (HTTPS),
               le navigateur affiche un avertissement et désactive la saisie automatique.
               L'envoi est composé par site.js ; sans JavaScript, le bouton « Écrire à … »
               ci-dessous prend le relais. -->
          <form class="formulaire" data-formulaire data-destinataire="{EMAIL}" novalidate>

            <h2 style="font-size:clamp(1.4rem,1.2rem+.6vw,1.8rem);margin-top:0">
              Votre demande
            </h2>
            <p style="color:var(--gris-chaud);font-size:.95rem;margin-bottom:2rem">
              Les champs marqués d'un astérisque (*) sont obligatoires.
              Plus vous m'en dites, plus le devis sera précis.
            </p>

            <div class="champs champs--2">
              <p class="champ">
                <label for="prenom">Prénom *</label>
                <input type="text" id="prenom" name="prenom" autocomplete="given-name" required>
              </p>
              <p class="champ">
                <label for="nom">Nom *</label>
                <input type="text" id="nom" name="nom" autocomplete="family-name" required>
              </p>
            </div>

            <p class="champ">
              <label for="entreprise">Entreprise ou association
                <span class="facultatif">(facultatif)</span></label>
              <input type="text" id="entreprise" name="entreprise" autocomplete="organization">
            </p>

            <div class="champs champs--2">
              <p class="champ">
                <label for="email">E-mail *</label>
                <input type="email" id="email" name="email" autocomplete="email"
                       inputmode="email" required>
              </p>
              <p class="champ">
                <label for="telephone">Téléphone <span class="facultatif">(facultatif)</span></label>
                <input type="tel" id="telephone" name="telephone" autocomplete="tel"
                       inputmode="tel">
              </p>
            </div>

            <div class="champs champs--2">
              <p class="champ">
                <label for="projet">Type de projet *</label>
                <select id="projet" name="projet" required>
                  <option value="" selected disabled>Choisissez…</option>
                  <option>Votre site internet — clé en main</option>
                  <option>Refaire mon site actuel</option>
                  <option>Modification d'un site existant (40 €/h)</option>
                  <option>Site pour une association</option>
                  <option>J'ai un autre besoin</option>
                </select>
              </p>
              <p class="champ">
                <label for="budget">Budget indicatif
                  <span class="facultatif">(facultatif)</span></label>
                <select id="budget" name="budget">
                  <option value="" selected>Je ne sais pas encore</option>
                  <option>Autour de 420 € (Forfait Basic)</option>
                  <option>420 à 700 € (avec quelques options)</option>
                  <option>700 à 1 200 €</option>
                  <option>Plus de 1 200 €</option>
                  <option>À définir ensemble</option>
                </select>
              </p>
            </div>

            <p class="champ">
              <label for="message">Votre projet *</label>
              <textarea id="message" name="message" rows="7" required
                        placeholder="Votre activité, ce que vous attendez du site, si vous avez déjà un site, un délai souhaité…"></textarea>
            </p>

            <p class="pot-de-miel" aria-hidden="true">
              <label for="societe_web">Ne remplissez pas ce champ</label>
              <input type="text" id="societe_web" name="societe_web" tabindex="-1" autocomplete="off">
            </p>

            <div class="formulaire__pied">
              <button class="btn btn--accent btn--large" type="submit" data-formulaire-envoi>
                Envoyer ma demande
              </button>
              <a class="btn btn--fantome" href="mailto:{EMAIL}">
                {icone('enveloppe', 17)} Écrire à {EMAIL}
              </a>
            </div>

            <p class="message-etat" data-etat role="status" aria-live="polite"></p>

            <p class="formulaire__note">
              En envoyant ce formulaire, votre messagerie s'ouvre avec un message
              pré-rempli à destination de <strong>{EMAIL}</strong> : rien n'est envoyé
              tant que vous ne validez pas vous-même l'envoi. Vos informations servent
              uniquement à répondre à votre demande.
              <a href="confidentialite.html">Politique de confidentialité</a>.
            </p>
          </form>
        </div>

      </div>
    </div>
  </section>

  <section class="section sur-ivoire">
    <div class="conteneur">
      <div class="entete-section reveler">
        <div>
          <p class="surtitre">Et après ?</p>
          <h2>Ce qui se passe une fois votre message envoyé.</h2>
        </div>
        <div>
          <p class="chapo">
            Aucun démarchage, aucune relance insistante. Juste une réponse utile.
          </p>
        </div>
      </div>
      <div class="etapes reveler" style="--retard:60ms">
        <article class="etape">
          <span class="etape__num">01</span>
          <h3>Je vous réponds</h3>
          <p>Sous 24 h, week-end compris. Avec de vraies questions sur votre activité si
             quelque chose manque.</p>
        </article>
        <article class="etape">
          <span class="etape__num">02</span>
          <h3>On en discute</h3>
          <p>Par e-mail, ou de vive voix si vous êtes dans le secteur de Dinan. L'objectif :
             comprendre ce dont vous avez réellement besoin.</p>
        </article>
        <article class="etape">
          <span class="etape__num">03</span>
          <h3>Vous recevez un devis</h3>
          <p>Gratuit, détaillé ligne par ligne, sans engagement. Le prix et le délai sont
             fixés avant que quoi que ce soit ne commence.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section" id="faq-contact">
    <div class="conteneur conteneur--etroit">
      <div class="reveler" style="text-align:center;margin-bottom:clamp(2rem,4vw,3rem)">
        <p class="surtitre surtitre--centre">Avant d'écrire</p>
        <h2>Les questions posées le plus souvent</h2>
      </div>
      <div class="faq reveler" style="--retard:60ms">
{bloc_faq(limite=5, titre_id='contact')}
      </div>
      <p style="margin-top:2rem;text-align:center;color:var(--gris-chaud);font-size:.95rem">
        <a class="lien-fleche" href="tarifs.html#faq">Voir toutes les questions {FLECHE}</a>
      </p>
    </div>
  </section>

  </main>

"""
    h += pied()
    ecrire("contact.html", h)


# ===========================================================================
# PAGES LÉGALES
# ===========================================================================
def _page_legale(slug, titre_onglet, description, titre, chapo, corps, fil_label):
    fil = schema_fil([("Accueil", "index.html"), (fil_label, slug)])
    h = tete(titre_onglet, description, slug, schema=fil)
    h += entete("", clair=True)
    h += bandeau([("index.html", "Accueil"), (None, fil_label)], titre, chapo)
    h += f"""  <main id="contenu">
  <section class="section">
    <div class="conteneur conteneur--etroit texte-legal">
{corps}
    </div>
  </section>
  </main>

"""
    h += pied()
    ecrire(slug, h)


def page_mentions():
    corps = f"""      <p class="maj">Dernière mise à jour : août 2026</p>

      <h2>1. Éditeur du site</h2>
      <p>
        Le présent site est édité par <strong>Gabriel LEGENTIL</strong>, entrepreneur
        individuel, exerçant sous le nom commercial <strong>WebetGo</strong>.
      </p>
      <dl class="fiche">
        <div><dt class="cle">Responsable de la publication</dt>
             <dd class="val">Gabriel LEGENTIL</dd></div>
        <div><dt class="cle">Statut juridique</dt>
             <dd class="val">Entrepreneur individuel</dd></div>
        <div><dt class="cle">Nom commercial</dt><dd class="val">WebetGo</dd></div>
        <div><dt class="cle">SIRET</dt><dd class="val">106 879 794 00019</dd></div>
        <div><dt class="cle">Siège</dt>
             <dd class="val">38 Le Hambout, 22630 Saint-André-des-Eaux, France</dd></div>
        <div><dt class="cle">Contact</dt>
             <dd class="val"><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt class="cle">TVA</dt>
             <dd class="val">TVA non applicable, art. 293 B du CGI</dd></div>
      </dl>

      <h2>2. Activité</h2>
      <p>
        Création de sites internet professionnels : conception, réalisation, mise en ligne
        et accompagnement. Les prestations et leurs tarifs sont décrits sur la page
        <a href="tarifs.html">Tarifs</a> et encadrés par les
        <a href="cgv.html">conditions générales de vente</a>.
      </p>

      <h2>3. Hébergement du site</h2>
      <p>
        Ce site est hébergé sur une plateforme d'hébergement de pages statiques. Pour toute
        question relative à l'hébergement ou pour signaler un contenu, vous pouvez écrire
        directement à <a href="mailto:{EMAIL}">{EMAIL}</a>.
      </p>

      <h2>4. Propriété intellectuelle</h2>
      <p>
        L'ensemble des éléments composant ce site — structure, textes, mise en page, code
        source, éléments graphiques et images — est protégé par le droit de la propriété
        intellectuelle. Toute reproduction, représentation, adaptation ou exploitation,
        totale ou partielle, sans autorisation écrite préalable, est interdite.
      </p>
      <p>
        Les noms, marques et logos des clients cités ou présentés dans la rubrique
        <a href="realisations.html">Réalisations</a> demeurent la propriété de leurs
        titulaires respectifs et sont mentionnés à titre de références de travaux réalisés.
      </p>

      <h2>5. Liens externes</h2>
      <p>
        Ce site comporte des liens vers des sites tiers (notamment les sites réalisés pour
        les clients et un lien vers Google Maps). Web et Go n'exerce aucun contrôle sur ces
        sites et décline toute responsabilité quant à leur contenu ou à leur disponibilité.
      </p>

      <h2>6. Responsabilité</h2>
      <p>
        Les informations publiées sur ce site sont fournies à titre indicatif et tenues à
        jour avec soin. Elles ne constituent pas un engagement contractuel : seul le devis
        signé fait foi. Web et Go ne saurait être tenu responsable d'une erreur, d'une
        omission ou d'une indisponibilité temporaire du site.
      </p>

      <h2>7. Données personnelles et cookies</h2>
      <p>
        Le traitement de vos données et l'usage des cookies sont détaillés dans la
        <a href="confidentialite.html">politique de confidentialité</a>.
      </p>

      <h2>8. Droit applicable</h2>
      <p>
        Les présentes mentions légales sont soumises au droit français. En cas de litige et
        à défaut de résolution amiable, les tribunaux français seront seuls compétents.
      </p>"""
    _page_legale(
        "mentions-legales.html",
        "Mentions légales | Web et Go",
        "Mentions légales du site Web et Go : éditeur Gabriel Legentil, entrepreneur "
        "individuel, SIRET 106 879 794 00019, Saint-André-des-Eaux (22).",
        "Mentions légales",
        "Les informations légales relatives à l'éditeur de ce site et aux conditions "
        "de son utilisation.",
        corps, "Mentions légales",
    )


def page_cgv():
    corps = f"""      <p class="maj">Dernière mise à jour : août 2026</p>

      <h2>Article 1 — Objet et identification</h2>
      <p>
        Les présentes conditions générales de vente régissent les prestations de création
        de sites internet fournies par <strong>Gabriel LEGENTIL</strong>, entrepreneur
        individuel exerçant sous le nom commercial <strong>WebetGo</strong>, SIRET
        <strong>106 879 794 00019</strong>, dont le siège est situé
        <strong>38 Le Hambout, 22630 Saint-André-des-Eaux</strong> (ci-après « le
        prestataire »), au bénéfice de tout client professionnel ou association
        (ci-après « le client »).
      </p>
      <p>
        Toute commande implique l'acceptation sans réserve des présentes conditions, qui
        prévalent sur tout autre document du client.
      </p>

      <h2>Article 2 — Commande</h2>
      <p>
        La commande devient ferme et définitive à la signature du devis ou à sa validation
        expresse par e-mail. Le devis précise le contenu de la prestation, son prix et le
        délai indicatif de réalisation.
      </p>
      <p>
        En cas d'annulation par le client après validation du devis, l'acompte
        éventuellement versé reste acquis au prestataire, au titre du travail déjà engagé.
      </p>

      <h2>Article 3 — Obligations du prestataire</h2>
      <p>
        Le prestataire est tenu d'une <strong>obligation de moyens</strong>. Il s'engage à
        apporter tout le soin nécessaire à la réalisation de la prestation, conformément
        aux règles de l'art.
      </p>
      <p>
        Sa responsabilité ne saurait être engagée pour les dommages indirects, notamment la
        perte de chiffre d'affaires, de clientèle ou de données. En tout état de cause,
        elle est limitée au montant effectivement payé par le client au titre de la
        prestation concernée.
      </p>

      <h2>Article 4 — Obligations du client</h2>
      <p>
        Le client s'engage à fournir en temps utile l'ensemble des éléments nécessaires à
        la réalisation du site (textes, images, logo, informations légales) et à garantir
        qu'il dispose des droits nécessaires sur ces éléments.
      </p>

      <h2>Article 5 — Recette et livraison</h2>
      <p>
        La validation du site par le client vaut recette. Toute réclamation relative à une
        non-conformité doit être formulée par écrit dans un délai de <strong>8 jours</strong>
        suivant la mise en ligne. Passé ce délai, la prestation est réputée acceptée.
      </p>

      <h2>Article 6 — Propriété intellectuelle</h2>
      <p>
        Les codes sources et éléments créés demeurent la propriété du prestataire
        <strong>jusqu'au paiement intégral</strong> du prix convenu. Après complet
        paiement, les droits d'exploitation relatifs au site livré sont cédés au client.
      </p>
      <p>
        Le prestataire se réserve le droit de mentionner le site réalisé et le nom du
        client à titre de référence commerciale, sauf opposition écrite de ce dernier.
      </p>

      <h2>Article 7 — Données personnelles (RGPD)</h2>
      <p>
        Le prestataire livre le site en conformité avec la réglementation applicable
        (bandeau cookies, mentions légales). La conformité du site dans la durée, ainsi que
        le traitement des données collectées via celui-ci, relèvent de la responsabilité
        du client, en sa qualité de responsable de traitement.
      </p>

      <h2>Article 8 — Conditions financières</h2>
      <ul>
        <li>Forfait Basic : <strong>420 € TTC</strong>, paiement unique.</li>
        <li>Options : selon le devis accepté (contrat sur mesure).</li>
        <li>
          Interventions après livraison : <strong>40 € TTC de l'heure</strong>, sur devis
          gratuit préalable, avec un minimum d'une heure facturée.
        </li>
        <li>
          Carnet de <strong>5 heures prépayées : 180 € TTC</strong>, sans limite de durée
          d'utilisation.
        </li>
        <li>
          <strong>TVA non applicable, art. 293 B du CGI.</strong>
        </li>
        <li>
          Paiement à réception de facture. Tout retard de paiement peut donner lieu aux
          pénalités légales applicables entre professionnels.
        </li>
        <li>
          L'hébergement et le nom de domaine sont souscrits <strong>au nom et à la charge
          du client</strong> (environ 50 à 100 € par an selon le prestataire choisi). Leur
          configuration initiale est incluse dans le forfait.
        </li>
      </ul>

      <h2>Article 9 — Droit applicable et juridiction</h2>
      <p>
        Les présentes conditions sont soumises au <strong>droit français</strong>. En cas
        de litige, et à défaut d'accord amiable, compétence expresse est attribuée au
        tribunal du ressort du siège du prestataire.
      </p>

      <hr class="filet">

      <h2>Informations légales du prestataire</h2>
      <dl class="fiche">
        <div><dt class="cle">Prestataire</dt><dd class="val">Gabriel LEGENTIL</dd></div>
        <div><dt class="cle">Statut</dt><dd class="val">Entrepreneur individuel</dd></div>
        <div><dt class="cle">Nom commercial</dt><dd class="val">WebetGo</dd></div>
        <div><dt class="cle">SIRET</dt><dd class="val">106 879 794 00019</dd></div>
        <div><dt class="cle">Adresse</dt>
             <dd class="val">38 Le Hambout, 22630 Saint-André-des-Eaux</dd></div>
        <div><dt class="cle">Contact</dt>
             <dd class="val"><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt class="cle">TVA</dt>
             <dd class="val">Non applicable, art. 293 B du CGI</dd></div>
      </dl>"""
    _page_legale(
        "cgv.html",
        "Conditions générales de vente | Web et Go",
        "Conditions générales de vente de Web et Go (Gabriel Legentil, WebetGo) : "
        "commande, livraison, propriété intellectuelle, tarifs et droit applicable.",
        "Conditions générales de vente",
        "Les règles qui encadrent chaque prestation Web et Go, de la validation du devis "
        "à la mise en ligne de votre site.",
        corps, "CGV",
    )


def page_confidentialite():
    corps = f"""      <p class="maj">Dernière mise à jour : août 2026</p>

      <h2>1. Le principe, en une phrase</h2>
      <p>
        Ce site ne pratique aucun profilage publicitaire, ne revend aucune donnée et
        n'installe <strong>aucun cookie de mesure d'audience ou de publicité</strong>. Les
        seules informations traitées sont celles que vous choisissez de m'envoyer pour
        obtenir une réponse.
      </p>

      <h2>2. Responsable du traitement</h2>
      <p>
        Gabriel LEGENTIL, entrepreneur individuel (nom commercial WebetGo), 38 Le Hambout,
        22630 Saint-André-des-Eaux — SIRET 106 879 794 00019.
        Contact : <a href="mailto:{EMAIL}">{EMAIL}</a>.
      </p>

      <h2>3. Données collectées et finalité</h2>
      <p>
        Le formulaire de la page <a href="contact.html">Contact</a> fonctionne
        par <strong>ouverture de votre propre messagerie</strong> : les informations
        saisies servent uniquement à pré-remplir un e-mail que vous validez vous-même.
        Aucune donnée n'est enregistrée sur ce site, ni transmise à un serveur tiers avant
        cet envoi.
      </p>
      <dl class="fiche">
        <div><dt class="cle">Données concernées</dt>
             <dd class="val">Prénom, nom, entreprise ou association, adresse e-mail,
                 téléphone, type de projet, budget indicatif, contenu du message.</dd></div>
        <div><dt class="cle">Finalité</dt>
             <dd class="val">Répondre à votre demande et, le cas échéant, établir un devis.</dd></div>
        <div><dt class="cle">Base légale</dt>
             <dd class="val">Votre démarche volontaire (mesures précontractuelles prises
                 à votre demande).</dd></div>
        <div><dt class="cle">Destinataire</dt>
             <dd class="val">Gabriel LEGENTIL uniquement. Aucune cession, aucune revente.</dd></div>
        <div><dt class="cle">Durée de conservation</dt>
             <dd class="val">3 ans à compter du dernier échange, puis suppression. Les
                 documents contractuels sont conservés selon les délais légaux.</dd></div>
      </dl>

      <h2 id="cookies">4. Cookies</h2>
      <p>
        <strong>Ce site ne dépose aucun cookie.</strong> Il n'utilise ni Google Analytics,
        ni pixel publicitaire, ni bouton de réseau social traceur. Aucun consentement n'est
        donc nécessaire pour le consulter.
      </p>
      <p>
        Les polices de caractères et les images sont hébergées sur le site lui-même : votre
        navigateur n'a pas besoin de contacter un serveur tiers pour afficher ces pages.
      </p>
      <p>
        <strong>Carte du secteur d'intervention.</strong> La page
        <a href="a-propos.html#zone">À propos</a> affiche une carte dont les fonds sont
        fournis par OpenStreetMap et CARTO. Elle s'affiche directement à l'ouverture de la
        page : votre adresse IP est alors transmise au serveur qui fournit ces fonds de
        carte, car elle lui est nécessaire pour vous envoyer les images. C'est le seul
        appel à un service extérieur de tout le site. Cette carte ne dépose aucun cookie
        et ne sert à aucun suivi publicitaire.
      </p>
      <p>
        <strong>Vous pouvez la désactiver.</strong> Le bandeau affiché lors de votre
        première visite propose un bouton « Rejeter » ; le même choix reste
        accessible à tout moment par le lien « Cookies &amp; données » en bas de page. Si
        vous la désactivez, plus aucune donnée n'est transmise à OpenStreetMap et un lien
        vers Google Maps remplace la carte. Votre choix est conservé dans la mémoire locale
        de votre navigateur (<code>localStorage</code>), et non dans un cookie : il ne
        quitte jamais votre appareil et n'est lisible que par ce site. Vider les données du
        site dans votre navigateur l'efface.
      </p>
      <p>
        Si vous suivez un lien vers un site externe (site d'un client, Google Maps), ce site
        applique alors sa propre politique en matière de cookies, sur laquelle Web et Go n'a
        aucun contrôle.
      </p>

      <h2>5. Sécurité</h2>
      <p>
        Le site est servi en HTTPS. Les échanges par e-mail sont conservés dans une
        messagerie protégée par mot de passe, accessible au seul responsable du traitement.
      </p>

      <h2>6. Vos droits</h2>
      <p>
        Conformément au RGPD et à la loi « Informatique et Libertés », vous disposez d'un
        droit d'accès, de rectification, d'effacement, de limitation et d'opposition
        concernant vos données, ainsi que d'un droit à la portabilité.
      </p>
      <p>
        Pour l'exercer, il suffit d'écrire à <a href="mailto:{EMAIL}">{EMAIL}</a>. Une
        réponse vous sera apportée dans un délai maximum d'un mois.
      </p>
      <p>
        Si vous estimez, après m'avoir contacté, que vos droits ne sont pas respectés, vous
        pouvez adresser une réclamation à la CNIL —
        <a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a>.
      </p>

      <h2>7. Sites réalisés pour les clients</h2>
      <p>
        La présente politique concerne le seul site de Web et Go. Les sites créés pour les
        clients sont livrés conformes au RGPD au moment de leur mise en ligne, mais chaque
        client demeure responsable du traitement des données collectées par l'intermédiaire
        de son propre site.
      </p>

      <h2>8. Modification</h2>
      <p>
        Cette politique peut être mise à jour pour tenir compte d'évolutions légales ou
        techniques. La date de dernière mise à jour figure en haut de cette page.
      </p>"""
    _page_legale(
        "confidentialite.html",
        "Confidentialité et cookies | Web et Go",
        "Politique de confidentialité de Web et Go : aucune donnée revendue, aucun cookie "
        "de suivi, vos droits RGPD et comment les exercer.",
        "Confidentialité &amp; cookies",
        "Ce site ne dépose aucun cookie de suivi et ne revend aucune donnée. Voici, "
        "précisément, ce qui est traité et pourquoi.",
        corps, "Confidentialité",
    )
