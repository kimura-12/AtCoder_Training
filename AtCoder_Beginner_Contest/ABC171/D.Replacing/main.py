n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [map(int, input().split()) for _ in range(q)]
b, c = [list(i) for i in zip(*bc)]

nums = [0]*(max(max(a), max(c))+1)
for i in a:
  nums[i] += 1
Sum = sum(a)

for k in range(q):
  B, C = b[k], c[k]
  nums[C] += nums[B]
  Sum -= nums[B] * (B - C)
  nums[b[k]] = 0
  print(Sum)
