# encoding=utf-8
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''
#Facebook的题目   这道：  给TreeNode写Iterator，使得以上代码可以in order traversal

#意思其实是实现bst  inorder traversal的iterator

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 # 分拆了binary search tree in order traversal的代码。
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack!=[]

    # @return an integer, the next smallest number
    def next(self):
        cur = self.stack.pop()
        self.pushLeft(cur.right)
        return cur.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())