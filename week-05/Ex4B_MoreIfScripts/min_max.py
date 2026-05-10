''' Lab 4 '''
# Display the smallest and the largest of three numbers

a, b, c = input("Enter three numbers (press space between them): ").split()

a = float(a)
b = float(b)
c = float(c)

# Largest number
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

# Smallest number
smallest = a

if b < smallest:
    smallest = b

if c < smallest:
    smallest = c

print(
    f"From ({a:.2f}, {b:.2f}, {c:.2f}), "
    f"the smallest number is {smallest:.2f}, "
    f"and the largest number is {largest:.2f}"
)