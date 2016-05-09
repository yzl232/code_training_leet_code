'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, arr, target):
        l = 0; h = len(arr) - 1
        while l<=h:
            m = (l+h)/2
            if arr[m] == target: return m
            if arr[m] < target: l=m+1
            else: h=m-1
        return l
#较大的l