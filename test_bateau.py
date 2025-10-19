from bateau import Bateau


def test_longueur():
    b = Bateau(2, 3)
    assert b.longueur == 1


def test_horizontal():
    b = Bateau(2, 3)
    assert b.vertical is False
