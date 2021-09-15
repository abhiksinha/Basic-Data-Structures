## BST implementation

## basic template of binary tree node
class createNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

## this class will contain all the basic bst operation

class BST:
    def __init__(self):
        self.root=None  ## initialising root as null
    
    ##  Element < Parent will be stored on left and >= Parent  will store on right
    def insertnode(self,data):
        new_node=createNode(data) ## new node is created
        
        if self.root==None:
            self.root=new_node ## if the first element is inserted
            
        else:
            parent=self.root 
            ## This while loop will run untill the node is stored in the bst  
            while True:
                if(data<parent.data):
                    
                    ## if  left child of parent node is empty thn store thr.
                    if(parent.left == None):
                        parent.left=new_node
                        return 
                    parent=parent.left ## else if nodes present in left of the parent thn move left.
                    
               ## if data is >= parent thn move right    
                else:
                    
                    if(parent.right==None):
                        parent.right=new_node
                        return
                    parent=parent.right
     
    ## this method will traverse and print data inorder (LeftRootRight),,it nakes starting node as input
    def inorder(self,node): 
        if self.root==None:
            print("Tree is Empty") ## underflow condition
        
        else:
            #move to the leftmost node
            if node.left!=None:
                self.inorder(node.left)
                
            #print the data of the leftmost node    
            print(node.data)
            
            #move to the rightmost node
            if node.right!=None:
                self.inorder(node.right)
    
    

                
            
