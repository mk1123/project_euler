"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""
from collections import Counter
import itertools
import re
from typing import List
import sys

from utils import gen_primes

def gen_alternates(num: int, repeated_digit_str: str) -> List[int]:
    
    str_num = str(num)
    
    return [int(re.sub(repeated_digit_str, str(n), str_num)) for n in range(10)]

five_digit_primes = list(itertools.takewhile(lambda x: x < 1000000, itertools.dropwhile(lambda x: x < 10000, gen_primes())))
five_digit_primes_set = set(five_digit_primes)

for prime in five_digit_primes:
    digit_counts = Counter(str(prime))
    for digit_str, count in digit_counts.items():
        if count == 3:
            alternates = gen_alternates(prime, digit_str)
            is_prime = lambda x: x in five_digit_primes_set
            if sum(map(is_prime, alternates)) == 8:
                print(prime)
                sys.exit()
