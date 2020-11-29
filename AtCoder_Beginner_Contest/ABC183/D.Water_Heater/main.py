n, w = map(int, input().split())

hw = [0] * (2 * 10 ** 5 + 1)

for i in range(n):
    s, t, p = map(int, input().split())
    hw[s] += p
    hw[t] -= p

ans = [0] * (2 * 10 ** 5 + 1)
for j in range(len(hw)-1):
  ans[j + 1] = ans[j] + hw[j]

if max(ans) > w:
    print("No")
else:
    print("Yes")
