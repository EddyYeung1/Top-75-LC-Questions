'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

'''
Solution: This one is a bit tricky in my opinion. A case to consider is that when the root and subtree are the same its considered true. We need two functions to help us solve this. The first is the traverse function which traverses the two trees at the same point, and then all left subtrees with t and all right subtrees with t. 

The issue I had before was that without the traverse function, I only check the IMMEDIATE subtrees of the root and not potentially the subtress of the subtrees of the subtrees etc. 

After that all we need to do is check to make sure the values are equal in checkTree.

Time Complexity: O(M*N) M and N are the nodes of the tree and the subtree we are comparing
Space Complexity: O(N)

Apparently there is a linear time solution to this, but let's pretend there isn't
'''


def traverse(self, s, t):
    # the two expression with Traverse is actually moving down each subtree and then checking it with self.checkTree(s,t)
    return s and (self.checkTree(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))


def checkTree(self, a, b):
    if not a and not b:  # both reach the end that's gucci
        return True

    if not a or not b:  # if one node is valid and the other is not that means its not the same bad
        return False

    if a.val != b.val:  # not same val, bad
        return False

    # check subtrees
    return (self.checkTree(a.left, b.left) and self.checkTree(a.right, b.right))


def isSubtree(self, s, t):

    return self.traverse(s, t)
