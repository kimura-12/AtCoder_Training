n, k = map(int, input().split())

t = n % k

ans = min(t, abs(t-k))
print(ans)