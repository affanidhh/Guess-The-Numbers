# Guess The Numbers

Bienvenue dans **Guess The Numbers**, un jeu de devinette où vous devez deviner le nombre correct pour gagner de l'argent virtuel. Ce dépôt contient le code source du jeu écrit en Python.

## Description

**Guess The Numbers** est un jeu de casino où le joueur doit deviner un nombre choisi aléatoirement par l'ordinateur dans une certaine plage. Le joueur peut choisir parmi différents niveaux de difficulté, chacun avec ses propres règles et contraintes. Le jeu devient progressivement plus difficile avec des niveaux de difficulté croissants et des modes de jeu spéciaux.

## Fonctionnalités

- **Niveaux de difficulté** :
  - Facile : Plage de 1 à 10, 5 essais, limite de temps de 10 secondes.
  - Moyen : Plage de 1 à 20, 7 essais, limite de temps de 7 secondes.
  - Difficile : Plage de 1 à 30, 10 essais, limite de temps de 5 secondes.
  - Expert : Plage de 1 à 50, 15 essais, limite de temps de 3 secondes.
  - Impossible : Plage de 1 à 100, 5 essais, limite de temps de 2 secondes.
  - Secret : Plage de 1 à 200, 3 essais, limite de temps de 1 seconde (débloqué en gagnant plus de 100€ en mode Impossible).

- **Système de réalisations** :
  - First Win : Gagner une partie pour la première fois.
  - Quick Thinker : Gagner une partie en moins de 30 secondes.
  - High Roller : Miser plus de 50€ en une seule partie.
  - Lucky Guess : Deviner le nombre correct du premier coup.
  - Marathon Player : Jouer pendant plus de 30 minutes sans perdre tout son argent.
  - Persistent Player : Jouer et gagner après avoir perdu plus de 5 fois.
  - Jackpot : Gagner plus de 200€ en une seule partie.

- **Pénalités de temps** : Si le joueur dépasse le temps limite pour deviner, il perd cet essai.
- **Bonus pour devinettes successives correctes** : Le joueur reçoit des bonus pour des devinettes correctes consécutives.
- **Interface utilisateur améliorée** : Interface intuitive avec des messages clairs et des instructions.

## Instructions

### Installation

1. Clonez ce dépôt sur votre machine locale :
   ```sh
   git clone https://github.com/affanidhh/Guess-The-Numbers.git
