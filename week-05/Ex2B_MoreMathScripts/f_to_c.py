# convert a temperature from Fahrenheit to Celsius

f_temp = float(input("Enter the temperature in Fahrenheit: "))

c_temp = (f_temp - 32) * (5/9)

print(f"The temperature is {c_temp:.2f}°C")