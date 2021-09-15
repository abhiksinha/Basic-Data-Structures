#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define size 5 
// Implemenatation of circular queue using circular array.
// Circular array is the linear array with modular arithmetic so that no space is wasted.
// Overflow condition=> when front==(rear+1) mod size
// Underflow condition=> when front==rear

int queue[size];
int front=0,rear=0; 

// function  to enqueue in the queue.
void enqueue(int data){
rear=(rear+1)%size;
// first checking the overflow condition
if(front==rear){
    printf("Queue is full ");
    // have to make rear node pointing to the last element(as we already incremented)
    if(rear==0) 
       rear=size-1;
    else
      rear--;  
    
    }
    // if no overflow store the data
else{
    queue[rear]=data;
    }
}

void dequeue(){
    //checking the underflow condition
    if(front==rear){
        printf("Queue is empty");
    }
    else{
        //dequeuing the data from the front node.
        front=(front+1)%size;
        printf("%d ",queue[front]);
    }
}
// Main program
int main(){
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
}