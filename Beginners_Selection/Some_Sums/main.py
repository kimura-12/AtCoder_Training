N, A, B = map(int, input().split())

all_sum = []
for i in range(1, N+1):
  sum_ = 0
  for j in str(i):
    sum_ += int(j)
  if sum_ >= A and sum_ <= B:
    all_sum.append(i)

print(sum(all_sum))