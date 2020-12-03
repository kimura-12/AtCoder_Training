a,b,c = map(int,input().split())
m = 100
dp = [[[0] * (m+1) for i in range(m+1)] for j in range(m+1)]

for x in range(m-1, -1, -1):
  for y in range(m-1, -1, -1):
    for z in range(m-1, -1, -1):
      if x+y+z == 0:
        continue
      dp[x][y][z] = (dp[x+1][y][z] * x +
                     dp[x][y+1][z] * y +
                     dp[x][y][z+1] * z) / (x+y+z) + 1
ans = dp[a][b][c]
print(ans)