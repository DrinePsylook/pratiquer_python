# 6 - Tax and Tip

meal_cost = float(input('Veuillez saisir le montant du repas : '))
tax = 20/100
tip = 18/100

tax_cost = meal_cost * tax
tip_cost = (meal_cost-tax_cost) * tip

addition = meal_cost + tax_cost + tip_cost

# print(format(tax_cost, '.2f'))
# print(format(tip_cost, '.2f'))

print(f"Le repas hors-taxe coûte {format(meal_cost, '.2f')} $. La taxe sélève à {format(tax_cost, '.2f')} $. le pourboire est de {format(tip_cost, '.2f')} $. Le montant à payer est de {format(addition, '.2f')} $.")