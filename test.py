class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=createNode(data)
        if(self.head==None):
            self.head=new_node
        
        else:
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.next=new_node
        
    def traverse(self):
        if(self.head==None):
            print("empty list")
        else:
            tmp=self.head
            while(tmp!=None):
                print(tmp.data)
                tmp=tmp.next

if __name__=="__main__":
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.traverse()

