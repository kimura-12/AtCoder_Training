n, s = input().split()
n = int(n)

a_ = []
t_ = []
c_ = []
g_ = []

for i in range(n):
    T = s[:i+1]
    a_.append(T.count("A"))
    t_.append(T.count("T"))
    c_.append(T.count("C"))
    g_.append(T.count("G"))

l = 2
ans = 0
while l <= n:
    for i in range(n):

        local = i
        if local + l > n:
            break
        if local != 0:
          a = a_[local + l-1] - a_[local-1]
          t = t_[local + l-1] - t_[local-1]
          c = c_[local + l-1] - c_[local-1]
          g = g_[local + l-1] - g_[local-1]
        else:
          a = a_[local + l-1] 
          t = t_[local + l-1]
          c = c_[local + l-1] 
          g = g_[local + l-1]
        
        if a == t and c == g:
            ans += 1
    l += 2
print(ans)