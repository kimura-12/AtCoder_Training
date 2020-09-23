n = list(map(int, input()))

SUM = sum(n)
if SUM % 9 == 0:
  print('Yes')
else:
  print("No")