''' Lab 2 '''

pay_rate = float(input("Enter pay rate amount: "))
hours_worked = int(input("Enter worked houres: "))

if hours_worked > 40:
    overtime = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
    reason = "Over 40 hours"

elif hours_worked < 40:
    gross_pay = pay_rate * hours_worked
    reason = "Under 40 hours"
    
else:
    gross_pay = pay_rate * hours_worked
    reason = "Exactly 40 hours"

print(f"{'Pay Rate':<15}{'Hours Worked':<15}{'Gross Pay':<15}{'Reason':<15}")
print(f"{pay_rate:<15}{hours_worked:<15}{gross_pay:<15,.2f}{reason:<15}")