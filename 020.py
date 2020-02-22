"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""


def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(digit_sum(factorial(100)))
