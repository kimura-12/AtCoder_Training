a, b, c, d = map(int, input().split())

count = 0
while a > 0 and c > 0:
    if count % 2 == 0:
        c -= b
    else:
        a -= d
    count += 1

print("Yes") if count % 2 != 0 else print("No") 