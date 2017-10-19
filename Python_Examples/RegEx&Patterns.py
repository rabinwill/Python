'''
Sample Input
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output
julia
julia
riya
samantha
tanya
'''

#!/bin/python3

import sys
import re
lst = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search("@gmail.com",emailID):
        lst.append(firstName)
sortedlst = sorted(lst)
for z in range(len(sortedlst)):
    print(sortedlst[z])
