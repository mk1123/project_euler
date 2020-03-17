"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from itertools import product
from fractions import Fraction

numerator = 1
denominator = 1

for a_tens, a_ones in product(range(1, 10), repeat=2):
    for b_tens, b_ones in product(range(1, 10), repeat=2):
        a_val = a_tens * 10 + a_ones
        b_val = b_tens * 10 + b_ones
        if a_val / b_val < 1:
            if a_tens == b_ones:
                if a_ones / b_tens == a_val / b_val:
                    numerator *= a_ones
                    denominator *= b_tens
            elif a_ones == b_tens:
                if a_tens / b_ones == a_val / b_val:
                    numerator *= a_tens
                    denominator *= b_ones

print(Fraction(numerator, denominator).denominator)
