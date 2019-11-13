'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

'''
Solution 1: Using DFS we can keep track of the runningSum and once we reach a leaf we can decide whether the running sum is equal the sum we are targetting for. O(N) time because we have to go to every node, O(N) space for both each recursive call and list for storing the path. 
'''


def pathSum(self, root, sum):
    ans = []

    def traverse(node, runningSum, path):
        if not node:
            return

        runningSum += node.val #add to running sum
        path.append(node.val) #add node to path 

        traverse(node.left, runningSum, path) 
        traverse(node.right, runningSum, path)

        if runningSum == sum and not node.left and not node.right: #once we reach a leaf check the sum  
            #we append path[:] because we want a reference copy of the path, if we were to just add the path it will be manipulated throughout the recursive calls and not give you the correct paths.
            ans.append(path[:])  

        path.pop() #when we finished visiting nodes remove from the path 

    traverse(root, 0, [])
    return ans
