"""
Project Euler Problem 58
========================

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

                           37 36 35 34 33 32 31
                           38 17 16 15 14 13 30
                           39 18  5  4  3 12 29
                           40 19  6  1  2 11 28
                           41 20  7  8  9 10 27
                           42 21 22 23 24 25 26
                           43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

from utils import is_prime
from typing import Set

curr_diag_elems = {37, 17, 5, 1, 9, 25, 49, 43, 21, 7, 3, 13, 31}

num_diags = len(curr_diag_elems)
num_primes = 0
for num in curr_diag_elems:
    if is_prime(num):
        num_primes += 1

last_num = 49
curr_side_length = 9
while num_primes / num_diags >= 0.1:
    num_primes += sum(
        is_prime(last_num + (curr_side_length - 1) * x) for x in range(1, 5)
    )
    num_diags += 4
    last_num = curr_side_length ** 2
    curr_side_length += 2

print(curr_side_length - 2)
