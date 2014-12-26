'''
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(arr); ret = 0
        l = [0 for i in range(n)];  r =l[:]
        for i in range(1, n-1):    l[i] = max(l[i-1], arr[i-1])
        for i in range(n-2, 0, -1):    r[i] = max(r[i+1], arr[i+1])
        for i in range(1, n-1):  ret += max(  min(l[i], r[i])-arr[i],   0)
        return ret
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(A)  #最左边最右边没有值。 舍去0， n-1
        l = [0 for i in range(n)]
        r = [0 for i in range(n)]
        water = 0
        for i in range(1, n-1):
            l[i] = max(l[i-1], A[i-1])  if A[i-1] != 0 else 0
        for i in range(n-2, 0, -1):
            r[i] = max(r[i+1], A[i+1]) if A[i+1] !=0 else 0
        for i in range(1, n-1):
            water +=max(0,  min(l[i], r[i]) - A[i])
        return  water
'''