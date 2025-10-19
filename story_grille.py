from grille import Grille


print("=== Plouf dans l'eau ===")
g = Grille(5, 8)

continuer = True
while continuer:
    print("\nGrille actuelle :")
    print(g)
    saisie = input("\nEntrez les coordonnées du tir (x y), ou 'q' pour quitter : ")

    if saisie.lower() == 'q':
        continuer = False
    else:
        try:
            x_str, y_str = saisie.split()
            x, y = int(x_str), int(y_str)
            g.tirer(x, y)
        except ValueError:
            print("coordonées invalides. "
                  "Entrez deux entiers séparés par un espace (ex : 2 3).")

print("Fin du jeu. Merci d’avoir joué !")
