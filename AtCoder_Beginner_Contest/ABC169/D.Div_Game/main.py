import sys
n = int(input())
if n == 1:
  print("0")
  sys.exit()
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

fact = factorization(n)
ans = 0
for _, i in fact:
    temp = i
    j = 1
    while temp >= j:
        temp -= j
        j += 1
        ans += 1
print(ans)
