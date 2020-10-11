import sys
n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [map(int, input().split()) for _ in range(m)]
l, v = [list(i) for i in zip(*lv)]

if min(w) > min(v):
    print("-1")
    sys.exit()

w.sort()
ans = 0
for i in range(m):
    count = 0
    temp = 0
    for j in range(n):
        temp += w[j]
        if temp <= v[i]:
            count += 1
        else:
            break
    ans = max(ans, l[i] * (m -count + 1))
print(ans)
            
