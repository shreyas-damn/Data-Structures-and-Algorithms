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
    def iae(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
    def add_vals(self,data_list):
        for data in data_list:
            self.iae(data)
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
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def insert_at(self,idx,data):
        if idx<0 or idx>=self.get_len():
            raise Exception
        if idx==0:
            self.iab(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==idx-1:
                new_node=Node(data,itr.next)
                itr.next=new_node
                break
            
            itr=itr.next
            count+=1
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end='-->')
            itr=itr.next
        print("none \n")

ll=LinkedList()
ll.add_vals([1,2,3,4,5])
ll.print()
ll.remove_at(3)
ll.print()
ll.insert_at(3,4)
ll.print()
