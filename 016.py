"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


print(digit_sum(2 ** 1000))
