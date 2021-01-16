n, C = map(int, input().split())

abc = [map(int, input().split()) for _ in range(n)]
a, b, c = [list(i) for i in zip(*abc)]

cost = [0] * (max(b) + 1)

for i in range(n):
    for j in range(a[i], b[i] + 1):
        cost[j] += c[i]

for i in range(max(b) + 1):
    cost[i] = min(cost[i], C)
print(sum(cost))