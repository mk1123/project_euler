"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import math

def sieve(n):
    arr = [True] * (n-1)
    for i in range(2, int(math.sqrt(n)) + 2):
        if arr[i-2]:
            for j in range(2*i, n+1, i):
                arr[j-2] = False
    return [i+2 for i in range(len(arr)) if arr[i]]

print(sieve(500000)[10000])

