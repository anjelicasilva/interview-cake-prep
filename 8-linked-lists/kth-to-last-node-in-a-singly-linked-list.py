# Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.

# For example:

#   class LinkedListNode:

#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# a = LinkedListNode("Angel Food")
# b = LinkedListNode("Bundt")
# c = LinkedListNode("Cheese")
# d = LinkedListNode("Devil's Food")
# e = LinkedListNode("Eccles")

# a.next = b
# b.next = c
# c.next = d
# d.next = e

## Returns the node with value "Devil's Food" (the 2nd to last node)
# kth_to_last_node(2, a)




# IC Solution: First Approach

def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: %s' % k
        )

    # Step 1: get the length of the list
    # Start at 1, not 0
    # else we'd fail to count the head node!
    list_length = 1
    current_node = head

    # Traverse the whole list,
    # counting all the nodes
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    # If k is greater than the length of the list, there can't
    # be a kth-to-last node, so we'll return an error!
    if k > list_length:
        raise ValueError(
            'k is larger than the length of the linked list: %s' % k
        )

    # Step 2: walk to the target node
    # Calculate how far to go, from the head,
    # to get to the kth to last node
    how_far_to_go = list_length - k
    current_node = head
    for i in range(how_far_to_go):
        current_node = current_node.next

    return current_node