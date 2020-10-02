n, k = map(int, input().split())

A = [0] * k
for i in range(1, n+1):
  A[i % k] += 1

count = 0
for a in range(k):
  b = (k - a)%k
  c = (k - a)%k
  if (b + c) % k == 0:
    count += A[a]*A[b]*A[c]
    
print(count)