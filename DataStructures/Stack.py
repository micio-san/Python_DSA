#declare stack
#push
# push()pop()peek()isEmpty()size()

#stack of strings 
from typing import *
myStack = [];

def push(stack):
    value = input("Add something: ")
    stack.insert(len(stack), value)

def pop(self, len):
    if(self.is_empty()):
        print("Stack is empty!")  
    else:
        el = self.stack[self.get_size()-1]
        self.stack= self.stack[:self.get_size()-1]  

def peek(stack, len):
    return stack[len -1]

def is_empty(stack):
    value= True if len(stack) == 0 else False
    return value

def size(stack):
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
        return val
    
    def get_size(self):
        return len(self.stack)
    
    def push(self, value):
        self.stack.insert(self.get_size(), value)
        return self.stack
    
    def print_all(self):
        print(" | ".join(self.stack))

    def pop(self):
        if(self.is_empty()):
         print("Stack is empty!")  
        else:
         el = self.stack[self.get_size()-1]
         self.stack= self.stack[:self.get_size()-1]   
                   

#deque

# A deque (Doubly Ended Queue) is part of the collections module, it looks the same as a list, but it is faseter in 
# adding elemnts to the end and beginning, it has a time complexity of
#O(1) 

from collections import deque



class Deques:
    def __init__(self, d) -> None:
        self.d= d
    def print_first(self):
        print(self.d[0])
    def print_last(self):
        print(self.d[-1])
    def print_all(self):
        print(self.d)
    def pop(self):
        pass
    def pop_left(self):
        pass
    def append_left(self):
        pass
    def append(self):
        return self.d.append("x")
    def get_size(self):
        print(len(self.d))
        return len(self.d)


        
    

my_deque = Deques(deque())
my_deque.get_size()
my_deque.append_left()
my_deque.get_size()
my_deque.print_first()
my_deque.print_all()
