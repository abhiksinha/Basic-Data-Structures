## Implementation of Stack using Linear Linked List.
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
## this class will contain all the basic methods and variable for Stack
class Stack:
    def __init__(self):
        self.head=None ## initialising head as Null
    ## push at top of the stack,,head will act as stack pointer   
    def push(self,data):
        new_node=createNode(data) ## creating a new object of class createnode
        ## checking if first element to insert
        if self.head==None: 
            self.head=new_node
            
        ##inserting at begining of the list   
        else:
            new_node.next=self.head
            self.head=new_node
    
    def pop(self):
        if self.head==None:
            print("Underflow")
            return
        x=self.head.data
        tmp=self.head
        self.head=self.head.next
        del(tmp) ## deleting the popped node
        return x
 

