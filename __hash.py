class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size

    def insert(self,data):
        key=data
        i=0
        while(self.table[key%self.size]):
            i+=1
            key=data+i**2
            
        self.table[key%self.size]=data

    def search(self,data):
        key=data
        i=0
        while(self.table[key%self.size]):
            if self.table[key%self.size]==data:
                return True
            i+=1
            key=data+i**2
            

        return False