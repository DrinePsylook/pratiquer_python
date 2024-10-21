# 38 - Name that shape

nb_sides = int(input('Combien de côtés possède votre forme ? '))

match nb_sides :
    case 3:
        print("Votre forme est un triangle")
    case 4:
        print("Votre forme est un quadrilatère")
    case 5:
        print("Votre forme est un pentagone")
    case 6:
        print("Votre forme est un hexagone")
    case 7:
        print("Votre forme est un heptagone")
    case 8:
        print("Votre forme est un octogone")
    case 9:
        print("Votre forme est un ennéagone")
    case 10:
        print("Votre forme est un décagone")
    case _:
        print("Nous ignorons le nom de votre forme")