import sys
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c_ = []
d_ = []
par = list(range(n))
for i in range(m):
    c, d = map(int, input().split())
    m = min(c-1, d-1)
    par[c-1] = m
    par[d-1] = m
    c_.append(c)
    d_.append(d)

for _ in range(100):
  for c, d in zip(c_, d_):
      m = min(par[c-1], par[d-1])
      par[c-1] = m
      par[d-1] = m

balance = [0] * n
for i,t in enumerate(par):
    balance[t] += b[i]-a[i]
allgood = all(b == 0 for b in balance)
 
if allgood:
    print('Yes')
else:
    print('No')