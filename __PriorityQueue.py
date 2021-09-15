
##  Implementation of Priority Queue using peek function and Queue.
##  Peek function will lookup all the elements in the queue and will return the highest priority.

## Basic template of priority queue
class createNode:
    def __init__(self,data,priority):
        self.data=data
        self.priority=priority
        self.next=None
        
## This Class will contain all the basic operation needed for priority queue
class PriorityQueue:
    def __init__(self):
        self.head=None ## ininitialising head and tail pointer as Null
        self.tail=None
    
    def enqueue(self,data,priority):
        ## creating new node
        new_node=createNode(data,priority)
        if self.head==None:
            ## if first element to insert 
            self.head=new_node
            self.tail=new_node
        else:
            ## inserting after the tail,,O(1) time
            self.tail.next=new_node
            self.tail=self.tail.next
            
    ##  This method will search for the highest priority in the queue. It will take O(n) time for each call.    
    def peek(self):
        highest=self.head.priority
        tmp=self.head
        while(tmp!=None):
            if(tmp.priority>highest):
                highest=tmp.priority
            tmp=tmp.next
        return highest
   
    #This method will dequeue based on the priority,, highest priority will be dequeued first.
    #This method uses peek on each call. So for n dequeue operation the time complexity is O(n^2)
    def dequeue(self):
        if self.head==None:
            print("Queue is empty")
        else:
            highest=self.peek() ## calling peek function to get the highest priority
            tmp=self.head
            
            ##finding the highest priority match(if same priority thn the element enqueued first will be dequeued)
            ## Checking whether the first element is itself having highest priority
            if tmp.priority==highest:
                print(tmp.data)
                self.head=tmp.next
                del(tmp)
                return
            
            ## Now if first element is not highest(priority) thn we can apply common logic for all the elements.  
            ## peeking one element ahead so to conserve the current node,hence deleting the actual node takes O(1) time.
            while(tmp.next.priority!=highest):
                tmp=tmp.next
            print(tmp.next.data)
            current=tmp.next 
            tmp.next=current.next
            del(current)
            
            

        
