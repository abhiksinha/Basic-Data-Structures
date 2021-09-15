#include <stdio.h>
#include <stdlib.h>
// BST implementation 

// basic structure of a node in binary tree
struct node{
    int data;
    struct node *left;
    struct node *right;
    };

    // initialising root as null
    struct node *root=NULL;
// This function  will assign values to a newnode,,it is used by insertnode function.
struct node* createnode(int data){

    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->left=NULL;
    newnode->right=NULL;
    return newnode;
}

// Insert the node as per BST rule.
// Element < Parent will be stored on left and >= Parent  will store on right
void insertnode(int data){

    struct node *newnode=createnode(data);
// if first element thn insert at root
    if(root==NULL){
        root=newnode;
        return;
    }

    else{
        struct node *parent=root;
        
      // This while loop will run untill the node is stored in the bst  
        while(1){
    // if data is < parent thn move left
        if(data < parent->data){
         // if  left child of parent node is empty thn store thr.
            if(parent->left==NULL){
                parent->left=newnode;
                return;
            }
            // else if nodes present in left of the parent thn move left.
            parent=parent->left;
            }

// if data is >= parent thn move right
        else{
            // if right child of parent node is empty thn store thr
             if(parent->right==NULL){
               parent->right=newnode;
                return;
            }
            // else move right.
             parent=parent->right;
        }

    }// while loop closing
 }// else (if root is not null) closing

}// insertnode function closing

// traverse  and print data inorder (LeftRootRight)
void inorder(struct node *node ){

    if(root=NULL){
        printf("Tree is empty");
    }

    else{
        // move to the leftmost node
        if(node->left!=NULL)
        {
        inorder(node->left);}
        // print the data
        printf("%d\n",node->data);
        // move to the rightmost node
        if(node->right !=NULL){
            inorder(node->right);
        }

    }
}
// Main program
void main(){

    insertnode(1);
    insertnode(15);
    insertnode(7);
    insertnode(16);
    insertnode(18);
    insertnode(34);

    inorder(root);

}