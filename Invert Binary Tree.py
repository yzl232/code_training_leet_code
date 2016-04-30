'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''
class Solution:
    def invertTree(self, root):
        if not root: return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root    

'''
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root: return []
        pre = [root]   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
                n.left, n.right = n.right, n.left
            pre = cur
        return root
'''