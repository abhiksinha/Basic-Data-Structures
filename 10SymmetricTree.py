
   
## Finding Tree is symmetric or not on every node
## It is same as asking if the given binary tree is complete?
## The criteria of complete binary tree is that leaf=2^height

## Basic binary tree   
class Binary_Tree:
     def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

## This function will find height of the tree
def find_height(node):
    if node==None:
        return -1  
    
    l=find_height(node.left) ## going to the depth
    r=find_height(node.right)
    return 1+max(l,r) ## as we reach leaf add +1,,it is bottom up approach

## this function will find number of leaf      
def count_leaf(node):
    if node==None: 
        return 0
    if(node.left==None and node.right==None): ## we are at leaf node
        return 1
    else:
        return count_leaf(node.left)+ count_leaf(node.right) ## returning the leaf


## this function will check if leaf=2^h       
def symmetry(node):
    height=find_height(node)
    leaf=count_leaf(node)
    if (leaf==2**height):
        print("The Tree is symmetric")
    else:
        print("The Tree is not symmetric")
         
## main Program       
if __name__=="__main__":
    root=Binary_Tree(1)
    root.left=Binary_Tree(2)
    root.right=Binary_Tree(3)
    root.left.left=Binary_Tree(4)
    root.left.right=Binary_Tree(5)
    root.right.left=Binary_Tree(6)
    root.right.right=Binary_Tree(7)
 

    symmetry(root)