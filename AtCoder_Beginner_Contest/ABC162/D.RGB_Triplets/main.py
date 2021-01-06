n = int(input())
s = input()

ans = 0

R = s.count("R")
G = s.count("G")
B = s.count("B")

ans = R * G * B

for i in range(1, n - 1):
    for j in range(i + 1, n):
        k = 2 * j - i
        if k > n:
            continue
        if s[i-1] == s[j-1] or s[i-1] == s[k-1] or s[j-1] == s[k-1]:
            continue
        ans -= 1
print(ans)