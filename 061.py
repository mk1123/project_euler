"""
Project Euler Problem 61
========================

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

 1. The set is cyclic, in that the last two digits of each number is the
    first two digits of the next number (including the last number with
    the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
    and pentagonal (P[5,44]=2882), is represented by a different number in
    the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.
"""
from collections import defaultdict
from typing import Iterator, List, Dict, Set
import itertools as it
import sys

from utils import (
    triangular_generator,
    square_generator,
    pentagonal_generator,
    hexagonal_generator,
    heptagonal_generator,
    octogonal_generator,
)


def gen_in_range(iterator: Iterator[int]) -> List[int]:
    return list(
        it.takewhile(lambda x: x < 10000, it.dropwhile(lambda x: x < 1000, iterator))
    )


get_first_two = lambda x: x // 100
get_last_two = lambda x: x % 100


def group_by_first_two(nums: List[int]) -> Dict[int, Set[int]]:
    grouped_vals = defaultdict(set)
    for num in nums:
        grouped_vals[get_first_two(num)].add(num)
    return grouped_vals


def group_by_last_two(nums: List[int]) -> Dict[int, Set[int]]:
    grouped_vals = defaultdict(set)
    for num in nums:
        grouped_vals[get_last_two(num)].add(num)
    return grouped_vals


special_nums = {
    3: gen_in_range(triangular_generator()),
    4: gen_in_range(square_generator()),
    5: gen_in_range(pentagonal_generator()),
    6: gen_in_range(hexagonal_generator()),
    7: gen_in_range(heptagonal_generator()),
    8: gen_in_range(octogonal_generator()),
}

grouped_by_first_2_digits: Dict[int, Dict[int, Set]] = defaultdict(
    lambda: defaultdict(set)
)

for type_, nums in special_nums.items():
    just_this_type_grouped = group_by_first_two(nums)
    for first_two, full_nums in just_this_type_grouped.items():
        grouped_by_first_2_digits[first_two][type_].update(full_nums)


def recurse(curr_num, nums_seen_so_far, types_seen_so_far, count):
    if count == 5:
        if get_last_two(curr_num) == get_first_two(nums_seen_so_far[0]):
            print(sum(nums_seen_so_far))
            sys.exit()
        else:
            return
    if get_last_two(curr_num) not in grouped_by_first_2_digits:
        return
    for type_, nums_set in grouped_by_first_2_digits[get_last_two(curr_num)].items():
        if type_ in types_seen_so_far:
            continue
        for num in nums_set:
            if num in nums_seen_so_far:
                continue
            recurse(
                num, nums_seen_so_far + [num], types_seen_so_far | {type_}, count + 1
            )


triangle_first = group_by_first_two(special_nums[3])

for triangular_num in special_nums[3]:
    recurse(triangular_num, [triangular_num], {3}, 0)