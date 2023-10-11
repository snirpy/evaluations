continuer = ""
ips = 25

def afficherMenu():
    print("\nQuel calcul souhaitez vous réaliser ?")
    print("\n1: Espace Stockage ")
    print("2: Durée Enregistrement ")
    print("q: Pour quitter\n\n>> ",end ="")

def saisir (message):
    valeur_int = 0
    while valeur_int == 0:
        valeur_str = input(f"Sasir {message} : ")
        try:
            valeur_int = float(valeur_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
        except: # si le cast ne fonctionne pas je lève une exception
            print("Vous n'avez pas saisi une valeur numérique")
        else:
            if valeur_int == 0: # si la valeur saisie est = zéro
                print("Vous avez saisi zéro")
            elif valeur_int < 0: # si la valeur saisie est négative
                print("Vous avez saisi une valeur négative")
                valeur_int = 0   #je réaffecte 0 à valeur_int pour revenir à la condition initiale
            else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
                print("Vous avez saisi {}".format(valeur_int))
    return valeur_int

def calculerStockage():
    tailleImage= saisir("la taille de l'image en Ko")
    duree = saisir("la durée en secondes")
    return (tailleImage*ips *duree)/(1024*1024)
    
  
def calculerDuree():
    tailleImage= saisir("la taille de l'image en Ko")
    tailleStockage = saisir("la taille du HDD en Go")
    return (1024*1024*tailleStockage)/(tailleImage*ips)

while continuer != "q":  
    afficherMenu()
    choix = input()
    
    if choix == "1":
        print(f"Stockage: {calculerStockage()}")
        
    elif choix == "2":
        print(f"Durée: {calculerDuree()}")
        
    elif choix == "q":
        print("Vous venez de quitter le programme!")
        continuer = "q"
        
    else:
        print("Je n'ai pas compris votre choix! Veuillez recommencer")


