# Description: This script tests various numeric  
#              conversion techniques 
# Author: Sam Q. Newprogrammer

a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

'''a) Cast as integer using int()'''
# print(int(a)) # ValueError: invalid literal for int() with base 10: '  101.1 '
# print(int(b)) # 55
# print(int(c)) # ValueError: invalid literal for int() with base 10: '402 Stevens'
# print(int(d)) # ValueError: invalid literal for int() with base 10: 'Number 5  '

'''b) Cast as float using float()'''
# print(float(a)) # 101.1
# print(float(b)) # 55.0
# print(float(c)) # ValueError: could not convert string to float: '402 Stevens'
# print(float(d)) # ValueError: could not convert string to float: 'Number 5  '

'''c) For variable a, try casting into a float then integer, like this: int(float(a))'''
# print(int(float(a))) # 101

'''d) Use slicing to add just the numeric portion of the string to a new variable'''
new_a = int(a[2:5])
new_b = int(b)
new_c = int(c[0:3])
new_d = int(d[7])
print(new_a, type(new_a))
print(new_b, type(new_b))
print(new_c, type(new_c))
print(new_d, type(new_d))

'''e) For variables a and d, use the .strip() method to remove the leading/trailing 
spaces, within a print statement to display each result.'''
print(a.strip())
print(d.strip())