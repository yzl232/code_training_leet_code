'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


'''
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:   return 0
        h1=h2=0;   cur1=cur2=root
        while cur1:
            h1+=1;  cur1=cur1.left
        while cur2:
            h2+=1;  cur2=cur2.right
        return 2**h1-1 if h1==h2 else self.countNodes(root.left)+self.countNodes(root.right)+1  

'''
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:    return 0
        h1, h2 = self.height(root, True), self.height(root, False)
        return 2**h1-1 if h1==h2 else self.countNodes(root.left)+self.countNodes(root.right)+1
    
    def height(self, root, isLeft):
        if not root: return 0
        return 1+self.height(root.left, isLeft) if isLeft else 1+self.height(root.right, isLeft)
'''
