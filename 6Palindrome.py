from __linkedlistModule import linkedlist
from __StackModule import Stack

## checking if given list is palindrome
## Traverse the list and push all the elements in a stack
## Traverse the list again, pop from stack and match each elements  
def palindrome(list):
    if(list.head==None):
        print("List is empty")
        return
    tmp=list.head
    S=Stack() ## initialsing stack

    ## traversing first time,pushing all the elements in stack
    while(tmp!=None):
        S.push(tmp.data)
        tmp=tmp.next
    tmp=list.head
    ## traversing 2nd time poping element and matching
    while(tmp!=None):
        if(tmp.data!=S.pop()): ## if not matched
            print("List is not Palindrome")
            return
        tmp=tmp.next
        
    print("The list is palindrome")


ll=linkedlist()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(1)
print("traversing the list:")
ll.traverse()
palindrome(ll)
