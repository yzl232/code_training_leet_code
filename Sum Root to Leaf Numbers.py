# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:return 0
        if not root.left and not root.right:return root.val
        self.result = 0
        if root.left:self.getSum(root.left, root.val)
        if root.right:self.getSum(root.right, root.val)
        return self.result
    def getSum(self, root, valFromParent):
        if not root:return
        if root.left == None and root.right ==None:
            self.result += 10 * valFromParent + root.val
        self.getSum(root.left, 10 * valFromParent + root.val)
        self.getSum(root.right, 10 * valFromParent + root.val)