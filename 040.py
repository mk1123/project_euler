"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""
from itertools import count
from math import ceil, log

prod = 1
interesting_nums = {1, 10, 100, 1000, 10000, 100000, 1000000}
curr_digit_place = 0
num_generator = count(start=1)
num_to_list_of_digits = lambda n: [int(i) for i in str(n)]

while curr_digit_place <= 1000000:
    next_num = next(num_generator)
    for digit in num_to_list_of_digits(next_num):
        curr_digit_place += 1
        if curr_digit_place in interesting_nums:
            prod *= digit

print(prod)
