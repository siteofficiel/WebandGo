/* =========================================================================
   Web et Go — script du site
   Vanilla JS, sans dépendance. Défensif : chaque module vérifie sa cible.
   ========================================================================= */
(function () {
  'use strict';

  var reduit = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* -----------------------------------------------------------------------
     1. En-tête : état « collé » au défilement
     ----------------------------------------------------------------------- */
  (function entete() {
    var el = document.querySelector('[data-entete]');
    if (!el) return;
    var seuil = 24;
    var tic = false;

    function maj() {
      var y = window.scrollY || window.pageYOffset;
      el.classList.toggle('est-collee', y > seuil);
      // au-dessus d'un héros sombre, l'en-tête reste transparent en haut de page
      if (el.hasAttribute('data-entete-clair')) {
        el.classList.toggle('entete--transparent', y <= seuil);
      }
      tic = false;
    }
    function surDefilement() {
      if (!tic) { window.requestAnimationFrame(maj); tic = true; }
    }
    window.addEventListener('scroll', surDefilement, { passive: true });
    maj();
  })();

  /* -----------------------------------------------------------------------
     2. Menu mobile
     ----------------------------------------------------------------------- */
  (function menu() {
    var bouton = document.querySelector('[data-menu-bouton]');
    var panneau = document.querySelector('[data-menu-panneau]');
    if (!bouton || !panneau) return;

    var dernierFocus = null;

    function ouvrir() {
      dernierFocus = document.activeElement;
      panneau.classList.add('est-ouvert');
      panneau.removeAttribute('inert');
      bouton.setAttribute('aria-expanded', 'true');
      bouton.setAttribute('aria-label', 'Fermer le menu');
      document.body.classList.add('nav-ouverte');
      var premier = panneau.querySelector('a, button');
      if (premier) premier.focus({ preventScroll: true });
    }
    function fermer() {
      panneau.classList.remove('est-ouvert');
      bouton.setAttribute('aria-expanded', 'false');
      bouton.setAttribute('aria-label', 'Ouvrir le menu');
      document.body.classList.remove('nav-ouverte');
      window.setTimeout(function () {
        if (!panneau.classList.contains('est-ouvert')) {
          panneau.setAttribute('inert', '');
        }
      }, 400);
      if (dernierFocus) dernierFocus.focus({ preventScroll: true });
    }
    function basculer() {
      if (bouton.getAttribute('aria-expanded') === 'true') fermer(); else ouvrir();
    }

    panneau.setAttribute('inert', '');
    bouton.addEventListener('click', basculer);

    panneau.addEventListener('click', function (e) {
      if (e.target.closest('a')) fermer();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && bouton.getAttribute('aria-expanded') === 'true') {
        fermer();
      }
    });

    // piège de focus simple
    panneau.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var cibles = panneau.querySelectorAll('a[href], button:not([disabled])');
      if (!cibles.length) return;
      var premier = cibles[0];
      var dernier = cibles[cibles.length - 1];
      if (e.shiftKey && document.activeElement === premier) {
        e.preventDefault(); dernier.focus();
      } else if (!e.shiftKey && document.activeElement === dernier) {
        e.preventDefault(); premier.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1040 &&
          bouton.getAttribute('aria-expanded') === 'true') fermer();
    });
  })();

  /* -----------------------------------------------------------------------
     3. Apparition progressive des sections
     ----------------------------------------------------------------------- */
  (function reveler() {
    var cibles = document.querySelectorAll('.reveler');
    if (!cibles.length) return;

    if (reduit.matches || !('IntersectionObserver' in window)) {
      cibles.forEach(function (c) { c.classList.add('est-visible'); });
      return;
    }
    var obs = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (entree) {
        if (!entree.isIntersecting) return;
        var el = entree.target;
        el.classList.add('est-visible');
        obs.unobserve(el);
        // libère la couche de composition une fois l'apparition terminée
        el.addEventListener('transitionend', function poser(ev) {
          if (ev.target !== el || ev.propertyName !== 'opacity') return;
          el.classList.add('est-posee');
          el.removeEventListener('transitionend', poser);
        });
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });

    cibles.forEach(function (c) { obs.observe(c); });

    /* Sécurité : tout bloc encore invisible 3 s après le chargement complet
       est affiché d'office (onglet en arrière-plan, image très lente, etc.). */
    window.addEventListener('load', function () {
      setTimeout(function () {
        document.querySelectorAll('.reveler:not(.est-visible)').forEach(function (c) {
          var r = c.getBoundingClientRect();
          if (r.top < window.innerHeight && r.bottom > 0) c.classList.add('est-visible');
        });
      }, 3000);
    });
  })();

  /* -----------------------------------------------------------------------
     4. FAQ — accordéon accessible
     ----------------------------------------------------------------------- */
  (function faq() {
    var boutons = document.querySelectorAll('[data-faq-question]');
    if (!boutons.length) return;

    boutons.forEach(function (bouton) {
      var reponse = document.getElementById(bouton.getAttribute('aria-controls'));
      if (!reponse) return;
      bouton.addEventListener('click', function () {
        var ouvert = bouton.getAttribute('aria-expanded') === 'true';
        bouton.setAttribute('aria-expanded', String(!ouvert));
        reponse.setAttribute('data-ouvert', String(!ouvert));
      });
    });
  })();

  /* -----------------------------------------------------------------------
     5. Parallaxe très légère sur les grandes images
     ----------------------------------------------------------------------- */
  (function parallaxe() {
    var cibles = document.querySelectorAll('[data-parallaxe]');
    if (!cibles.length || reduit.matches) return;
    if (window.matchMedia('(max-width: 820px)').matches) return;

    var tic = false;
    function maj() {
      var h = window.innerHeight;
      cibles.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -100 || r.top > h + 100) return;
        var progression = (r.top + r.height / 2 - h / 2) / h; // -1 .. 1
        var force = parseFloat(el.getAttribute('data-parallaxe')) || 14;
        el.style.transform = 'translate3d(0,' +
          (progression * -force).toFixed(2) + 'px,0)';
      });
      tic = false;
    }
    function surDefilement() {
      if (!tic) { window.requestAnimationFrame(maj); tic = true; }
    }
    window.addEventListener('scroll', surDefilement, { passive: true });
    window.addEventListener('resize', surDefilement, { passive: true });
    maj();
  })();

  /* -----------------------------------------------------------------------
     6. Formulaire de contact
     Site statique : pas de serveur. On compose un e-mail pré-rempli
     vers l'adresse réelle de Web et Go et on ouvre la messagerie.
     ----------------------------------------------------------------------- */
  (function formulaire() {
    var form = document.querySelector('[data-formulaire]');
    if (!form) return;

    var etat = form.querySelector('[data-etat]');
    var destinataire = form.getAttribute('data-destinataire');

    function ligne(etiquette, valeur) {
      return valeur ? etiquette + ' : ' + valeur + '\n' : '';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // anti-robot : si le champ caché est rempli, on ignore
      var miel = form.querySelector('[name="societe_web"]');
      if (miel && miel.value) return;

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var d = new FormData(form);
      var v = function (n) { return (d.get(n) || '').toString().trim(); };

      var sujet = 'Demande de site internet — ' + (v('prenom') + ' ' + v('nom')).trim() +
                  (v('entreprise') ? ' (' + v('entreprise') + ')' : '');

      var corps =
        'Bonjour Gabriel,\n\n' +
        'Je vous contacte au sujet d\u2019un projet de site internet.\n\n' +
        '— Mes coordonnées —\n' +
        ligne('Prénom', v('prenom')) +
        ligne('Nom', v('nom')) +
        ligne('Entreprise / association', v('entreprise')) +
        ligne('E-mail', v('email')) +
        ligne('Téléphone', v('telephone')) +
        '\n— Mon projet —\n' +
        ligne('Type de projet', v('projet')) +
        ligne('Budget indicatif', v('budget')) +
        '\nMessage :\n' + v('message') + '\n\n' +
        'Bien cordialement,\n' + (v('prenom') + ' ' + v('nom')).trim();

      var lien = 'mailto:' + destinataire +
                 '?subject=' + encodeURIComponent(sujet) +
                 '&body=' + encodeURIComponent(corps);

      if (etat) {
        etat.hidden = false;
        etat.textContent =
          'Votre messagerie s\u2019ouvre avec la demande déjà rédigée. ' +
          'Il ne reste qu\u2019à l\u2019envoyer. Si rien ne se passe, écrivez directement à ' +
          destinataire + '.';
        etat.setAttribute('role', 'status');
      }

      window.location.href = lien;
    });
  })();

  /* -----------------------------------------------------------------------
     7. Année courante dans le pied de page
     ----------------------------------------------------------------------- */
  (function annee() {
    var els = document.querySelectorAll('[data-annee]');
    var a = new Date().getFullYear();
    els.forEach(function (el) { el.textContent = a; });
  })();

})();
