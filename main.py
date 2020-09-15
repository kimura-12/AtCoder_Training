N = int(input())
A = list(map(int, input().split()))

flag = 1
max_count = 0
while flag == 1:
  count = 0
  for i in range(N):
    if A[i] % 2 == 0:
      count += 1
    A[i] = A[i] / 2
  if count == N:
    max_count += 1
  else:
    flag = 0

print(max_count)