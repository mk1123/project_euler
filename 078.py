"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

from itertools import count, islice
from typing import Iterator


def pm_count() -> Iterator[int]:
    for x in count(start=1):
        yield x
        yield -x


def generalized_pentagonal() -> Iterator[int]:
    for x in pm_count():
        yield x * (3 * x - 1) // 2


partitions = [1]


def get_from_partitions(i: int) -> int:
    return 0 if i < 0 else partitions[i]


pentagonal_gen = generalized_pentagonal()

pentagonals = [next(pentagonal_gen)]

new_count = count(1)

for i in new_count:
    curr_val_sum = 0
    for idx, pentagonal_num in enumerate(pentagonals):
        val = (
            get_from_partitions(i - pentagonal_num)
            if (idx // 2) % 2 == 0
            else -get_from_partitions(i - pentagonal_num)
        )
        if val == 0:
            break
        curr_val_sum += val

    partitions.append(curr_val_sum)

    if curr_val_sum % 1000000 == 0:
        print(i)
        break

    if i - pentagonals[-1] >= 0:
        pentagonals.append(next(pentagonal_gen))

