#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Implementation of Priority Queue using peek function and Queue.
// Peek function will lookup all the elements in the queue and will return the highest priority.

// Basic structure of priority queue
struct node{
    int data;
    int priority;
    struct node *next;
};
// initialising head,tail pointer to null
struct node *head=NULL;
struct node *tail=NULL;

// Function to create new node(used for insert function)
struct node* createNode(int data,int priority){  
   // assigning dynamic memory in heap for a new node and inserting data and next pointer as null.
     struct node *new_node = (struct node*)malloc(sizeof(struct node));
     new_node->data= data; 
     new_node->priority=priority; 
     new_node->next = NULL;  
     return new_node; 
}

// Function to insert at the end of the list. O(1) time
void enqueue(int data,int priority){

// creating a new node 
    struct node *new_node=createNode(data,priority);

// checking if it is the first element to insert
    if (head==NULL){
        head=new_node;
        tail=new_node;
    }

// Adding new node after tail.
    else{
      tail->next=new_node;
      new_node->next=NULL; 
      tail=tail->next;  // tail pointing to the newly inserted element.
    }
}
// This function will search for the highest priority in the queue. It will take O(n) time for each call.
int peek(){
    struct node *tmp=head;
    // using basic maximum finding algorithm 
    int highest=tmp->priority;
    while(tmp!=NULL){
        if(tmp->priority> highest){
            highest=tmp->priority;
        }
        tmp=tmp->next;

    }

  return highest;
   

}

// This function will dequeue based on the priority,, highest priority will be dequeued first.
// This function uses peek on each call. So for n dequeue operation the time complexity is O(n^2)
void dequeue(){
    if (head==NULL){
        //underfloqw condition
        printf("Empty Queue");
        return;
    }
    int highest=peek();// calling peek function to get the highest priority
    struct node *tmp=head;
    // finding the highest priority match(if same priority thn the element enqueued first will be dequeued)
    // Checking whether the first element is itself having highest priority
    if(tmp->priority==highest){
        printf("%d ",tmp->data);
        head=head->next;
        free(tmp);
    }
    // Now if first element is not highest(priority) thn we can apply common logic for all the elements.
    else{
        //peeking one element ahead so to conserve the current node,hence deleting the actual node takes O(1) time.
    while(tmp->next->priority!=highest){ 
        tmp=tmp->next;
    }
    printf("%d ",tmp->next->data); // printing the data 
    struct node* current=tmp->next; // the actual node with highest priority which we have to delete is stored in current
    tmp->next=current->next;
    free(current);

}}
//  Main program
int main(){
    enqueue(12,1);
    enqueue(16,4);
    enqueue(1,2);
    enqueue(24,7);
    dequeue();
    dequeue();
    dequeue();
    dequeue();

}