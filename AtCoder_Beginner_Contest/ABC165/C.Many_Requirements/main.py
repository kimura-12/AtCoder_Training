n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

ans = 0
for i in range(1, m + 1):
    A = [i] * n
    for j in range(1, n):
        for k in range(m):
            A[-j] += 1
            temp = 0
            for l in range(q):
                if A[abcd[l][1]] - A[abcd[l][0]] == abcd[l][2]:
                    temp += abcd[l][3]
            ans = max(ans, temp)
print(ans)
