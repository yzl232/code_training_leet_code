'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

    Consider implement these two helper functions:
        getPredecessor(N), which returns the next smaller node to N.
        getSuccessor(N), which returns the next larger node to N.
    Try to assume that each node has a parent pointer, it makes the problem much easier.
    Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
    You would need two stacks to track the path in finding predecessor and successor node separately.



'''
class Solution(object):
    def closestKValues(self, root, target, k):
        self.ret = [];  self.k = k
        self.dfs(root, target)
        return self.ret

    def dfs(self, root, target):
        if not root: return 
        self.dfs(root.left, target)
        if len(self.ret) == self.k:
            if abs(target-root.val)<abs(target-self.ret[0]): self.ret.pop(0)
            else: return 
        self.ret.append(root.val)
        self.dfs(root.right, target)
#头疼O(logN)的。  有这个O(n)就好了。  #这个pop(0)损耗高， 适合用queue.
#真要碰到了这道题目， 就跳过， 说我做过， 装影帝。。。