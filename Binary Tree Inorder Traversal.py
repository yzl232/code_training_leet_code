# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        n = root
        result = []
        while True:
            while n:
                stack.append(n)
                n = n.left
            if len(stack) == 0: break
            else:
                n = stack.pop()
                result.append(n.val)
                n = n.right
        return result