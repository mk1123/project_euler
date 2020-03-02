"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
from math import sqrt
from collections import Counter


def prime_factorization(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n //= i
    if n > 2:
        primes.append(n)

    return Counter(primes)


def sum_of_divisors(n):
    if n in {0, 1}:
        return 0
    sum_ = 1
    prime_factors = prime_factorization(n)
    for prime in prime_factors:
        sum_ *= (prime ** (prime_factors[prime] + 1) - 1) // (prime - 1)

    return sum_ - n


abundant = set()
total_sum = 0

for i in range(1, 47):
    if sum_of_divisors(i) > i:
        abundant.add(i)

for i in range(1, 47):
    add = True
    for val in abundant:
        if i - val in abundant:
            add = False
            break
    if add:
        total_sum += i


for i in range(47, 20162):
    if sum_of_divisors(i) > i:
        abundant.add(i)


for i in range(47, 20162, 2):
    add = True
    for val in abundant:
        if i - val in abundant:
            add = False
            break
    if add:
        total_sum += i


print(total_sum)
