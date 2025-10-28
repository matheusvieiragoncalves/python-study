# Exercise 005: conditionals
# Create a program that ready any year and show if it's a leap year or not.

from calendar import isleap
from datetime import date

year = int(input('Enter a year or use current year in your computer (0): '))

if year == 0:
  year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'this year {year} is leap')
else:
    print(f'this year {year} is not leap')

print(f'This year {year} is {'leap' if isleap(year) else 'not leap'}')
