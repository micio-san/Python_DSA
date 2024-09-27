# #a binary tree has at most 2 children and only one root and only one path between nodes
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f
# depth first traversal, first down than laterally
#0(n)

class Node:
    def __init__(self, value) -> None:
        self.value=value
        self.left = None
        self.right=None
#Iteratively=> creating a stack (left=>right)
def depth_first_value_IT(node):
    result = []
    stack= [node]
    while len(stack)>0:
         current = stack.pop() #removes the last element from an array
         result.append(current.value)
         if current.left is not None:
              stack.append(current.left)
         if current.right is not None:
              stack.append(current.right)
    print(result)
#Recursively => using recursion
def depth_first_value_REC(node):
    if node is None:
         return []
    left = depth_first_value_REC(node.left)
    right = depth_first_value_REC(node.right)
    return [node.value] + left + right 
#breadth is width, it takes all the values in a level before going down
def breadth_first_value(node):
    queue =[node]
    while len(queue)>0:
       current =queue.pop(0)
       print(current.value)
       if current.left is not None:
            queue.append(current.left)
       if current.right is not None:
            queue.append(current.right)
    print(queue)


if __name__ == "__main__":
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")
        f = Node("F")
        a.left=b
        a.right=c
        b.left=d
        b.right= e
        c.right=f
        breadth_first_value(a)


        

