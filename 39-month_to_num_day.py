#39 - Month Name to Number of Days

month = input('Saisissez un mois : ')

if month == "février":
    print("28 ou 29 jours")
elif month == "avril" or month == "juin" or month == "septembre" or month == "novembre":
    print(f'En {month}, il y a 30 jours.')
elif month == "janvier" or month == "mars" or month == "mai" or month == "juillet" or month == "août" or month == "octobre" or month == "décembre":
    print(f'En {month}, il y a 31 jours.')
else:
    print(f"{month} n'est pas un mois.")