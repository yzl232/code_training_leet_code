'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):  #核心在于 1 找rootval。 用pre或者post  2 inorder的index找出root的位置
        if not inorder: return
        rootV = postorder[-1]
        lCnt = inorder.index(rootV)
        root = TreeNode(rootV)
        root.left = self.buildTree(inorder[:lCnt], postorder[:lCnt])
        root.right = self.buildTree(inorder[lCnt+1:], postorder[lCnt:-1])
        return root