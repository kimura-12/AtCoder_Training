import itertools
import sys
s = input()
if len(s) > 100:
  p = list(set(s))
else:
  p = s

count = 0
for i in s:
  if i == "8":
    count += 1
if count > 2:
  print("Yes")
  sys.exit()
  
if len(p) < 3:
  a = list(itertools.permutations(p))
  for i in range(len(a)):
    temp = "".join(a[i])
    if int(temp) % 8 == 0:
      print("Yes")
      sys.exit()

  print("No")
else:
  a = list(itertools.permutations(p, 3))
  for i in range(len(a)):
    temp = "".join(a[i])
    if int(temp) % 8 == 0:
      print("Yes")
      sys.exit()
  print("No")