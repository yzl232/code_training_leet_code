class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        result = mini = maxn = A[0];
        for i in range(1, len(A)):
            a = min(mini * A[i], maxn * A[i])
            b = max(mini * A[i], maxn * A[i])
            mini = min(A[i], a)
            maxn = max(A[i], b)
            result = max(result, maxn)
        return result
        
'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 
'''