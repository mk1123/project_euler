"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""


def is_leap_year(year):
    if not year % 4:
        if year % 100 or not year % 400:
            return True
    return False


months_normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jan_1_1900 = 1

curr_day = jan_1_1900 + (365 if is_leap_year(1900) else 366) % 7


sundays = 0

for year in range(1901, 2001):
    months = months_leap_year if is_leap_year(year) else months_normal_year
    for month_length in months:
        curr_day = (curr_day + month_length) % 7
        if not curr_day:
            sundays += 1

print(sundays)
