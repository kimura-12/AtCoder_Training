import sys

h, w = map(int, input().split())
a = [list(map(int, input().split())) for l in range(h)]

ans = 0
m = 101
for i in range(h):
    for j in range(w):
       m = min(m, a[i][j])

for i in range(h):
    for j in range(w):
       ans += a[i][j] - m 

print(ans)