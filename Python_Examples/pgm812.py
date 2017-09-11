# Name = Rabin William David
# WSUID = J965V385
# Program = pgm812.py

#   Pseudo Code
# Reads from a text file and prints out the heating and cooling costs for the cold
# and hot days.
#
# Inputs: None, because this program takes input from the text file.
# Outouts: Prints the number of cooling days
#          Prints the average of the cooling days
#          Prints the number of heating days
#          Prints the average of the heating days
#          Printing the total number of days with no heating and cooling needs.
#
# Start of main
# Initialising all the variables needed
# opening the file with read-only permissions
# Reading the file line wise and assinging the values to theint
# Start of for loop that loops through theint
#   assinging x as type int
#   If loop that checks if int(x) is less than 60 for cooling days
#       getting the cooling difference, that is 60 - the value of x
#       adding the amount to int(a) to hold the total difference
#       Adding +1 for the cooling days
#   elif loop that checks if int(x) is greater than 80 for heating days
#       getting the heating difference, that is the value of x - 80
#       adding the amount to int(b) to hold tha total difference
#       Adding +1 for the heating days
#   else
#       adding +1 to days
# Closing the opened file
# Printing out all the outputs as discussed above
#
# Close of main()

def main():                                         #Start of main
                                                    #Initialising the variables needed
    day = 0                                         #days with no heating or cooling needs                                         
    coolday = 0                                     #days with cooling needs                 
    heatday = 0                                     #days with heating needs
    a = 0.0                                         #variable to hold the total amount of cooling days cost
    b = 0.0                                         #variable to hold the total amount of heating days cost
    amount = 0                  
    theint = []                                     #theint is type string to read the input from the file                                    
   
    infile = open("test.txt", "r")                  #opening the file with read-only permission
    theint= (infile.readlines())                    #Reading the lines in the file and assigning it to theint

    for x in theint:                                #Start of for loop that goes through theint
        
        x = int(x)                                  #Assigining x as type int
        if int(x) < 60:                             #checks if int(x) is less than 60 for cooling days
            coolamount = 60 - x                     
            a = a + coolamount
            coolday = coolday + 1
        elif int(x) > 80:                           #checks if int(x) is greater than 80 for heating days
            heatamount = x - 80
            b = b + heatamount
            heatday = heatday + 1
        else:
            day = day + 1
                    
    infile.close()                                  #Closing the openied file

    a = round((a/coolday),2)                                 #Doing the logic to find the average of heating and cooling days
    b = round((b/heatday),2)
                                                    #Printing the above discussed values, below.
    print("The total number of cooling days is:", coolday)          
    print("The average of the cooling days is:", a)
    print("The total number of heatng days is:", heatday)
    print("The average of the heating days is:",b)
    print ("The Total number of days with no heating or cooling needed", day)

main()                                              #Closing main
        
        
