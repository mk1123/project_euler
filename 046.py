"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
import itertools as it
import math
from utils import gen_composites, is_prime

for odd_composite in filter(lambda x: x % 2, it.islice(gen_composites(), 1, None)):
    valid = any(
        map(
            lambda x: is_prime(odd_composite - 2 * x ** 2),
            range(1, int(math.sqrt(odd_composite)) + 1),
        )
    )

    if not valid:
        print(odd_composite)
        break
