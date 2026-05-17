''' Lab 1 (10 - 17)'''

f = open("Ex4A_ReadWriteFiles/about_me.txt", "r")

readf = f.read(50)
readlinef = []
readlinesf = f.readlines(100)

#print(f.read(50))
#print(f.read(50))

# print(f.readline(10))
# print(f.readline())
for i in range(1, 5): 
    readlinef.append(f.readline())

# print(f.readlines(1))
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(10))
# print(f.readlines(-1))

print(
    f"First 50 characters: {readf}\n"
    f"Next four lines, as list by line: {readlinef}\n"
    f"Next 100 characters, as list by line, rounded up to complete lines: {readlinesf}"
)

f.close()