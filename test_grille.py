from grille import Grille


def test_init():
    g = Grille(0, 0)
    assert isinstance(g, Grille)


def test_grille_vide():
    g = Grille(3, 4)
    assert g.nb_lignes == 3
    assert g.nb_colonnes == 4
    assert len(g.grille) == 12
    assert all(c == g.vide for c in g.grille)


def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 2)
    assert g.grille[1 * 3 + 2] == g.touche
