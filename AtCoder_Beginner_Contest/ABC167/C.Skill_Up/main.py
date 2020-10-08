n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

ans = float("inf")
for i in range(2 ** n):
    skill = [0] * m
    money = 0

    for j in range(n):
        if i >> j & 1:
            money += ca[j][0]
            for k in range(m):
                skill[k] += ca[j][k + 1]
    if all(l >= x for l in skill):
        ans = min(ans, money)
    
print(ans if ans != float("inf") else -1)