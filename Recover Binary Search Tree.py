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

class Solution:       #显然要in order
    # @param root, a tree node   # http://www.cnblogs.com/zuoyuan/p/3746594.html
    # @return a tree node
    def recoverTree(self, root):
        self.pre = self.n1= self.n2 = None  #pre用来root.val与前面比较
        self.dfs(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre and self.pre.val > root.val:  #发现逆序
            self.n2 = root
            if not self.n1: self.n1 = self.pre  #n1只更新第一次
        self.pre = root
        self.dfs(root.right)


'''
举简单例子。
   2
3     1


交换了1， 3.

例如一颗被破坏的二叉查找树如下：

　　　　　　　　4

　　　　　　　/     \

　　            2        6

                /   \    /   \

               1    5  3    7

n1=5, n2=4.    n2=3

第一个逆序。 x比后面大。
第二个逆序。 x比前面小。

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