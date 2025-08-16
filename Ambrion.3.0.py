

import random
from time import sleep

def jeu_probabilite():
    print("\n" + "🎲🎰🪄 Jeu de Probabilité 🎲🎰🪄".center(50, ' ') + "\n")
    
    # Affichage des règles
    regles = [
        "1- Vous ne pouvez entrer un nombre qu'une seule fois 🚫",
        "2- Pas de nombre négatif 🚫",
        "3- Pas de nombre à virgule 🚫",
        "4- Vous avez 5 tentatives",
        "5- Le système choisit un nombre aléatoire dans votre liste"
    ]
    
    print("REGLES DU JEU :\n")
    for regle in regles:
        print(f"    {regle}")
    
    # Initialisation
    nombres_entres = set()
    tentatives_restantes = 5
    
    # Saisie des nombres
    while tentatives_restantes > 0:
        try:
            nombre = int(input(f"\nEntrez le nombre {6 - tentatives_restantes} : "))
            
            if nombre < 0:
                print("Erreur : Pas de nombre négatif !")
                continue
                
            if nombre in nombres_entres:
                print("Erreur : Vous avez déjà entré ce nombre !")
                continue
                
            nombres_entres.add(nombre)
            tentatives_restantes -= 1
            
        except ValueError:
            print("Erreur : Entrez un nombre entier valide !")
    
    # Affichage des nombres choisis
    print("\n" + "="*50)
    print(f"Vos nombres : {sorted(nombres_entres)}")
    
    # Choix du système
    choix_systeme = random.choice(list(nombres_entres))
    sleep(1)  # Petit effet dramatique
    
    # Choix du joueur
    while True:
        try:
            choix_joueur = int(input("\nFaites votre choix parmi vos nombres : "))
            if choix_joueur not in nombres_entres:
                print("Erreur : Choisissez un nombre de votre liste !")
            else:
                break
        except ValueError:
            print("Erreur : Entrez un nombre valide !")
    
    # Résultat
    print("\n" + "="*50)
    print("Résultat :".center(50))
    
    if choix_joueur == choix_systeme:
        message = f"Félicitations ! Vous gagnez car nous avons choisi le même nombre : {choix_systeme}"
        print("\n" + message.center(50) + "\n")
    else:
        message = f"Désolé ! Je gagne car j'ai choisi {choix_systeme} et vous {choix_joueur}"
        print("\n" + message.center(50) + "\n")
    
    # Nouvelle partie
    replay = input("Voulez-vous rejouer ? (Oui/Non) : ").lower()
    if replay in ['oui', 'o', 'y', 'yes']:
        jeu_probabilite()
    else:
        print("\nMerci d'avoir joué ! À bientôt !")

# Lancement du jeu
if __name__ == "__main__":
    jeu_probabilite()