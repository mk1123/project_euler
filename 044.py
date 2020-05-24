"""
Project Euler Problem 44
========================

Pentagonal numbers are generated by the formula, P[n]=n(3n-1)/2. The first
ten pentagonal numbers are:

               1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
and difference is pentagonal and D = |P[k] - P[j]| is minimised; what is
the value of D?
"""
import itertools as it
import math
import sys
from typing import Generator, Iterator, List

from utils import pentagonal_values_generator, is_pentagonal

previous_vals = list()  # type: List[int]

for index, curr_value in enumerate(pentagonal_values_generator()):
    for prev_value in previous_vals:
        sum_ = curr_value + prev_value
        diff_ = curr_value - prev_value
        if is_pentagonal(sum_) and is_pentagonal(diff_):
            print(diff_)
            sys.exit()
    previous_vals.append(curr_value)
