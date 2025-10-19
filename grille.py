class Grille:
    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.vide = '~'
        self.touche = 'x'
        self.grille = [self.vide] * (nb_lignes * nb_colonnes)

    def tirer(self, ligne, colonne):
        if 0 <= ligne < self.nb_lignes and 0 <= colonne < self.nb_colonnes:
            indice = ligne * self.nb_colonnes + colonne
            self.grille[indice] = self.touche
        else:
            print("Erreur : coordonnées invalides.")

    def __str__(self):
        lignes = []
        for i in range(self.nb_lignes):
            debut = i * self.nb_colonnes
            fin = debut + self.nb_colonnes
            lignes.append("".join(self.grille[debut:fin]))
        return "\n".join(lignes)
