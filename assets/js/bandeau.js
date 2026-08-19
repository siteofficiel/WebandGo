/* ---------------------------------------------------------------------------
   Web et Go — bandeau d'information « cookies & données »
   Ce site ne dépose aucun cookie et n'utilise aucun traceur. Le seul appel à
   un service tiers est le fond de carte OpenStreetMap/CARTO, sur la page
   À propos, qui reçoit l'adresse IP du visiteur pour envoyer les images.
   Le bandeau informe et permet de refuser ce chargement.
   Le choix est mémorisé dans localStorage (pas un cookie, aucun envoi).
   --------------------------------------------------------------------------- */
(function () {
  'use strict';

  var CLE = 'webetgo-carte';
  var socle = document.querySelector('[data-bandeau]');
  if (!socle) return;

  function lire() {
    try { return window.localStorage.getItem(CLE); } catch (e) { return null; }
  }
  function ecrire(v) {
    try { window.localStorage.setItem(CLE, v); } catch (e) { /* mode privé */ }
  }

  var dernierFocus = null;

  function fermer(rendreFocus) {
    socle.hidden = true;
    document.documentElement.classList.remove('a-bandeau');
    if (rendreFocus && dernierFocus && dernierFocus.focus) {
      dernierFocus.focus();
    }
  }

  function ouvrir() {
    dernierFocus = document.activeElement;
    socle.hidden = false;
    document.documentElement.classList.add('a-bandeau');
    var p = socle.querySelector('[data-bandeau-accepter]');
    if (p) p.focus();
  }

  /* --- Boutons du bandeau ------------------------------------------------- */
  var accepter = socle.querySelector('[data-bandeau-accepter]');
  var refuser = socle.querySelector('[data-bandeau-refuser]');

  if (accepter) {
    accepter.addEventListener('click', function () {
      ecrire('accord');
      fermer(false);
      if (window.WebEtGoCarte) window.WebEtGoCarte.activer(false);
    });
  }

  if (refuser) {
    refuser.addEventListener('click', function () {
      ecrire('refus');
      fermer(false);
      if (window.WebEtGoCarte) window.WebEtGoCarte.desactiver();
    });
  }

  /* Échap ferme sans rien changer au choix déjà en mémoire. */
  socle.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') fermer(true);
  });

  /* --- Rouvrir le choix depuis le pied de page ---------------------------- */
  var rappels = document.querySelectorAll('[data-bandeau-rouvrir]');
  rappels.forEach(function (lien) {
    lien.addEventListener('click', function (e) {
      e.preventDefault();
      ouvrir();
    });
  });

  /* --- Affichage initial --------------------------------------------------- */
  if (lire() === null) {
    /* On laisse la page se poser avant d'afficher le bandeau. */
    if ('requestAnimationFrame' in window) {
      requestAnimationFrame(function () {
        setTimeout(ouvrir, 550);
      });
    } else {
      setTimeout(ouvrir, 550);
    }
  }
})();
