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
        self.result = []
        self.inOrderTraversal(root)
        l = len(self.result)
        for i in range(l-1):
            if self.result[i].val > self.result[i+1].val:
                mark1 = i
                break
        for i in range(l-1, 0, -1):
            if self.result[i].val < self.result[i-1].val:
                mark2 = i
                break
        self.result[mark1].val, self.result[mark2].val = self.result[mark2].val, self.result[mark1].val
        return root

    def inOrderTraversal(self, root):
        if not root: return
        self.inOrderTraversal(root.left)
        self.result.append(root)
        self.inOrderTraversal(root.right)
        
        
'''
 Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''