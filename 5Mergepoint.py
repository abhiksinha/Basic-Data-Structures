from __linkedlistModule import linkedlist


## to find the merge point both the list traversed in parallel,, once reach the end then point to the head of other list
## Next time they meet at the merge point

def mergepoint(list1,list2):
    tmp1=list1.head
    tmp2=list2.head
    if(tmp1==None or tmp2==None):
        print("Error")
        return
    while True:
        ## traversing both list with two pointers tmp1,tmp2
        tmp1=tmp1.next
        if(tmp1==None): ## once reach the end of first list thn point to the second list
            tmp1=list2.head 
        tmp2=tmp2.next
        if(tmp2==None):  ## once reach the end of second list thn point to the first list
            tmp2=list1.head

        if(tmp1==tmp2): ## they meet at the intersection point
            print("Intersection point is: "+str(tmp1.data))
            return
        

## creating list  1__2__ 3__4__5
##                       /
##              6__7____/
                
ll1=linkedlist()
ll2=linkedlist()
ll1.insert(1)
ll1.insert(2)
ll1.insert(3)
ll1.insert(4)
ll1.insert(5)
ll2.insert(6)
ll2.insert(7)
ll2.head.next.next=ll1.head.next.next
print("Traversing list 1 :")
ll1.traverse()
print("Traversing list 2 :")
ll2.traverse()
mergepoint(ll1,ll2)
    
