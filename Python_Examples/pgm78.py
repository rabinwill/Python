# Name = Rabin William David
# WSUID = J965V385
# Program = pgm78.py
#
#   Pseudo Code
# Decodes and Encodes a Caesar Cipher text
#
# Inputs: Asking the user to enter the text he/she wants to Encode and the key
# Outputs: Gives out the Encoded Caesar Cipher text
#
# for loop to read the input text by each character
#   if statement that checks if there are no spaces in the character
#       gets the ord value of the character
#       adds the key to the ord value
#           if statement that checks if the character is lower case
#               if statement that checks if the ord value is > 122 (Greater than z)
#               substracts 26 from the ord value
#           else if statement that checks if the character is upper case
#               if statement that checks if the ord value is > 90 (Greater than Z)
#               substracts 26 from the ord value
#       adds the character to the decoded text
#   else statements
#       adds the character to the decoded text
# Prints the decoded text
#       
#
# Inputs: Asking the user if he/she wants to Decode a Caesar Cipher and the key
# Outputs: If the user wants to Decode a text, the text is decoded and printed out.
#           If the user doesn't want to decode a text, Thank you message is printed out
#
# if loop to check if the user wants to decode
#   for loop to read the input text by each character
#       if statement that checks if there are no spaces in the character
#           gets the ord value of the character
#           adds the key to the ord value
#           if statement that checks if the character is lower case
#               substracts the key value from the ord value
#               if statement that checks if the ord value is < 97 (Less than a)
#                   adds 26 from the ord value
#           else if statement that checks if the character is upper case
#               substracts the key value from the ord value
#               if statement that checks if the ord value is < 65 (Less than A)
#                   adds 26 from the ord value
#           adds the character to the encoded text
#   else statements
#       adds the character to the encoded text
# Prints the encoded text
# Prints a thank you message
# if loop if the user selects not to encode
#   prints a thank you message


import string                                               #importing the string library
def main():                                                 #Start of main
    text = input("Please enter the plain text message:")
    key = int (input("Please enter the key value:"))

    print ("The Decoded text is >> ", end = "")
    decodedtext= " "
    for x in text:                                          #Start of for loop through each character  
        if x.isalpha():                                     #checking for non spaced character
            b = ord(x)
            b = b + key                                     #Adding the key value
            if ( x.islower() ):                             #Checking for lower case      
                if ( b > 122 ):                             #checking if ord value is greater than z
                    b = b - 26                              
            elif ( x.isupper() ):                           #Checking for upper case
                 if ( b > 90 ):                             #Checking if ord value is greater than Z
                    b = b - 26
            decodedtext = decodedtext + chr(b)              #adding the decoded char value to decodedtext
        else:
            decodedtext = decodedtext + x                   #else if there is no space
    print (decodedtext,end = "")                            #printing the decoded text and ignoring the new line
    print()


    question = int (input("Do you want to Encode a Caesar Cipher? If yes enter 1 if not enter 2 >"))

    if ( question == 1 ):
        text2 = input("Please enter the Ciper text you want to encode:")
        ecodekey = int (input("Please enter the key value:"))
        encodedtext = " "
        print ("The Decoded text is >> ", end = "")
        for y in text2:                                     #Start of for loop through each character
            if y.isalpha():                                 #checking for non spaced character          
                c = ord(y)
                c = c - key                                 #Adding the key value
                if ( y.islower() ):                         #Checking for lower case 
                    if ( c < 97 ):                          #checking if ord value is less than a
                        c = c + 26
                elif ( y.isupper() ):                       #Checking for upper case
                    if ( c < 65 ):                          #Checking if ord value is less than A
                        c = c + 26
                encodedtext = encodedtext + chr(c)          #adding the encoded char value to encodedtext
            else:                                           #else if there is no space
                encodedtext = encodedtext + y               #printing the decoded text and ignoring the new line
        print (encodedtext, end = "") 
        print()
        print ("Thank You!")
    if ( question == 2 ):                                   #If the user selects not to encode  
        print ("Thank You!")

main()                                                      #end of main
