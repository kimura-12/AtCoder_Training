import sys
x = int(input())

for i in range(-118, 119):
    for j in range(-119, 118):
        if i ** 5 - j ** 5 == x:
            print(i, j)
            sys.exit()