from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def append(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def print(self):
        for i in self.container:
            print(i,end="------>")
        print("None")
stack=Stack()
stack.append("Shreyas")
stack.append("Pravallika")
stack.append("Chechi")
stack.append("Udith")
stack.print()       
stack.pop()
stack.print()
print(stack.size())
print(stack.peek())
stack.pop()
stack.print()
stack.pop()
stack.print()
stack.pop()
stack.print()
print(stack.is_empty())