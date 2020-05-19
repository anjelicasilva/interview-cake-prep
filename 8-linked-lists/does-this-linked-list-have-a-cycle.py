# Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

# My Attempt

def contains_cycle(first_node):

    current = first_node

    while current.next:
        current.value = "visited"
        if current.next.value == "visited":
            return True
        current = current.next

    return False