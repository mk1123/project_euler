"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""
from collections import defaultdict
import itertools as it

cubes = map(lambda x: x ** 3, it.count())

same_digits = defaultdict(list)

for cube in cubes:
    sorted_str_cube = "".join(sorted(str(cube)))
    same_digits[sorted_str_cube].append(cube)
    if len(same_digits[sorted_str_cube]) == 5:
        print(same_digits[sorted_str_cube][0])
        break
