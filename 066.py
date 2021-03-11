"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""

from math import sqrt
from typing import Generator, Tuple


def cont_fraction_rep_of_root(num: int) -> Generator[int, None, None]:
    root = sqrt(num)
    limit = int(root)
    if root == limit:
        yield -1
        return
    yield limit
    while True:
        d = 1
        m = 0
        a = limit
        while a != 2 * limit:
            m = d * a - m
            d = (num - m * m) // d
            a = (limit + m) // d
            yield a


def convergents_of_root(num: int) -> Generator[Tuple[int, int], None, None]:
    cont_frac_reps = cont_fraction_rep_of_root(num)
    p = next(cont_frac_reps)
    q = 1
    prev_prev = (p, q)
    yield prev_prev
    a1 = next(cont_frac_reps)
    p = p * a1 + 1
    q = a1
    prev = (p, q)
    yield prev
    for i in cont_frac_reps:
        curr = (
            i * prev[0] + prev_prev[0],
            i * prev[1] + prev_prev[1],
        )
        yield curr
        prev_prev = prev
        prev = curr


def min_x_pells(D: int) -> int:
    convergents = convergents_of_root(D)
    for p, q in convergents:
        if p ** 2 - D * q ** 2 == 1:
            return p

    return -1


max_D = 0
max_X = 0

for D in range(1, 1001):
    if int(sqrt(D)) != sqrt(D):
        x = min_x_pells(D)
        if x > max_X:
            max_X = x
            max_D = D

print(max_D)

