import sys
import queue
import math

n ,m = map(int, input().split())

print(pow(10, n, m ** 2) // m % m)
