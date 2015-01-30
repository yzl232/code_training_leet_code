#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#这里是按照list的顺序来 inorder,   left =dfs,  然后root.left = left , root.right = dfs 然后self.head = self.head.next 之前array是preorder或者inorder都可以。  list只能从左到右， 所以必须inorder. array 任意access。所以无所谓
class Solution:
    def sortedListToBST(self, head):
        cur, n = head, 0
        while cur:
            cur = cur.next
            n+=1
        self.head = head
        return self.dfs(0, n - 1)

    def dfs(self, start, end):
        if start > end:    return
        mid = (start + end) / 2
        left = self.dfs(start, mid - 1)   #因为是inorder    root压根还没建立起来。。
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.dfs(mid + 1, end)
        return root




'''
转换成array的方法比较简单。 要一些空间

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.createBST(array, 0, len(array) - 1)

    def createBST(self, num, start, end):
        if start > end:return None
        mid = (start + end)/2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid-1)
        root.right = self.createBST(num, mid+1, end)
        return root
'''