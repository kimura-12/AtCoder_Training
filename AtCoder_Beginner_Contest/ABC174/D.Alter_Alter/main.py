n = int(input())
c = input()
r_num = 0
count = 0
for i in c:
  if i == "R":
    r_num += 1

for i in range(r_num):
  if c[i] == "W":
    for j in reversed(range(len(c))):
      if c[j] == "R":
        c[i] == "R"
        c[j] == "W"
        count += 1
        break
print(count)