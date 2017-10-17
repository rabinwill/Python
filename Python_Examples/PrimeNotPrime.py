'''
Input Format
The first line contains an integer, T, the number of test cases. 
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Sample Input
3
12
5
7

Sample Output
Not prime
Prime
Prime
'''

import math 
def primeCheck(num):
    if (num ==1):
        return "Not prime"
    sq = int(math.sqrt(num))
    for z in range(2, sq+1):
        if (num % z == 0):
            return "Not prime"
    return "Prime"
T = int(input())
a = list()
for i in range(T):
    num = int(input())
    a.append(num)

for x in range(len(a)):
    prime = primeCheck(int(a[x]))
    print (prime)

