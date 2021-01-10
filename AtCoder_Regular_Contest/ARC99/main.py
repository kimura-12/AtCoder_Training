n, k = map(int, input().split())
a = list(map(int, input().split()))


l = n - a.count(min(a)) + 1
if (l - k) % (k - 1) == 0:
    print((l - k) // (k-1) + 1)
else:
    print((l - k) // (k-1) + 2)