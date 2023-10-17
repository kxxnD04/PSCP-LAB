"""Numdays"""
from datetime import date
DAY_1, MONTH_1, DAY_2, MONTH_2 = int(input()), int(input()), int(input()), int(input())
try:
    print(abs(date(2017, MONTH_1, DAY_1)-date(2017, MONTH_2, DAY_2)).days)
except ValueError:
    print('Impossible')
