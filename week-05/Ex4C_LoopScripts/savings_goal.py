''' Lab 2 '''

bank_balance = float(input("Enter your starting bank balance: "))
savings_goal = float(input("Set your savings goal: "))
weekly_savings_amount = float(input("Enter your weekly savings amount: "))

treat_cost = 10

while bank_balance < savings_goal:

    if bank_balance > 0.75 * savings_goal:
        bank_balance += weekly_savings_amount
        bank_balance -= treat_cost
        print(f"So close! After treating myself, my balance is up to {bank_balance:.2f}")

    elif bank_balance > 0.5 * savings_goal:
        bank_balance += weekly_savings_amount
        print(f"Almost there! This week my balance is up to {bank_balance:.2f}")

    else:
        bank_balance += weekly_savings_amount
        print(f"This week my balance increased to {bank_balance:.2f}")


print(f"\nGoal met! My current balance is {bank_balance:.2f}")