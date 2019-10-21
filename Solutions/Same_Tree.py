'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
'''

'''
Solution: Recursively traverse the tree at the same time
The key concept I learned here is how I can traverse the left and right subtrees at the same time to get a value
'''


def sameTree(p, q):
    if not p and not q:  # reach a null node
        return True

    if not p and q:  # if theres a node in p, but not q
        return False

    if not q and p:  # if theres a node in q, but not p
        return False

    if p.val != q.val:  # if vals dont match
        return False

    # both the left and right subtrees have to return true
    return(sameTree(p.left, q.left) and sameTree(p.right, q.right))
