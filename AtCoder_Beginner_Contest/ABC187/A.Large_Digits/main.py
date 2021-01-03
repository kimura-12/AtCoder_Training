a, b = input().split()

a_ = 0
b_ = 0
for i in a:
    a_ += int(i)

for i in b:
    b_ += int(i)

print(max(a_, b_))


