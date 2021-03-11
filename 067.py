"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

from utils import process_grid

with open("./resources/triangle.txt") as f:
    grid = f.read()
    grid = process_grid(grid)

    max_length = len(grid[-1])

    dp = [[None] * i for i in range(1, max_length + 1)]

    dp[-1] = grid[-1]

    for i in range(max_length - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] = grid[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    print(dp[0][0])
