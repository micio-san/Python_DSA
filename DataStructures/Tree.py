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
        return str(self.val)

class Vars(Exp):
  def __init__(self, name) -> None:
          super().__init__()
          self.name=name
  def __str__(self) -> str:
      return self.name

e1=Times(Const(3), Plus(Vars("y"), Vars("x")))
e2=Plus(Times(Const(3), Vars("y")), Vars("x"))

print(e1)
print(e2)