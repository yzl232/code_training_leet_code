class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        s = [0 for i in range(len(A))]
        s[0] = A[0]
        for i in range(1, len(A)):
            s[i] = A[i] if s[i-1]<0 else A[i]+s[i-1]
        return max(s)
    #  the subarray ends with i th element.    
     #We should ignore the sum of the previous n-1 elements if A[i] is greater than the s[i-1]+A[i]