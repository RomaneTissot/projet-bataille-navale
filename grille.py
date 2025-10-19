class Grille:
    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.vide = '∿'
        self.touche = 'x'
        self.grille = [self.vide] * (nb_lignes * nb_colonnes)
