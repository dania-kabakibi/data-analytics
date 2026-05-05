customer_id = 101 # I assumed this is a numeric ID, but in real systems it could be a string (e.g., "C101") or auto-generated.

customer_name = "John Doe" # I used full name in one variable, but it might be better to split into first_name and last_name.

customer_gender = "Male" # I used a simple string, but it could be char ('M', 'F').

customer_date_of_birth = "2000-05-04" # I used a string in YYYY-MM-DD format.

drivers_license_number = "K0004-12345-67890" # I assumed it's a string because it may include letters and symbols.

auto_policy_number = "AP-987654321" # I assumed it's an alphanumeric string; actual format depends on the insurance company.

my_name = "Dania Kabakibi"
birth_city = "Bloomfield"
birth_state = "New Jersey"


# a) What is the full list of reserved words that can’t be used for variable names?
'''
False    def       if        raise
None     del       import    return
True     elif      in        try
and      else      is        while
as       except    lambda    with
assert   finally   nonlocal  yield
break    for       not
class    from      or
continue global    pass
'''

# b) Pick 5 of these words and review the explanation for how it is used as a keyword in Python.

# 1- def The def function is used to define a function or a method in Python.

# 2- raise The raise statement is used to raise an error. These errors are visible in 
#   the ^traceback^ and they cancel the execution of the program if not handled properly.

# 3- del The del statement is used to delete an object in Python.

# 4- import This statement is used to import modules to the project.

# 5- elif Shorthand for else if, checks if some other condition holds when 
#   the condition in the if statement is false.