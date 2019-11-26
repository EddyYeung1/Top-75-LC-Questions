'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
'''

'''
Solution: Similar concept to Two Sum by using a mapping except we are traversing a tree for it. At each node check to see if its complement is already in the hashmap. If it is return True otherwise return False. This method does not actually take advantage of the fact it is a BST, but I was too lazy to figure out the other way.
'''


def findTarget(self, root, k):

    mapping = {}

    def traverse(node):
        if not node:
            return False

        if k-node.val in mapping:
            return True

        if node.val not in mapping:
            mapping[node.val] = ""

        return traverse(node.left) or traverse(node.right)

    return traverse(root)
