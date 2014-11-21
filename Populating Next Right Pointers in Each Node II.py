'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL


'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
 # O(1) space
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        cur=root
        while cur:
            firstNextLevel=None     #存第一个next level的node
            prev=None
            while cur:
                if not firstNextLevel:   #找第一个next level node
                    firstNextLevel=cur.left if cur.left else cur.right
                if cur.left:      #如果有pre， left。连上left
                    if prev:
                        prev.next=cur.left
                    prev=cur.left
                if cur.right:   #如果有pre。有right。梁上
                    if prev:
                        prev.next=cur.right
                    prev=cur.right
                cur=cur.next
            cur=firstNextLevel
'''
level order traversal 可以做  用O(n) space

这个递归很好， 不考虑recursion stack, 只用O(1) space

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return
        cur = root.next
        while cur:
            if cur.left:
                cur = cur.left
                break
            if cur.right:
                cur = cur.right
                break
            cur = cur.next
        if root.right:  root.right.next = cur
        if root.left:
            root.left.next = root.right if root.right else cur
        self.connect(root.right)
        self.connect(root.left)


'''