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
    def sortedArrayToBST(self, arr):  #用了start, end.  start>end return.  注意连接。 root.left = dfs()
        return self.dfs(arr, 0, len(arr)-1)  #然后就是mid

    def dfs(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        root = TreeNode(arr[mid])  # array可以random access。直接找到root
        root.left = self.dfs(arr, start, mid-1)
        root.right = self.dfs(arr, mid+1, end)
        return root