a, b, n = map(int, input().split())

ans = 0
x = min(b-1, n)
ans = max(ans, (a * x) // b - a * (x//b))
print(ans)
