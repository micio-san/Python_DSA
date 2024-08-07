#size- first - last - transverse - add at start- remove at start- remove- remove by idx- add by idx - search:


class Node:
    def __init__(self, data=None) -> None:
        self.data=data
        self.next = None

class Linked_List:
    def __init__(self) -> None:
        self.head= Node()

    def insert_at_end(self, data):
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        current_node.next= Node(data)

    def insert_at_start(self, data):
        current_node=self.head
        new_node= Node(data)
        container_for_current_next= current_node.next
        current_node.next=new_node
        new_node.next=container_for_current_next

    def insert_at_idx(self, idx, data):
        index=0
        current_node=self.head
        new_node=Node(data)
        if idx>self.size():
           print("wrong!")
        else:
            while current_node.next is not None:
                prev= current_node
                index +=1
                current_node=current_node.next
                if index == idx:
                    prev.next=new_node
                    new_node.next=current_node
                 

    def remove_at_end(self):
        current_node= self.head
        while current_node.next is not None:
            current_node=current_node.next
        del current_node

    def remove_at_start(self):
        self.head=self.head.next
    
    def remove_at_idx(self, idx):
        current_node=self.head
        index=0
        if idx>self.size():
           print("wrong!")
        else:
            while current_node.next is not None:
               prev= current_node
               index +=1
               current_node=current_node.next
               if index == idx:
                   prev.next= current_node.next


    def transverse(self):
        container=[]
        current_node= self.head
        while current_node.next is not None:
            #prima va avanti di uno per saltare la testa
            current_node=current_node.next
            container.append(current_node.data)
        print(container) 
    
    def size(self):
        current_node=self.head
        idx=0
        while current_node.next is not None:
            current_node=current_node.next
            idx +=1
        return idx
    
    def get_first_item(self):
        current_node=self.head
        while current_node.next is not None:
            return self.head.next.data
        return "list is empty!"
    
    def get_last_item(self):
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        return current_node.data
    
    def search_by_idx(self, idx):
        current_node=self.head
        index=0
        if idx>self.size():
            print("wrong!")
        else:
            while current_node.next is not None:
                index +=1
                current_node=current_node.next
                if index == idx:
                    print("by idx ", current_node.data)
            
