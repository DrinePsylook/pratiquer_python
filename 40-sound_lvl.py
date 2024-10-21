# 40 - Sound Levels

decibel_level = int(input("Indiquez le niveau de décibels : "))

if decibel_level < 40:
    print("Super calme")
elif decibel_level <= 70:
    print('entre lieu calme et réveil')
elif decibel_level <= 106:
    print('entre réveil et tondeuse à gaz')
elif decibel_level <= 130:
    print('entre tondeuse à gaz et marteau piqueur')
else:
    print('Trop de bruit !!!')