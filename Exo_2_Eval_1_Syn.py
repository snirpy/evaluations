
donnees_meteo = {
    "Paris": {"temperature": 20.0, "humidite": 60},
    "New York": {"temperature": 25.0, "humidite": 70},
    "Tokyo": {"temperature": 28.0, "humidite": 80}
}

def afficher_donnees_meteo(dictionnaire):
    # Afficher les données météorologiques pour chaque ville
    print("Affichage des données météorologiques pour chaque ville:")
    for ville, meteo in dictionnaire.items():
        print(f"Ville : {ville}")
        print(f"Température : {meteo['temperature']}°C")
        print(f"Humidité : {meteo['humidite']}%\n")

def rechercher_donnees_meteo(dictionnaire, ville):
    # Rechercher et afficher les données météorologiques pour une ville
    if ville in dictionnaire:
        print(f"Données météorologiques pour {ville}:")
        print(f"Température : {dictionnaire[ville]['temperature']}°C")
        print(f"Humidité : {dictionnaire[ville]['humidite']}%")
    else:
        print(f"Données météorologiques non disponibles pour {ville}.")

def mettre_a_jour_donnees_meteo(dictionnaire):
    # Mettre à jour les données météorologiques pour une ville
    ville = input("Saisir le nom de la ville à mettre à jour: ")
    if ville in dictionnaire:
        temperature= int(input("Sasir la nouvelle valeur de la température: "))
        humidite= int(input("Sasir la nouvelle valeur de l'humidité: "))
        dictionnaire[ville]["temperature"] = temperature
        dictionnaire[ville]["humidite"] = humidite
        print(f"Données météorologiques mises à jour pour {ville}.")
    else:
        print(f"Données météorologiques non disponibles pour {ville}.")


# Afficher les données météorologiques:
afficher_donnees_meteo(donnees_meteo)

# Exemple de recherche de données pour une ville
uneVille = input("Saisir le nom de la ville à chercher: ")
rechercher_donnees_meteo(donnees_meteo, uneVille)

# Exemple de mise à jour des données pour une ville
mettre_a_jour_donnees_meteo(donnees_meteo)
# Afficher à nouveau les données mises à jour
afficher_donnees_meteo(donnees_meteo)


