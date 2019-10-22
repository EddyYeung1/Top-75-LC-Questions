'''
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

'''
Solution: Just watch this video https://www.youtube.com/watch?v=MILxfAbIhrE&t=207s
'''


def validateBST(root):

    def traverse(node, lower, upper):
        if not node:  # reached end of subtree
            return True
        if node.val <= lower or node.val >= upper:  # found an invalid node
            return False

        # when traversing left subtrees, the lower bound can be anything whilst the upper bound must be the parent node
        # if any of the subtrees return false from that above condition where a node is invalid
        if not traverse(node.left, lower, node.val):
            return False

        # when traversing right subtrees, the upper bound can be anything whilst the lower bound must be the parent node
        if not traverse(node.right, node.val, upper):
            return False

        return True

    return traverse(root, float('-inf'), float('inf'))
