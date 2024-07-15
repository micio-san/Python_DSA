#decklare stack
#push
# push()pop()peek()isEmpty()size()

#stack of strings 
from typing import *
myStack = [];

def push(stack):
    value = input("Add something: ")
    stack.insert(len(stack), value)

def pop(stack, len):
    pass

def peek(stack, len):
    print(stack[len -1]) 

def is_empty(stack):
    value= True if len(stack) == 0 else False
    print(value)
    return value

def size(stack):
    print(f"{len(stack)}")
    return len(stack)

def print_all(stack):
    for x in range(size(stack)):
        print(stack[x], end=", ")

def search(stack, value):
    if value in stack:
        return True
    False
    

def main():
    is_empty(myStack)
    for _ in range(3):
        push(myStack)
    print_all(myStack)
    is_empty(myStack)
    peeking= peek(myStack, size(myStack))
    search(myStack, "idx")


#class
    
class Stack:
    def __init__(self, stack, max_size) -> None:
        self.stack = stack
        self.max_size= max_size
    
    def is_empty(self):
        val = True if len(self.stack) == 0 else False
        print(val)
        return val
    
    def get_size(self):
        return len(self.stack)
    
    def push(self, value):
        self.stack.insert(self.get_size(), value)
        print(self.stack)
    
    def print_all(self):
        print(" | ".join(self.stack))

    def pop(self):
        if(self.is_empty()):
         print("Stack is empty!")  
        else:
         el = self.stack[self.get_size()-1]
         self.stack= self.stack[:self.get_size()-1]   
                   
        



my_stack = Stack([], 5)
my_stack.is_empty()  
for _ in range(3):
    value = input("Add something: ")
    my_stack.push(value)
my_stack.is_empty() 
my_stack.print_all() 
my_stack.pop()
my_stack.print_all() 
my_stack.pop()
my_stack.print_all() 
my_stack.pop()
my_stack.print_all() 
my_stack.pop()
my_stack.print_all() 

#deque