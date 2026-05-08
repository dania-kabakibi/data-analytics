''' Lab 1 '''
# 2. Create a list with the titles of your favorite movies
movies = ["Inside Out", "Babys Day Out", "Sing", "Johnny English"]

# 3. Use the len() function to print the descriptive statement
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)
print("-" * 30)

# 4. Print a sorted list two ways
# a) Use the sorted() function
print(sorted(movies))
print(movies)
print("-" * 30)

# b) Use the .sort() method
movies.sort() 
print(movies)
print("-" * 30)

# 5. Think of at least one more movie to add to your list
movies.append("The Wild Robot")

print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)