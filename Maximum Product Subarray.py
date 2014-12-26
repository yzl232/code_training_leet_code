'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        ret = maxN = minN = A[0]
        for i in range(1, len(A)):
            t = (A[i], maxN*A[i], minN*A[i])
            maxN, minN = max(t), min(t)
            ret = max(ret, maxN)
        return ret