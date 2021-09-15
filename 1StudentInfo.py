## Store data records in a linked list.

## Template of linear linked list
class createNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
## this class will contain all the methods(CRUD)
class Student_Details:
    def __init__(self):
        self.head=None ## initialising head as none
      
    ## create a record and add at the end
    def create(self,data):
        new_node=createNode(data)
        if(self.head==None):
            self.head=new_node ## if first element 
        else:
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next 
            tmp.next=new_node ## adding the record at end
        
    def read(self):
        if(self.head==None):
            print("Empty List") ##underflow condition
            return
        
        print("\nReading data")
        tmp=self.head
        while(tmp!=None):
            print(tmp.data) ## printing data sequentially
            tmp=tmp.next
       
    ## this method will update the student data based on Roll Number(unique)
    def update(self,roll,data):
        
        if(self.head==None):
            print("Empty List") ##underflow condition
            return
        
        tmp=self.head
        while(tmp.data["roll"]!=roll): 
            tmp=tmp.next
        tmp.data=data
     
    ## this method will delete the student data based on Roll Number(unique)
    def delete(self,roll):
        
        if(self.head==None):
            print("Empty List") ##underflow condition
            return
        
        tmp=self.head
        ## if the first record is itself matched thn  delete  
        if(tmp.data["roll"]==roll):
            self.head=self.head.next
            del(tmp)
        ## if not the first record thn match rest of the node and delete 
        else:
            while(tmp.next.data["roll"]!=roll):
                tmp=tmp.next
            current=tmp.next
            tmp.next=current.next
            del(current)
    
if __name__=="__main__":
   
 ## data is stored in Json format
    data1={"roll":1,
           "name":"Abhi",
           "phn":"1234"}
    data2={"roll":2,
           "name":"Amit",
           "phn":"4321"}
    data3={"roll":3,
           "name":"Ajay",
           "phn":"3421"}
    data4={"roll":4,
           "name":"Shyam",
           "phn":"23456"}
    
    ## Initiating stud object and storing data
    Stud=Student_Details()
    Stud.create(data1)
    Stud.create(data2)
    Stud.create(data3)
    Stud.create(data4)
    
    Stud.read()
    ## udating roll number 1 name
    data1["name"]="Abhishek"
    roll=1
    Stud.update(roll,data1)
    
    Stud.read()
    ## deleting student with roll 2
    Stud.delete(roll=2)
    
    Stud.read()
