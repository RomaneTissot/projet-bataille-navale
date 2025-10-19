from grille import Grille
from bateau import Bateau


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


def test_affichage_vide():
    g = Grille(3, 4)
    attendu = "~~~~\n~~~~\n~~~~"
    assert str(g) == attendu


def test_affichage_avec_tir():
    g = Grille(3, 4)
    g.tirer(1, 2)
    attendu = "~~~~\n~~x~\n~~~~"
    assert str(g) == attendu


def test_ajoute_horizontal_ok():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.ajoute(b)
    expected = ["~", "~", "~", "⛵", "⛵", "~"]
    assert g.grille == expected


def test_ajoute_vertical_depasse():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=True)
    g.ajoute(b)
    expected = ["~", "~", "~", "~", "~", "~"]
    assert g.grille == expected


def test_ajoute_vertical_trop_long():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=4, vertical=True)
    g.ajoute(b)
    expected = ["~", "~", "~", "~", "~", "~"]
    assert g.grille == expected
