n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

c = [0] * (max(a) + 1)

for i in range(n):
    c[a[i]] += 1

ans = 0
m = float("inf")
for i in range(max(a) + 1):
    if c[i] == 0:
        break
    m = min(m, c[i])
    ans += min(m, k)

print(ans)