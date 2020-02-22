"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""
import re


def full_name(n):
    if n < 10:
        return ones(n)
    elif n >= 10 and n < 20:
        return tens(n)
    elif n >= 20 and n < 100:
        return rest_of_two_digit(n)
    elif n >= 100 and n < 1000:
        return hundreds(n)
    elif n == 1000:
        return thousands(n)


def ones(n):
    full_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    return full_words[n]


def tens(n):
    full_words = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    return full_words[n]


def rest_of_two_digit(n):
    tens_digit_name = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    if n % 10:
        return tens_digit_name[n // 10] + "-" + full_name(n % 10)
    else:
        return tens_digit_name[n // 10]


def hundreds(n):
    if n % 100:
        return full_name(n // 100) + " hundred and " + full_name(n % 100)
    else:
        return full_name(n // 100) + " hundred"


def thousands(n):
    return "one thousand"


cum_length = 0
for i in range(1, 1001):
    cum_length += len(re.sub("\s|-", "", full_name(i)))

print(cum_length)
