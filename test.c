// #include<stdio.h>
// #include<stdlib.h>
// #include<string.h>

// struct node{
//     int data;
//     struct node *next;
// };
// struct node* head=NULL;

// struct node *createNode(int data){
//     struct node* new_node=(struct node*)malloc(sizeof(struct node));
//     new_node->data=data;
//     new_node->next=NULL;
//     return new_node;
// }

// void insert(int data){
//     struct node* new_node=createNode(data);
//     if(head==NULL){
//         head=new_node;
//     }
//     else{
//         struct node *tmp=head;
//         while(tmp->next!=NULL){
//             tmp=tmp->next;
//         }
//         tmp->next=new_node;
//     }
// }

// void traverse(){
//     if(head==NULL){
//         printf("empty list");
//         return;
//     }
//     struct node *tmp=head;
//     while(tmp!=NULL){
//         printf("%d",tmp->data);
//         tmp=tmp->next;
//     }
// }

// void delete(struct node *head)
// {
//     if(head==NULL)return;
//     delete(head->next);
//     free(head);
// }
// int main(){
//      insert(1);
//      insert(2);
//      insert(3);
//      insert(4);
//      traverse(head);
//      delete(head);
//  }

