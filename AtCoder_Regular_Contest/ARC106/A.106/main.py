import sys
n = int(input())

a = 1
b = 1

if n % 2 == 1:
    print("-1")
    sys.exit()

for i in range(1, 40 + 1):
    for j in range(1, 26 + 1):
        temp = 3 ** i + 5 ** j
        if temp == n:
            print("{} {}".format(i, j))
            sys.exit()
        elif temp > n:
            break
print("-1")