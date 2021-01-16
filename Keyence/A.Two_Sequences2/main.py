n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_ = []
for i in range(n):
    if i == 0:
        a_.append(a[i])
    else:
        a_.append(max(a_[-1], a[i]))


c = []
c.append(a[0] * b[0])
temp = 0
for i in range(1, n):
    c.append(max(c[-1], a_[i] * b[i]))

for i in c:
    print(i)
