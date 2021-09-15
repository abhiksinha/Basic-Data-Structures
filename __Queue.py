## Implementation of queue using two pointers and Linear linked list

## basic template of linear ll
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
## this class will contain all the methods and variables for Queue    
class Queue:
    def __init__(self):
        ## initialising head,tail pointer to null
        self.head=None
        self.tail=None
    ## enqueuing method   
    def enqueue(self,data):
        new_node=createNode(data) 
        if self.head==None:
            self.head=new_node ##first element
            self.tail=new_node
        else:
            self.tail.next=new_node  ## inserting at the end
            self.tail=self.tail.next
        
    def dequeue(self):
        if self.head==None:
            ## underflow condition
            return None
        tmp=self.head
        x=tmp.data
        self.head=self.head.next 
        del(tmp) ## deleting the dequeued node
        return x