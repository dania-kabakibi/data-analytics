''' Lab 3 '''

# Dictionary
contact_info = {
    "name" : "Bob", 
    "address" : "123 street", 
    "city" : "Belleville",
    "state" : "New Jersey", 
    "zip" : "07109"
}

# print the address
print(
    f"{contact_info.get('name')}\n"
    f"{contact_info.get('address')}\n"
    f"{contact_info.get('city')}, {contact_info.get('state')} {contact_info.get('zip')}"
    )
print("-" * 30)

# Remove the key:value pair for name
contact_info.pop("name")

# Add a new variable for full_name
full_name = {
    "first_name" : "Alice",
    "last_name" : "Yellow"
    }

# Add honorific
full_name.update({"honorific" : "Ms."})

# Add full_name to contact_info
contact_info.update(full_name)

# Print the formatted address again
print(
    f"{contact_info.get('honorific')} {contact_info.get('first_name')} {contact_info.get('last_name')}\n"
    f"{contact_info.get('address')}\n"
    f"{contact_info.get('city')}, {contact_info.get('state')} {contact_info.get('zip')}"
    )