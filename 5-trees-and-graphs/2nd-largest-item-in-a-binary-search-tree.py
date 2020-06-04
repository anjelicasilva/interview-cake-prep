# Write a function to find the 2nd largest element in a binary search tree. ↴

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


# My Attempt with hints

def find_largest(root_node):
    if root_node is None:
        raise ValueError('Tree must have at least 1 node')
        
    if root_node.right is not None:
        return find_largest(root_node.right)
    return root_node.value


def find_second_largest(root_node):

    # Find the second largest item in the binary search tree
    
    if (root_node is None or (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')
        
    if root_node.left and not root_node.right:
        return find_largest(root_node.left)
        
    if (root_node.right and not root_node.right.right and not root_node.right.left):
        return root_node.value
        
    return find_second_largest(root_node.right)


# IC Solution

def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right