"""Module d'encodage de chaînes en art ASCII (run-length encoding simple)."""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # Cas particulier : chaîne vide
    if not s:
        return []

    # Initialisation
    chars = [s[0]]   # liste des caractères rencontrés
    occs = [1]       # liste des occurrences correspondantes
    k_index = 1      # indice courant dans la chaîne
    length = len(s)  # longueur de la chaîne

    # Parcours de la chaîne
    while k_index < length:
        if s[k_index] == s[k_index - 1]:
            # même caractère que le précédent : on incrémente la dernière occurrence
            occs[-1] += 1
        else:
            # nouveau caractère : on l'ajoute, avec 1 occurrence
            chars.append(s[k_index])
            occs.append(1)
        k_index += 1

    # Construction de la liste de tuples (caractère, occurrences)
    return list(zip(chars, occs))


def artcode_r(s):
    """Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # cas de base : chaîne vide -> aucun tuple
    if not s:
        return []

    # recherche nombre de caractères identiques au premier
    first = s[0]
    count = 1
    index = 1
    length = len(s)
    while index < length and s[index] == first:
        count += 1
        index += 1

    # appel récursif sur le reste de la chaîne
    # on construit la liste en ajoutant le tuple courant
    return [(first, count)] + artcode_r(s[index:])


#### Fonction principale


def main():
    """Fonction principale de test des fonctions artcode_i et artcode_r."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()
