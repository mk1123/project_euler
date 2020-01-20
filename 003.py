"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factor(n):
    if n == 1:
        return 1
    for i in range(2, n+1) :
        if n % i == 0:
            return max(i, largest_prime_factor(n // i))

print(largest_prime_factor(600851475143))
