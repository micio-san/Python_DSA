#Tree includes
#        1
#       / \
#     69   11
#    / \    \
#   3   4    31

class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.left=None
        self.right=None

def find_thinghy_REC(node,target):
    if node is None:
       return False
    if node.data == target:
       return True 
    res = find_thinghy_REC(node.left, target) or find_thinghy_REC(node.right, target)
    return res

def find_thingy_IT(node, target):
    stack = [node]
    while len(stack)>0:
        current_node = stack.pop()
        if current_node.data == target:
            return True
        if current_node.left is not None:
            stack.append(current_node.left)
        if current_node.right is not None:
            stack.append(current_node.right)
    return False


if __name__ == "__main__":
      a = Node(1)
      b = Node(69)
      c = Node(11)
      d = Node(3)
      e = Node(4)
      f = Node(31)
      a.left=b
      a.right=c
      b.left=d
      b.right= e
      c.right=f
      print("qua", find_thinghy_REC(a, 12))
      print("la", find_thingy_IT(a, 1))