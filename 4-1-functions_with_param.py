def drawBox(width, height):
    if width < 2 or height < 2:
        print("Erreur : la longueur ou la largeur est trop petite")
        quit()
    
    print("*" * width)
    print("*" + " " * (width - 2) + "*")
    print("*" * width)


drawBox(15, 4)

def drawBox2(width, height, outline, fill):
    if width < 2 or height < 2:
        print("Erreur : la longueur ou la largeur est trop petite")
        quit()
    
    print(outline * width)

    for i in range(height - 2):
        print(outline + fill * (width - 2) + outline)

    print(outline * width)


drawBox(15, 4)

drawBox2(14, 5, "@", ".")