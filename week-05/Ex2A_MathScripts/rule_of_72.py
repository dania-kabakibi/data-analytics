# interest_rate = 6  # 6%
# saving = 10200.75

'''Lab 3: Update the script using input() function'''
interest_rate = float(input("What is the interest rate (e.g., enter 6 for 6%)? "))
saving = float(input("What is your saving amount? "))

years_to_double = 72 / interest_rate
doubled_saving = saving * 2

print(f"Your current savings is {saving}.")
print(f"At a {format(interest_rate / 100, '.0%')} interest rate, your savings account will be\n" 
      f"worth {format(doubled_saving, '.2f')} in {format(years_to_double, '.1f')} years")