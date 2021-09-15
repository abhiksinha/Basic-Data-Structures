#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for Doubly linked list(insert,traverse back and fourth,delete)


// defining the structure of doubly linked list
struct node{
    int data;
    struct node *next;
    struct node *previous;
};
struct node *head=NULL;

struct node* createNode(int data){  
   // assigning dynamic memory in heap for a new node and inserting data and next,previous pointer as null.
     struct node *new_node = (struct node*)malloc(sizeof(struct node));
     new_node->data= data; 
     new_node->next = NULL;  
     new_node->previous = NULL;  
     return new_node; 
}

void insertdoubleLL(int data){

// creating a new node 
    struct node *new_node=createNode(data);

// checking if it is the first element to insert
    if (head==NULL){
        head=new_node;
    }

// tracing the end of the list and adding the node. It is O(n) time 
    else{
        struct node *tmp= head;
        while(tmp->next!=NULL){
            tmp=tmp->next;
        }
        tmp->next=new_node; //adding the new node at end of the list
        tmp->next->previous=tmp; // assigning previous pointer of the new node
    }
}

// Function to traverse the doubly list and print from the begining and thn from the end(back n forth).
void traverseBacknForth(){

     if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
    struct node* tmp=head;
    struct node* prev=NULL;
    // First printing from the start
    while(tmp!=NULL){
        printf("%d ",tmp->data);
        prev=tmp; // taking care of the previous pointer
        tmp=tmp->next;}
    // Traversing back from the end
    while(prev!=NULL){
        printf("%d ",prev->data);
        prev=prev->previous;
     }

}

// Recursive Function to delete the entire list
void deleteList(struct node* head)
{
  if (head == NULL) return;
  deleteList(head->next);
  free(head);
}
 // Main Program
 int main(){
     insertdoubleLL(1);
     insertdoubleLL(2);
     insertdoubleLL(3);
     insertdoubleLL(4);
     traverseBacknForth();
     deleteList(head);
 }
