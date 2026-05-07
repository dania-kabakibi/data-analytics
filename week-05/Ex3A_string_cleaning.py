name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

'''Use .lower() to convert all three names to lowercase'''
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())
print('-' * 30)

'''Use .title() to convert all three names to title case (first letter of each word capitalized)'''
print(name_1.title())
print(name_2.title())
print(name_3.title())
print('-' * 30)

'''Use .replace() to remove the $ from both salary strings'''
salary_1 = salary_1.replace('$', '')
print(salary_1)
print(type(salary_1))

salary_2 = salary_2.replace('$', '')
print(salary_2)
print(type(salary_2))
print('-' * 30)

'''What would you need to do next to perform math on them?'''
# salary_1 = salary_1.replace(',', '')
# salary_1 = float(salary_1)
# print(salary_1, type(salary_1))

# salary_2 = salary_2.replace(',', '')
# salary_2 = float(salary_2)
# print(salary_2, type(salary_2))

'''chain .replace() and int() together in a single line to produce a usable integer from salary_1.'''
salary_1 = int(salary_1.replace(',', ''))
print(salary_1, type(salary_1))

salary_2 = int(salary_2.replace(',', ''))
print(salary_2, type(salary_2))