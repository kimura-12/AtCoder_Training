import math
a, b, h, m = map(float, input().split())

h_ = 30. * h + 30. * m / 60.
m_ = 6. * m
rad = math.radians(abs(h_ - m_))


dist = a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)

print(math.sqrt(dist))