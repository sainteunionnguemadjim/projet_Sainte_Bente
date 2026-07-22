#Sainte_union et Diallo Bente

comptes = [{"numero": 1, "titulaire": "Sainte union", "solde": 150000}, 

{"numero": 2,"titulaire": "Aissatou Bente","solde": 75000},

{"numero": 3,"titulaire": "Carole Yollah", "solde": 320000}, 
]

# afficher le menu principal
def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n=====AGENCE_CESAG_BANK =====")
    print("1. Afficher tous les comptes")
    print("2. Consulter le solde d'un compte")
    print("3. Créer un nouveau compte")
    print("4. Effectuer un dépôt")
    print("5. Effectuer un retrait")
    print("6. Effectuer un transfert entre deux comptes")
    print("7. Quitter")
    print("==============================")
    
# demander le choix de l'utilisateur et verifier qu'il est compris entre 1 et 7 
def saisir_choix_menu():
    saisie_valide = False
    while True:
        choice = input("Votre choix : ")
        if choice.isdigit() and 1 <= int(choice) <= 7:
            saisie_valide = True
        else:
            print("Erreur: veuillez choisir entre 1-7")
    return int(choice)

    # recherche un compte avec son numero
def trouver_compte(comptes, numero):
    for compte in comptes:
        if compte["numero"] == numero:
            return compte
    return None
    
# Demande un numéro de compte jusqu'à ce qu'il corresponde à un compte existant.
def numero_compte_existant(comptes, message):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            if trouver_compte(comptes, num) is not None:
                return num
            else :
                print("compte invalide")
                
#Demander un montant jusqu'à obtenir un nombre strictement positif.          
def saisir_montant_positif(message):
    while True:
        montant = input(message) 
        try:
            montant= float(montant) 
            if montant> 0:
                return montant
        except ValueError:
            pass
        print("Erreur : veuillez saisir un montant positif.") 

#Afficher tous les comptes existants
def afficher_comptes(comptes):
    print("\n===== LISTE DES COMPTES =====")
    for compte in comptes:
        print(f"Numéro: {compte['numero']}")
        print(f"Nom: {compte['titulaire']}")
        print(f"Solde : {compte['solde']} FCFA")

comptes = [
{"numero": 1, "titulaire": "Sainte union", "solde": 150000}, 
{"numero": 2, "titulaire": "Aissatou Bente", "solde": 75000}, 
{"numero": 3, "titulaire": "Carole Yollah", "solde": 320000}, 
]
# afficher le menu principal
def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("===== AGENCE_CESAG_BANK =====")
    print("1. Afficher tous les comptes")
    print("2. Consulter le solde d'un compte")
    print("3. Créer un nouveau compte")
    print("4. Effectuer un dépôt")
    print("5. Effectuer un retrait")
    print("6. Effectuer un transfert entre deux comptes")
    print("7. Quitter")
    print("==============================")
    
# demander le choix de l'utilisateur et verifier qu'il est compris entre 1 et 7 
def saisir_choix_menu():
    while True:
        choix = input("Votre choix : ")
        if choix.isdigit() and 1 <= int(choix) <= 7:
            return int(choix)
        print("Erreur : choisissez un nombre entre 1 et 7.")
        
# rechercher un compte avec son numero
def trouver_compte(comptes, numero):
    for compte in comptes:
        if compte["numero"] == numero:
            return compte
    return None
    
# Demander un numéro de compte jusqu'à ce qu'il corresponde à un compte existant.
def numero_compte_existant(comptes, message):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            if trouver_compte(comptes, num) is not None:
                return num
        print("Compte invalide.")
        
#Demander un montant jusqu'à obtenir un nombre strictement positif.
def saisir_montant_positif(message):
    while True:
        montant = input(message)
        try:
            montant= float(montant) 
            if montant> 0:
                return montant
        except ValueError:
            pass
        print("Erreur : veuillez saisir un montant positif.") 
        
