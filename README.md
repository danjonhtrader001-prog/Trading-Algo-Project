# Projet : Simulation Monte-Carlo du Paradoxe des Anniversaires

## Introduction

Ce projet de finance quantitative propose une simulation Monte-Carlo du célèbre paradoxe des anniversaires à l’aide du langage Python. À travers une approche empirique et une visualisation graphique grâce à Matplotlib, il permet d’explorer l’intuition contre-intuitive derrière la probabilité que, dans un groupe de personnes, au moins deux partagent la même date d’anniversaire.

## Théorie Mathématique

Le paradoxe des anniversaires repose sur des principes de **combinatoire**. Pour un groupe de *n* personnes, on cherche à calculer la probabilité qu’au moins deux personnes aient le même anniversaire, en supposant 365 jours possibles (année non-bissextile). La probabilité complémentaire (qu’aucun anniversaire ne coïncide) se calcule grâce aux combinaisons possibles, puis on en déduit la probabilité recherchée. Dès qu’un groupe atteint 23 personnes, la probabilité de partage d’anniversaire dépasse 50%, ce qui rend ce paradoxe particulièrement surprenant pour l’intuition humaine.

## Simulation

La simulation repose sur la méthode de Monte-Carlo : pour chaque taille de groupe allant de 1 à 60 personnes, on effectue **10 000 essais** aléatoires. Pour chaque essai, on attribue à chaque membre un anniversaire tiré au hasard, puis on vérifie si une coïncidence se produit. La fréquence relative des coïncidences est alors tracée selon la taille du groupe pour illustrer la croissance rapide de la probabilité.

## Comment exécuter le script

1. **Prérequis** :
    - Python 3.x, `matplotlib`
2. **Installation des dépendances** (si nécessaire) :

    ```bash
    pip install matplotlib
    ```

3. **Exécution du script** :

    ```bash
    python main.py
    ```

Le programme affichera automatiquement la courbe de probabilité du paradoxe des anniversaires pour différentes tailles de groupes.
