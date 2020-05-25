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

UPPER_LIMIT = 50000
primes = list(it.takewhile(lambda x: x < UPPER_LIMIT, gen_primes())) # type: List[int]

dp = [(0, 0)] + [(-1, -1)] * UPPER_LIMIT

def largest_prime_smaller_than_index(x):
    # type: (int) -> int
    return bisect.bisect_right(primes, x) - 1
    

def dp_func(x):
    # type: (int) -> Tuple[int, int]
    if x < 0:
        return (0, 0)
    
    if dp[x] != (-1, -1):
        return dp[x]
    
    print(x)
    
    max_length = -2
    last_prime = -2
    
    for i in range(largest_prime_smaller_than_index(x) + 1):
        curr_prime = primes[i]
        prev_dp_length, prev_dp_largest = dp_func(x - curr_prime)
        if prev_dp_largest in (primes[i-1], 0):
            if prev_dp_length + 1 > max_length:
                max_length = prev_dp_length + 1
                last_prime = curr_prime
                
    return_val = (max_length, last_prime)

    dp[x] = return_val
    return return_val

print(max(primes, key=lambda x: dp_func(x)[0]))
    
