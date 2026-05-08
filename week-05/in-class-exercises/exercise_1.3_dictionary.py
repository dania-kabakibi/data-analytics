student = { 
    "name"  : "Alice", 
    "age"   : 20, 
    "major" : "Data Analytics", 
    "gpa"   : 3.5 
}

'''1.  Use get() to access "name"'''
student_name = student.get("name")
print(student_name) # Alice

'''2.  Use get() with a default value for "grade"'''
student_grade = student.get("grade", "grade is not available")
print(student_grade) # grade is not available

'''3.  Use update() to add "year": "Sophomore"'''
student.update({"year": "Sophomore"})

'''4.  Use pop() to remove "age"'''
student.pop("age")

'''5.  Use popitem()'''
student.popitem() # Removes and returns the last inserted item

'''6.  Use keys()'''
all_keys = student.keys()
print(all_keys)

'''7.  Use values()'''
all_values = student.values()
print(all_values)

'''8.  Use items()'''
all_items = student.items()
print(all_items) # Returns a view of all key-value pairs

'''9.  Use copy()'''
student_copy = student.copy()

'''10. Use clear()'''
# student.clear()
# print(f"---After using clear()---\n{all_items}")


'''--- Part 4 — Challenge Section ---'''

# 1.  Add "courses" with a list of 3 courses using update()
student.update({"courses" : ["English", "Excel", "Programming"]})

# 2.  Check if "gpa" exists as a key in the dictionary
key = "gpa"
check_key = student.get(key, "The key is not existing")
if (check_key == "The key is not existing"):
    print("The key is not existing")
else: print(f"The {key} key is existing")

# 3.  Loop through the dictionary and print each key and its value
for item in student.items():
    print(item)