class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces=" "*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root=TreeNode("Nipul (CEO)")
    leva1_1=TreeNode("Chinmay (CTO)")
    leva1_2=TreeNode("Gels (HR head)")
    lev2=TreeNode("Vishwa Infra Head")
    lev2.add_child(TreeNode("Dhaval (Cloud Manager)"))
    lev2.add_child(TreeNode("Abhijeet (App Manager)"))
    leva1_2.add_child(TreeNode("Peter (Recruitment Manager)"))
    leva1_2.add_child(TreeNode("Wakas (Policy Manager)"))
    root.add_child(leva1_1)
    root.add_child(leva1_2)
    leva1_1.add_child(lev2)
    root.print_tree()

build_tree()
