"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

# kinda cheated on this one

import itertools as it
from typing import Dict, Set
from utils import gen_primes, is_prime

largest_prime = 10000

primes = list(it.takewhile(lambda x: x < largest_prime, gen_primes()))

all_pairs: Dict[int, Set[int]] = {}


def all_pairs_for_num(a: int) -> Set[int]:
    pairs = set()
    for i in range(a + 1, len(primes)):
        if is_prime(int(str(primes[i]) + str(primes[a]))) and is_prime(
            int(str(primes[a]) + str(primes[i]))
        ):
            pairs.add(primes[i])

    return pairs


def valid(a: int, b: int) -> bool:
    return primes[b] in all_pairs[a]


min_sum = float("inf")


for a in range(1, len(primes)):
    if 5 * primes[a] >= min_sum:
        break
    if a not in all_pairs:
        all_pairs[a] = all_pairs_for_num(a)
    for b in range(a + 1, len(primes)):
        if primes[a] + 4 * primes[b] >= min_sum:
            break
        if b not in all_pairs:
            all_pairs[b] = all_pairs_for_num(b)
        if not valid(a, b):
            continue
        for c in range(b + 1, len(primes)):
            if primes[a] + primes[b] + 3 * primes[c] >= min_sum:
                break
            if c not in all_pairs:
                all_pairs[c] = all_pairs_for_num(c)
            if not (valid(a, c) and valid(b, c)):
                continue
            for d in range(c + 1, len(primes)):
                if primes[a] + primes[b] + primes[c] + 2 * primes[d] >= min_sum:
                    break
                if d not in all_pairs:
                    all_pairs[d] = all_pairs_for_num(d)
                if not (valid(a, d) and valid(b, d) and valid(c, d)):
                    continue
                for e in range(d + 1, len(primes)):
                    if (
                        primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
                        >= min_sum
                    ):
                        break
                    if e not in all_pairs:
                        all_pairs[e] = all_pairs_for_num(e)
                    if valid(a, e) and valid(b, e) and valid(c, e) and valid(d, e):
                        min_sum = min(
                            min_sum,
                            primes[a] + primes[b] + primes[c] + primes[d] + primes[e],
                        )

print(min_sum)

