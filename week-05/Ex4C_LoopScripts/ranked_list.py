''' Lab 3 '''

cities = ["Istanbul", "Amsterdam", "Rome", "Dubai", "Doha", "London"]

print("Cities I would like to visit:")

for num, city in enumerate(reversed(cities), 1):

    if num == 1:
        print(f"{num}. {city} <- top pick!")
        
    else:
        print(f"{num}. {city}")