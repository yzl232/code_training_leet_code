'''
 Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

'''
#1....n的数。 自然有特点。。。可以作为index。 
'''
The main idea is the same with problem Linked List Cycle II,https://leetcode.com/problems/linked-list-cycle-ii/. Use two pointers the fast and the slow. The fast one goes forward two steps each time, while the slow one goes only step each time. They must meet the same item when slow==fast. In fact, they meet in a circle, the duplicate number must be the entry point of the circle when visiting the array from nums[0]. Next we just need to find the entry point. We use a point(we can use the fast one before) to visit form begining with one step each time, do the same job to slow. When fast==slow, they meet at the entry point of the circle. The easy understood code is as follows.
'''
class Solution(object):
    def findDuplicate(self, arr):
        slow, fast, ret = arr[0], arr[arr[0]], 0#从0开始走。 因为一直不会碰到0.
        while slow!=fast:
            slow, fast = arr[slow], arr[arr[fast]]
        while ret!=slow:
            slow, ret = arr[slow], arr[ret]
        return ret


'''
如果允许改变array  。 geeks有一种办法。
class Solution3:  #假定没有负数出现
    def isCon(self, arr):  #利用index, 以及正负标记. 来check是否重复
        small = min(arr)
        if max(arr)-small + 1!=len(arr): return False
        for i in range(len(arr)):
            t = abs(arr[i]) - small
            if arr[t]<0: return False
            else: arr[t] == -arr[t]
        return True

'''