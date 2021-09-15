from __linkedlistModule import linkedlist

## Merging two sorted list without usinh any extra space   l1=14,15,16  l2=3,5,12
## the logic is that second list is merged to the first list and the first list will act as the final list

def mergelist(list1,list2):
    tmp1=list1.head
    tmp2=list2.head
    

    ## checking the first element
    ## if second list's first element is < first thn brk the link f=of 2nd list and move it to the begining of first list
    if(tmp1.data>tmp2.data):
        list1.head=list2.head
        previous=tmp2 
        tmp2=tmp2.next
        previous.next=tmp1
    else:
        previous=tmp1
        tmp1=tmp1.next
    ## now iteratively check if second list<first thn do the same
    while(tmp1!=None and tmp2!=None):
        if(tmp1.data>tmp2.data):
            current=tmp2
            tmp2=tmp2.next
            current.next=tmp1
            previous.next=current
            previous=previous.next
        else:
            tmp1=tmp1.next
            previous=previous.next
    ## merging the rest of the elemnt of list 2 if any
    if(tmp2!=None):
        previous.next=tmp2


## Main program
l1=linkedlist()
l2=linkedlist()
l1.insert(3)
l1.insert(5)
l1.insert(12)
print("traversing list 1:")
l1.traverse()
l2.insert(2)
l2.insert(7)
l2.insert(13)
l2.insert(15)
print("traversing list 2:")
l2.traverse()
mergelist(l1,l2)
print("Sorted list :")
l1.traverse()
            

    
  


    
        