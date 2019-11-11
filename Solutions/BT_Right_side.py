'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

'''
Solution: Do a Breadth First Search Traversal of the tree. After recording the nodes of each level, just get the last element of each level and put it into a new list for the answer. If you don't know how to do BFS refer to the problem in my other solution.  O(N) Time and Space
'''


def rightSideView(self, root):
    if not root:
        return

    bfs,q,ans = [], [], []
    size = 0

    q.append(root)

    while q:
        size = len(q)
        temp = []
        for i in range(size):
            node = q.pop()
            if node.left: q.insert(0, node.left)
            if node.right: q.insert(0, node.right)
            temp.append(node.val)
        bfs.append(temp)

    for level in bfs: #go through each level
        ans.append(level[len(level)-1]) #add the last element in each level to the ans
 
    return ans
