n = int(input())

s = "abcdefghijklmnopqrstuvwxyz"

N = n
length = len(s)
ans = ""
while 1:
    x = N % length
    N -= x

    if x == 0:
        x = 26
        N -= x
    ans += s[x-1]

    if N == 0:
        break

    N //= length

print(ans[::-1])