# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        self.result = []
        self.dfs(root, 1)
        return self.result[::-1]

    def dfs(self, root, level):
        if not root: return
        if len(self.result) < level:
            self.result.append([])
        self.result[level-1].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)