
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        pre, d = [(root, 0)], {}   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for x, col in pre:
                if col not in d: d[col] = []
                d[col].append(x.val)
                if x.left:  cur.append((x.left, col-1))
                if x.right:  cur.append((x.right, col+1))
            pre = cur
        return [d[k] for k in sorted(d)]

#做过。。

# encoding=utf-8
'''
We have a binary tree, suppose like this:

       8
     /   \
    6     10
   / \   /  \
  4   7 9    12
 / \    \
3   5     11

如果10在11前面， 就是适合用BFS。   用DFS药加上row变量
如果11在10前面。 就是适合用DFS。    root, left, right
本题下面的DFS错误。

'''
#可以看出，注意8, 7, 9的顺序，  是inorder, root,   left, ，  right
class Solution:
    def findVertical(self, root):
        self.d = {}  #用hashtable是因为不知道最左边index有多左。
        self.dfs(root, 0)
        return [self.d[key] for key in sorted(self.d)]

    def dfs(self, root, col):
        if not root: return
        if col not in self.d:  self.d[col] = [] ##可以看出，注意8, 7, 9的顺序，  是inorder, root,   left, ，  right
        self.d[col].append(root.val)
        self.dfs(root.left, col - 1)
        self.dfs(root.right, col + 1)

#也可以BFS
'''



'''





'''
geeks的做法时间复杂度比较高。
我这个耗费空间。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(8)
t2 = TreeNode(6)
t3 = TreeNode(10)
t4 = TreeNode(7)
t5 = TreeNode(9)
t6 = TreeNode(6)
t1.left = t2
t1.right = t3
t2.right = t4
t3.left = t5

s = Solution()
print s.findVertical(t1)