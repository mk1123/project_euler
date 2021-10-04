"""
Project Euler Problem 83
========================

NOTE: This problem is a significantly more challenging version of
   Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in red and
is equal to 2297.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by moving left, right, up,
and down.
"""

from collections import defaultdict
from typing import List, Tuple, Dict
import heapq
import pandas as pd

start, end = (0, 0), (79, 79)

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

pq: List[Tuple[int, Tuple[int, int]]] = []

grid = pd.read_csv("./resources/matrix.txt", header=None).values
best_vals: Dict[Tuple[int, int], int] = defaultdict(lambda: 2 ** 32)


def get_from_2d(i: int, j: int, grid: List[List[int]]) -> int:
    return (
        2 ** 33
        if ((not (0 <= i < len(grid))) or (not (0 <= j < len(grid[0]))))
        else grid[i][j]
    )


heapq.heappush(pq, (grid[0][0], start))

while pq:
    dist, loc = heapq.heappop(pq)
    for delta_x, delta_y in deltas:
        new_x, new_y = loc[0] + delta_x, loc[1] + delta_y
        potential_dist = dist + get_from_2d(new_x, new_y, grid)
        if potential_dist < best_vals[(new_x, new_y)]:
            best_vals[(new_x, new_y)] = potential_dist
            heapq.heappush(pq, (best_vals[(new_x, new_y)], (new_x, new_y)))

print(best_vals[end])

