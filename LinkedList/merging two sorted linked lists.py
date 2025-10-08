class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class LinkedList():
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
    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def insert_at(self,data,index):
        if index==0:
            self.head=Node(data)
        if index>self.get_len() or index<0:
            raise Exception
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                break
            count+=1
            itr=itr.next
    def remove_at(self,index):
        if index==0:
            self.head=self.head.next
        if index>self.get_len() or index<0:
            raise Exception
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def print(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None")

def mergi(list1,list2):
    curr=a=Node()
    while list1 and list2:
        if list1.data>list2.data:
            curr.next=list2
            list2=list2.next
            curr=curr.next
        else:
            curr.next=list1
            list1=list1.next
            curr=curr.next
    curr.next=list1 or list2
    while a.next:
        print(a.next.data, end="-->")
        a.next = a.next.next
    print("None")





ll=LinkedList()
ll.add_values([1,2,3,4])
ll.print()
ll2=LinkedList()
ll2.add_values([5,6,7,8])
ll2.print()
mergi(ll.head,ll2.head)