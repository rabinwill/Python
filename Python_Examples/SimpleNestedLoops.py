'''
Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15x(number of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500x(number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.

Sample Input
9 6 2015
6 6 2015

Sample Output
45
'''

import sys

inlist = sys.stdin.readlines()

da,ma, ya = map(int,inlist[0].strip().split())
de,me, ye = map(int,inlist[1].strip().split())

if ya>ya:
    print("10000")
elif (ma>me and ya==ye):
    print((ma-me)*15)
elif (ya==ye and ma==me and da>de):
    print((da-de)*15)
else:
    print("0")