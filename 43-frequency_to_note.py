# 43 - Frequency to Note

frequ = int(input("Indiquez la fréquence (en Hz) : "))

c4_freq = 261.63
d4_freq = 293.66
e4_freq = 329.63
f4_freq = 349.23
g4_freq = 392.00
a4_freq = 440.00
b4_freq = 493.88
limit = 1

if frequ > c4_freq - limit or frequ < c4_freq + limit:
    print("Note : C4")
elif frequ > d4_freq - limit or frequ < d4_freq + limit:
    print("Note : D4")
elif frequ > e4_freq - limit or frequ < e4_freq + limit:
    print("Note : E4")
elif frequ > f4_freq - limit or frequ < f4_freq + limit:
    print("Note : F4")
elif frequ > g4_freq - limit or frequ < g4_freq + limit:
    print("Note : G4")
elif frequ > a4_freq - limit or frequ < a4_freq + limit:
    print("Note : A4")
elif frequ > b4_freq - limit or frequ < b4_freq + limit:
    print("Note : B4")