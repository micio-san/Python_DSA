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
        index = self.find_max()
        element = self.queue[index]
        del self.queue[index]
        self.__repr__()
        return element

    def is_empty(self):
        True if PriorityQueue.index== -1 else False

    def find_max(self):
      temp=-sys.maxsize
      i=0
      index_to_return=-1
      while PriorityQueue.index > i:
          if self.queue[i].priority >= temp:
              temp= self.queue[i].priority
              index_to_return=i
          i+=1
      return index_to_return
    
    def main(self):
        self.insertNew(4,"miao")
        self.__repr__()
        self.insertNew(10,"tretatretr")
        self.__repr__()
        self.insertNew(21,"tre")
        self.insertNew(19,"trent")
        self.insertNew(2,"bau")
        self.get_maximum_element()



if __name__=="__main__":
  priority_queue= PriorityQueue([])
  priority_queue.main()

    #    tempPriority = -1
    #     i=-1
    #     index = 0
    #     if self.get_size()>0:
    #       while index < self.get_size():
    #         if tempPriority < self.queue[index].priority:
    #            tempPriority=self.queue[index].priority
    #            i=index
    #         elif :
    #            print("k")
    #         index +=1
    #       print(self.queue[i].value)
    #       return i
    #     else:
    #         print("nothing to remove")

