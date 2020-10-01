n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A, B = [0], [0]
for i in range(n):
  A.append(a[i] + A[i])
for i in range(m):
  B.append(b[i] + B[i])

ans = 0
j = m
for i in range(n + 1):
  if A[i] > k:
    break
  while B[j] + A[i] > k:
    j -= 1
  ans = max(ans, i + j)
print(ans)