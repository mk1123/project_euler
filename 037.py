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


primes = set()

start_double_digit_primes = {23, 25, 29, 31, 35, 37, 53, 59, 71, 73, 79}
end_double_digit_primes = {}

for prime in gen_primes():
    primes.add(prime)
