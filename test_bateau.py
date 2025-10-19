from bateau import Bateau


def test_longueur():
    b = Bateau(2, 3)
    assert b.longueur == 1


def test_horizontal():
    b = Bateau(2, 3)
    assert b.vertical is False


def test_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    expected = [(2, 3), (2, 4), (2, 5)]
    assert b.positions() == expected


def test_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    expected = [(2, 3), (3, 3), (4, 3)]
    assert b.positions() == expected
