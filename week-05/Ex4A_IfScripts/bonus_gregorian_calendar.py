''' BONUS Lab '''
'''
Leap Year Calculation Rules (Gregorian Calendar):
# Step 1: Is the year divisible by 4? If no, it is not a leap year. If yes, move to step 2.
# Step 2: Is the year divisible by 100? If no, it is a leap year. If yes, move to step 3.
# Step 3: Is the year divisible by 400? If yes, it is a leap year. If no, it is not a leap year
'''

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")