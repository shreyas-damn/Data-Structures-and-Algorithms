class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
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
            self.insert_at_end(data)
    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_len():
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
        if index<0 or index>=self.get_len():
            raise Exception
        if index==0:
            self.insert_at_begining(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                break
            count+=1
            itr=itr.next
    def remove_val(self,value):
        itr=self.head
        while itr:
            if itr.next.data==value:
                itr.next=itr.next.next
                break
            itr=itr.next
    def insert_after_val(self,value,data):
        itr=self.head
        while itr:
            if itr.data==value:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None")
        
ll=LinkedList()
ll.insert_at_begining("Shravya")
ll.print()
ll.insert_at_end("Vajih")
ll.add_values(["Inchara","Kaveri","Pranit","Udith","shreyas","Aditya","Kundan"])
ll.print()
ll.insert_at(3,"sh****g")
ll.print()
ll.remove_at(3)
ll.print()
ll.remove_val("shreyas")
ll.print()
ll.insert_after_val("Kundan","friends")
ll.print()
ll.get_len
ll.print()
            
        
        