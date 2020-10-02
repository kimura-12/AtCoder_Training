n, k = map(int, input().split())
x = list(map(int, input().split()))

time = float("inf")
for i in range(n - k + 1):
  l = x[i]
  r = x[i + k - 1]
  time1 = abs(l) + abs(r - l)
  time2 = abs(r) + abs(r - l)
      
  time = min(time, time1, time2)
print(time)