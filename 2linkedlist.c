#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for linear linked list(insert,traverse,delete)


// defining the structure of linked list
struct node{
    int data;
    struct node *next;
};
// initialising head pointer to null
struct node *head=NULL;

// Function to create new node(used for insert function)
struct node* createNode(int data){  
   // assigning dynamic memory in heap for a new node and inserting data and next pointer as null.
     struct node *new_node = (struct node*)malloc(sizeof(struct node));
     new_node->data= data; 
     new_node->next = NULL;  
     return new_node; 
}

// Function to insert at the end of the list
void insert(int data){

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
        tmp->next=new_node;
    }
}
// Function to traverse the list and print from the begining.
void traverseList(struct node* head){
     if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
    struct node *tmp=head;
    while(tmp!=NULL){
        printf("%d ",tmp->data);
        tmp=tmp->next;
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
     insert(1);
     insert(2);
     insert(3);
     insert(4);
     traverseList(head);
     deleteList(head);
 }