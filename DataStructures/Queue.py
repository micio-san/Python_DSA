#A queue is a linear Fifo data structure, it is a collection designed to hold elements prior to processing,
#enqueue is the process of adding, while dequeue is the process of removing

class Queue:
    def __init__(self, queue, max_size) -> None:
        self.queue=queue
        self.max_size=max_size

    def enqueue(self, value):
        if self.max_size >= self.get_size():
         idx = self.get_size()
         self.queue.insert(idx, value)
    
    def dequeue(self):
        if self.get_size()>0:
            item = self.queue[0]
            print(item)
            self.queue = self.queue[1:self.get_size()]
            print(self.queue)
            return self.queue

    def get_head(self):
        return self.queue[0] if my_queue.get_size()>0 else ""

    def get_tail(self):
        idx = self.get_size() -1
        return self.queue[idx] if my_queue.get_size()>0 else ""

    def get_size(self):
        return len(self.queue)
    

my_queue = Queue([], 5)
print(my_queue.get_size())
print(my_queue.get_tail())
for _ in range(3):
    value = input("Add something: ")
    my_queue.enqueue(value)
print(my_queue.get_size())
print(my_queue.get_tail())
my_queue.dequeue()