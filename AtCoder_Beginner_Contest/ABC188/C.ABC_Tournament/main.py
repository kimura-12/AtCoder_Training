import queue
import sys
n = int(input())
a = list(map(int, input().split()))

q = queue.Queue()

for i in range(2 ** n):
    q.put((i + 1, a[i]))

while not q.empty():
    low = q.get()
    hig = q.get()
    if len(q.queue) == 0:
        if low[1] > hig[1]:
            print(hig[0])
            sys.exit()
        else:
            print(low[0])
            sys.exit()
    if low[1] > hig[1]:
        q.put(low)
    else:
        q.put(hig)