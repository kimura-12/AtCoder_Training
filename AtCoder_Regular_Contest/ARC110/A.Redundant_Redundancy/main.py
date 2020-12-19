import sys
import itertools
import math
from functools import reduce

# a = int(input())
# a, b = map(int, input().split())
# a = list(map(int, input().split()))
n = int(input())

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


lcm = lcm_list(list(range(2, n + 1)))
print(lcm + 1)