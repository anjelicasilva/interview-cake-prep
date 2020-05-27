# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).

# A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

# Here's a sample binary tree node class:

#   class BinaryTreeNode(object):

#     def __init__(self, value):
#         self.value = value
#         self.left  = None
#         self.right = None

#     def insert_left(self, value):
#         self.left = BinaryTreeNode(value)
#         return self.left

#     def insert_right(self, value):
#         self.right = BinaryTreeNode(value)
#         return self.right


# My Attempt

def is_balanced(tree_root):

    # Determine if the tree is superbalanced
        
    to_visit = [(tree_root, 1)]
    minimum = None

    while to_visit:
        current, level = to_visit.pop(0)


        if (current.left is None or current.right is None) and minimum is None:
            minimum = level
        
        if minimum and (level > minimum + 1):
            return False

        else:
            if current.left:
                to_visit.append((current.left, level + 1))

            if current.right:
                to_visit.append((current.right, level + 1))

    return True