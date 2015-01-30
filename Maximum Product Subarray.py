'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, arr):
        if not arr: raise ValueError
        ret = maxN = minN = arr[0]
        for i in range(1, len(arr)):
            t = (arr[i], maxN*arr[i], minN*arr[i])
            maxN, minN = max(t), min(t)
            ret = max(ret, maxN)
        return ret