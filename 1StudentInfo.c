#include<stdio.h>
#include<stdlib.h>
#include<string.h>
// Store data records in a linked list.

// Structure of Student record 
struct student{
    int roll;
    char *name;
    char *phn;
    };
typedef struct student stud; // typdef to stud for ease to use.


// Structure of linear linked list
struct node{
    stud data;
    struct node *next;
};
struct node *head=NULL; // Assigning head to null

// This function will create a new node. It is used by create function.
struct node *createNode(stud data){
    struct node *new_node=(struct node*)malloc(sizeof(struct node)); //creating space in heap
    new_node->data=data;  //assigning data and setting next pointer as null
    new_node->next=NULL; 
    return new_node;
}

// This function will create a new node and at at the end O(n) time.
void create(stud data){
    struct node *new_node=createNode(data);
    if(head==NULL){
        head=new_node; // if first element to insert
    }
    else{
        struct node *tmp=head;
        while(tmp->next!=NULL){
            tmp=tmp->next;
        }
        tmp->next=new_node; // inserting at the end
    }
}

// this function will traverse entire list and print data sequentially
void read(){
    if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
    printf("\nreading data\n");
    struct node *tmp=head;
    while(tmp!=NULL){
        printf("\nRoll: %d\n",tmp->data.roll);
        printf("name: %s\n",tmp->data.name);
        printf("phn: %s\n",tmp->data.phn);

        tmp=tmp->next;
    }


}

// this function will update the data using roll number as key
void update(int roll,stud data){
    if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
    struct node *tmp=head;
    // traversing untill find a match
    while(tmp->data.roll!=roll){ 
        tmp=tmp->next;
    }
    tmp->data=data; // update the record


}
// This function will delete the record based on roll number
void delete(int roll){
     if(head==NULL){
        printf("Empty list"); //undeflow condition
        return;
    }
     struct node *tmp=head;
     // if first record is found match delete it
     if(tmp->data.roll==roll){
         head=head->next; 
         free(tmp);
     }
     else{// else traverse the entire list, delete once found match
         while(tmp->next->data.roll!=roll){
             tmp=tmp->next;
         }
        struct node *current=tmp->next;
        tmp->next=current->next;
        free(current);
     }

}

// Main program 

int main(){
   
    stud data1={1,"Abhi","1234"};
    stud data2={2,"Amit","4321"};
    stud data3={3,"Ajay","3421"};
    stud data4={4,"Shyam","23456"};

    create(data1);
    create(data2);
    create(data3);
    create(data4);

    read();
    data1.name="Abhishek"; // updating the name of roll no  1
    update(1,data1);

    read();

    delete(2); // deleting the record with roll number 2

    read();

}