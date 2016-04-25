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



class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        dummy = TreeNode(0);  cur = root
        while cur:
            pre = dummy;  dummy.next = None   # dummy.next就是每层的第一个node,  也就是firstN
            while cur:     # 想象一下， dummy， pre都是下一层的。  上一层的是cur
                if cur.left:   #和下面的区别是dummy避免了pre为空得情况
                    pre.next = cur.left ;  pre = pre.next
                if cur.right:
                    pre.next = cur.right;  pre = pre.next
                cur = cur.next
            cur = dummy.next

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
            firstN=None     #存第一个next level的node
            prev=None
            while cur:
                if not firstN:   #找第一个next level node
                    firstN=cur.left if cur.left else cur.right
                if cur.left:      #如果有pre， left。连上left
                    if prev:           prev.next=cur.left
                    prev=cur.left
                if cur.right:   #如果有pre。有right。梁上
                    if prev:        prev.next=cur.right
                    prev=cur.right
                cur=cur.next
            cur=firstN

level order traversal 可以做  用O(n) space

这个递归很好， 不考虑recursion stack, 只用O(1) space

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return
        x = self.getNext(root.next)
        if root.right: root.right.next = x
        if root.left:
            root.left.next = root.right if root.right else x
        self.connect(root.right)  #顺序重要.  逻辑上要求右边决定好next.  getNext才有效
        self.connect(root.left)

    def getNext(self, cur):
        while cur:
            if cur.left: return cur.left
            if cur.right:   return cur.right
            cur = cur.next

'''