import sys

n = int(input())

if n % 3 == 0:
    print(0)
    sys.exit()

l = [x for x in list(str(n))]

max_num = 0
for i in range(2 ** len(l)):
    temp = ""
    for j in range(len(l)):
        if ((i >> j) & 1):
            temp += l[j]
    if temp == "":
      continue
    if int(temp) % 3 == 0:
        max_num = max(len(temp), max_num)
if max_num == 0:
  print("-1")
else:
  print(len(l) - max_num)
        


