from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

ans = 0

for i in combinations_with_replacement(range(1, m+1), n):
    temp = 0
    for l in range(q):
        if i[abcd[l][1]-1] - i[abcd[l][0]-1] == abcd[l][2]:
            temp += abcd[l][3]
    ans = max(ans, temp)
print(ans)