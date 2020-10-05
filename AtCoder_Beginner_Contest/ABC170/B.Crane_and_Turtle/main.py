import sys
x, y = map(int, input().split())

for i in range(0, 101):
  for j in range(0, 101):
    if i + j == x and 2 * i + 4 * j == y:
      print("Yes")
      sys.exit()
print("No")