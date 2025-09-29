class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    def iae(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
    def add_values(self,data_list):
        for data in data_list:
            self.iae(data)
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None \n")
    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
ll=Linkedlist()
ll.add_values([1,2,3,4,5,6])
ll.print()
print(ll.get_len())
        