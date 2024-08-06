#A linked list is a way to store data linearly in memory, where every element contains it's data and a pointer to the next element in it,
# which are called nodes, it's storage capacity is dynamic and allocated at runtime, it's maximum size depends on heap.

#example for stupid people (i.e: me)

class MyNodeEl:
     def __init__(self, data) -> None:
          self.data=data
          self.next = None

class ThisIsTheList:
    def __init__(self, first=None) -> None:
         #Punto di ingresso alla linked list
         self.head=first
    def get_size(self):
         idx=0;
         while self.head.next != None:
              idx +=1
              self.head = self.head.next
         return idx
    def get_last(self):
         while self.head.next != None:
              self.head=self.head.next
         else:
              return self.head.data
    def get_first(self):
         return self.head.data
    

node1= MyNodeEl("prima")
node2=MyNodeEl("seconda")
node1.next=node2
node3=MyNodeEl("terza")
node2.next=node3
lista= ThisIsTheList(node1)

class Node:
    def __init__(self, data=None) -> None:
        self.data=data
        #the last element in the linked list will always have it's pointer set to none!!
        self.next=None

class Linked_List:
    def __init__(self) -> None:
        #the head node is never gonna contain any actual data and will never be indexable, it's just a placeholder to point to the 1st Node in the list
        #this is not going to be one of the data nodes, it has no info.
        self.head=Node() 

    def append(self,data):
        #we create the first node, pass the data in it the create the holder to the current Node, which in the first iteration is the head_node
        new_node=Node(data)
        curr= self.head
        #iterate from head until we reach the point where the next node is equal to None, then we insert at the end there
        while curr.next != None:
              #traverse the list
              curr = curr.next
        #when next is none append new node which is 
        curr.next=new_node
    
    def length(self):
        curr=self.head
        total_nodes=0
        while curr.next != None:
            total_nodes += 1
            curr = curr.next
        return total_nodes
    
    def display_content(self):
        elems=[]
        curr= self.head
        while curr.next != None:
                  curr = curr.next  
                  elems.append(curr.data)  
        print(elems)
    
    def get(self, idx):
         if idx >= self.length():
              print("error, index our of range")
              return None
         curr_idx=0
         curr_node=self.head
         while True:
              curr_node= curr_node.next
              if curr_idx == idx:
                   return curr_node.data
              curr_idx += 1

    def del_node(self, idx):
        if idx >= self.length():
             print("error, index our of range")
             return None
        curr_idx=0
        curr_node=self.head
        while True:
             last_node= curr_node
             curr_node= curr_node.next
             if curr_idx == idx:
                   last_node.next= curr_node.next
                   return
             curr_idx +=1

