'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


'''

class Solution:  #logN * logN
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:    return 0
        h1=h2=0
        node=root
        while node:
            h1+=1
            node=node.left
        node=root
        while node:
            h2+=1
            node=node.right
        if h1==h2:    return 2**h1-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1