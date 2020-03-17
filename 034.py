"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from itertools import product, chain
from math import factorial

digits = {5: [3], 6: (3, 4), 7: (4, 5), 8: (5, 6), 9: (6, 7)}


def nums_with_max_digit(n):
    return_set = set()
    for first_digit in range(1, n + 1):
        for repeat_num in digits[n]:
            for rest_of_digits_tuple in product(range(n + 1), repeat=repeat_num - 1):
                val = int(str(first_digit) + "".join(map(str, rest_of_digits_tuple)))
                if (
                    factorial(first_digit) + sum(map(factorial, rest_of_digits_tuple))
                    == val
                ):
                    return_set.add(val)

    return return_set


print(
    sum(
        {
            num
            for curr_set in [nums_with_max_digit(n) for n in digits]
            for num in curr_set
        }
    )
)
