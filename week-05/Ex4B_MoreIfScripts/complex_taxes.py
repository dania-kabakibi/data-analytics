''' Lab 3 '''
''' Calculate federal tax based on annual income and filing status '''

pay_rate = float(input("Enter pay rate amount: "))
hours_worked = int(input("Enter worked hours (weekly): "))
filing_status = input("Enter filing status (single/joint): ").lower()

tax_rate = 0

# Calculate weekly gross pay
if hours_worked > 40:
    overtime = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime * (pay_rate * 1.5)
    weekly_gross_pay = regular_pay + overtime_pay
    
else:
    weekly_gross_pay = pay_rate * hours_worked

# Annual gross pay
annual_gross_pay = weekly_gross_pay * 52

# =================================================

# Determine tax rate
if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 5
    elif annual_gross_pay < 25000:
        tax_rate = 10
    elif annual_gross_pay < 75000:
        tax_rate = 15
    else:
        tax_rate = 20

elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0
    elif annual_gross_pay < 25000:
        tax_rate = 6
    elif annual_gross_pay < 75000:
        tax_rate = 11
    else:
        tax_rate = 20

else:
    print("Enter only single or joint as filing status")

# =================================================

# Tax calculations
tax_withheld = weekly_gross_pay * (tax_rate / 100)
net_pay = weekly_gross_pay - tax_withheld

print( 
    f"\n{'-' * 30}\n"
    f"You worked {hours_worked} hours this period.\n"
    f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}\n"
    f"Your filing status is {filing_status}.\n"
    f"Your tax withholding for the week is ${tax_withheld:.2f}\n"
    f"Your net pay is ${net_pay:.2f}"
)