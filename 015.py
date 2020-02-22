"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


print(nCr(40, 20))

