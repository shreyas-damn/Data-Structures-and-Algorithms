class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def iab(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def iae(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node

    def add_values(self,datalist):
        for data in datalist:
            self.iae(data)

    def insert_after_value(self,data_after,data):
        itr=self.head
        while itr:
            if itr.data==data_after:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next

    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("none \n")
ll=LinkedList()
ll.add_values(["apple","banana","orange","pineapple","kiwi"])
ll.print()
ll.insert_after_value("banana","Bvd")
ll.print()