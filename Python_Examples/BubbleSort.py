'''
Bubble Sort!
Sample Input 0
3
1 2 3

Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
'''

#!/bin/python3

import sys
swaps = 0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
for i in range(n):
    
    for j in range(n-1):
        if (a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps = swaps + 1

    if (swaps == 0):
             break;
        
print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element: "+ str(a[0]))
print("Last Element: "+ str(a[n-1]))