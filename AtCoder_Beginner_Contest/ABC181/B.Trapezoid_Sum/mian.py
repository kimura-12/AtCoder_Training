n = int(input())

ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

ans = 0
for i in range(n):
    ans += (b[i] - a[i] + 1) * (b[i] + a[i]) // 2

print(ans)

