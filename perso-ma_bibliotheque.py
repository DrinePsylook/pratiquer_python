# perso - ma bibliotheque
# creation d'une bibliothèque. A l'intérieur, classement par genre

bookshelves = { 
    "fantasy" : { 
        "os" : 126, 
        "mort" : 666, 
        "dracula" : 786
        }
    }

def main():
    message = input("Que voulez-vous faire ? Tapez C pour effectuer une recherche, E pour entrer des données : ").upper()

    if message == "C":
        filter()
    elif message == "E":
        print("Editer")

  

def filter():
    search = input("Que recherchez-vous ? Tapez G pour le genre littéraire, T pour un titre de livre, P pour le nombre de pages minimum : ").upper()

    if search == "G":
        cat = input("Quel genre littéraire voulez-vous chercher ? ").lower()
        if cat in bookshelves.keys():
            print(bookshelves[cat])
        else:
            create_cat = input("cette catégorie n'existe pas encore. Voulez-vous la créer ? (O/N) ").upper()
            print(create_cat)
            if create_cat == "O":
                edit()
            else:
                print("Au revoir")
                quit()
    elif search == "T":
        title = input("Quel titre recherchez-vous ? ").lower()
        for genre, datas in bookshelves.items():
            for index, row in datas.items():
                if title == index:
                    book = index, " : ", row
                else:
                    print(f"{title} n'est pas en base de données")
    elif search == "P":
        how_many_p = int(input("Combien de pages minimum ? : "))
        for pg in bookshelves.values():
            if pg >= how_many_p:
                print(bookshelves[pg])



def edit():
    bookshelf = input('Saisissez un genre littéraire : ').lower()
    bookshelves[bookshelf] = {}
    print("Genre créé.")

    book = input("Renseigner le titre du livre (blanc pour quitter) : ").lower()
    nb_page = int(input(f'Combien de pages a "{book}" : '))

    while book != "":
        bookshelves[bookshelf][book] = nb_page
        book = input("Renseigner le titre du livre (blanc pour quitter) : ")
        nb_page = input(f'Combien de pages a "{book}" : ')

        if book == "":
            main()

        print(bookshelves)
        


if __name__ == "__main__":
    main()
