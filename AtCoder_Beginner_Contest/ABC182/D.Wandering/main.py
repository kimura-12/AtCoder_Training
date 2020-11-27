import sys

n = int(input())
a = list(map(int, input().split()))


p = [0] * (n + 1)
sum_list = [0] * (n + 1)
temp = 0
for i in range(n):
    sum_list[i + 1] = sum_list[i] + a[i]
    temp = max(sum_list[i + 1], temp)
    p[i + 1] = temp

ans = 0
x = 0
for i in range(n):
    ans = max(ans, x + p[i + 1])
    x += sum_list[i + 1]
print(ans)

