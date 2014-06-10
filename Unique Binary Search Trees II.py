# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end: return [None]
        result = []
        for rootVal in range(start, end+1):
            leftList = self.dfs(start, rootVal-1)
            rightList = self.dfs(rootVal+1, end)
            for i in leftList:
                for j in rightList:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    result.append(root)
        return result