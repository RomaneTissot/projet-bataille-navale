from grille import Grille
from bateau import Bateau


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


def test_coule_pas_touche():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    assert b.coule(g) is False


def test_coule_partiellement_touche():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.tirer(1, 0)
    assert b.coule(g) is False


def test_coule_entierement_touche():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.tirer(1, 0)
    g.tirer(1, 1)
    assert b.coule(g) is True


def test_coule_vertical():
    g = Grille(4, 4)
    b = Bateau(1, 1, longueur=3, vertical=True)
    g.tirer(1, 1)
    g.tirer(2, 1)
    g.tirer(3, 1)
    assert b.coule(g) is True


def test_coule_vertical_partiel():
    g = Grille(4, 4)
    b = Bateau(1, 1, longueur=3, vertical=True)
    g.tirer(1, 1)
    g.tirer(2, 1)
    assert b.coule(g) is False
