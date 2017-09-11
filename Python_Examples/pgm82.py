# Name = Rabin William David
# WSUID = J965V385
# Program = prog82.py
#
# NOTE: In the table printed, the first row prints the WINDSPEEDS.
#       The first coloumn prints the TEMPERATURES, also denoted by (T) in the table.
#       The rest of the coloums are the WIND CHILL INDEXes, also denoted by (A) in the table.
#
# Pseudo Code
# Program that computes the wind chill index using the given formula
#
# Inputs: Asking the user to select an option 1 or 2, where 1 is the option for the
#         user to enter the temperature and wind speed, and 2 is the option where the
#         program prints out a table.
# Outout: Outouts the the windchill index when the user enters wind speed and temperature.
#         Also outputs a table of different wind chill indexes.
#
# importing the string library
# start of function windchillformula
#   a equals to the given wind chill index formula
#   returning a. That is the answer
#
# Start of main()
# Printing the options for the user to select
# Option 1: Asking if the user if he/she wants to enter specifc temperature and
#           wind speed values.
# Option 2: Asking the user if he/she wants to print out the table
# Getting the input from the user in variable ans
#
# if loop, if the user selects to enter the his/her own specific values
#   Asking the user to enter the temperature and taking in the input
#   Asking the user to enter the wind speed and taking in the input
#   sending the user entered values to the function windchillformula
#   printing the answer for the wind chill index after caluculating the value
#   printing a thank you message
#
# elif loop, if the user selects to print out the table
#   assigining wind2 to the for loop of the windspeeds given in the question
#   assigning the 
#

import string                                                                       #importing the string library

def windchillformula(temp, wind):                                                   #Start of windchillformula function
    a = 35.74 + (0.6215*temp) - (35.75*(wind**.16)) + (0.4275*temp*(wind**.16))     #Formula for the windchill index
    return a                                                                        #Returning the answer to the above function

def main():                                                                         #Start of main
    print("Please select one of the following options:")                            #Printing out the list of options 
    print("1. Enter specifc temperature and wind speed values.")
    print("2. Print a table.")
    ans = int(input("Enter option 1 or 2 >>"))                                      #Getting the input from the user

    if (ans == 1):                                                                  #If the user selects to enter the values
        intemp = int(input("Please enter the temperature >>"))                      #Taking in the value of the temperaure
        inwind = int(input("Please enter the wind speed >>"))                       #Taking in the values of the wind speed
        windchillindex = windchillformula(intemp,inwind)                            #Sending the values to the windchillformula function
        print ("%3d"%(windchillindex))                                              #Printing the value of the wind chill index
        print ("thank you")

    elif (ans == 2):                                                                #If the user selects to generate a table
        wind2 = [x for x in range (5,50,5)]                                         #assigning a for loop for the wind speed
        temp2 = [y for y in range (-20,60,10)]                                      #assigning a for loop for the temperature 
        print("Winds", end="")                              
        for x in wind2:                                                             #For loop that gies through the wind speeds
            print("\t%3dMPH" % x, end="")                                           #Printing the windspeeds as a row
        print()
        
        for y in temp2:                                                             #For loop that goes through the temperatures
            print("%3d(T)" %y,end="")                                               #printing the temperatures as a coloumn
            for z in wind2:                                                         #For loop that goes through the winds speeds
                windchillindexin = windchillformula(y,z)                            #Sending the values to the windchillformula function
                print("\t%3d(A)"  % windchillindexin,end="")                        #Printing the windchill indexe's                 
            print()                                                                 
    else:
        print("\tThank You!")
    print("\tThank You!")

main()                                                                              #Close of main()
