
## Implementing  max heap using build heap method
## build heap will work if all the data is present(in an array)
## Build heap will take O(n) time to implement a heap(max or min)

## this is heapify function,, it will work whn left and right subtree of a node is a maxheap.
## this method takes O(logn) time  
def max_heapify(arr,i,n):
    left=2*i+1 ## left and right children of a node
    right=2*i+2
    ## finding the largest among node and its childrens
    largest=i 
    if (left<n and arr[left]>arr[i]):
        largest=left
        
    if (right<n and arr[right]>arr[largest]):
        largest=right

    ## if node is not largest i.e max heap property fails thn  swap the node with largest and again apply max heapify recusively
    
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,largest,n)


    return arr

## this method will work on max heapify funxction
## It will call from the parent of the last leaf down to root
def build_heap(arr,n):
    i=n//2 -1 ## the first leaf index is at n//2 so -1 will be the index parent of last leaf
    while(i>=0):
        arr=max_heapify(arr,i,n)
        i-=1
    return arr

## this function will extract the maximum from the heap(O(logn) time)
def extract_max(arr,n):
    print("extracting maximum :" + str(arr[0])) 
    arr[0],arr[-1]=arr[-1],arr[0]  ##swapping last element with tyhe first
    n=n-1  ## Decreasing the heap size
    max_heapify(arr,0,n) ## apply the max heapify function to make it max heap
    return arr,n  

## main program 

    # binary tree     9
    #                /  \
    #               6    14
    #              / \   / \
    #             0   8 2   7
    #            / \  
    #           1   13

arr=[9,6,14,0,8,2,7,1,3]
heap_size=len(arr)
arr=build_heap(arr,heap_size)
print("Printing heap:")
print(arr[0:heap_size])
arr,heap_size=extract_max(arr,heap_size)
print("Printing heap after max extracted:")
print(arr[0:heap_size])
