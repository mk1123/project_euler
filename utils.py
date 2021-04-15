from collections import Counter
import itertools as it
import numpy as np
import math
import gmpy2
from typing import Iterator, Generator, Any, List, Tuple
import sympy
import primefac
import operator as op
from functools import reduce


def sieve(n):
    """This function should be depracated in favor of gen_primes and it.takewhile."""
    arr = [False, False] + [True] * (n - 2)
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            for j in range(2 * i, n, i):
                arr[j] = False
    return (i for i in range(len(arr)) if arr[i])


def prime_factorization(n):
    primes = list(sieve(n))
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


def fast_prime_factorization(n):
    # type: (int) -> Any
    return primefac.primefac(n)


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def gen_composites():
    # type: () -> Generator[int, None, None]
    """Generate an infinite sequence of composite numbers.
    Pretty much exactly the same logic as gen_primes."""
    D = {}
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            yield q
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def largest_prime_factor(n):
    if n == 1:
        return 1
    for i in range(2, n + 1):
        if n % i == 0:
            return max(i, largest_prime_factor(n // i))


def process_grid(grid_string: str) -> np.ndarray:
    return np.array(
        [[int(y) for y in x.strip().split(" ")] for x in grid_string.split("\n")]
    )


all_factors = lambda n: {
    f for i in range(1, int(n ** 0.5) + 1) if not n % i for f in [i, n // i]
}


def sum_of_divisors(n):
    if n in {0, 1}:
        return 0
    sum_ = 1
    prime_factors = prime_factorization(n)
    for prime in prime_factors:
        sum_ *= (prime ** (prime_factors[prime] + 1) - 1) // (prime - 1)

    return sum_ - n


def num_ways_coin_change(denoms, max_currency):
    stored = [0] * (max_currency + 1)
    stored[0] = 1

    for coin in denoms:
        for i in range(coin, max_currency + 1):
            stored[i] += stored[i - coin]

    return stored


def is_prime(n: int) -> bool:
    return cast(bool, gmpy2.is_prime(n))


word_to_score = lambda word: sum(ord(char) - ord("A") + 1 for char in word)
is_triangular = lambda n: gmpy2.is_square(8 * n + 1)


def is_pentagonal(n):
    # type: (int) -> bool
    discriminant = 1 + 24 * n
    return (
        gmpy2.is_square(discriminant) and ((int(math.sqrt(discriminant)) + 1) % 6) == 0
    )


def pentagonal_values_generator():
    # type: () -> Iterator[int]
    return map(lambda x: x * (3 * x - 1) // 2, it.count(start=1))


def is_hexagonal(n):
    # type: (int) -> bool
    discriminant = 1 + 8 * n
    return (
        gmpy2.is_square(discriminant) and ((int(math.sqrt(discriminant)) + 1) % 4) == 0
    )


def is_heptagonal(n: int) -> bool:
    K = (3 + math.sqrt(40 * n + 9)) / 10
    return int(K) == K


def is_octogonal(n: int) -> bool:
    K = (2 + math.sqrt(12 * n + 4)) / 6
    return int(K) == K


def hexagonal_values_generator():
    # type: () -> Iterator[int]
    return map(lambda x: x * (2 * x - 1), it.count(start=1))


def mod_exp(base, exp, modulus):
    # type: (int, int, int) -> int
    return gmpy2.powmod(base, exp, modulus)  # type: ignore


def ncr(n, r):
    # type: (int, int) -> int
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


from math import log10, floor
from typing import cast


def reverse_num(num: int) -> int:
    if num < 10:
        return num
    return cast(int, 10 ** floor(log10(num)) * (num % 10) + reverse_num(num // 10))


def is_palindrome(num: int) -> bool:
    return num == reverse_num(num)


def digital_sum(num: int) -> int:
    if num < 10:
        return num
    return num % 10 + digital_sum(num // 10)


def triangular_generator() -> Iterator[int]:
    return map(lambda n: n * (n + 1) // 2, it.count())


def square_generator() -> Iterator[int]:
    return map(lambda n: n * n, it.count())


def pentagonal_generator() -> Iterator[int]:
    return map(lambda n: (3 * n ** 2 - n) // 2, it.count())


def hexagonal_generator() -> Iterator[int]:
    return map(lambda n: 2 * n ** 2 - n, it.count())


def heptagonal_generator() -> Iterator[int]:
    return map(lambda n: (5 * n ** 2 - 3 * n) // 2, it.count())


def octogonal_generator() -> Iterator[int]:
    return map(lambda n: (3 * n ** 2 - 2 * n), it.count())


def contfrac_to_frac(seq: List[int]) -> Tuple[int, int]:
    """ Convert the simple continued fraction in `seq` 
        into a fraction, num / den
    """
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num * u, num
    return num, den


def totientrange(a: int, b: int) -> List[int]:
    return sympy.sieve.totientrange(a, b)


def is_permutation(a: int, b: int) -> bool:
    return Counter(str(a)) == Counter(str(b))
