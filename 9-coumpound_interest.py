#Compound Interest

savings = 1389

money_deposited = input("Quelle est le montant déposé :")

total_savings = savings + float(money_deposited)
percent_interest = 4/100
yr = 1

for i in range(3):
    total_savings = total_savings + (total_savings*percent_interest)
    print(f"L'année n° {i}, le montant du compte épargne s'élève à {format(total_savings, '.2f')}")

