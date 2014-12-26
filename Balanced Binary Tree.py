'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def isBalanced(self, root):
        return self.checkHeight(root)!=-1

    def checkHeight(self, root):
        if not root: return 0
        lh, rh = self.checkHeight(root.left), self.checkHeight(root.right)
        if lh==-1 or rh==-1 or abs(lh-rh)>1: return -1
        return max(lh, rh)+1

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def isBalanced(self, root):
        if not root: return True
        if abs(self.depth(root.left) - self.depth(root.right))>1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left)+1, self.depth(root.right)+1)
'''