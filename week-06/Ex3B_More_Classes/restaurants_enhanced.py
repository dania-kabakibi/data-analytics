''' Lab 1 '''

class Restaurant:
    ''' class for restaurants info and customers rating '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, num_cust_served):
        self.number_served += num_cust_served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):
        while True:
            user_input = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
            try:
                rate = int(user_input)
                if 1 <= rate <= 5:
                    break
                else: print("Error: Rating must be an integer between 1 and 5.")
            except ValueError:
                print("Error: Please enter a valid whole number (integer).")

        self.customer_ratings.append(rate)
        avg = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"“Your rating was {rate}. The average rating for this restaurant is {avg:.2f}”")

restaurant1 = Restaurant("Wendy", "fast-food")
restaurant2 = Restaurant("Dunkin' Donuts", "quick-service restaurant (QSR)")
restaurant3 = Restaurant("Subway", "fast-casual food")

print("--- Restaurant 1 ---")
restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.print_num_served()
restaurant1.add_num_served(146)
restaurant1.add_num_served(89)
restaurant1.print_num_served()
restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()
print()

print("--- Restaurant 2 ---")
restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.print_num_served()
restaurant2.add_num_served(97)
restaurant2.add_num_served(135)
restaurant2.print_num_served()
restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()
print()

print("--- Restaurant 3 ---")
restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.print_num_served()
restaurant3.add_num_served(114)
restaurant3.add_num_served(92)
restaurant3.print_num_served()
restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()
print()