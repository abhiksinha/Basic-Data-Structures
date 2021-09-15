##  Implemenatation of circular queue using circular array.
##  Circular array is the linear array with modular arithmetic so that no space is wasted.
##  Overflow condition=> when front==(rear+1) mod size
##  Underflow condition=> when front==rear

## This class will contains all the basic operation of CircularQueue
class CircularQueue:
    ## size parameter should be given at the initiation
    def __init__(self,size): 
        self.front=0
        self.rear=0
        self.queue=[0]*size 
        self.size=size
        
    def enqueue(self,data):
        self.rear=(self.rear+1)%self.size
        if(self.front==self.rear): ## checking overflow condition
            print("Overflow")
            if(self.rear==0):
                self.rear=self.size-1
            else:
                self.rear-=1
            return
        else:
            self.queue[self.rear]=data 
        
    def dequeue(self):
        if(self.front==self.rear): ## checking underflow condition
            print("Queue is empty")
        else:
            self.front+=1
            print(self.queue[self.front])
  
## main program
if __name__=="__main__":
    A=CircularQueue(5)
    A.enqueue(1)
    A.enqueue(2)
    A.enqueue(3)
    A.enqueue(4)
    A.dequeue()
    A.dequeue()
    A.dequeue()
    A.dequeue()
    
        
