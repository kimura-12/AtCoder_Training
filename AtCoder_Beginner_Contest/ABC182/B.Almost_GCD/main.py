import sys

n = int(input())
a = list(map(int, input().split()))

temp = 0
for i in range(2, max(a) + 1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count > temp:
        temp = count
        ans = i
print(ans)

