# Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.

# My Attempt

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

    def delete_node(item):
        current = self.value

        while current.next:
            if current.next == item:
                current.next = current.next.next
            current = current.next
