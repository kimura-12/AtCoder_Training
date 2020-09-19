N = int(input())

count = 0

for i in range(1, N):
  count += int(N / i)
  if N % i == 0:
    count -= 1
print(count)