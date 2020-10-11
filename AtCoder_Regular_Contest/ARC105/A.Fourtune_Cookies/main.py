import sys
abcd = list(map(int, input().split()))

total = sum(abcd)
eat = 0
for i in range(2 ** 4):
    eat = 0
    for j in range(4):
        if ((i >> j) & 1):
            eat += abcd[j]
    if eat == total - eat:
        print("Yes")
        sys.exit()
print("No")
