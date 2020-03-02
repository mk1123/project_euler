"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

from math import factorial

digits = list(range(10))
num = 1000000 - 1
count = 10
answer_digits = []

while digits:
    next_digit = digits[int(num % factorial(count) / factorial(count - 1))]
    answer_digits.append(next_digit)
    digits.remove(next_digit)
    count -= 1

print("".join(map(str, answer_digits)))

