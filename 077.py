"""
Project Euler Problem 77
========================

It is possible to write ten as the sum of primes in exactly five different
ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""
from itertools import count, takewhile
from utils import num_ways_coin_change, gen_primes

max_num = 100

primes = takewhile(lambda x: x < max_num, gen_primes())

stored = num_ways_coin_change(primes, max_num)
for i, num in enumerate(stored):
    if num > 5000:
        print(i)
        break
# primes_seen_so_far = []
# latest_prime = next(primes)

# for i in count(2):
#     if latest_prime < i:
#         primes_seen_so_far.append(latest_prime)
#         latest_prime = next(primes)

