'''Task 
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. 

Input Format
The first line contains an integer,  T(the number of test cases). 
The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.

Output Format
Print the data value of each node in the tree's level-order traversal as a single line of  space-separated integers.

Sample Input
6
3
5
4
7
2
1

Sample Output
3 2 5 1 4 7 '''

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        #Write your code here
        if root is None:
            return 0
        thislevel = [root]
        results = []
        while thislevel:
            nextlevel = []
            for n in thislevel:
                results.append(n.data)
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            thislevel=nextlevel
        final = ' '.join(str(e) for e in results)    
        print (final)
		
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
