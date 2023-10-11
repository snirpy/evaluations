def  est_port_valide(port) :
    if  1 <= port <= 65535:
        return True
    else:
        return False
    
def service_associe_port(port):
    if est_port_valide(port):
        if port == 80:
            print(f"Le service associé au port {port}: HTTP")
        elif port == 443:
            print(f"Le service associé au port {port}: HTTPS")
        elif port == 21:
            print(f"Le service associé au port {port}: FTP")
        elif port == 22:
            print(f"Le service associé au port {port}: SSH")
        elif port == 25:
            print(f"Le service associé au port {port}: SMTP")
        else:
            print(f"Le port {port} valide mais le service associé est non reconnu")
    else:
        print(f"Le port {port} est invalide")
   

    
def saisir (message):
    valeur_int = -1
    while valeur_int == -1:
        valeur_str = input(f"Saisir {message} : ")
        try:
            valeur_int = int(valeur_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
        except: # si le cast ne fonctionne pas je lève une exception
            print("Vous n'avez pas saisi une valeur numérique")
        else:
           
            if valeur_int < 0: # si la valeur saisie est négative
                print("Vous avez saisi une valeur négative")
                valeur_int = -1   #je réaffecte 0 à valeur_int pour revenir à la condition initiale
            
            # else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            #     print("Vous avez saisi {}".format(valeur_int))
    return valeur_int


service_associe_port(saisir("le numéro de port"))