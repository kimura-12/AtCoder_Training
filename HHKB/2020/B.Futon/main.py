h, w = map(int, input().split())

M = ["#"+input()+"#" for l in range(h)]
M.insert(0,"#"*(w+2))
M.append("#"*(w+2))

ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if M[i][j] == ".":
          if M[i][j - 1] == ".":
            ans += 1
          if M[i - 1][j] == ".":
            ans += 1
print(ans)