from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,value):
        self.buffer.appendleft(value)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    def print(self):
        for i in self.buffer:
            print(i,end="-->")
        print("None")

bday=Queue()
bday.enqueue({
    "Name":"Udith",
    "Birthday":"24th March"
})
bday.enqueue({
    "Name":"Kaveri",
    "Birthday":"14th November"
})
bday.enqueue({
    "Name":"Bhavadharani",
    "Birthday":"15th March"
})

bday.print()