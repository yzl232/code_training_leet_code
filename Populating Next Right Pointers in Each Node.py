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
        self.result = []
        self.dfs(root, 1)
        for nodes in self.result:
            l = len(nodes)
            for i in range(l-1):
                nodes[i].next = nodes[i+1]
        
    def dfs(self, root, level):
        if not root: return
        if len(self.result)< level: self.result.append([])
        self.result[level-1].append(root)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
        
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