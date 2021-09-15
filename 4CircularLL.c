#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for linear linked list(insert,traverse,delete)


// defining the structure of Circular linked list
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

// Function to insert at the end of the list
void insertCircular(int data){

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
      new_node->next=head; //new node pointing the head and hence folow the circular structure
      tail=tail->next;  // tail pointing to the newly inserted element.
    }
}
// Function to traverse the list and print from the begining.
void traverseList(){
     if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
    struct node* tmp=head;
    // loop should stop whn we reach to the tail of ll
    while(tmp!=tail){ 
        printf("%d ",tmp->data);
        tmp=tmp->next;
    }
    // printing the last element
    printf("%d ",tmp->data);
    printf("%d ",tmp->next->data); // to check the circular property
    
    

}

// Recursive Function to delete the entire list
void deleteList(struct node* head)
{
  if (head == tail) {
  free(tail);
  return;}
  deleteList(head->next);
  free(head);

}
 // Main Program
 int main(){
     insertCircular(1);
     insertCircular(2);
     insertCircular(3);
     insertCircular(4);
     traverseList();
     deleteList(head);
 }