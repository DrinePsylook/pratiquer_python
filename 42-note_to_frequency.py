# 42 - Note to frequency

note = input("Entrez le nom des deux caractères note (ex.: C4): ").upper()

c4_freq = 261.63
d4_freq = 293.66
e4_freq = 329.63
f4_freq = 349.23
g4_freq = 392.00
a4_freq = 440.00
b4_freq = 493.88

note_char = note[0]
octave = int(note[1])

match note_char:
    case "C":
        frequ = c4_freq
    case "D":
        frequ = d4_freq
    case "E":
        frequ = e4_freq
    case "F":
        frequ = f4_freq
    case "G":
        frequ = g4_freq
    case "A":
        frequ = a4_freq
    case "B":
        frequ = b4_freq
    case _:
        frequ = "inconnue"

frequ = frequ /2 ** (4 - octave)

print(f"La fréquence de la {note} est {frequ}")