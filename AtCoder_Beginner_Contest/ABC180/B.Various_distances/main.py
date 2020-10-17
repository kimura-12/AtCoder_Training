import math
n = int(input())
x = list(map(int, input().split()))

ma = 0
yu = 0.
che = -float("inf")
for i in x:
    ma += abs(i)
    yu += abs(i) ** 2
    che = max(abs(i), che)
print(ma)
print(math.sqrt(yu))
print(che)