'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):  #用了start, end.  start>end return.  注意连接。 root.left = dfs()
        return self.dfs(num, 0, len(num)-1)  #然后就是mid

    def dfs(self, num, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        root = TreeNode(num[mid])
        root.left = self.dfs(num, start, mid-1)
        root.right = self.dfs(num, mid+1, end)
        return root