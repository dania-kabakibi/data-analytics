''' Lab 4 '''

sales_data = [
    ('Marcus Webb',    'East',  4250.00),
    ('Priya Sharma',   'West',  5875.50),
    ('DeShawn Carter', 'East',  3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen',     'West',  4980.25),
]

total_sales = 0.0

for name, region, person_sales in sales_data:

    total_sales += person_sales

    print(f"{name} ({region}): ${person_sales:,.2f}")

    if person_sales > 5000:
        print("  ^ Top performer!")

print(f"\nOverall total sales = ${total_sales:,.2f}")