/* ---------------------------------------------------------------------------
   Web et Go — carte interactive de la zone d'intervention
   Leaflet auto-hébergé + fond de carte CARTO (OpenStreetMap).
   Aucun cookie n'est déposé. La carte s'affiche directement, sauf si le
   visiteur l'a désactivée depuis le bandeau d'information.
   --------------------------------------------------------------------------- */
(function () {
  'use strict';

  var socle = document.querySelector('[data-carte]');
  if (!socle) return;

  var bouton = socle.querySelector('[data-carte-activer]');
  var toile = socle.querySelector('[data-carte-toile]');
  if (!toile) return;

  var CLE = 'webetgo-carte';

  function pref() {
    try { return window.localStorage.getItem(CLE); } catch (e) { return null; }
  }

  /* Communes du secteur. Dinan = point principal. */
  var LIEUX = [
    { nom: 'Dinan',                 lat: 48.4553, lon: -2.0464, pole: true },
    { nom: 'Évran',                 lat: 48.3819, lon: -1.9800 },
    { nom: 'Saint-André-des-Eaux',  lat: 48.3733, lon: -2.0250 },
    { nom: 'Léhon',                 lat: 48.4394, lon: -2.0453 },
    { nom: 'Lanvallay',             lat: 48.4550, lon: -2.0250 },
    { nom: 'Taden',                 lat: 48.4753, lon: -2.0333 },
    { nom: 'Pleudihen-sur-Rance',   lat: 48.5225, lon: -1.9578 },
    { nom: 'Caulnes',               lat: 48.2833, lon: -2.1667 },
    { nom: 'Plouasne',              lat: 48.3372, lon: -1.9814 }
  ];

  var etat = 'vide';   /* vide | charge | prete */
  var carte = null;

  function charger(url, type) {
    return new Promise(function (ok, ko) {
      var deja = document.querySelector('[data-carte-res="' + url + '"]');
      if (deja) { ok(); return; }
      var el;
      if (type === 'css') {
        el = document.createElement('link');
        el.rel = 'stylesheet';
        el.href = url;
      } else {
        el = document.createElement('script');
        el.src = url;
      }
      el.setAttribute('data-carte-res', url);
      el.onload = ok;
      el.onerror = function () { ko(new Error(url)); };
      document.head.appendChild(el);
    });
  }

  function construire() {
    var L = window.L;

    carte = L.map(toile, {
      center: [48.4300, -2.0200],
      zoom: 11,
      scrollWheelZoom: false,   /* on ne capture pas la molette : le visiteur défile */
      attributionControl: true
    });

    carte.attributionControl.setPrefix(
      '<a href="https://leafletjs.com" target="_blank" rel="noopener">Leaflet</a>'
    );

    L.tileLayer(
      'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
      {
        maxZoom: 17,
        minZoom: 8,
        subdomains: 'abcd',
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright" ' +
          'target="_blank" rel="noopener">OpenStreetMap</a> &copy; ' +
          '<a href="https://carto.com/attributions" target="_blank" ' +
          'rel="noopener">CARTO</a>'
      }
    ).addTo(carte);

    /* Rayon indicatif : englobe toutes les communes citées (Caulnes, 21 km). */
    var rayon = L.circle([48.4553, -2.0464], {
      radius: 22000,
      color: '#1B4B5A',
      weight: 1.5,
      opacity: 0.55,
      dashArray: '5 5',
      fillColor: '#2E7387',
      fillOpacity: 0.06,
      interactive: false
    }).addTo(carte);

    LIEUX.forEach(function (lieu) {
      var pole = !!lieu.pole;
      var marqueur = L.circleMarker([lieu.lat, lieu.lon], {
        radius: pole ? 8 : 5.5,
        color: '#FCFAF6',
        weight: pole ? 3 : 2,
        fillColor: pole ? '#1B4B5A' : '#2E7387',
        fillOpacity: 1
      }).addTo(carte);

      marqueur.bindPopup(
        '<strong>' + lieu.nom + '</strong>' +
        (pole ? '<br>Secteur principal d\u2019intervention' : '')
      );
      marqueur.bindTooltip(lieu.nom, {
        direction: pole ? 'right' : 'top',
        offset: pole ? [10, 0] : [0, -6],
        permanent: pole,             /* Dinan reste lisible : son point masque le fond */
        className: pole ? 'carte__etiq carte__etiq--pole' : 'carte__etiq'
      });
    });

    carte.fitBounds(rayon.getBounds().pad(0.12));

    /* Le clavier doit pouvoir sortir de la carte : Échap rend le focus. */
    toile.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && bouton) bouton.focus();
    });

    carte.whenReady(function () {
      setTimeout(function () { carte.invalidateSize(); }, 120);
    });
  }

  function ecran() { return socle.querySelector('[data-carte-ecran]'); }

  function activer(donnerFocus) {
    if (etat !== 'vide') return;
    etat = 'charge';
    if (bouton) {
      bouton.disabled = true;
      bouton.textContent = 'Chargement de la carte…';
    }

    Promise.resolve()
      .then(function () { return charger('assets/vendor/leaflet.css', 'css'); })
      .then(function () { return charger('assets/vendor/leaflet.js', 'js'); })
      .then(function () {
        socle.classList.add('est-active');
        toile.hidden = false;
        toile.setAttribute('tabindex', '0');
        construire();
        var e = ecran();
        if (e) e.hidden = true;
        etat = 'prete';
        /* Le bouton disparaît avec l'écran : on rend le focus à la carte,
           sinon le clavier repart au début du document. */
        if (donnerFocus) toile.focus({ preventScroll: true });
      })
      .catch(function () {
        etat = 'vide';
        if (bouton) {
          bouton.disabled = false;
          bouton.textContent = 'Réessayer';
        }
        var err = socle.querySelector('[data-carte-erreur]');
        if (err) err.hidden = false;
      });
  }

  function desactiver() {
    if (carte) { carte.remove(); carte = null; }
    etat = 'vide';
    socle.classList.remove('est-active');
    toile.hidden = true;
    toile.removeAttribute('tabindex');
    toile.innerHTML = '';
    var e = ecran();
    if (e) e.hidden = false;
    if (bouton) {
      bouton.disabled = false;
      bouton.textContent = 'Afficher la carte';
    }
  }

  /* Le bandeau d'information peut piloter la carte sans recharger la page. */
  window.WebEtGoCarte = { activer: activer, desactiver: desactiver };

  if (bouton) {
    bouton.addEventListener('click', function () { activer(true); });
  }

  /* Affichage direct, sauf refus explicite du visiteur. */
  if (pref() !== 'refus') activer(false);
})();
