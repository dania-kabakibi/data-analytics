''' Lab 1 '''

class Restaurant:
    ''' class for restaurants info '''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

restaurant1 = Restaurant("Wendy", "fast-food")
restaurant2 = Restaurant("Dunkin' Donuts", "quick-service restaurant (QSR)")
restaurant3 = Restaurant("Subway", "fast-casual food")

print("--- Restaurant 1 ---")
restaurant1.describe_rest()
restaurant1.rest_open()
print()

print("--- Restaurant 2 ---")
restaurant2.describe_rest()
restaurant2.rest_open()
print()

print("--- Restaurant 3 ---")
restaurant3.describe_rest()
restaurant3.rest_open()
print()