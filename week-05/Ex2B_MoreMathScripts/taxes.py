# Federal taxes are 23% of your salary every month. You make X amount of money. 
# How much is withheld for taxes?

salary = float(input("Enter your salary: "))

tax_withheld = salary * 0.23

print(f"Your withheld for taxes is ${format(tax_withheld, ".2f")}")