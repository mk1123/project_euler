"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
from utils import all_factors


from itertools import permutations

total_sum = 0

for num_tuple in permutations(range(1, 10), 4):

    for factor, other_factor in all_factors(int("".join(map(str, num_tuple)))):
        if set(num_tuple) | set(map(int, set(str(factor)))) | set(
            map(int, set(str(other_factor)))
        ) == set(range(1, 10)):
            total_sum += int("".join(map(str, num_tuple)))
            break

print(total_sum)
