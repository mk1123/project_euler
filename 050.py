"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
import bisect
import itertools as it
from typing import Optional, List, Tuple

from utils import gen_primes, is_prime

UPPER_LIMIT = 1000000
primes = list(it.takewhile(lambda x: x < UPPER_LIMIT, gen_primes())) # type: List[int]

temp = 0
cum_sums = [0]

for prime in primes:
    temp += prime
    cum_sums.append(temp)
    
longest_sequence = 0
max_value = 0

for i in range(len(primes) - 1, -1, -1):
    curr_prime = primes[i]
    
    if curr_prime <= cum_sums[longest_sequence]:
        break
    
    start = 0
    end = longest_sequence
    
    sum_ = cum_sums[end]
    
    while sum_ != curr_prime:
        if sum_ < curr_prime:
            end += 1
        else:
            start += 1
        
        if end - start <= longest_sequence:
            break
        
        sum_ = cum_sums[end] - cum_sums[start]
        
    if sum_ == curr_prime:
        longest_sequence = end - start
        max_value = curr_prime
        
print(max_value)
    
