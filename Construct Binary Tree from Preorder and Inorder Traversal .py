
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder): #  #核心在于 1 找rootval。 用pre或者post  2 inorder的index找出root的位置
        if not preorder: return None   # #建立tree.    pre order
        rootV = preorder[0]
        root = TreeNode(rootV)
        lCnt = inorder.index(rootV)
        root.left = self.buildTree(preorder[1:lCnt+1], inorder[:lCnt])
        root.right = self.buildTree(preorder[1+lCnt:], inorder[1+lCnt:])
        return root