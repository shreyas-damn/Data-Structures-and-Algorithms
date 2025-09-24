class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def print(self):
        if self.head is None:
            print("the list is empty")
            return
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
    def insert_val(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_len(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

if __name__=="__main__":
    ll=Linkedlist()
    ll.insert_val([1,2,3,4,5,6,7,8])
    ll.print()
    print("\nlength of the linked list= ",ll.get_len())
        
        