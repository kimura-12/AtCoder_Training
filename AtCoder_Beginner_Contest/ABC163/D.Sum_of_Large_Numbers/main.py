import itertools
import sys
n, k = map(int, input().split())
if n + 1 == k:
    print(1)
    sys.exit()
mod = 10 ** 9 + 7
ans = 0
for i in range(k, n+2):
    min_ = (i-1) * (i) // 2
    max_ = (i) * (n-i+1 + n) // 2
    ans += (max_ -min_ + 1) % mod
print(ans % mod)