'''
 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]


'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, s):
        self.ret = []
        self.dfs(root, s, [])
        return self.ret
    
    def dfs(self, root, s, cur):
        if not root: return
        if not root.left and not root.right and s == root.val:
            self.ret.append(cur + [root.val])
            return
        self.dfs(root.left, s-root.val, cur+[root.val])
        self.dfs(root.right, s-root.val, cur+[root.val])
        
        
