n, m, t = map(int, input().split())

ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]

tn = n
dif = 0
flag = 0
for i in range(m):
    tn -= a[i] - dif
    if tn <= 0:
        flag = 1
    tn += b[i] - a[i]
    if tn > n:
      tn = n
    dif = b[i]
tn -= t - b[-1]
if tn <= 0:
    flag = 1
print("Yes") if flag == 0 else print("No")