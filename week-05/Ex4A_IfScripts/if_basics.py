''' Lab 1 '''

x = 100
y = 20

# a) If x divided by y is 5
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else: 
    print("are the variables set up correctly?")

print('-' * 30)

# b) If x times y is y
if x * y == y:
    print("now x times y is y")
    x = 10
else: 
    print(f"Whoops, x equals {x}")

print('-' * 30)

# c) If x is less than y
if x < y:
    print("x is less than y")
    x *= 2
else: 
    print("uh oh, x is not less than y")

print('-' * 30)

# d) If x is greater than y
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

print('-' * 30)

# The final print statement
print(f"The final value of x is {x} and the final value of y is {y}")