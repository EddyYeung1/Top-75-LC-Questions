'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

'''
Solution: DFS, post order traversal gets us the deepest node for each subtree and returns it to the parent
in this case, every parent grabs the max depth of either its left or right substree and adds 1 to it. We add one because we are counting itself. 
'''


def maxDepth(root):
    if not node:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right) + 1
