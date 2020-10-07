from collections import deque

n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a ,b = [list(i) for i in zip(*ab)]

ma = [[] for i in range(n + 1)]
for i in range(m):
  ma[a[i]].append(b[i])
  ma[b[i]].append(a[i])

r = [-1] * (n+1)
r[1] = 0
q = deque([])
q.append(1)

while q:
  x = q.popleft()
  
  for i in ma[x]:
    if r[i] == -1:
      r[i] = x
      q.append(i)

print("Yes")
for i in range(2,n+1):
    print(r[i])
