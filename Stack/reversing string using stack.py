from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def rev_str(self,str):
        for i in str:
            self.container.append(i)
        for j in range(len(self.container)-1,-1,-1):
            print(self.container[j],end="")
hihi = Stack()
hihi.rev_str("shreyas")    