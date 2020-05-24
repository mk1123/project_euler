"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""
import itertools as it

from utils import fast_prime_factorization

for first_num in it.count(start=2):
    if all(
        map(
            lambda n: len(set(fast_prime_factorization(n))) == 4,
            range(first_num, first_num + 4),
        )
    ):
        print(first_num)
        break
