
from __linkedlistModule import linkedlist


## finding loop in a list using floyd warshall agorithm
## Traverse the list using two pointers,, one slow which moves one node at a time
## 2nd is fast which moves two node at a time
## if there is loop thn after some time both fast and slow meets at some distance
## To find the entry point of the loop,,leave fast as it is and point the slow to the head of the node
## Now move fast and slow one node at a time
## the node where they meet is the starting point of the loop   


class llist(linkedlist):
    def __init__(self):
        linkedlist.__init__(self)

    def findloop(self):
        if self.head==None:
            print("Empty List")
            return

        slow=self.head.next 
        fast=self.head.next.next
        ## move pointers at different speed untill they meets
        while(slow!=fast):
            
            if(fast==None or fast.next==None): ## if loop is not present
                print("No loops")
                return
            slow=slow.next
            fast=fast.next.next
        ## pont slow to the head
        slow=self.head
        ## move pointers with same speed untill they meet
        while(slow!=fast):
            slow=slow.next
            fast=fast.next

        print("Point of loop is: " + str(slow.data))

            
            

if __name__=="__main__":

    #testing with linked list   1__2__3__4__5
    #                                  \___/

    
    l=llist()
    
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)    
    l.head.next.next.next.next.next=l.head.next.next
    l.findloop()



        
    



       
            

            

    
