def add(nom,prix,quantite):
    try:
        with open('magasin.txt', 'a') as f:
            f.write(nom + "," + str(prix) + "," + str(quantite) + "\n")
            print("Ajouté avec succès")
            return 1
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return 0
    except PermissionError:
        print("Vous n'avez pas les droits pour lire ce fichier")
        return 0
    
def afficherstock():
    try:
        with open('magasin.txt', 'r') as f:
            f = f.read().splitlines()
            stocke = len(f)
            print("Le stock est : " + str(stocke))
            return stocke
    except FileNotFoundError:
        print("Pas de stock dans le magasin")
        return 0
    except PermissionError:
        print("Vous n'avez pas les droits pour lire ce fichier")
        return 0
    
def fairechoix():
    print("Faire un choix")
    print("1. Ajouter un produit")
    print("2. Afficher le stock")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        nom = input("Entrez le nom du produit : ")
        prix = input("Entrez le prix du produit : ")
        quantite = input("Entrez la quantité du produit : ")
        add(nom,prix,quantite)
    elif choix == "2":
        stock = afficherstock()
        print("Le stock est : " + str(stock))
    else:
        print("Choix invalide")

fairechoix()