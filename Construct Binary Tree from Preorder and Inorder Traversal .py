
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

'''
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder): #  #核心在于 1 找rootval。 用pre或者post  2 inorder的index找出root的位置
        if not preorder: return None
        rootV = preorder[0]
        root = TreeNode(rootV)
        lCnt = inorder.index(rootV)
        root.left = self.buildTree(preorder[1:lCnt+1], inorder[:lCnt])
        root.right = self.buildTree(preorder[1+lCnt:], inorder[1+lCnt:])
        return root
'''
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder): #  #核心在于 1 找rootval。 用pre或者post  2 inorder的index找出root的位置
        if not preorder: return None
        lCnt = inorder.index(preorder[0])
        return TreeNode(preorder[0], self.buildTree(preorder[1:lCnt+1], inorder[:lCnt]), self.buildTree(preorder[1+lCnt:], inorder[1+lCnt:]))
'''