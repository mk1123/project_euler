"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def sieve(n):
    arr = [True] * (n-1)
    for i in range(2, int(math.sqrt(n)) + 2):
        if arr[i-2]:
            for j in range(2*i, n+1, i):
                arr[j-2] = False
    return [i+2 for i in range(len(arr)) if arr[i]]

print(sum(sieve(2000000)))
