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

    def remove_at_end(self):
        pass

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

my_list = Linked_List()
my_list.insert_at_end("prima")
my_list.insert_at_end("seconda")
my_list.transverse()
my_list.insert_at_end("terza")
my_list.transverse()
print(my_list.size())
print(my_list.get_first_item())
my_list.insert_at_start("zero")
my_list.transverse()
print("last",my_list.get_last_item())
