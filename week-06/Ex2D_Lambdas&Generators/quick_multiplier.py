''' Lab 1 '''

doubler = lambda n: n * 2

print("--- doubler ---")
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n * 3

print()
print("--- tripler ---")
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multiplier(n, f):
    return f(n)

quadrupler = multiplier(5, lambda n: n * 4)
quintupler = multiplier(8, lambda n: n * 5)
sextupler = multiplier(4, lambda n: n * 6)
septupler = multiplier(2, lambda n: n * 7)
octupler = multiplier(4, lambda n: n * 8)
nonupler = multiplier(3, lambda n: n * 9)
decupler = multiplier(5, lambda n: n * 10)

print()
print(
    f"quadrupler: {quadrupler}\n"
    f"quintupler: {quintupler}\n"
    f"sextupler : {sextupler}\n"
    f"septupler : {septupler}\n"
    f"octupler  : {octupler}\n"
    f"nonupler  : {nonupler}\n"
    f"decupler  : {decupler}\n"
)