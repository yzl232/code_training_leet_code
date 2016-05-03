'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless. 

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        self.ret = []  #就是preorder加上特殊符号(none node)而已
        self.dfs(root)
        return " ".join(self.ret)#要加上空格来join

    def dfs(self, root):
        if not root:
            self.ret.append('#')
            return
        self.ret.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)

    def deserialize(self, data):
        self.vals = iter(data.split())
        return self.helper()

    def helper(self):
        x = next(self.vals, None)   # if not x: return 
        if x=="#": return
        root = TreeNode(x)
        root.left, root.right = self.helper(), self.helper()
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

'''

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.index = 0; self.arr = data.split()
        return self.helper()

    def helper(self):
        if self.index>=len(self.arr): return
        rootVal = self.arr[self.index]
        self.index+=1
        if rootVal == '#':    return
        root = TreeNode(rootVal)  #尝试从pre-order+符号来 还原
        root.left = self.helper()
        root.right = self.helper()
        return root

'''