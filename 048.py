"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from utils import mod_exp

modulus = 10 ** 10

print(sum(map(lambda x: mod_exp(x, x, modulus), range(1, 1001))) % modulus)



