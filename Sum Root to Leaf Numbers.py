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
        
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25. 
'''