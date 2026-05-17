''' Lab 1 '''
import math

# ----- ValueError -----
# Occurs when a function receives an argument of the correct type but an inappropriate value.

print("--- Testing ValueError (Example 1: String to Int) ---")
try:
    # Way 1: Trying to convert a non-numeric string to an integer
    user_num = int("five")
except ValueError:
    print("ValueError: You tried to convert an invalid string into a number.")
else:
    print(f"Success! The number is {user_num}")
finally:
    print("Let's try another one.\n")

print("--- Testing ValueError (Example 2: Math Domain) ---")
try:
    # Way 2: Square root of a negative number (outside the allowed mathematical domain)
    result = math.sqrt(-10)
except ValueError:
    print("ValueError: You cannot take the square root of a negative number in standard math.")
else:
    print(f"Success! The result is {result}")
finally:
    print("Let's try another one.\n")

# ========================================================
# ----- NameError -----
# Occurs when the script tries to use a variable or function that hasn't been defined.

print("--- Testing NameError (Example 1: Undefined Variable) ---")
try:
    # Way 1: Calling a variable that doesn't exist
    print(my_secret_variable)
except NameError:
    print("NameError: You tried to access a variable that has not been defined yet.")
else:
    print("Success! Variable accessed.")
finally:
    print("Let's try another one.\n")

print("--- Testing NameError (Example 2: Typos in Functions) ---")
try:
    # Way 2: Typing a built-in function name incorrectly
    prrnt("Hello World")
except NameError:
    print("NameError: You called a function name that Python doesn't recognize.")
else:
    print("Success! Function called.")
finally:
    print("Let's try another one.\n")

# ========================================================
# ----- TypeError -----
# Occurs when an operation or function is applied to an object of an inappropriate type.

print("--- Testing TypeError (Example 1: Adding Incompatible Types) ---")
try:
    # Way 1: Trying to add a string and an integer together
    total = "Apples" + 5
except TypeError:
    print("TypeError: You cannot add a string and an integer together.")
else:
    print(f"Success! Total is {total}")
finally:
    print("Let's try another one.\n")

print("--- Testing TypeError (Example 2: Incompatible Length Check) ---")
try:
    # Way 2: Trying to find the length (len) of an integer
    number_length = len(12345)
except TypeError:
    print("TypeError: Integers do not have a length. len() requires a sequence like a string or list.")
else:
    print(f"Success! Length is {number_length}")
finally:
    print("Let's try another one.\n")

# ========================================================
# ----- SyntaxError -----
# Occurs when Python's parsing rules are broken.
## We must pass it as a string to eval() so the program doesn't crash before running.

print("--- Testing SyntaxError (Example 1: Missing Closing Quote) ---")
try:
    # Way 1: Missing a closing quote inside an evaluation string
    eval("print('Hello)")
except SyntaxError:
    print("SyntaxError: There is a missing quote or structural mistake in the code.")
else:
    print("Success! No syntax errors.")
finally:
    print("Let's try another one.\n")

print("--- Testing SyntaxError (Example 2: Invalid Variable Assignment) ---")
try:
    # Way 2: Trying to assign a value to a literal number
    eval("5 = x")
except SyntaxError:
    print("SyntaxError: You cannot assign a value to a literal number.")
else:
    print("Success! No syntax errors.")
finally:
    print("Let's try another one.\n")