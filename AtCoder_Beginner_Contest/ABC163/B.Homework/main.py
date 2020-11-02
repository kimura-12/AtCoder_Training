n, m = map(int, input().split())
a = list(map(int, input().split()))

free = n - sum(a)
print(free) if free >= 0 else print("-1")