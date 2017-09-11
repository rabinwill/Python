# NAME = Rabin William David
#
# WSUID = J965V385
#
# DATE = 4/26/15
#
#########################################

#!/usr/bin
import random
import sys
import timeit

sys.setrecursionlimit(500000)

def quicksort(array):
    
    quick(array,0,len(array)-1)
    return array
    

def quick(arr,lower,upper):
    if (upper > lower ):			#if r>p
        m = split (arr,lower,upper)
        quick(arr,lower,m-1)
        quick(arr,m+1,upper)

def split(ar,low,up):
    pos = low   					# p = a[low] that is the first element    
    for i in range(low, up):           
        if ar[i] < ar[up]:             
            ar[i],ar[pos] = ar[pos],ar[i]
            pos += 1

    ar[pos],ar[up] = ar[up],ar[pos] #exchange A{i+1} with A[r]
                                          
    return pos


def compute(array):
    
    start = timeit.default_timer()
    array = quicksort(array)
    stop = timeit.default_timer()
    return array,(stop-start)

def display(array,time):
    
    print('computation time'+str(time))
    print (('sorted array: ' + str(array)))
    f = open('output.txt','a')
    f.write('sorted array: '+ str(array)+'\n')
    f.write('computation time: '+ str(time)+'\n')
    return time
    f.close()
    

def main():
    leave = 0
    while (leave != 1 ):
        print ("enter the number of elements you want to sort")
        array1=[]
        array2=[]
        array3=[]
        mode=input('Input:')

        #same element - case1

        same_element = random.randint(0,10000)
        for i in range(0,int(mode)):
            array1.append(same_element)  
        print (array1)
        average_time(array1)

        #same element - case2
        for i in range(0,int(mode)):
            array2.append(random.randint(0,10000))
            
        print(array2)
        average_time(array2)

        #diff element- case3
        
        for i in range(0,int(mode)):
            array3.append(random.randint(0,10000))
            
        print(array3)
        avg_time = average_time(array3)

        f = open('output.txt','a')
        f.write('Avg computation time: '+ str((avg_time)/3)+'\n')
        f.close()
        leave = int(input('enter 1 if you want to quit'))
            

def average_time(array):
    array,time= compute(array)
    time = display(array,time)
    total_time = 0
    total_time = total_time + time
    return total_time

main()	

