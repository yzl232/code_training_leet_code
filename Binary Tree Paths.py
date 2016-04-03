'''
 Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.ret = []
        self.dfs(root, "")
        return self.ret
    
    def dfs(self, root, cur, ):
        if not root: return 
        if not root.left and not root.right:
            self.ret.append(cur + str(root.val))
        self.dfs(root.left, cur + str(root.val) + "->")
        self.dfs(root.right, cur + str(root.val) + "->")