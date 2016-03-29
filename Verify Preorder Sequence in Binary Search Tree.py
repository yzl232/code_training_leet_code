'''

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
'''
#  pre order 是先降序再升序的.
class Solution: # https://segmentfault.com/a/1190000003874375
    def verifyPreorder(self, preorder):  # keep pushing till you hit the leftmost leaf
        stack = []
        lower = float('-inf')
        for x in preorder:
            if x < lower:    return False
            while stack and x > stack[-1]:    lower = stack.pop()
            stack.append(x)       # 有点理解了. 每次append的都是当前最小的.  lower则是第二小的
        return True

class Solution2:
    def verifyPreorder(self, preorder):
        # stack = preorder[:i], reuse preorder as stack
        lower = float('-inf')
        i = 0
        for x in preorder:
            if x < lower:    return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True
'''
To solve above problem, you do not need to construct a Binary Tree from a given pre-order sequence.

The pre-order sequence of binary tree can form a sorted stack. So lets break it in a few “SIMPLE” steps as follows:

Iterate over each element and follow the steps below:

1. Push to stack till you get higher element than the topmost element of the stack. [i.e. you keep pushing till you hit the leftmost leaf]
2. If you find current value which is greater than the TOP of Stack, POP till you hit higher element, and also mark the last poped value, which is your variable (Left_Tree_Highest). This variable is used to check whether the order is correct or not.
3. In all the steps, if you find current element lesser than Left_Tree_Highest, then your tree is not a Binary Search Tree and it should return “NO”.

4. If all the element traversed, and you have not hit “NO”, means given sequence follows the Binary Search Tree rule.

Above step might be confusing, but take a pen and paper, try to follow the steps by taking stacks and Left_Tree_Highest values at each step. Once you are able to track it, you will able to co-relate it with the steps given above.

So the basic idea is that at any point, left subtree’s highest element should be lowest for the untraversed elements [Right Tree].




Kinda simulate the traversal, keeping a stack of nodes (just their values) of which we're still in the left subtree. If the next number is smaller than the last stack value, then we're still in the left subtree of all stack nodes, so just push the new one onto the stack. But before that, pop all smaller ancestor values, as we must now be in their right subtrees (or even further, in the right subtree of an ancestor). Also, use the popped values as a lower bound, since being in their right subtree means we must never come across a smaller number anymore.
'''
