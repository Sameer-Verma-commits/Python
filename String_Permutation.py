# factorial function
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# calculating permutation
s = input("Enter a String: ")
s = s.lower()

n = len(s)

# factorial of total letters
total_fact = factorial(n)

D = {}

for x in s:
    if s.count(x) > 1:
        if x in D:
            D[x] += 1
        else:
            D[x] = 1

# calculate factorial of repeated counts
rep = 1
for x in D:
    rep *= factorial(D[x])

# total number of distinct permutations
p = total_fact // rep

print("Total Number Of Permutation:", p)
