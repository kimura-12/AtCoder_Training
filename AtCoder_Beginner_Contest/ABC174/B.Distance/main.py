n, d = map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

count = 0
for i in range(n):
  if (x[i] ** 2 + y[i] ** 2) ** 0.5 <= d:
    count += 1
print(count)