# Investype

*16 profils pour découvrir quel investisseur vous êtes vraiment.*

Test de tempérament d'investisseur : quatre axes, seize profils, les biais de chacun et l'allocation d'actifs qui lui ressemble.

© 2026 QuidHabes — Alexandre Hezez. Version 1.1.

## Contenu

| Fichier | Rôle |
| --- | --- |
| `index.html` | Page du site (à publier sur GitHub Pages) |
| `assets/questions.js` | Les 56 questions, les axes, les paires miroirs, la version courte |
| `assets/marches.js` | Les 15 classes d'actifs, rendements attendus, crises de référence, sources |
| `assets/profils.js` | Les 16 profils, familles, portefeuilles de référence, allocations et inclinaisons factorielles |
| `assets/textes-*.js` | Les descriptions longues des 16 profils (une famille par fichier) |
| `assets/scoring.js` | Le calcul des scores (fonctions pures, testables sous Node) |
| `assets/app.js` | L'application : accueil, test, résultat, galerie, méthode |
| `assets/style.css` | La mise en forme, thèmes clair et sombre |
| `src/page.html` | Source de la page ; `python3 build.py` régénère `index.html` |

Le site est entièrement statique : pas de serveur, pas de base de données, aucune donnée envoyée. Les réponses restent dans le navigateur ; le résultat se partage par un code (`r-f-…`) qui contient les scores.

## Publier sur GitHub Pages

1. Créer un dépôt, par exemple `investype`, et y copier tout le dossier.
2. Dans le dépôt : Settings → Pages → Source : « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Le site est en ligne à l'adresse `https://<votre-compte>.github.io/investype/` après une à deux minutes.

## Modifier le contenu

- Une question : `assets/questions.js`. Les points vont toujours vers le second pôle (Offensive, Court terme, Intuition, Tendance, Réactif).
- Un profil ou une allocation : `assets/profils.js`. Chaque allocation doit totaliser 100.
- Une hypothèse de marché ou une perte de crise : `assets/marches.js`.
- Une description longue : `assets/textes-sl.js`, `-sc`, `-ol` ou `-oc`.
- Tester le calcul : `node -e "global.window=globalThis;require('./assets/questions.js');const S=require('./assets/scoring.js');console.log(S.decode('r-f-60-40-45-40-40-100-50-50-50-50-33-33-42-33-33-73'))"`

## Avertissement

Outil de connaissance de soi et de sensibilisation aux biais comportementaux. Ce n'est ni un questionnaire d'adéquation réglementaire, ni un conseil en investissement. Les allocations sont illustratives.
