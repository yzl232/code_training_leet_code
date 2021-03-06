'''
 Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#based on level order traversal
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#based on level order traversal

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        leftMost=root
        while leftMost:  #每层的最左边
            cur=leftMost
            while cur:  #下一层全部连起来
                if cur.left:   cur.left.next=cur.right  #和recursion的一模一样的。
                if cur.next and cur.right :   cur.right.next=cur.next.left
                cur=cur.next
            leftMost=leftMost.left

'''
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return   #自上而下。 preorder。 有逻辑顺序的。
        if root.left:  root.left.next = root.right
        if  root.next and root.right : root.right.next = root.next.left
        self.connect(root.right)  #先left也可以。 不过II的递归解法必须先right。  保持一致好了。
        self.connect(root.left)
'''