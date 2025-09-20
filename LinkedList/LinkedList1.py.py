class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        Node=node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("empty linked list")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head=node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node(data,None)
if __name__=='__main__':
    ll=linkedlist()
    ll.insert_at_begining(0)
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.insert_at_begining(5)
    ll.print()

