# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.deep = 0   #self.deep is used to control return value
        self.maxSum = -10**10
        return self.dfs(root)

    def dfs(self, root):
        if not root: return 0
        self.deep+=1
        vLeft = self.dfs(root.left)
        vRight = self.dfs(root.right)
        self.deep -=1
        self.maxSum = max(self.maxSum, vLeft+vRight+root.val)
        if self.deep == 0:
            return self.maxSum
        return max(root.val+vLeft, root.val+vRight, 0)  #pass value up   # since (vLeft+vRight+root.val) can not be passed up,  it is updated before return..       since vLeft, vRight >=0, we do not need to add a single root.val here