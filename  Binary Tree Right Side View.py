'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []    #就是level order traversal 改了一点点.
        pre, ret = [root], []   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for i in range(len(pre)):
                n = pre[i]
                if i == len(pre)-1: ret.append(n.val)   #
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
            pre = cur
        return ret


'''

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = {}
        self.ret = []
        self.dfs(root, 0)
        return self.ret

    def dfs(self, root, level):
        if not root: return
        if level not in self.d:
            self.d[level] = True
            self.ret.append(root.val)
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)
'''