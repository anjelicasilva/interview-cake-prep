# Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).

# My Attempt

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.in_stack = []
        self.out_stack =[]

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                add_item = self.in_stack.pop()
                self.out_stack.append(add_item)
        return add_item


# IC Solution

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.in_stack = []
        self.out_stack =[]

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                add_item = self.in_stack.pop()
                self.out_stack.append(add_item)
        return self.out_stack.pop()