#permet d'afficher tous les comptes
def afficher_comptes(comptes):
    print("\n===== LISTE DES COMPTES =====")
    for compte in comptes:
        print("----------------------------")
        print("Numéro :", compte["numero"])
        print("Titulaire :", compte["titulaire"])
        print("Solde :", compte["solde"], "FCFA")

#Permet de consulter le solde d'un compte existant.
def consulter_solde(comptes):
    num = numero_compte_existant(comptes,"Numéro du compte : ")
    compte = trouver_compte(comptes, num)
    print("Solde :", compte["solde"], "FCFA")

#Créer un nouveau compte et l'ajouter à la liste des comptes.
def creer_compte(comptes):

    nom = input("Nom du titulaire : ")

    while True:
        try:
            solde = float(input("Solde initial : "))

            if solde >= 0:
                break
            else:
                print("Erreur : le solde doit être positif ou nul.")

        except ValueError:
            print("Erreur : veuillez saisir un nombre valide.")

    # Rechercher le plus grand numéro de compte existant
    plus_grand_numero = 0

    for compte in comptes:
        if compte["numero"] > plus_grand_numero:
            plus_grand_numero = compte["numero"]

    numero = plus_grand_numero + 1

    # Création du nouveau compte sous forme de dictionnaire
    nouveau_compte = {
        "numero": numero,
        "titulaire": nom,
        "solde": solde
    }

    # Ajout du compte crée la liste des comptes exisrants
    comptes.append(nouveau_compte)

    print("Compte créé avec succès.")
    print("Numéro du compte :", numero)
    

#Permet d'ajouter de l'argent sur un compte existant.
def deposer(comptes):
    numero = numero_compte_existant(
        comptes, 
        "Numéro du compte à créditer : "
    )
    montant = saisir_montant_positif("Montant du dépôt : ")
    compte = trouver_compte(comptes, numero)
    compte["solde"] += montant
    print("Dépôt effectué avec succès.")
    print("Nouveau solde :", compte["solde"], "FCFA")
    
#Permet de retirer de l'argent d'un compte existant.

def retirer(comptes):
    numero = numero_compte_existant(
        comptes,
        "Numéro du compte : "
    )

    montant = saisir_montant_positif(
        "Montant du retrait : "
    )

    compte = trouver_compte(comptes, numero)

    if compte["solde"] >= montant:

        compte["solde"] -= montant

        print("Retrait effectué.")
        print("Nouveau solde :", compte["solde"], "FCFA")

    else:

        print("Erreur : solde insuffisant.")
        
#Transferer de l'argent entre deux comptes, compte source vers celui de la destination
def transferer(comptes):

    numero_source = numero_compte_existant(
        comptes,
        "Compte source : "
    )

    numero_destination = numero_compte_existant(
        comptes,
        "Compte destination : "
    )

    while numero_source == numero_destination:

        print("Les deux comptes doivent être différents.")

        numero_destination = numero_compte_existant(
            comptes,
            "Compte destination : "
        )

    montant = saisir_montant_positif(
        "Montant du transfert : "
    )

    compte_source = trouver_compte(comptes, numero_source)
    compte_destination = trouver_compte(comptes, numero_destination)

    if compte_source["solde"] >= montant:

        compte_source["solde"] -= montant
        compte_destination["solde"] += montant

        print("Transfert effectué avec succès.")

    else:

        print("Erreur : solde insuffisant.")

#Menu principal du programme
def main():
    """Boucle principale."""

    while True:

        afficher_menu()

        choix = saisir_choix_menu()

        if choix == 1:

            afficher_comptes(comptes)

        elif choix == 2:

            consulter_solde(comptes)

        elif choix == 3:

            creer_compte(comptes)

        elif choix == 4:

            deposer(comptes)

        elif choix == 5:

            retirer(comptes)

        elif choix == 6:

            transferer(comptes)

        else:

            print("Merci d'avoir utilisé CESAG BANK.")
            break
main()
