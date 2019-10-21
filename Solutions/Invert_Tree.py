'''
Invert a binary tree.
Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

'''
Solution: same recursive approach and using post order traversal once we grab our left and right subtrees switch them hoes and return the node up the stack
'''


def invertBinaryTree(root):
    if not root:
        return None

    left = invertBinaryTree(root.left)
    right = invertBinaryTree(root.right)

    root.left = right
    root.right = left

    return root
