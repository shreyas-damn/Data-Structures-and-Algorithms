class Binary_search_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        #if the data given is lesser than the current data, goes into the loop
        if data<self.data:
            #if the left exists already then we give it a child 
            if self.left:
                self.left.add_child(data)
            #if the left does not exist we create a left subtreee 
            else:
                self.left=Binary_search_tree(data)
        #if the data given is bigger than the current data, goes into the loop
        else:
            #if right exists already then we give it a child
            if self.right:
                self.right.add_child(data)
            #if right doesn not exist we create a right subtree
            else:
                self.right=Binary_search_tree(data)
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()  
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()   
        return elements
        



def build_tree(elements):
    root=Binary_search_tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

numbers=[440,630,120,160,290,470]
numbers_tree=build_tree(numbers)
print(numbers_tree.in_order_traversal())

