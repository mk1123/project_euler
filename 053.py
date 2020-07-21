"""
Project Euler Problem 53
========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5,3) = 10.

In general,

nCr(n,r) = n!/(r!(n-r)!), where r =< n, n! = n * (n1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: nCr(23,10) =
1144066.

How many values of nCr(n,r), for 1 =< n =< 100, are greater than one-million?
"""

from utils import ncr

counter = 0

for n in range(23, 101):
    for r in range(1, n // 2 + 1):
        if ncr(n, r) > 1e6:
            if r == n / 2:
                counter += 1
            else:
                counter += 2

print(counter)
