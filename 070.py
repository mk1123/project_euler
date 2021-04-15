"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""

from utils import is_permutation, totientrange

totient_nums = totientrange(2, 10 ** 7)
lowest_ratio = float("inf")
optimal_n = 0

for idx, totient in enumerate(totient_nums):
    n = idx + 2
    if is_permutation(n, totient):
        if n / totient < lowest_ratio:
            lowest_ratio = n / totient
            optimal_n = n

print(optimal_n)

