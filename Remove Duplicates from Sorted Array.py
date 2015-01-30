'''
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, arr):
        if not arr:return 0
        slow = 1
        for fast in range(1, len(arr)):
            if arr[fast-1]==arr[fast]: continue
            arr[slow] = arr[fast]
            slow+=1
        return slow