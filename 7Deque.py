##Source code for Deque using doubly linked list using two pointers.
## basic template of doubly ll
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
        
## this class will contain all the methods and variables for Dequeue
class Deque:
    def __init__(self):
        ## initalising head and tail pointer as Null
        self.head=None 
        self.tail=None
        
    ## this method will enqueue at front,for e.g if we have deque with elements [1,2,3] after enqueue_front(4) deque will become[4,1,2,3]
    def enqueue_front(self,data):
        new_node=createNode(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head ## inserting at begining of the node
            self.head.previous=new_node
            self.head=new_node
            
    ## this method will  Enqueue at end of the node, for e.g if we have deque with elements [1,2,3] after enqueue_rear(4) deque will become[1,2,3,4]
    def enqueue_rear(self,data):
        new_node=createNode(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node ## inserting at the end
            new_node.previous=self.tail
            self.tail=self.tail.next
     
    
    # this method will  dequeuue from the front. for e.g [1 2 3 4] after dequeue_front will bcm [2,3,4]
    def dequeue_front(self):
        if self.head==None:
            ## if deque is empty
            print("Queue is empty")
        else:
            tmp=self.head
            print(tmp.data)
            self.head=self.head.next
            self.previous=None
            del(tmp)  ##freeing the dequeued node from the memory.
     
    # this method will dequeuue from the rear. for e.g [1 2 3 4] after dequeue_rear will bcm [1,2,3]
    def dequeue_rear(self):
        if self.tail==None:
            print("Queue is empty")
        else:
            tmp=self.tail
            print(tmp.data)
            self.tail=self.tail.previous
            if self.tail!=None: ##checking if tail is null(it is required as in previous line might give segmentation fault)
                self.tail.next=None
            del(tmp) ##freeing the dequeued node from the memory.
if __name__=="__main__":
    ## deque of data set [1 2 3 4 5 6]
    A=Deque()
    A.enqueue_front(3)
    A.enqueue_front(2)
    A.enqueue_front(1)
    A.enqueue_rear(4)
    A.enqueue_rear(5)
    A.enqueue_rear(6)
    A.dequeue_front()
    A.dequeue_front()
    A.dequeue_front()
    A.dequeue_rear()
    A.dequeue_rear()
    A.dequeue_rear()
    ## expected output should be 1 2 3 6 5 4 
 
