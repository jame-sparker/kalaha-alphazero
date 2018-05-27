### For storing history
import random

class Queue:
    def __init__(self, size):
        self.max_size = size
        self.size = 0
        self.array = []
        self.index = 0

    def add(self, item):
        if self.size < self.max_size:
            self.array.append(item)
            self.size += 1
        else:
            self.array[self.index] = item
            
        self.index = (self.index + 1) % self.max_size

    # random samples with uniform distribution
    def random_samples(self, size):
        return random.sample(self.array, min(size, self.size))

    def copy(self):
        queue = Queue(self.size)
        queue.size = self.size
        queue.index = self.index
        queue.array = self.array[:]
        
        return queue


