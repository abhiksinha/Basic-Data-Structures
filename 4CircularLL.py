## template of circular ll
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
## this class will contain all the methods and variables require for CLL        
class CircularLL:
    def __init__(self):
        ## initialising the head and tail pointers
        self.head=None 
        self.tail=None
 ## this method will insert at the end of cll   
    def insert(self,data):
        new_node=createNode(data)
        ## checking if first element to insert
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node ## adding at the end of tail..This will  take O(1) time
            new_node.next=self.head ## pointing to the first node and hence maintaining the circular property
            self.tail=self.tail.next
        
## this method will traverse the cll and also verify the circular property
    def traverse(self):
        if(self.head==None):
            print("Empty List") ##underflow condition
            return
        tmp=self.head
        while(tmp!=self.tail): 
            print(tmp.data) 
            tmp=tmp.next
        print(tmp.data) ## printing the last data
        print(tmp.next.data) ## printing the first node through the tail node.
        

if __name__=="__main__":
    Cll=CircularLL()
    Cll.insert(1)
    Cll.insert(2)
    Cll.insert(3)    
    Cll.insert(4)
    Cll.traverse()
        
