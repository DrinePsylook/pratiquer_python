# 37 - Vowel or consonant

character = input("Entrez une lettre : ")

if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
    print(f'La lettre "{character}" est une voyelle.')
elif character == "y":
    print(f'Parfois "{character}" est une voyelle, parfois une consonne.')
else: 
    print(f'La lettre "{character}" est une consonne.')