'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, s, is a palindrome?

To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means s isn't a palindrome).

Sample Input
racecar

Sample Output
The word, racecar, is a palindrome. '''

import sys

class Solution:

    def __init__(self):
        self.stack = list()
        self.queue = list()
        
    def pushCharacter(self, char):
        self.stack.append(char)
    
    def popCharacter(self):
        return (self.stack.pop(-1))      #pop(-1) removes and returns the last entry in the list
    
    def enqueueCharacter(self, char):
        self.queue.append(char)
        
    def dequeueCharacter(self):
        return(self.queue.pop(0))       #pop(0) removes and returns the first entry from the list
		
		
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")   