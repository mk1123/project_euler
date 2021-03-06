"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""
sum_ = 0
curr = 1
prev = 0

while curr < 4000000:
    if curr % 2 == 0:
        sum_ += curr

    old_curr = curr
    curr += prev
    prev = old_curr

print(sum_)

