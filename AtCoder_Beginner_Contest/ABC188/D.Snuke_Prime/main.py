n, C = map(int, input().split())

abc = [map(int, input().split()) for _ in range(n)]
a, b, c = [list(i) for i in zip(*abc)]

