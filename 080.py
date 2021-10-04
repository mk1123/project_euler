"""
Project Euler Problem 80
========================

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum
of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots.
"""

"""
Compute the square root of an irrational number, digit by digit.
"""

from math import sqrt
from typing import List
import gmpy2
from utils import digital_sum


def integer_sqrt(n: int) -> int:
    assert n >= 0, "sqrt works for only non-negative inputs"
    if n < 2:
        return n

    # Recursive call:
    small_cand = integer_sqrt(n >> 2) << 1
    large_cand = small_cand + 1
    if large_cand * large_cand > n:
        return small_cand
    else:
        return large_cand


total_sum = 0
for i in range(1, 101):
    if not gmpy2.is_square(i):
        total_sum += digital_sum(integer_sqrt(i * 10 ** (2 * 99)))


print(total_sum)
