import itertools

n, k = map(int, input().split())
t = list(list(map(int, input().split())) for _ in range(n))

if n == 2:
    a = []
    a .append((2,))
else:
    a = list(itertools.permutations(range(2, n + 1)))

temp = [0] * len(a)
for i in range(len(a)):
    
    temp[i] += t[0][a[i][0]-1]
    for j in range(len(a[i])-1):            
        temp[i] += t[a[i][j]-1][a[i][j+1]-1]
    temp[i] += t[a[i][n-2]-1][0]

ans = 0
for i in temp:
    if i == k:
        ans += 1
        
print(ans)
