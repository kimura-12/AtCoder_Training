import queue

k = int(input())

q = queue.Queue()

for i in range(1, 10):
    q.put(i)

c = 1
while 1:
    x = q.get()
    if c == k:
        print(x)
        break
    if x % 10 != 0:
        q.put(10 * x + (x % 10) - 1)
    q.put(10 * x + (x % 10))
    if x % 10 != 9:
        q.put(10 * x + (x % 10) + 1)
    c += 1

