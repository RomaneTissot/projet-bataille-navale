from bateau import Bateau


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
