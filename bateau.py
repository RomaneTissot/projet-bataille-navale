class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        pos = []
        if self.vertical:
            for i in range(self.longueur):
                pos.append((self.ligne + i, self.colonne))
        else:
            for i in range(self.longueur):
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille):
        for (l, c) in self.positions:
            indice = l * grille.nb_colonnes + c
            if grille.grille[indice] != 'x':
                return False
        return True
