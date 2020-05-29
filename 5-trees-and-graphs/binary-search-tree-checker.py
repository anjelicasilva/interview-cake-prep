# Write a function to check that a binary tree ↴ is a valid binary search tree. ↴

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