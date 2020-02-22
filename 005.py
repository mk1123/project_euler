"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math
from collections import Counter


def sieve(n):
    arr = [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            for j in range(2 * i, n + 1, i):
                arr[j - 2] = False
    return [i + 2 for i in range(len(arr)) if arr[i]]


def prime_factorization(n):
    primes = sieve(n)
    counter = 0
    i = primes[counter]
    factors = []
    while i * i <= n:
        if n % i:
            counter += 1
            i = primes[counter]
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return Counter(factors)


def problem(n):
    global_counter = Counter()
    for i in range(2, n + 1):
        factors = prime_factorization(i)
        for num in factors:
            global_counter[num] = max(global_counter[num], factors[num])
    base = 1
    for num in global_counter:
        base *= num ** global_counter[num]
    return base


print(problem(20))

