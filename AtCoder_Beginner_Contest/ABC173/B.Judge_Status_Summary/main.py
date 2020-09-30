n = int(input())
s = [input() for _ in range(n)]

ac = 0
wa = 0
tle = 0

for i in s:
  if i == "AC":
    ac += 1
  elif i == "WA":
    wa += 1
  elif i == "TLE":
    tle += 1
print("AC x {}".format(ac))
print("WA x {}".format(wa))
print("TLE x {}".format(tle))
print("RE x {}".format(n - (ac + wa + tle)))