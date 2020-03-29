"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

curr_max = 918273645

from itertools import permutations
from functools import reduce


def is_pandigital(n):
    return len(set(str(n))) == len(str(n)) and "0" not in str(n)


for largest_3_digit in list(permutations(range(1, 10), 3)):
    num_str = "9" + "".join(map(str, largest_3_digit))
    double_num = str(2 * int(num_str))
    cum_num = int(num_str + double_num)
    if is_pandigital(cum_num):
        curr_max = max(cum_num, curr_max)

print(curr_max)
