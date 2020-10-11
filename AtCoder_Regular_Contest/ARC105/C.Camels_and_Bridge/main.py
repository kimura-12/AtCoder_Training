import sys
n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [map(int, input().split()) for _ in range(m)]
l, v = [list(i) for i in zip(*lv)]

if min(w) > min(v):
    print("-1")
    sys.exit()

