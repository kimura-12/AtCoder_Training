n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a,b = [list(i) for i in zip(*ab)]

ans="Yes"
for i in range(n):
    for j in range(n):
        if min(a[j], b[j]) < 0 : continue
        for k in range(n):
            if a[j]<a[k]<b[j]>b[j]-a[j]!=b[k]-a[k]<b[k]>0 : ans="No"
            if b[j]>a[k]>a[j]>0>d : 