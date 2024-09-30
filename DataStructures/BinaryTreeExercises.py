import functools
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


# if __name__ == "__main__":
#       a = Node(1)
#       b = Node(69)
#       c = Node(11)
#       d = Node(3)
#       e = Node(4)
#       f = Node(31)
#       a.left=b
#       a.right=c
#       b.left=d
#       b.right= e
#       c.right=f
#       print(find_thinghy_REC(a, 12))
#       print(find_thingy_IT(a, 1))

#Tree sum
# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
# The function should return the total sum of all values in the tree.

#      7
#     / \
#    8   2
#   /   / \
#  3   1   9
 
def breadth_fist_sum(root):
    queue=[root]
    result_list=[]
    while len(queue)>0:
        first = queue.pop(0)
        result_list.append(first.data)
        if first.left is not None:
            queue.append(first.left)
        if first.right is not None:
            queue.append(first.right)
    result=0
    for res in result_list:
        result += res
    print(result)


def depth_first_iterative_sum(root):
    stack=[root]
    result_list=[]
    while len(stack)>0:
        first=stack.pop()
        result_list.append(first.data)
        if first.left is not None:
            stack.append(first.left)
        if first.right is not None:
            stack.append(first.right)
    res = functools.reduce(lambda a,b:a+b,result_list)
    print(res)
    
    

def depth_first_recursive_sum(node,val):
    if node is None:
        return ["nada"]
    val = val + node.data
    print(node.data, end="/")
    left = depth_first_recursive_sum(node.left, val)
    right= depth_first_recursive_sum(node.right, val)
    return val
            

if __name__ == "__main__":
    A = Node(7)
    B=Node(8)
    C=Node(2)
    D=Node(3)
    E=Node(1)
    F=Node(9)
    A.left=B
    B.left=D
    A.right=C
    C.left=E
    C.right=F
    # depth_first_iterative_sum(A)
    print(depth_first_recursive_sum(A,0))
