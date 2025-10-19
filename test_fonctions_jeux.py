from grille import Grille
from bateau import Bateau
from types_bateaux import PorteAvion, Croiseur, Torpilleur, SousMarin


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


def test_ajoute_porte_avion():
    g = Grille(5, 5)
    pa = PorteAvion(0, 0)
    g.ajoute(pa)
    for (l, c) in pa.positions:
        indice = l * g.nb_colonnes + c
        assert g.grille[indice] == pa.marque


def test_ajoute_croiseur():
    g = Grille(5, 5)
    c = Croiseur(1, 0)
    g.ajoute(c)
    for (l, col) in c.positions:
        indice = l * g.nb_colonnes + col
        assert g.grille[indice] == c.marque


def test_ajoute_torpilleur():
    g = Grille(5, 5)
    t = Torpilleur(2, 0)
    g.ajoute(t)
    for (l, col) in t.positions:
        indice = l * g.nb_colonnes + col
        assert g.grille[indice] == t.marque


def test_ajoute_sous_marin():
    g = Grille(5, 5)
    sm = SousMarin(3, 0)
    g.ajoute(sm)
    for (l, col) in sm.positions:
        indice = l * g.nb_colonnes + col
        assert g.grille[indice] == sm.marque
