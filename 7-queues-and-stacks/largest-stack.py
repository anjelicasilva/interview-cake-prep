# You want to be able to access the largest element in a stack.
# Use your Stack class to implement a new class MaxStack with a method get_max() that returns the largest element in the stack. get_max() should not remove the item.

# My Attempt
class MaxStack(object):

    def __init__(self):
        self.stack = Stack()

    def get_max():
        max = 0
        for number in Stack().items:
            if number > max:
                max = number
        return max

# IC Solution
class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()