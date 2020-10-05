from collections import Counter

x, n = map(int, input().split())
p = list(map(int, input().split()))

c = Counter(p)
for i in range(100):
    x1 = x + i
    x2 = x - i
    c1 = c[x1]
    c2 = c[x2]
    if c1 == 0 and c2 == 0:
        print(min(x1, x2))
        break
    if c1 == 0:
        print(x1)
        break
    elif c2 == 0:
        print(x2)
        break
        