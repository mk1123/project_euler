"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""

num = 100

dp = [[0] * (num + 1) for _ in range(num + 1)]

for n in range(num + 1):
    dp[0][n] = 1
    dp[n][1] = 1

for n in range(2, num + 1):
    for k in range(2, n):
        return_sum = 0
        if (n - k) <= k:
            return_sum += 1 + dp[n - k][n - k - 1]
        else:
            return_sum += dp[n - k][k]
        return_sum += dp[n][k - 1]
        dp[n][k] = return_sum

print(dp[num][num - 1])

