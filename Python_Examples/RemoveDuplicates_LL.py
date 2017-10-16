'''
A removeDuplicates function takes a pointer to the head node of a linked list as a parameter. It deletes any duplicate nodes from the list and returns the head of the updated list.

Sample Input
6
1
2
2
3
3
4

Sample Output
1 2 3 4 
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
			
    def removeDuplicates(self,head):
	#Note: got this solution from stackoverflow.com/questions/42728271/remove-duplicates-from-linked-list-python 
        current = second = head
        while current is not None:
            while second.next is not None:   # check second.next here rather than second
                if second.next.data == current.data:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   
            current = second = current.next
        
        return head
		
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 