# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root: return 
        if root.left:  self.invertTree(root.left)
        if root.right: self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
        
'''
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root: return []
        pre = [root]   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
                n.left, n.right = n.right, n.left
            pre = cur
        return root
'''