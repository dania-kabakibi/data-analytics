# calculate the distance between coordinates (x1, y1) and (x2, y2)

from math import sqrt

x1, y1 = input("Enter two values as the coordinates (x1 y1): ").split()

x2, y2 = input("Enter two values as the coordinates (x2 y2): ").split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")