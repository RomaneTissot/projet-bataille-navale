from bateau import Bateau


def bateaux_chevauchent(b1, b2):
    positions_b1 = set(b1.positions)
    positions_b2 = set(b2.positions)
    return not positions_b1.isdisjoint(positions_b2)


b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(2, 4, longueur=2)
print("Exemple chevauchement :")
print(f"b1.positions = {b1.positions}")
print(f"b2.positions = {b2.positions}")
print("Chevauchent ?", bateaux_chevauchent(b1, b2))

b3 = Bateau(0, 0, longueur=2)
b4 = Bateau(2, 0, longueur=3)
print("\nExemple sans chevauchement :")
print(f"b3.positions = {b3.positions}")
print(f"b4.positions = {b4.positions}")
print("Chevauchent ?", bateaux_chevauchent(b3, b4))
