''' Lab 1 '''
import random

products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 
    'USB Hub', 'Desk Lamp', 'Surge Protector'
]

# a) Product of the Day based on one randomly selected item
product_of_the_Day = random.choice(products)
print(f"Product of the Day: {product_of_the_Day}\n")

# b) Three products selected for survey
survey_products = random.sample(products, 3)
print(f"Three product for survey: {survey_products}\n")

# c) Display all products in randomized order
random.shuffle(products)
print("All products:")
print(products)

# d) Generate a simulated daily transaction
single_transaction = random.randint(50, 300)
print(f"\nRandomly selected daily transaction count: {single_transaction}")

# All products with simulated daily transaction as table
print(f"\n{'Product':<18} | {'Daily transaction'}")
print(f"{'-' * 16:<18} | {'-' * 16}")

for p in products:
    t = random.randint(50, 300)
    print(f"{p:<18} | {t}")