import sys
n = int(input())

xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

for i in range(n):
    for j in range(n):
        if i == j:
          continue
        if x[j] == x[i]:
          for k in range(n):
            if i == j or j == k or i == k:
              pass
            else:
              if x[j] == x[k]:
                print("Yes")
                sys.exit()
          continue
        else:
          a = (y[j] - y[i]) / (x[j] - x[i])
        for k in range(n):
            if k == i or k == j:
              continue
            if x[k] == x[i]:
              if x[k] == x[i] == x[j]:
                print("Yes")
            elif (y[k] - y[i]) / (x[k] - x[i]) == a:
                print("Yes")
                sys.exit()

print("No")
