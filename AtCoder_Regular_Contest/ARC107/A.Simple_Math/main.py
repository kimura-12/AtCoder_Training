a,b,c = map(int, input().split())

ans = 0
mod = 998244353

sum_a = int(a * (a + 1))
sum_b = int(b * (b + 1))
sum_c = int(c * (c + 1))

ans = int(sum_a * sum_b * sum_c) // 8
print(ans % mod)