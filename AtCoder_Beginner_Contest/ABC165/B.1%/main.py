import math
x = int(input())

deposit = 100
year = 0
while deposit < x:
    deposit += deposit // 100
    year += 1
print(year)