''' Lab 1-1 '''

dep_code = input("Enter department code: ")

if dep_code == "1":
    print("Marketing")
elif dep_code == "5":
    print("Human Resources")
elif dep_code == "10":
    print("Accounting")
elif dep_code == "12":
    print("Legal")
elif dep_code == "18":
    print("IT")
elif dep_code == "20":
    print("Customer Relations")

else: print("The department code is not found")