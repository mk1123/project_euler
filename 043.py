"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


def divisibility_rules(num_string):
    return not (
        int(num_string[1:4]) % 2
        or int(num_string[2:5]) % 3
        or int(num_string[3:6]) % 5
        or int(num_string[4:7]) % 7
        or int(num_string[5:8]) % 11
        or int(num_string[6:9]) % 13
        or int(num_string[7:10]) % 17
    )


def generate_0_to_9_pandigital():
    for i in range(1, 10):
        for rest_permutation in permutations(set(range(10)).difference({i}), 9):
            yield str(i) + "".join(map(str, rest_permutation))


print(sum(map(int, filter(divisibility_rules, generate_0_to_9_pandigital()))))
