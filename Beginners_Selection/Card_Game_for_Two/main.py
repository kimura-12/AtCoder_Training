N = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

Alice_points = 0
Bob_points = 0

for i in range(N):
  if i % 2 == 0:
    Alice_points += cards[i]
  else:
    Bob_points += cards[i]

print(Alice_points - Bob_points)