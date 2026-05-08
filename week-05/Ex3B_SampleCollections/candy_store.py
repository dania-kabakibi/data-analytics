''' Lab 2 '''

# Tuples
candy_brands = ("Skittles", "Airheads", "Sour Patch Kids")
fruit_flavors = ("Cherry", "Apple", "Watermelon")

# Set of candy combinations
candy_combinations = {
    candy_brands[0] + " " + fruit_flavors[1],
    candy_brands[1] + " " + fruit_flavors[2],
    candy_brands[2] + " " + fruit_flavors[0]
}

# The output message
print("Today's candy options include:")
print(candy_combinations)

# The order appear different when I run the program again
# A set does not keep items in a fixed order