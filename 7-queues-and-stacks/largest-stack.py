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

