"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import gen_primes
from math import log10


def valid_property(n):
    copy_n = n
    while copy_n:
        if copy_n not in primes:
            break
        copy_n //= 10
    if copy_n > 0:
        return False

    digits = int(log10(n))
    while n:
        if n not in primes:
            break
        n %= 10 ** digits
        digits -= 1
    return n == 0


primes = set()

counter = 0
sum_ = 0

for prime in gen_primes():
    primes.add(prime)
    if prime > 10 and valid_property(prime):
        counter += 1
        sum_ += prime
        if counter == 11:
            break

print(sum_)
