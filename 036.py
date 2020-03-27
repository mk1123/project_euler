"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
total_sum = 0

for i in range(1, 1000000, 2):
    str_i = str(i)
    if str_i == str_i[::-1]:
        base_2_str_i = str(bin(i))[2:]
        if base_2_str_i == base_2_str_i[::-1]:
            total_sum += i

print(total_sum)
