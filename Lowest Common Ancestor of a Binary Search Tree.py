# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val>max(p.val, q.val): root=root.left      #偏大就往右。 偏小就往左
            elif root.val <min(p.val, q.val): root=root.right
            else: return root