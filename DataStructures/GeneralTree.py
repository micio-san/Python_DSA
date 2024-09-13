#abstract syntax tree (AST) 
class Exp:
    pass

class Times(Exp):
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right=right
    def __str__(self) -> str:
        #recursion
        return str(self.left) + "*" + str(self.right)


class Plus(Exp):
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right=right
    def __str__(self) -> str:
        return str(self.left) + "+" + str(self.right)

class Const(Exp):
    def __init__(self, val) -> None:
        super().__init__()
        self.val=val
    def __str__(self) -> str:
        return str(self.val ) + "yaaa"

class Vars(Exp):
  def __init__(self, name) -> None:
          super().__init__()
          self.name=name
  def __str__(self) -> str:
      return self.name

e1=Times(Const(3), Plus(Vars("y"), Vars("x")))
e2=Plus(Times(Const(3), Vars("y")), Vars("x"))

#print(e1)
#print(e2)

#GeNeral tree 

class TreeNode:
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.children=[]
        self.parent = None

    def add_child(self,child ):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        print(self.data)
        if len(self.children) >0:
         for child in self.children:
             child.print_tree()
        else:
            pass
    
    def get_level(self):
        level=0;
        p=self.parent
        while p:
            level +=1
            p=p.parent
        print(level)

def buid_product_tree():
    root=TreeNode("Root")
    child = TreeNode("Child")
    root.add_child(child)
    child2 = TreeNode("Child2")
    root.add_child(child2)
    grand_child = TreeNode("Grandchild")
    child2.add_child(grand_child)
    child2.get_level()

#if __name__ == "__main__":
#    buid_product_tree()

#exercise

class Node:
    def __init__(self, data) -> None:
       super().__init__()
       self.data= data
    #    self.parent=None
       self.children = []

class Tri:
    def __init__(self) -> None:
        super().__init__()
        self.root=None
    def add_node(self, data, mom):
        new_node= Node(data)
        if mom is None:
            mom= new_node
            self.root=mom
        else:
            mom.children.append(new_node)

    def tri_pint(self):
        print(self.root.data)
    
tre =  Tri()
eh = Node(1)
tre.add_node(eh, None)
tre.tri_pint()
        




