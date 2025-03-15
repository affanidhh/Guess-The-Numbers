import os
import random
from math import ceil
import time

# Constants
INITIAL_ARGENT = 20

# Difficulty settings
DIFFICULTY_SETTINGS = {
    "Facile": (10, 5, 10),
    "Moyen": (20, 7, 7),
    "Difficile": (30, 10, 5),
    "Expert": (50, 15, 3),
    "Impossible": (100, 5, 2),
    "Secret": (200, 3, 1)  # Niveau secret très difficile
}

# Achievements
ACHIEVEMENTS = {
    "First Win": "Gagner une partie pour la première fois",
    "Quick Thinker": "Gagner une partie en moins de 30 secondes",
    "High Roller": "Miser plus de 50€ en une seule partie",
    # Ajoutez d'autres réalisations ici
}

def demander_nombre(message, min_val, max_val):
    """Demande à l'utilisateur de saisir un nombre entre min_val et max_val."""
    while True:
        try:
            nombre = int(input(message))
            if min_val <= nombre <= max_val:
                return nombre
            else:
                print(f"Veuillez saisir un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Vous n'avez pas saisi de nombre valide.")

def demander_mise(argent):
    """Demande à l'utilisateur de saisir une mise valide."""
    while True:
        try:
            mise = int(input("Tapez le montant de votre mise : "))
            if 0 < mise <= argent:
                return mise
            else:
                print(f"Veuillez saisir une mise entre 1 et {argent}.")
        except ValueError:
            print("Vous n'avez pas saisi de montant valide.")

def demander_nom():
    """Demande le nom du joueur."""
    return input("Quel est ton nom ? ")

def choisir_difficulte():
    """Permet au joueur de choisir la difficulté."""
    print("Choisissez une difficulté :")
    for i, difficulty in enumerate(DIFFICULTY_SETTINGS.keys(), 1):
        if difficulty != "Secret":  # Ne pas afficher le niveau secret dans la liste
            print(f"{i}. {difficulty}")
    choix = demander_nombre("Votre choix : ", 1, len(DIFFICULTY_SETTINGS) - 1)
    return list(DIFFICULTY_SETTINGS.keys())[choix - 1]

def jouer_niveau(max_val, essais, temps_limite, argent):
    """Joue un niveau du jeu."""
    nb_python = random.randint(1, max_val)
    print(f"Devinez le nombre entre 1 et {max_val} (vous avez {essais} essais et {temps_limite} secondes par essai).")

    for _ in range(essais):
        start_time = time.time()
        nb_user = demander_nombre("Votre nombre : ", 1, max_val)
        elapsed_time = time.time() - start_time

        if elapsed_time > temps_limite:
            print(f"Vous avez dépassé le temps limite de {temps_limite} secondes. Vous perdez cet essai.")
            continue

        mise = demander_mise(argent)
        if nb_user == nb_python:
            gain = mise * 3
            print(f"Félicitations ! Vous gagnez {gain} € !")
            return argent + gain, nb_python
        elif nb_user % 2 == nb_python % 2:
            gain = ceil(mise * 0.5)
            print(f"Le nombre choisi est pair ou impair. Vous gagnez {gain} €.")
            argent += gain
        else:
            print("Désolé, vous perdez votre mise.")
            argent -= mise

        if argent <= 0:
            print("Vous êtes ruiné ! C'est la fin de la partie.")
            break

        print(f"Il vous reste {argent} €.")

    print(f"Le nombre exact était {nb_python}.")
    return argent, nb_python

def afficher_realisations(realisations):
    """Affiche les réalisations obtenues."""
    print("Réalisations obtenues :")
    for realisation in realisations:
        print(f"- {realisation}: {ACHIEVEMENTS[realisation]}")

def main():
    os.environ['TK_SILENCE_DEPRECATION'] = '1'
    nom = demander_nom()
    argent = INITIAL_ARGENT
    realisations = set()

    print(f"Bienvenue au casino, {nom} ! Vous commencez avec {argent} €.")
    difficulte = choisir_difficulte()
    max_val, essais, temps_limite = DIFFICULTY_SETTINGS[difficulte]
    continuer_partie = True

    while continuer_partie:
        argent, nb_python = jouer_niveau(max_val, essais, temps_limite, argent)
        if argent <= 0:
            break
        quitter = input("Souhaitez-vous quitter le jeu (o/n) ? ").strip().lower()
        if quitter == 'o':
            break

        # Condition spéciale pour débloquer le niveau secret
        if difficulte == "Impossible" and argent > 100:
            print("Félicitations ! Vous avez débloqué le niveau secret !")
            difficulte = "Secret"
            max_val, essais, temps_limite = DIFFICULTY_SETTINGS[difficulte]

    print(f"Le nombre exact était {nb_python}.")
    print(f"Merci d'avoir joué, {nom} ! Vous repartez avec {argent} €.")
    afficher_realisations(realisations)

if __name__ == "__main__":
    main()
