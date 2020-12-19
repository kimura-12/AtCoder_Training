import sys

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0
s = sum(a)
for i in range(n-1):
    s = s - a[i]
    ans += s - a[i] * (n - i - 1)
    

print(ans)
