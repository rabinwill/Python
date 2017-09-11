# Name = Rabin William David
# WSUID = J965V385
# Program = pgm56.py
#
#   Pseudo Code
# Program that calculates the numeric value of a full name or any sentence
#
# Inputs: Asking the user the name/sentence
# Outputs: Gives the numeric value of the given name/sentence
#
# changing the user given name/sentence to lower case and the replacing the spaces
# for loop that goes through all the characters
#   adding the ord values of the characters to sum and subtracting 96 to get the desired values
# printing the total values, that is printing the sum



import string                               #importing the string library
def main():                                 #start of main
    
    name = input("Enter You Name->")
    name1 = name.lower()                    #replacing the user given name/sentence to lower case
    name2 = name1.replace(" ", "")          #cutting out the spaces in the sentence
    print("Taking all in lower case")
    print("And taking out all the white spaces in between, we get", name2)
    sum = 0

    for x in name2:                         #For loop that goes through individual characters in the name2
        sum = sum + ord(x) - 96             #Adding the ord value of the charater and subtrating 96 from it

    print ("The Total Value Is =", sum)

main()                                      #end of main
