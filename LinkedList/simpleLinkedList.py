class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
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
        print("none")
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_end(8)
    ll.insert_at_end(6)
    ll.insert_at_end(4)
    ll.print()