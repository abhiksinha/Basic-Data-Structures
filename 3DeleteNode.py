from __linkedlistModule import linkedlist

## Delete the node given the poiter of the node
## the idea is simply copy the data and next pointer fielf of the next node and delete the next node
## this is done in O(1) time
class llist(linkedlist):
    def __init__(self):
        super().__init__()
    

    def deletenode(self,pointer):
        tmp=pointer.next 
        pointer.data=tmp.data ## copying data of next node
        pointer.next=tmp.next ## copying link of next node
        del(tmp) ## deletig the next node


## main program
ll=llist()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
pointer=ll.head.next.next ## this is pointing toi the node with  data element 3
ll.deletenode(pointer)
ll.traverse()

