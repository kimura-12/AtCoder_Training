import math

k = int(input())

ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        for l in range(1, k + 1):
            temp = math.gcd(i, j)
            ans += math.gcd(temp, l)
print(ans)