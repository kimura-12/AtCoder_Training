n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        if a[i] % a[j] != 0:
            count += 1
print(count)