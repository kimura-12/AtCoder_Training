s = input()

count = 0
for i in range(len(s)):
    for j in range(i + 4, len(s) - 4):
        if int(s[i:j + 1]) % 2019 == 0:
            count += 1 

print(count)