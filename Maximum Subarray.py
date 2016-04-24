'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, arr):
        if not arr: raise ValueError
        ret = maxN = float('-inf')
        for x in arr:
            maxN = max(maxN +x, x)
            ret = max(ret, maxN)
        return ret
''' #  the subarray ends with i th element.    
     #We should ignore the sum of the previous n-1 elements if A[i] is greater than the s[i-1]+A[i]
     # space O(n), time O(n) We can optimize the space to be O(1)

def maxSubArray(self, a):
    s = [0 for i in range(len(a))]
    s[0] = a[0]
    for i in range(1, len(a)):
        s[i] = max(s[i-1] + a[i],  a[i])
    return max(s)

naive solution:    O(n3) time and space.  Since every subarray has its own start point and end point.

 array分成2个部分。divide and conquer. 这样子是 O(nlogn) .
 #分治法是二分，不停的二分至不能再分再倒退递归

 '''