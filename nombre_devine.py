#*  *  *  *  *  *  *  *  *  *  * PROJET : REALISER UN JEU DE CASINO *  *  *  *  *  *  *  *  *

#	Le jeu comporte trois levels. Dans chaque level, Python tire un nombre : level 1 (entre 1 et 10),
#	level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux au bout avec 5 essais
#	en tout pour le 1è level, 7 pour le 2è level et 10 coup pour le 3è level. Chaque essai ne dure pas plus
#	de 5 secondes. Peut importe la raison, si vous dépassez ce délai, vous perdez l'essai courant.
#	Quand vous souhaitez quitter le jeu, Python mets en place un compteur jusqu'à 10 secondes pour valider votre décision.
#	Au-delà, Python quitte le jeu.
#	Lorsque vous gagnez un level et/ou terminer une partie Python fournit des statistiques sur la partie.

from time import sleep
from math import ceil

# print('''\n### Hello World !###\n ''')

name_user = input ("Quel est ton pseudo ?\n- Rép : \n")
# print("Hello **{}**!\n".format(name_user.capitalize()))
# print("* Installe toi à la table de jeu. * Je t'explique le principe de jeu :\n")
# sleep(2)
# print("""* - Le jeu dispose de plusieurs niveaux avec des taux de mise différentes selon le niveau que tu choissira;\n""")
# sleep(2)
# print("""* - J'ai pensé à un nombre entre 1 et 10 pour ce premier niveau et tu aura une limite de mise de 20€ pour ton choix;\n""")
# sleep(2)
# print("""* - ATT!: Attention tu aura trés peu de essais afin de trouver le bon numéro, donc veille bien à faire attention !!\n""")
# sleep(2)
# print(""" - Si vous devinez mon nombre dès le premier coup, vous serez vainqueur et passera automatiquement au niveau suivant !\n""")
# sleep(2)            
# print(""" - Le jeu et de deviner le bon nombre afin d'être vainqueur du jeu.\n""")
# sleep(2)     
# print('- Le jeu commence, entrez votre choix : \n')


from random import randrange
nb_python = randrange(1, 11, 1)
#print("nb_python est: ", nb_python)


# Déclaration des variables de départ
argent = 20 # On a 20 € au début du jeu
continuer_partie = True  # Booléen qui est vrai tant qu'on doit
                         # continuer la partie

print(" Installez vous à la table de pari avec ***", argent, "€ ***")

while continuer_partie: # Tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur lequel il va miser
    nb_user = -1
    while nb_user < 0 or nb_user > 10:
        nb_user = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 10) : ")
        # On convertit le nombre misé
        try:
            nb_user = int(nb_user)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nb_user = -1
            continue
        if nb_user < 0:
            print("Ce nombre est négatif")
        if nb_user > 10:
            print("Ce nombre est supérieur à 10")

    # À présent, on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "€")

      
    # On établit le gain du joueurhttps://www.google.com/search?q=jeu+python+roulette&client=firefox-b-d&ei=OJutXJ-CJeqHjLsPq_Cn8AM&start=10&sa=N&ved=0ahUKEwif_vGtgMXhAhXqA2MBHSv4CT4Q8tMDCIkB
    if nb_python == nb_user:
        print("Félicitations ! Vous obtenez", mise * 3, "€ !")
        argent += mise * 3
    elif nb_python % 2 == nb_user % 2: 
        mise = ceil(mise * 0.5)
        print("Le nombre choisi est pair Ou Impair. Vous obtenez la moitié de la mise", mise, "€")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("\nVous avez à présent", argent, "€\n")
        quitter = input("\nSouhaitez-vous quitter le casino (o/n) ? \n- Rép :  ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False




#Boucle de niveau 2 



