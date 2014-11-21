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
    def removeDuplicates(self, A):
        if not A:return 0
        slow = 0
        for fast in range(len(A)):
            if A[slow] == A[fast]:continue
            else:
                slow +=1
                A[slow] = A[fast]
        return slow+1