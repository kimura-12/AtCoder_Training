from collections import deque

h, w = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())

#ワープで迷路外に出ないようにする
M = ["##"+input()+"##" for l in range(h)]
for i in range(2):
    M.insert(0,"#"*(w+4))
    M.append("#"*(w+4))

#道であれば-1を壁なら-2で初期化
C=[[-1 if M[j][i]=="." else -2 for i in range(w+4)] for j in range(h+4)]

#歩いて到達できれば0を
C[Ch + 1][Cw + 1] = 0

QA,QB=deque(),deque()
QA.append((Ch + 1, Cw + 1, 0))

#魔法での移動範囲
W=[[i,j] for i in range(-2,3) for j in range(-2,3) if abs(i)+abs(j)>1]

#歩いて行ける範囲を先に探索
while QA:
  h,w,c=QA.popleft()
  QB.append((h,w,c))
  
  for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
    dh, dw = h + i, w + j
    if C[dh][dw] == -1:
      C[dh][dw] = c
      QA.appendleft((dh, dw, c))
  
  if QA:
    continue
  
  #歩いて行ける範囲がなくなれば魔法で新たな場所に行く
  #そしてまた歩いて行ける範囲を探す
  while QB:
    h,w,c = QB.popleft()
    for i,j in W:
      dh, dw = h + i, w + j
      if C[dh][dw] == -1:
        C[dh][dw] = c + 1
        QA.append((dh, dw, c + 1))
print(C[Dh + 1][Dw + 1])
    