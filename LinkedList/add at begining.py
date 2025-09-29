class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def iab(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None")
ll=LinkedList()
ll.iab(1)
ll.iab(2)
ll.iab(3)
ll.print()