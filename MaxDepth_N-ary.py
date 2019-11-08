'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

'''
Solution: The same concept as maxDepth of a BT except we just compare the depth of the current level of the node with each of its children and update accordingly as we get the depth of a node's children. 
'''


def maxDepth(self, root):
    if not root:
        return 0

    depth = 0

    for child in root.children:
        depth = max(depth, self.maxDepth(child))

    return depth + 1
