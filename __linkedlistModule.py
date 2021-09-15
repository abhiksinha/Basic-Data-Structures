## Node class (template of node in a linear linked list) 
class createNode:
    ## __init__(dunder) is a kind of constructor. Initiated once an object is instantiated
    def __init__(self,data):  
        self.data=data
        self.next=None
        
        
## Linked list class,, it will contain all the methods and variables required for normal operation in linkedlist
class linkedlist:
    def __init__(self):
        self.head=None ## initiating head as null
    
    ## the insert method will take the argument data and insert at the end of the list(O(n) time). It is similar to insert function in C
    def insert(self,data):
        new_node=createNode(data) ## creating an object new_node of class CreateNode
        ##checking whether the first element is inserting
        if self.head==None:
            self.head=new_node
        else:
            tmp=self.head ## tmp variable is used to conserve the head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=new_node
     
    ## traverse method is same as traverse function in  C
    def traverse(self):
        if(self.head==None):
            print("Empty List") ##underflow condition
            return        
        tmp=self.head
        while(tmp!=None):
            print(tmp.data)
            tmp=tmp.next

