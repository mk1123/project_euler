"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
dp = {}


def chain(n):
    if n == 1:
        return 1

    if n in dp:
        return dp[n]

    if not n % 2:
        count = 1 + chain(n // 2)
    else:
        count = 1 + chain(n * 3 + 1)

    dp[n] = count
    return count


max_chain = 1
max_num = 1
for i in range(1, 1000000):
    if chain(i) > max_chain:
        max_chain = chain(i)
        max_num = i

print(max_num)

