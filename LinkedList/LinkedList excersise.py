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

    def getlen(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.getlen():
            raise Exception
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next

    def insert_at(self,index,data):
        if index<0 or index>=self.getlen():
            raise Exception
        if index==0:
            self.iab(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr=itr.next
                break
            itr=itr.next
            count+=1

    def insert_after(self,data_after,data):
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
ll.insert_after("banana","Bvd")
ll.print()
                
