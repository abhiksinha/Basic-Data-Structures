from __linkedlistModule import linkedlist
from __StackModule import Stack


## reverse a ll using stack and recursion
class llist(linkedlist):
    def __init__(self):
        linkedlist.__init__(self)
    
    ## this function  will craete a stack,,push all the element whiole traversing
    ## Thn traverse and copy the popped element from stack stack
    def reverse_stack(self):
        if(self.head==None):
            print("Empty List")
            return 
        S=Stack()
        tmp=self.head
        while(tmp!=None): ## traversing first time
            S.push(tmp.data)
            tmp=tmp.next
        tmp2=self.head
        while(tmp2!=None): ## traversing  2nd time
            tmp2.data=S.pop()
            tmp2=tmp2.next

    ## thsi function  will reverse the list using recursion   
    def reverse_recursion(self,current,previous):
        if(self.head==None):
            print("Empty List")
            return 
        if(current!=None): ## if node is not
            self.reverse_recursion(current.next,current)
            current.next=previous

        else:
            self.head=previous ## making head pointer pointing the last node 


        
        


    
## Main program
if __name__=="__main__":
    ll=llist()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.reverse_stack()
    print("reversed using stack :")
    ll.traverse()
    ll.reverse_recursion(ll.head,None)
    print("re reversed using recusion :")
    ll.traverse()



    
