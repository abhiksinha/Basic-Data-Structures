## Implementation of heap using priority queue
## The Only function of a Max heap is to extract the maxm element in order 1 time
## Here we will simulate the max heap property using priority queue

from __PriorityQueue import PriorityQueue

class Heap(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
    
    def Extract_max(self):
         PriorityQueue.dequeue(self)


heap=Heap()
## enqueuing the data as its priority
## the dequeue operation will print the maximum element
heap.enqueue(9,9) ## enqueueing data as priority
heap.enqueue(6,6)
heap.enqueue(14,14)
heap.enqueue(0,0)
heap.enqueue(8,8)
heap.enqueue(2,2)
heap.enqueue(7,7)
heap.enqueue(1,1)
heap.enqueue(3,3)
while(heap.head):
    heap.Extract_max()