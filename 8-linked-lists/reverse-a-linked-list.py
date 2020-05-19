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