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
    def print(self):
        itr=self.head 
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None")
ll=LinkedList()
ll.iae(1)
ll.iae(2)
ll.iae(3)
ll.print()
        