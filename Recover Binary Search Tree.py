'''
 Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.prev = self.n1= self.n2 = None
        self.dfs(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.prev and self.prev.val > root.val:
            self.n2 = root
            if not self.n1: self.n1 = self.prev
        self.prev = root
        self.dfs(root.right)

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.pValue = []; self.p = []
        self.dfs(root)
        self.pValue.sort()
        for i in range(len(self.p)):
            self.p[i].val = self.pValue[i]
        return root

    def dfs(self, root): #inorder traversal
        if not root: return
        self.dfs(root.left)
        self.p.append(root); self.pValue.append(root.val)
        self.dfs(root.right)

'''