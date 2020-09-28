import collections
n = int(input())
v = list(map(int, input().split()))

count = 0
v1 = []
v2 = []
while count < n:
  v1.append(v[count])
  v2.append(v[count + 1])
  count += 2

c1 = collections.Counter(v1)
c2 = collections.Counter(v2)

num1, count1 = c1.most_common()[0]
num2, count2 = c2.most_common()[0]

if num1 != num2:
  min_count = (n // 2 - count1) + (n // 2 - count2)
elif count1 == count2 and count1 == n // 2:
  min_count = (n // 2)
else:
  if len(c1.most_common()) > 1 and len(c2.most_common()) > 1:
    num3, count3 = c1.most_common()[1]
    num4, count4 = c2.most_common()[1]
    a = (n // 2 - count1) + (n // 2 -count4)
    b = (n // 2 - count2) + (n // 2 -count3)
    min_count = min(a,b)
  else:
    if count1 > count2:
      num2, count2 = c2.most_common()[1]
      min_count = (n // 2 - count1) + (n // 2 - count2)
    else:
      num1, count1 = c1.most_common()[1]
      min_count = (n // 2 - count2) + (n // 2 - count1)
print(min_count)