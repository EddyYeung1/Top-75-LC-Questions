'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''

'''
Solution 1: Doing inorder traversal of a BST gets a sorted list. So traverse the tree and add the values into the array. Inorder traversal has the order of Left, Root, Right. 
'''


class Solution(object):
    def kthSmallest(self, root, k):
        self.arr = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            self.arr.append(node.val)
            traverse(node.right)

        traverse(root)

        return self.arr[k-1]
