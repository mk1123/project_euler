"""
Project Euler Problem 73
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d 10,000?
"""

from math import gcd, ceil, floor

lower = 1 / 3
upper = 1 / 2

total_sum = 0

for i in range(4, 12001):
    lower_temp_num = ceil(i * lower)
    upper_temp_num = floor(i * upper)
    for j in range(lower_temp_num, upper_temp_num + 1):
        if gcd(i, j) == 1:
            total_sum += 1

print(total_sum)
