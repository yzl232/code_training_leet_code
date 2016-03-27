'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

    Try to utilize the property of a BST.
'''
#in-order traversal 就可以了。 G家。以前做过。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        self.cnt=k;  self.ret = None
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root or self.ret:       return  #已经找到了。 不用管了。
        self.dfs(root.left)
        self.cnt-=1
        if self.cnt==0:   self.ret = root.val
        self.dfs(root.right)

'''

class Solution(object):
    def kthSmallest(self, root, k):
        self.cnt=k;  self.ret = None
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root or self.ret:       return  #已经找到了。 不用管了。
        self.dfs(root.left)
        self.cnt-=1
        if self.cnt==0:   self.ret = root.val
        self.dfs(root.right)

'''