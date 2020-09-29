k = int(input())

sev = 7
count = 0

while count < k:
  count += 1
  if sev % k == 0:
    print(count)
    break
  sev = (sev * 10 + 7) % k
else:
  print(-1)