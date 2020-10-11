n = int(input())
p = list(map(int, input().split()))
buf = [0] * 30 ** 5
ans = 0

for i in range(n):
    buf[p[i]] = 1
    while buf[ans] == 1:
        ans += 1
    print(ans)    
