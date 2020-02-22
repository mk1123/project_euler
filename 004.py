"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
max_pal = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        mult = i * j
        if str(mult) == str(mult)[::-1]:
            if mult > max_pal:
                max_pal = mult
                break

print(max_pal)
