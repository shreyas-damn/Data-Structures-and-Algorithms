class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
    def add_vals(self,data_list):
        self.head=None
        for data in data_list:
            self.iae(data)
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next

ll=LinkedList()
a=[1,2,3,4,5]
ll.add_vals(a)
ll.print()