N, Y = map(int, input().split())

flag = 0
for i in range(N + 1):
  for j in range(N + 1 - i):
    if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
      x = i
      y = j
      z = N - i - j
      flag = 1
      break
  else:
      continue
  break


if flag:
  print("{} {} {}".format(x,y,z))
else:
  print("-1 -1 -1")