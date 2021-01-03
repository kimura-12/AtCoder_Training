n = int(input())

xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

ans = 0
for i in range(n-1):
    for j in range(i + 1, n):
        tilt = (y[i] - y[j]) / (x[i] - x[j])
        if tilt >= -1 and tilt <= 1:
            ans += 1
            print(i, j)

print(ans)
