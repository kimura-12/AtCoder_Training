h, w, k = map(int, input().split())
c = [input() for _ in range(h)]
ans = 0

for bith in range(1<<h):
    for bitw in range(1<<w):
        black=0
        for he in range(h):
            for wi in range(w):
                if c[he][wi]=='#' and bith&(1<<he) and bitw&(1<<wi):
                    black+=1
        if black==k:
            ans+=1
print(ans)