N = int(input())
D12 = [map(int, input().split()) for _ in range(N)]
D1, D2 = [list(i) for i in zip(*D12)]
    
count = 0
flag = 0
for i in range(N):
    
    if D1[i] == D2[i]:
        count += 1
        if count == 3:
            flag = 1
    else:
        count = 0
    
if flag == 1:
    print("Yes")
else:
    print("No")