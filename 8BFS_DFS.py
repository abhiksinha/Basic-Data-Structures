from __BST import BST
from __Queue import Queue
from __StackModule import Stack

## DFS AND BFS on a BST

## This class is the extention of BST class
class BST_EXTEND(BST):
    def __init__(self):
        BST.__init__(self)

    ## this function will traverse the bst in breadth first manner
    def BFS(self,node):
        if self.root==None:
            print("Tree is Empty")
        
        else:
            print(node.data) ## printing the root
            Q=Queue() ## Initialising a queue
            ## If root left and right exist just enqueue in queue
            if(node.left!=None):
                Q.enqueue(node.left)
            if(node.right!=None):
                Q.enqueue(node.right)
            ## This loop will end once all the node is visisted.It will iteretively enqueuing and dequeing from the queue
            while(Q.head!=None):
                node=Q.dequeue() 
                print(node.data)
                if(node.left!=None):
                    Q.enqueue(node.left)
                if(node.right!=None):
                    Q.enqueue(node.right)

    ## this function will traverse the bst in depth first manner using stack
    def dfs_stack(self,node):
        if self.root==None:
            print("Tree is Empty")
        else:
            print(node.data) ## printing the root
            S=Stack() ## Initialising a stack
            if(node.right!=None):
                S.push(node.right)

            if(node.left!=None):
                S.push(node.left)
             ## This loop will end once all the node is visisted.It will iteretively pushing and poping from the Stack
            while(S.head!=None):
                node=S.pop()
                print(node.data)
                if(node.right!=None):
                    S.push(node.right)
                if(node.left!=None):
                    S.push(node.left)
    
     ## this function will traverse the bst in depth first manner using recusrion
    def dfs_recursion(self,node):
        if self.root==None:
            print("Tree is Empty")

        else:
               print(node.data) 
               if(node.left!=None):
                   self.dfs_recursion(node.left)

               if(node.right!=None):
                   self.dfs_recursion(node.right)



            


        
## main Program
if __name__=="__main__":

    #  binary tree    15
    #                /  \
    #               1    18
    #                \     \
    #                  7    34
    #                 / \
    #                6   14   

    bst=BST_EXTEND()                         
    bst.insertnode(15)
    bst.insertnode(1)
    bst.insertnode(7)
    bst.insertnode(6)
    bst.insertnode(14)
    bst.insertnode(18)
    bst.insertnode(34)
    print("BFS")
    bst.BFS(bst.root)
    print("DFS using Stack")
    bst.dfs_stack(bst.root)
    print("DFS using Recursion")
    bst.dfs_recursion(bst.root)
   
