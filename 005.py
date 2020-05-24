"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math
from collections import Counter
from utils import prime_factorization


def problem(n):
    global_counter = Counter()
    for i in range(2, n + 1):
        factors = prime_factorization(i)
        for num in factors:
            global_counter[num] = max(global_counter[num], factors[num])
    base = 1
    for num in global_counter:
        base *= num ** global_counter[num]
    return base


print(problem(20))
