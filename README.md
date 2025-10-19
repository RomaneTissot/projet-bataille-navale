# Bataille Navale - Projet Python

## Description
Ce projet implémente un jeu de **Bataille Navale** où le but est de couler les quatres bateaux de la grille générée aléatoirement en un minimum de tentative.
La grille comporte 8 lignes et 10 colonnes et il y a un bateau de logueur 4, un bateau de longueur 3 et deux bateau de longueur 2.

Le projet inclut également des tests unitaires avec pytest.

## Contenu du projet
- `grille.py` : classe `Grille` pour gérer la grille du jeu.  
- `bateau.py` : classe `Bateau` et ses sous-classes .  
- `types_bateaux.py` : définition des différents types de bateaux : `PorteAvion`, `Croiseur`, `Torpilleur`, `SousMarin` (sous-classe de Bateau).  
- `story_bateau.py` : user stories pour tester le chevauchement des bateaux.
- `story_grille.py` : user stories pour tester les fonctionnalités de la classe Grille.
- `test_grille.py` : fichier contenant les tests unitaires des constructeurs et méthodes propre à grille.
- `test_bateau.py` : fichier contenant les tests unitaires des constructeurs et méthodes propre à bateau.
- `test_fonctions_jeux.py` : fichier contenant les tests unitaires des méthodes nécessitant grille, bateau et ses sous-classes.
- `main.py` : boucle du jeu.
- `requirement.txt` : fichier contenant les modules nécessaires au projet.
