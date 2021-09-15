#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for Queue using linear linked list using two pointers.


// defining the structure of linear linked list
struct node{
    int data;
    struct node *next;
};
// initialising head,tail pointer to null
struct node *head=NULL;
struct node *tail=NULL;

// Function to create new node(used for insert function)
struct node* createNode(int data){  
   // assigning dynamic memory in heap for a new node and inserting data and next pointer as null.
     struct node *new_node = (struct node*)malloc(sizeof(struct node));
     new_node->data= data; 
     new_node->next = NULL;  
     return new_node; 
}

// Function to insert at the end of the list. O(1) time
void enqueue(int data){

// creating a new node 
    struct node *new_node=createNode(data);

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

void dequeue(){

    if (head==NULL){
        printf("empty queue"); //underflow condition
    }
    else{
        struct node *tmp=head; //dequeing from the head
        printf("%d ",head->data);
        head=head->next;
        free(tmp);
    }
}

int main(){
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue(); // checking underflow condition
    
}