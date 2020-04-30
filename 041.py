"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# Can only be 7 or 4 digits, and can't end with an even number

from itertools import permutations

from utils import is_prime

tuple_to_int = lambda tuple_: int("".join(map(str, tuple_)))

# first check 7 digits
exists_at_7_digits = False


for tuple_ in reversed(list(permutations(range(1, 8), 7))):
    if tuple_[-1] % 2:
        curr_num = tuple_to_int(tuple_)
        if is_prime(curr_num):
            largest = curr_num
            exists_at_7_digits = True
            break

if exists_at_7_digits:
    print(largest)
else:
    # have to go to the 4 digit case
    for tuple_ in reversed(list(permutations(range(1, 5), 4))):
        if tuple_[-1] % 2:
            curr_num = tuple_to_int(tuple_)
            if is_prime(curr_num):
                largest = curr_num
                break
    print(largest)
