N = int(input())
txy = [map(int, input().split()) for _ in range(N)]
t, x, y = [list(i) for i in zip(*txy)]
t.insert(0, 0)
x.insert(0, 0)
y.insert(0, 0)

flag = 1
for i in range(1, N + 1):
  if t[i] - t[i - 1] < abs(x[i] -x[i - 1]) + abs(y[i] - y[i - 1]):
    flag = 0
  if not t[i] % 2 == (x[i] + y[i]) % 2:
    flag = 0
if flag:
  print("Yes")
else:
  print("No")