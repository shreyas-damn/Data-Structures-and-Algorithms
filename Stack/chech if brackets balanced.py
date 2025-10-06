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
def checki(str):
    p=p1=s=s1=c=c1=0
    for i in str:
        if i =="(":
            p+=1
        if i==")":
            p1+=1
        if i=="[":
            s+=1
        if i=="]":
            s1+=1
        if i=='{':
            c+=1
        if i=="}":
            c+=1
        
    if c==c1 and p==p1 and s==s1:
        print("balanced")

checki("({a+b})")