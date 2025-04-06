def afficher_menu():
    print("\n*************-----Gestionnaire de Budget Personnel-----*************")
    print("1. AJouter une depense")
    print("2. Voir les depenses")
    print("3. Resumer les depenses par categorie")
    print("4. Quitter l'application")

def ajouter_depense():
    montant = input("Entrer le montant a depense : ")
    categorie = input("Entrer le categorie (Nourriture, Transport, Loisir etc...) : ")
    try:
        with open('depense.txt','a') as f:
            f.write(f"\n{categorie}, {montant}")
    except FileNotFoundError:
        print("Vous ne pouvez pas ajouter une depense")

def voir_les_depenses():
    try:
        with open('depense.txt','r') as f:
            lines = f.readlines()
            print(lines)
            print("----- Voici la liste des depenses disponibles-----")
            print("Cartegorie   Montant ")
            print("____________________")
            for l in lines:
                cat,mon = l.strip().split(',')
                mon = float(mon)
                print(f"{cat}   {mon} ")
    except FileNotFoundError:
        print("Vous n'avez pas de depense.")

def resume_depense_categori():
    resume = {}
    som=0
    try:
        with open("depense.txt",'r') as f:
            lines = f.readlines()
            for i in lines:
                cat,mon = i.strip().split(',')
                cat = cat.capitalize()
                mon = float(mon)
                if cat in resume:
                    resume[cat] = resume.get(cat) + mon
                else:
                    resume[cat] = mon
            for c,m in resume.items():
                 print(f"{c.capitalize()} : {m:.2f} FCFA")


    except FileNotFoundError:
        print("Pas de depense pour le moment")


while True:
    afficher_menu()
    choix = input("Choisissez une option : ")
    if choix == "1":
        ajouter_depense()
    elif choix == "2":
        voir_les_depenses()
    elif choix=="3":
        resume_depense_categori()
    elif choix == "4":
        print("Merci d'avoir utilisé le gestionnaire. À bientôt !")
        break
    else:
        print("❌ Choix invalide. Veuillez réessayer.")