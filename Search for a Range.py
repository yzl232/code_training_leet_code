'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1
        result = [-1, -1]    #在二分查找到元素时，需要向前和向后遍历来找到target元素的起点和终点。
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                result[0] = mid
                result[1] = mid
                i = mid - 1
                while i >= 0 and A[i] == target:
                    result[0] = i
                    i -= 1
                i = mid + 1
                while i < len(A) and A[i] == target:
                    result[1] = i
                    i += 1
                return result
        return result