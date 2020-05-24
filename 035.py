"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils import is_prime

circulars = [None] * 1000001
total = 0

for i in range(1, len(circulars)):
    if circulars[i]:
        continue
    i_str = str(i)
    rotations = [int(i_str[j:] + i_str[:j]) for j in range(len(i_str))]
    valid = all([is_prime(x) for x in rotations])
    if valid:
        for prime in set(rotations):
            circulars[prime] = True
            total += 1

print(total)
