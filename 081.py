"""
Project Euler Problem 81
========================

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in red
and is equal to 2427.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
"""
import pandas as pd
from typing import List

grid = pd.read_csv("./resources/matrix.txt", header=None).values


def get_from_2d(i: int, j: int, grid: List[List[int]]) -> int:
    # print(((not (0 <= i < len(grid))) or (not (0 <= j < len(grid[0])))))
    return (
        float("inf")
        if ((not (0 <= i < len(grid))) or (not (0 <= j < len(grid[0]))))
        else grid[i][j]
    )


def dp(grid: List[List[int]]) -> int:
    min_path_vals = [[0] * len(grid[0]) for _ in range(len(grid))]
    min_path_vals[-1][-1] = grid[-1][-1]
    # print(min_path_vals)
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if not (i == j and i == len(grid) - 1):
                # print(i, j)
                min_path_vals[i][j] = grid[i][j] + min(
                    get_from_2d(i + 1, j, min_path_vals),
                    get_from_2d(i, j + 1, min_path_vals),
                )
        # break
    return min_path_vals[0][0]


print(dp(grid))

