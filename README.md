
# **Simulation d'épidémie**


On simule la propagation d’une épidémie dans un réseau de villes, l'objectif est de **mettre en place une stratégie de confinement** pour limiter le nombre final de personnes infectées.



## Objectifs

* On a un fichier avec les infos sur les villes (ville, habitant, nb infectés, connexion avec quelles autres villes)
* La maladie se propage chaque jour aux villes voisines et infecte un certain nombre de personnes supplémentaires.
* Objectif : Mettre en place une stratégie de confinement qui permettent de minimiser le nombre de personnes malade après `jours_max` jours.
* Pour simuler les confinements, on a la possibilité d'isoler une ville : La liste des voisins d’une ville isolée est temporairement vidée pour simuler le confinement. Les autres villes gardent leurs voisins initiaux.
* On cherche à définir une fonction `strat` pour limiter l’épidémie : Chaque jour, la fonction `strat` reçoit le DataFrame actuel et le numéro du jour. Elle doit renvoyer un DataFrame avec éventuellement certaines villes isolées.


## Les contraintes

* On peut isoler une ville : la ville ne peut plus infecter ses voisins, mais ses voisins peuvent toujours la contaminer.
* Maximum **2 villes isolées** par jour, sinon on isole tout et l'exo est fini
* Certaines villes ne peuvent pas être isolées, les villes suivantes doivent conserver leurs connexions initiales :

  * `Ville_0`, `Ville_1`, `Ville_4`

* Ces contraintes sont vérifiées par les tests déjà écrits.

## Fichiers fournis

1. **`df_epidemic.csv`** : contient les infos sur les villes

   * `ville` : nom de la ville
   * `population` : nombre d’habitants
   * `infectes_jour` : nombre d’infectés
   * `voisins` : liste des villes connectées (propagation possible)

2. **`strategie_confinement.py`** : contient les fonctions de stratégie de confinement et la doc `strat(df, jour)`

3. **`test_strategie_confinement.py`** : les tests pour vérifier que les stratégies respectent les contraintes

   * Max 2 villes isolées par jour
   * Connexions indispensables non coupées


## Définir la stratégie avant de coder

* Que cherche-t-on à optimiser ?
* Comment une infection passe d’une ville à une autre : quels paramètres entrent en jeu ? Comprendre le code
* Quelles sont les logiques possible pour choisir les villes à isoler chaque jour ?
* Écrivez **une pseudo-stratégie** avant de coder
* Discutez de différents scénarios et de leurs effets.
* Quelles variables faudra-t-il suivre ?
* Est-ce qu'on peut mutualiser des morceaux de code entre les stratégies ? Si oui définir les entrées/sorties de ces fonctions


## Etapes

1. Lire le CSV
2. Compléter la fonction `strat(df, jour)` pour appliquer la stratégie de confinement
3. Vérifier les contraintes avec pytest `test_strategie_confinement.py`
4. Tester votre stratégie en exécutant `main.py`
5. Analyser les résultats :

   * Nombre d’infectés par ville
   * Population saine finale
   * (éventuellemnt) Évolution jour par jour avec des graphiques


## Bonus

* Ajouter des graphes pour suivre l'évolution de la pandémie chaque jour
* Tester plusieurs variantes de la stratégie et comparer les résultats

