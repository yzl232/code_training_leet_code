# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:return []
        stack = []
        stack2 = []
        stack.append(root)
        #cur = root
        while len(stack)>0:
            cur = stack.pop()
            stack2.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        results = []
        while len(stack2)>0:
            results.append(stack2.pop().val)
        return results
        