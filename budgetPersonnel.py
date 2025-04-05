def afficher_menu():
    print("\n--- Gestionnaire de Budget Personnel ---")
    print("1. Ajouter une dépense")
    print("2. Voir les dépenses")
    print("3. Résumé des dépenses par catégorie")
    print("4. Quitter")

def ajouter_depense():
    categorie = input("Catégorie (nourriture, transport, etc.): ")
    montant = input("Montant: ")
    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{categorie},{montant}\n")
    print("✅ Dépense ajoutée avec succès.")
    
def voir_depenses():
    print("\n--- Liste des Dépenses ---")
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
            for ligne in lignes:
                categorie, montant = ligne.strip().split(",")
                print(f"{categorie.capitalize()} : {montant} FCFA")
    except FileNotFoundError:
        print("Aucune dépense enregistrée pour le moment.")

def resume_par_categorie():
    resume = {}
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for ligne in f:
                categorie, montant = ligne.strip().split(",")
                montant = float(montant)
                print(resume.get(categorie, 0))
                resume[categorie] = resume.get(categorie, 0) + montant
        print("\n--- Résumé par Catégorie ---")
        for cat, total in resume.items():
            print(f"{cat.capitalize()} : {total:.2f} FCFA")
    except FileNotFoundError:
        print("Aucune dépense trouvée.")

while True:
    afficher_menu()
    choix = input("Choisissez une option : ")
    if choix == "1":
        ajouter_depense()
    elif choix == "2":
        voir_depenses()
    elif choix == "3":
        resume_par_categorie()
    elif choix == "4":
        print("Merci d'avoir utilisé le gestionnaire. À bientôt !")
        break
    else:
        print("❌ Choix invalide. Veuillez réessayer.")



