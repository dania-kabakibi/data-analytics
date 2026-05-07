from math import ceil

x = int(input("Enter the number of passengers: "))

vans_num = ceil(x / 15)

vans_cost = vans_num * 250

passenger_pay = vans_cost / x

print(f"For {x} passengers, we need {vans_num} vans.")
print(f"The total cost for the vans is ${vans_cost:.2f}")
print(f"Each passenger has to pay ${passenger_pay:.2f}")


'''
Test your script with 38 tourists. Now do some separate calculations to check your 
work: 
a) How much money did your script say you had to charge per person?  
b) If you multiply that out, how much did you collect?  
c) How much were the vans?  
d) Why do you have leftover money?
'''
# a) Each person pays $19.74.
# b) 38 * 19.74 = $750.12 collected.
# c) The vans cost $750 total.
# d) There is leftover money because the cost per person was rounded to two decimal places.