import sys

n = int(input())

ans = 0
for i in range(1, n + 1):
    flag = 0
    oc = oct(i)
    for j in str(i):
        if j == "7":
            flag = 1
            break
    
    if flag == 1:
        continue

    for j in str(oc):
        if j == "7":
            flag = 1
            break
    
    if flag == 1:
        continue

    ans += 1

print(ans)
