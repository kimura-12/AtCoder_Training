N = int(input())
mochi = [int(input()) for _ in range(N)]
mochi.sort(reverse=True)

count = 1
for i in range(N - 1):
  if mochi[i] > mochi[i + 1]:
    count += 1
    
print(count)