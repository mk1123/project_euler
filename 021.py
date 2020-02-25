"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from collections import Counter
from math import sqrt


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


amicable = {}
amicable_sum = 0

for i in range(10000):
    amicable[i] = sum_of_divisors(i)

for i in range(10000):
    new_elem = amicable[i]
    if new_elem < 10000 and new_elem != i and amicable[new_elem] == i:
        # print(i)
        amicable_sum += i

print(amicable_sum)
