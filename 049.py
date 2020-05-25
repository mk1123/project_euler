"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from collections import defaultdict
import itertools as it
from typing import List, Set, Tuple

from utils import sieve, is_prime

four_digit_primes = filter(lambda x: x > 1000, sieve(10000))

uniques = defaultdict(set)


for prime in four_digit_primes:
    uniques["".join(sorted(str(prime)))].add(prime)
    
DIFF = 3330

def find_all_length_3_subsequences(input_set):
    # type: (Set[int]) -> List[Tuple[int, int, int]]
    valid_subsequences = []
    for first_num, second_num in it.combinations(input_set, 2):
        if second_num - first_num == DIFF:
            if second_num + DIFF in input_set:
                valid_subsequences.append((first_num, second_num, second_num + DIFF))
            
    return valid_subsequences

sequences = list(it.chain.from_iterable(map(find_all_length_3_subsequences, uniques.values())))

for sequence in sequences:
    if 1487 not in sequence:
        print("".join(map(str, sequence)))
