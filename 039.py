"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""
from math import gcd


def primitive_generators():
    denom = 2
    while True:
        start = 2 if denom % 2 else 1
        for numerator in range(start, denom, 2):
            if gcd(numerator, denom) == 1:
                yield (numerator, denom)

        denom += 1


m = n = 0
perimeters = [0] * 1000
pyth = primitive_generators()

while (m + n) < 32:
    m, n = next(pyth)
    per_sum = 2 * m ** 2 + 2 * m * n
    for i in range(per_sum, 1000, per_sum):
        perimeters[i] += 1

print(max(range(len(perimeters)), key=lambda x: perimeters[x]))
