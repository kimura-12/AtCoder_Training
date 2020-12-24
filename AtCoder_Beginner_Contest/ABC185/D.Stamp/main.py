import sys

n, m = map(int, input().split())
if m == 0:
    print(1)
    sys.exit()
a = list(map(int, input().split()))
a.sort()

dif = []
for i in range(len(a)-1):
    if a[i + 1] - a[i] > 1:
        dif.append(a[i + 1] - a[i] - 1)
if a[0] != 1:
    dif.append(a[0] - 1)
if a[-1] != n:
    dif.append(n - a[-1])
if len(dif) == 0:
    print(0)
    sys.exit()
    
mi = min(dif)
ans = 0
for i in range(len(dif)):
    ans += dif[i] // mi
    if dif[i] % mi != 0:
        ans += 1

print(ans)