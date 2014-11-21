
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
    def buildTree(self, preorder, inorder):
        if len(preorder) ==0: return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        left_count = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:1+left_count], inorder[:left_count])
        root.right = self.buildTree(preorder[1+left_count:], inorder[1+left_count:])
        
        return root
        
