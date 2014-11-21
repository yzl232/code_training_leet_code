# encoding=utf-8
'''
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer   #2345671      7123456
    def findMin(self, num):
        result = num[0]
        l, h = 0, len(num)-1
        while l<=h:
            m = (l+h)/2
            result = min(result, num[m])
            if num[m]<num[h]: h = m-1
            elif num[m] == num[h]: h-=1
            else: l=m+1
        return result