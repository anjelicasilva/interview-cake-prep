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


# IC Solution

def delete_node(node_to_delete):

    # Delete the input node from the linked list
    
    next_node = node_to_delete.next

    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        raise Exception("Can't delete the last node with this technique")

