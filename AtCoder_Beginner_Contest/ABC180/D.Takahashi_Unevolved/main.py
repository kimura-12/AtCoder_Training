x, y, a, b = map(int, input().split())

strong = x
pre = x
exp = 0
flag = 0
if a >= b:
    if (y-x) % b == 0:
      print((y-x) // b -1)
    else:
      print((y-x) // b)
else:
    while 1:
        strong = min(strong * a, strong + b)
        if strong >= y:
            break
        if strong - pre == b:
            flag = 1
            break
        exp += 1
        pre = strong
    if flag == 0:
      print(exp)
    else:
      if (y-strong) % b == 0:
        print((y-strong) // b + exp)
      else:
        print((y-strong) // b + exp + 1)