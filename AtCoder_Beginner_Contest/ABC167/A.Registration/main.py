s = input()
t = input()

if len(s) <= 10 and t[:-1] == s:
    print("Yes")
else:
    print("No")
