# A priority queue is a type of FIFO abstract data structure that arranges elements based on their priority values. 
# Elements with higher priority values are typically retrieved before elements with lower priority values.
# The data must be comparable, so it has to orderable by number, letter etc...

#list with insert item, remove maximum element, find maximum element(peek), check if empty

import sys

class Element:
    def __init__(self, value, priority) -> None:
        self.value=value
        self.priority=priority


class PriorityQueue:
    index=-1
    def __init__(self, queue) -> None:
        self.queue=queue
        
    def __repr__(self) -> str:
        le = len(self.queue)
        for x in range(le):
            lP = str(self.queue[x].value)

    def insertNew(self,*argv):
      PriorityQueue.index +=1
      element = Element(argv[1],argv[0])
      self.queue.insert(self.index, element)
    
    def get_size(self):
        return len(self.queue)

    def get_maximum_element(self):
        pass

    def is_empty(self):
        pass

    def find_max(self):
        temp = -1
        i=-1
        index = 0
        if self.get_size()>0:
          while index < self.get_size():
            if temp < self.queue[index].priority:
               temp=self.queue[index].priority
               i=index
               print("m")
            else:
               print("k")
            index +=1
          print(self.queue[i].value)
          return i
        else:
            print("nothing to remove")

    def main(self):
        pass



priority_queue= PriorityQueue([])

priority_queue.insertNew(4,"miao")
priority_queue.__repr__()
priority_queue.insertNew(10,"tretatretr")
priority_queue.__repr__()
priority_queue.insertNew(19,"tre")
priority_queue.insertNew(2,"bau")
priority_queue.find_max()
