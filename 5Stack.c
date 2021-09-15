#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Source code for stack using linear linked list

struct node{
    int data;
    struct node *next;
};
struct node *head=NULL;

// Function to create new node(used by push function)
struct node *createNode(int data){
    struct node *new_node=(struct node*)malloc(sizeof(struct node));
    new_node->data=data;
    new_node->next=NULL;
    return new_node;
}
// Function to push at top of stack
void push(int data){
    struct node* new_node=createNode(data);
    if (head==NULL){
        head=new_node;
    }
    else{
      new_node->next=head;// inserting at begining of the list
      head=new_node; // head will act as top of stack pointer. O(1) time per push,pop.

}}

void pop(){
    if (head==NULL){
        printf("underflow"); //underflow condition
    }
    else{
        struct node *tmp=head;
        printf("%d ",head->data); //popping from the head 
        head=head->next;
        free(tmp);
        
    }

}
// Main program
 int main(){
    push(1);
    push(2);
    push(3);
    push(4);
    pop();
    pop();
    pop();
    pop();
    pop();// testing whether underflow condition works
 }
