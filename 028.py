"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

top_right = lambda n: sum([n ** 2 for n in range(3, n + 1, 2)])
top_left = lambda n: sum([n ** 2 + n + 1 for n in range(2, n, 2)])
bottom_left = lambda n: sum([n ** 2 + 1 for n in range(2, n, 2)])
bottom_right = lambda n: sum([n ** 2 + n + 1 for n in range(1, n - 1, 2)])

print(1 + bottom_left(1001) + bottom_right(1001) + top_left(1001) + top_right(1001))
