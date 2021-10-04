"""
Project Euler Problem 85
========================

By counting carefully it can be seen that a rectangular grid measuring 3
by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest solution.
"""

import utils
from math import sqrt


def num_rectangles(n: int, m: int) -> int:
    return n * (n + 1) * m * (m + 1) // 4


def get_n_from_m(m: int) -> int:
    return round((-1 + sqrt(1 + (32000000 / (m ** 2 + m)))) / 2)


def get_diff_from_2_million(num: int) -> int:
    return abs(2000000 - num)


min_diff = float("inf")
closest_area = 0
j = float("inf")
i = 1

while i < j:
    j = get_n_from_m(i)
    curr_rectangles = num_rectangles(i, j)
    diff = get_diff_from_2_million(curr_rectangles)
    if diff < min_diff:
        min_diff = diff
        closest_area = i * j
    i += 1

print(closest_area)
