n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

c = []
for i in range(n):
    c.append(a[i] * 2 + b[i])


a = [i for _, i in sorted(zip(c, a), reverse=True)]
c.sort(reverse=True)

aoki = sum(a)
taka = 0
ans = 0

while aoki >= taka:
    taka += c[ans] - a[ans]
    aoki -= a[ans]
    ans += 1
print(ans)
    
