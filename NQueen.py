# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
def check_safe(board,row,col,n):
    if col>n-1:
        return False
    for i in range(n):
        if board[i][col]==1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    for i, j in zip(range(row,-1, -1), range(col,n,1)):
        if board[i][j] == 1:
            return False
  
    return True


def Nquin(board,row,col, n,obj):
   
    while(check_safe(board,row,col,n)!=True):
        col+=1
        if col>n-1:
            if row==0:
                print("Not possible")
                sys.exit()
            board[row-1][obj[row-1]]=0
            Nquin(board,row-1,obj[row-1]+1,n,obj)
            return
            
    
    board[row][col]=1
    obj[row]=col
    if row<n-1:
        Nquin(board,row+1,0,n,obj)
        

def print_board(board,n):
    for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
    
if __name__=="__main__":
    n=int(input())
    if(n==1):
        print(1)
    elif(n==2 or n==3):
        print("Not possible")
    else:
        obj={}
        board=[[0 for j in range(n)] for i in range(n)]
        Nquin(board,0,0,n,obj)
        print_board(board,n)
        

