my_tuple = (10, 20, 30, 40, 50) 
# Additional examples 
mixed_tuple = (1, "Alice", 3.14, True) 
nested_tuple = (1, (2, 3), (4, 5, 6)) 
single_item  = (42,)   # note: trailing comma required for single-item tuple

'''1.   Access the first element using indexing'''
print(f"The first element: {my_tuple[0]}\n")

'''2.   Access the last element using negative indexing'''
print(f"The last element: {my_tuple[-1]}\n")

'''3.   Slice the tuple to get elements from index 1 to 3'''
print(f"my tuple slice: {my_tuple[1: 4]}\n")

'''4.   Use count() to count how many times 30 appears'''
print(f"How many times 30 appears: {my_tuple.count(30)}\n")

'''5.   Use index() to find the position of 30'''
print(f"The position of 30: {my_tuple.index(30)}\n")

'''6.   Use len() to find the number of elements'''
print(f"The number of elements: {len(my_tuple)}\n")

'''7.   Check if 30 exists in the tuple using the in operator'''
print(f"30 in my_tuple: {30 in my_tuple}\n")

'''8.   Unpack the tuple into 5 separate variables'''
val1, val2, val3, val4, val5 = my_tuple
print(
    f"Unpack my tuple:\n"
    f"val1 = {val1}, val2 = {val2}, val3 = {val3}, val4 = {val4}, val5 = {val5}\n"
)

'''9.   Concatenate my_tuple with (60, 70)'''
tuple_b = (60, 70)
my_tuple += tuple_b
print(f"Concatenate my_tuple with (60, 70):\n{my_tuple}\n")

'''10.  Repeat my_tuple twice using the * operator'''
print(f"my_tuple twice:\n{my_tuple * 2}\n")

'''11.  Convert my_tuple to a list'''
my_tuple = list(my_tuple)
print(f"my tuple converted to list:\n{my_tuple}\n")

'''12.  Find the min(), max(), and sum() of my_tuple'''
print(
    f"min in my tuple = {min(my_tuple)}\n"
    f"max in my tuple = {max(my_tuple)}\n"
    f"sum of my tuple = {sum(my_tuple)}\n"
)

'''--- Part 6 — Challenge Section ---'''

# 1.   Create a tuple of 5 city names. Sort and display them without converting to a list 
cities = ("New York city", "Rome", "Tokyo", "Paris", "Istanbul")
print(f"cities: {sorted(cities)}")

# 2.   Create a nested tuple storing 3 students and their GPA. Access the second student's GPA
students = (
    ("Jane", 3.25), ("Alice", 3.83), ("Lana", 2.98)
)
second_student = students[1]
print(f"Second student's GPA: {second_student[1]}")

# 3.   Use a for loop with enumerate() to print each item in my_tuple with its index
for num, item in enumerate(my_tuple, 1):
    print(f"{num}. {item}")

# 4.   Convert my_tuple to a list, append 60, then convert back to a tuple
my_tuple = list(my_tuple)
my_tuple.append(60)
my_tuple = tuple(my_tuple)
print(my_tuple)

# 5.   Use my_tuple as a dictionary key to store the value 'data set A' 
my_dictionary = {my_tuple : 'data set A'}
print(my_dictionary)