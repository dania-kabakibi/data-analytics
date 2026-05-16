''' Lab 2 '''
from math import floor

cust_list = []

class RewardsProgram:
    ''' class to handle customers informations '''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}

    def profile(self):
        print(
            f"Name: {self.cust_name}\n"
            f"Phone: {self.phone}\n" 
            f"Email: {self.email}\n"
        )

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    def visit_rest(self):
        rest_name = input("Name of restaurant: ")
        if rest_name not in self.restaurants_visited:
            self.restaurants_visited.append(rest_name)
        self.calculate_rewards(rest_name)
        
    def calculate_rewards(self, rest_name):    
        total_bill = float(input("What was the total food bill for this visit? "))
        points = floor(total_bill)
        if rest_name in self.rewards_points:
            self.rewards_points[rest_name] += points
        else:
            self.rewards_points[rest_name] = points
            
        print(f"Points for this visit: {points}\n"
              f"Total rewards points earned at {rest_name}: {self.rewards_points[rest_name]}\n" 
              f"Thank you for visiting {rest_name}!\n")



customer1 = RewardsProgram("John Doe", "770-123-4567", "jdoe4@gmail.com")
customer2 = RewardsProgram("Barb Akew", "973-012-3456", "barba@gmail.com")
customer3 = RewardsProgram("Lana Kent", "862-345-6789", "lanak1@gmail.com")

print("--- Customer1 ---")
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()
customer1.visit_rest()
customer1.visit_rest()
print()

print("--- Customer2 ---")
customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()
customer2.visit_rest()
print()

print("--- Customer3 ---")
customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()
print('-' * 30)

print(f"Customer list: \n{cust_list}\n")
print(f"{customer1.cust_name}'s Rewards: {customer1.rewards_points}")
print(f"{customer2.cust_name}'s Rewards: {customer2.rewards_points}")