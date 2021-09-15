from __StackModule import Stack

## implementing queue using two stacks
## The implemention is a tradeoff between enqueue and dequee opearation
## If their is series of enqueue and dequeue operation thn below operation work in amortized time O(1)
## If their is alternated enqueue and dequeue operation then time complexity will be O(n) 

class Queue:
    def __init__(self):
        self.S1=Stack() ## initialising two stacks
        self.S2=Stack()

    def enqueue(self,data):
        ## if there is dequeue operation was last opearion thn copy all the elemnts from stack2 to stack 1
        while(self.S2.head!=None):
            self.S1.push(self.S2.pop())
        ## push to the top of the stack    
        self.S1.push(data)

    def dequeue(self):
        ## if enqueue operation was last opeartion thn copy all the elemnts from stack2
        while(self.S1.head!=None):
            self.S2.push(self.S1.pop())
        ## Checking underflow condtion    
        if(self.S2.head==None):
            print("Underflow")
            return
        ## printing the dequeud element    
        print(self.S2.pop())

    
if __name__=="__main__":
    Q=Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.dequeue()
    Q.dequeue()
    Q.enqueue(4)
    Q.dequeue()
    Q.dequeue()
   
     

    

