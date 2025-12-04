> [!CAUTION]
Ce travail s'effectue dans [l'environnement Github](https://perso.esiee.fr/~courivad/courses/utils/misc-01-github-environment.html)

# ASCII Art

[L'art ASCII](https://fr.wikipedia.org/wiki/Art_ASCII) consiste à réaliser des images uniquement à l'aide des lettres et caractères spéciaux contenus dans le code ASCII.

Vous pouvez trouver des [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) simples sur le site [ASCII art archive](https://www.asciiart.eu/) ou construire les votres à partir d'images et de ce [générateur](https://www.ascii-art-generator.org/).

L'objectif de cet exercice est d'encoder une chaine de caractères par une liste de tuples. Chaque tuple est composé d’un caractère (et d’un seul) et du nombre d’occurences consécutives de ce caractère. Par exemple :

- la chaîne MMMMaaacXolloMM
- est représentée par la liste [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]

Le fichier ``main.py`` contient :

- une fonction secondaire ``artcode_i()``
  
  - qui prend en argument une chaîne de caractères ;
  - construit une liste de tuples, correspondant au codage de la chaîne de caractères, avec un algorithme itératif ;
  - et retourne cette liste de tuples.

- une fonction secondaire ``artcode_r()``
  
  - qui prend en argument une chaîne de caractères ;
  - construit une liste de tuples, correspondant au codage de la chaîne de caractères, avec un algorithme récursif ;
  - et retourne cette liste de tuples.

- la fonction principale ``main()`` qui fait appel aux fonctions secondaires pour vérifier leur bon fonctionnement.

## Algorithme itératif

On peut construire un algorithme itératif sur la propriété suivante:

$I(C, O, k)$ : $C$ est la liste des caractères rencontrés lors du parcours de $s[0:k]$ et $O$ est la liste des occurrences correspondantes.

L'initialisation est directe :

- le premier caractère de $s$ est $s[0]$, et donc $C = [ s[0] ]$
- il a été rencontré une fois, et donc $O = [ 1 ]$
- et la chaîne restante à traiter est $s[1:]$, c'est à dire $k = 1$

Si $n$ est la longueur de la chaîne $s$ :

- le critère d'arrêt est $A : k \geq n$
- et la condition de continuation $\bar{A} : k < n$.

La progression, en supposant $I(C, O, k)$ et $\bar{A}$:

- si le caractère courant est identique au caractère précédent, on augmente le nombre d'occurrences d'une unité:

        SI s[k] = s[k-1]
        ALORS O[-1] += 1

-  sinon :

    - on ajoute un nouveau caractère à la liste $C$ des caractères rencontrés ;
    - et $1$ à la liste $O$ des occurrences.

-   dans les deux cas, on progresse dans la chaîne : $k = k+1$.


> [!TIP]
L'algorithme manipule deux listes distinctes (une liste de caractères et une liste d'occurrences) alors que la consigne est d'en retourner une seule formée de tuples dont le premier élément est pris dans $C$ et le second dans $O$. La fonction [`zip`](https://docs.python.org/3/library/functions.html#zip) réalise cette opération de façon très compacte.

## Algorithme récursif

Deux questions essentielles structurent le raisonnement :

- Quel est le cas de base ? La valeur retournée dans ce cas ?
- Quel est l'appel récursif permettant de résoudre un problème de taille inférieure ?

On peut penser à rechercher le nombre de caractères identiques au premier caractère de la chaîne passée en argument et recommencer l'opération sur la chaine restante. L'idée est de retourner une liste construite à partir du résultat ci dessus et d'un appel récursif.

> [!TIP]
Sur les listes, l'opérateur `+` permet de construire une nouvelle liste constituée des deux opérandes. Cette façon de faire est à privilégier. Attention, la méthode [`list.extend()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) modifie la liste sur place.

## To do

1️⃣ Ecrire (ou modifier) le code de la fonction secondaire.

2️⃣ Si nécessaire, ajouter (ou modifier) les appels à la fonction secondaire logés dans la fonction principale ``main()``. Cela permet de tester la fonction secondaire sur quelques cas simples.

3️⃣ Exécuter le programme depuis le terminal. Tant que la fonction secondaire ne retourne pas les résultats attendus, répéter le cycle 1️⃣ 2️⃣ 3️⃣.

    $ python main.py

4️⃣ Lorsque les résultats obtenus à l'étape 3️⃣ sont satisfaisants, soumettre le code à une procédure de test plus robuste, les tests unitaires.

    $ pytest .python

Le score de test ``ST`` obtenu est le pourcentage de tests réussis. Tant que certains tests échouent, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le score de test ``ST`` est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/courses/utils/sources/python-23-codequality.html).

    $ pylint main.py

Si le score de qualité ``SQ`` n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages dans le terminal

6️⃣ Lorsque les scores ``ST`` et ``SQ`` sont satisfaisants, pusher le travail vers votre repo distant. Ce travail est susceptible d'être pris en compte dans l'évaluation de l'unité.

    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.