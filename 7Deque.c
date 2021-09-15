#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for Deque using doubly linked list using two pointers.
// doubly linked list structure
struct node{
    int data;
    struct node *next; 
    struct node *previous;
};
// Initialising head and tail pointers
struct node* head=NULL;
struct node* tail=NULL;

// Create Node function used in enqueuing
struct node* createNode(int data){

    struct node *new_node=(struct node*)malloc(sizeof(struct node));
    new_node->data=data;
    new_node->next=NULL;
    new_node->previous=NULL;
    return new_node;
}

// Enqueue at front of the node, for e.g if we have deque with elements [1,2,3] after enqueue_front(4) deque will become[4,1,2,3]
void enqueue_front(int data){
    struct node *new_node=createNode(data);
    // if first node thn assign both  head and tail pointers to this node
    if(head==NULL){ 
        head=new_node;
        tail=new_node;
    }
    else{
        // adding node in the begining(it is implemented similar to stack)
        new_node->next=head;
        head->previous=new_node; // previous pointer used to point the previous node,,it will use to dequeue from rear end.
        head=new_node;
    }
}
// Enqueue at end of the node, for e.g if we have deque with elements [1,2,3] after enqueue_rear(4) deque will become[1,2,3,4]
void enqueue_rear(int data){
    struct node *new_node=createNode(data);
     // if first node thn assign both  head and tail pointers to this node
    if(tail==NULL){ 
        head=new_node;
        tail=new_node;
    }
    else{
         // adding node at the end
        tail->next=new_node;
        tail->next->previous=tail; //assigning previous pointer of new node
        tail=tail->next;// moving tail pointer to point the last node

    }
}

// Function to dequeuue from the front. for e.g [1 2 3 4] after dequeue_front will bcm [2,3,4]
void dequeue_front(){
    //if deque is empty
    if(head==NULL){
    
        printf("deque is empty");} 

    else{
        struct node *tmp=head;
        printf("%d ",head->data); // printing the front element
        head=head->next; // head is pointing to the next node
        head->previous=NULL; 
        free(tmp); // freeing the dequeued node from the memory.
    }
}

// Function to dequeuue from the rear. for e.g [1 2 3 4] after dequeue_rear will bcm [1,2,3]
void dequeue_rear(){
    if(tail==NULL){
        printf("deque is empty");}

    else{
        struct node *tmp=tail;
        printf("%d ",tail->data); // printing the rear element
        tail=tail->previous; 
        if(tail!=NULL) // checking if tail is null(it is required as in previous line might give segmentation fault)
        tail->next=NULL;
        free(tmp);
        
    }
}

// Main program
int main(){

    // deque of data set [1 2 3 4 5 6]
     enqueue_front(3);  
     enqueue_front(2);  
     enqueue_front(1);  
     enqueue_rear(4);
     enqueue_rear(5);    
     enqueue_rear(6);
     dequeue_front();
     dequeue_front();
     dequeue_front();
     dequeue_rear();
     dequeue_rear();
     dequeue_rear();
     // expected output should be 1 2 3 6 5 4 

     
}