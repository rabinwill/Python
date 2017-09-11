# Name = Rabin William David
# WSUID = J965V385
# Program = prog85.py
#
# Pseudo Code
# Program that prints the list of prime numbers from the start till the number
# entered by the user.
#
# Inputs: Asking the user to enter a number greater than 2
# Outputs: Prints the list of prime numbers from the start until the number entered
#          by the user
#
# importing the math library
# importing the string library
# start of a function isprime
# start of for loop between 2 until int(n**0.5)+1
#   if statement that check n mod x equals 0
#       returns false
#   returns true
#
# Start of def main()
#
# Asking the user to enter a number greater than 2
# initialising the variables needed
# printing the list of prime number from the start until the number entered
# if loop that checks if the entered value is greater than 2
#   for loop in range 2 until n+1
#       if the number is prime by calling the function isprime
#           printing the list of the prime numbers
# closing main ()


import math
import string
def isprime(n):                                                 #check if integer n is a prime
    for x in range(2, int(n**0.5)+1):                           # range starts with 2 and only needs to go up the squareroot of n
        if n % x == 0:
            return False
    return True
def main():

    n = int(input ("Please enter a number greater than 2 :"))   #Asking the user to enter a number greater than 2
    i = 2                                                       #Initialising the variables needed
    print("These are the prime numbers less than %d is:" %n)    
    if (n > 2):                                                 #If statement that checks if the entered number is greater than 2
        for i in range (2,n+1):                                 # for loop in range 2 until n+1
            if (isprime(i)):                                    #if the number is prime by calling the function isprime
                print(" ", i, end="")                           #printing the list of primes
    print()
                
main()                                                          #Closing main
