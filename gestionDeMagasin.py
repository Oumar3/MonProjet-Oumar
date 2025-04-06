def afficher():
    print("\n*************----- Gestion de Stock pour un  Magasin -----*************")
    print("1. Ajouter un produit")
    print("2. Afficher les produits en stock")
    print("3. Supprimer un produit")
    print("4. Rechercher un produit")
    print("5. Quitter l'application")

def add():
    nom = input("Entrez le nom du produit : ")
    prix = input("Entrez le prix du produit : ")
    prix = float(prix)
    quantite = input("Entrez la quantité du produit : ")
    quantite = int(quantite)
    try:
        with open('stock.txt', 'a') as f:
            f.write(f"{nom},{prix},{quantite}\n")
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    except PermissionError:
        print("Vous n'avez pas les droits pour lire ce fichier")
        return 0
    
def afficherstock():
    try:
        with open('stock.txt', 'r') as f:
            products = f.readlines()
            print("----- Voici la liste des produits en stock -----")
            print("Produit Prix  Quantite ")
            for p in products:
                pro,pri,quant = p.strip().split(',')
                pro = pro.capitalize()
                quant = int(quant)
                pri = float(pri)
                print(f"{pro}   {pri}   {quant}")
    except FileNotFoundError:
        print("Pas des produits en stock dans le magasin")
    except PermissionError:
        print("Vous n'avez pas les droits pour lire ce fichier")

def supprimer():
    nom = input("Entrez le nom du produit à supprimer : ")
    nom = nom.capitalize()
    dicproducte = []
    try:
        with open('stock.txt', 'r') as f:
            products = f.readlines()
            for p in products:
                pro,pri,quant = p.strip().split(',')
                pro = pro.capitalize()
                quant = int(quant)
                pri = float(pri)
                dicproducte.append({"nom":pro,"prix":pri,"quantite":quant})
            for d in dicproducte:
                if d["nom"] == nom:
                    products.remove(p)
                    print(f"{nom} supprimé avec succès")
                    break
                else:
                    print("Le produit n'existe pas")
        with open('stock.txt', 'w') as f:
            for p in products:
                f.write(p)
    except FileNotFoundError:
        print("Pas des produits en stock dans le magasin")
    except PermissionError:
        print("Vous n'avez pas les droits pour lire ce fichier")

def rechercher():
    nom = input("Entrez le nom du produit à rechercher : ")
    nom = nom.capitalize()
    try:
        with open('stock.txt', 'r') as f:
            products = f.readlines()
            listeproduits = []
            for p in products:
                pro,pri,quant = p.strip().split(',')
                pro = pro.capitalize()
                quant = int(quant)
                listeproduits.append({"nom":pro,"prix":pri,"quantite":quant})
            print(listeproduits)
            for d in listeproduits:
                if d["nom"] == nom:
                    print(f"Le produit {nom} est disponible en stock a une quantité de {d['quantite']}")
                    break
                else:
                    print("Le produit n'existe pas")
    except FileNotFoundError:
        print("Pas des produits en stock dans le magasin")
    

while True:
    afficher()
    choix = input("Choisissez une option : ")
    if choix == "1":
        add()
    elif choix == "2":
        afficherstock()
    elif choix == "3":
        supprimer()
    elif choix == "4":
        rechercher()
    elif choix == "5":
        print("Merci d'avoir utilisé l'application gestion de stock !")
        break
    else:
        print("❌ Choix invalide. Veuillez réessayer.")
