import math

l = int(input())

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(comb(l-1, 11))