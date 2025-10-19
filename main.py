import random
from grille import Grille
from types_bateaux import PorteAvion, Croiseur, Torpilleur, SousMarin

BATEAUX = [
    (PorteAvion, "Porte-avion coulé ! 🚢"),
    (Croiseur, "Croiseur coulé ! ⛴"),
    (Torpilleur, "Torpilleur coulé ! 🚣"),
    (SousMarin, "Sous-marin coulé ! 🐟"),
]


def positions_possibles(grille, longueur):
    possibles = []
    for vertical in [False, True]:
        for l in range(grille.nb_lignes):
            for c in range(grille.nb_colonnes):
                if vertical:
                    if l + longueur <= grille.nb_lignes:
                        possibles.append((l, c, vertical))
                else:
                    if c + longueur <= grille.nb_colonnes:
                        possibles.append((l, c, vertical))
    return possibles


def placement_aleatoire(grille, bateaux):
    places = []
    for bateau_cls, _ in bateaux:
        longueur = bateau_cls(0, 0).longueur
        possibles = positions_possibles(grille, longueur)
        ok = []
        for l, c, vertical in possibles:
            b = bateau_cls(l, c, vertical=vertical)
            if all(set(b.positions).isdisjoint(set(bp.positions)) for bp in places):
                ok.append((l, c, vertical))
        if not ok:
            raise ValueError("Impossible de placer tous les bateaux")
        l, c, vertical = random.choice(ok)
        b = bateau_cls(l, c, vertical=vertical)
        grille.ajoute(b)
        places.append(b)
    return places


def jouer():
    grille = Grille(8, 10)
    grille_joueur = Grille(8, 10)
    bateaux = placement_aleatoire(grille, BATEAUX)
    coups = 0
    bateaux_restants = bateaux[:]

    print("Bienvenue dans la Bataille Navale !")
    print(grille_joueur)

    while bateaux_restants:
        try:
            coords = input("Entrez vos coordonnées (ligne colonne) : ").split()
            if len(coords) != 2:
                print("Veuillez entrer deux nombres séparés par un espace.")
                continue
            ligne, colonne = map(int, coords)
            if ligne < 0 or ligne >= grille.nb_lignes or colonne < 0 or colonne >= grille.nb_colonnes:
                print("Coordonnées hors de la grille.")
                continue
        except ValueError:
            print("Entrée invalide.")
            continue

        coups += 1
        touche_bateau = False
        for b in bateaux_restants:
            if (ligne, colonne) in b.positions:
                touche_bateau = b
                break

        if touche_bateau is not False:
            if touche_bateau.coule(grille):
                print("Cette case a déjà été touchée et le bateau est déjà coulé.")
            else:
                grille.tirer(ligne, colonne, touche='x')
                grille_joueur.tirer(ligne, colonne, touche='💣')

                if touche_bateau.coule(grille):
                    for l, c in touche_bateau.positions:
                        idx = l * grille_joueur.nb_colonnes + c
                        grille_joueur.grille[idx] = getattr(touche_bateau, 'marque', '⛵')
                    print(f"{getattr(touche_bateau, 'marque', '')} {message_bateau(touche_bateau)}")
                    bateaux_restants.remove(touche_bateau)
                else:
                    print("Touché ! 💣")
        else:
            grille_joueur.tirer(ligne, colonne)
            print("À l'eau !")

        print(grille_joueur)

    print(f"Félicitations ! Vous avez coulé les bateaux en {coups} coups.")


def message_bateau(bateau):
    if getattr(bateau, 'marque', '') == "🚢":
        return "Porte-avion coulé !"
    elif getattr(bateau, 'marque', '') == "⛴":
        return "Croiseur coulé !"
    elif getattr(bateau, 'marque', '') == "🚣":
        return "Torpilleur coulé !"
    elif getattr(bateau, 'marque', '') == "🐟":
        return "Sous-marin coulé !"
    return "Bateau coulé !"


jouer()
