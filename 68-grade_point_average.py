import sys
# 68 - Compute a Grade Point Average

grade = input('Voulez-vous entrer une note (O/N) : ').upper()
cpt = 1
somme = 0
# print(somme)

if grade == "O":
    while grade != "" :
        grade = input('Entrez la "letter grade" (blanc pour quitter) : ').upper()
        match grade :
            case "A+" | "A":
                points = 4.0
            case "A-":
                points = 3.7
            case "B+":
                points = 3.3
            case "B":
                points = 3.0
            case "B-":
                points = 2.7
            case "C+":
                points = 2.3
            case "C":
                points = 2.0
            case "C-":
                points = 1.7
            case "D+":
                points = 1.3
            case "D":
                points = 1.0
            case "F":
                points = 0
        somme = somme + points
        cpt += 1
        #print(grade)
        # print(points)
        # print(somme)
        # print(cpt)
        if grade == "":
            cpt = cpt - 1
            moyenne = somme / cpt
            print(f"La moyenne est de {moyenne}")
else:
    sys.exit()