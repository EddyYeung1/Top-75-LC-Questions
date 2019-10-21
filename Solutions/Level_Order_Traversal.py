'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

'''
Solution: Actually easier than it seems once we make use of a Queue. To preserve the order of the level order traversal for every node we must appends its left and right nodes into the Queue. The more tricky part is return each level as its own list. For that, we must iterate through each level on its own to preserve the order. 

This guy has a good visual on it: https://www.youtube.com/watch?v=0Zsabo7ires
'''


def levelOrderTraversal(root):
    ans = []  # list for answer
    q = []  # queue

    q.append(root)  # add the first root to the queue

    while q:  # while the q is not empty
        # we have to get the size of the q beforehand because the size of the q changes as we pop from it
        size = len(q)
        level = []  # a temporary list to store levels

        for i in range(size):
            node = q.pop()  # pop the node at the top of the q
            if node.left:
                # add left we use insert() instead because append adds to back
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)  # add right
            level.append(node)

        ans.append(level)

    return ans
