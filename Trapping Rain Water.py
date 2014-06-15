class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(A)
        l = [0 for i in range(n)]
        r = [0 for i in range(n)]
        water = 0
        for i in range(1, n):
            l[i] = max(l[i-1], A[i-1])
        for i in range(n-2, -1, -1):
            r[i] = max(r[i+1], A[i+1])
        for i in range(n):
            if min(l[i], r[i]) - A[i] > 0:
                water +=min(l[i], r[i]) - A[i]
        return  water            
