''' Lab 2 '''

cust_list = []

class RewardsProgram:
    ''' class to handle customers informations '''

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

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

customer1 = RewardsProgram("John Doe", "770-123-4567", "jdoe4@gmail.com")
customer2 = RewardsProgram("Barb Akew", "973-012-3456", "barba@gmail.com")
customer3 = RewardsProgram("Lana Kent", "862-345-6789", "lanak1@gmail.com")

print("--- Customer1 ---")
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()
print()

print("--- Customer2 ---")
customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()
print()

print("--- Customer3 ---")
customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()
print('-' * 30)

print(f"Customer list: \n{cust_list}")