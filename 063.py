"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from math import log10, ceil

total_sum = 0

for i in range(1, 30):
    for j in range(1, 10):
        if ceil(log10(j ** i)) == i:
            total_sum += 1

print(total_sum + 1)  # doesn't include 1 because of log stuff
