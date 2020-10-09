n, m = map(int, input().split())
h = list(map(int, input().split()))

maxh = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    maxh[a-1] = max(maxh[a-1], h[b-1])
    maxh[b-1] = max(maxh[b-1], h[a-1])

ans = 0
for i in range(n):
  if h[i] > maxh[i]:
    ans += 1
print(ans)