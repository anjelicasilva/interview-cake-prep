# Write a function for reversing a linked list. ↴ Do it in place. ↴
# Your function will have one input: the head of the list.
# Your function should return the new head of the list.

# Here's a sample linked list node class:

#   class LinkedListNode(object):

#     def __init__(self, value):
#         self.value = value
#         self.next  = None

# My Attempt
def reverse(head_of_list):

    # Reverse the linked list in place
    
    previous = head_of_list
    current = head_of_list.next
    previous.next = None

    while current is not None:
        previous = current
        current = curent.next
        current.next = previous
    return


    # IC Solution

def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node