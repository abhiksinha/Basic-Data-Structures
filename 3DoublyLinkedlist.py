## basic template of doubly ll
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
## Double Linked list class,, it will contain all the methods and variables required for normal operation in doubly linkedlist        
class Doublell:
    def __init__(self):
        self.head=None
     ## this method will insert at the end of the dll.O(n) time   
    def insert(self,data):
        new_node=createNode(data)
         ##checking whether the first element is inserting
        if self.head==None:
            self.head=new_node
        else:
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.next=new_node
            tmp.next.previous=tmp ## this will make newnode pointing to the previous node
            
    def traverseBacknForth(self):
        if(self.head==None):
            print("Empty List") ##underflow condition
            return
        tmp=self.head
        prev=None ## this will keep track of the previous node.It will be used to traverse from the end
        while(tmp!=None):
            print(tmp.data)
            prev=tmp
            tmp=tmp.next ## incrementing untill we reach to the end
        
        while(prev!=None):
            print(prev.data)
            prev=prev.previous ## traversing back to the start
 
#main program
if __name__=="__main__":
    dll=Doublell()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    dll.traverseBacknForth()
     
        
        
        
