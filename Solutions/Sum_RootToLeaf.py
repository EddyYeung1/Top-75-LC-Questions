'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''

'''
Solution: this is just path sum mixed with a problem similar to reverse an integer. 10 is the magic number here. As we traverse the tree all we need to do is multiple our current running sum which is our val here by 10 and add the new nodes value. O(N) time and space.
'''


def sumNumbers(self, root):
    self.total = 0

    def traverse(node, val):
        if not node:
            return

        val += node.val

        traverse(node.left, val*10)
        traverse(node.right, val*10)

        if not node.left and not node.right:
            self.total += val

    traverse(root, 0)

    return self.total
