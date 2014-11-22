class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(A)  #最左边最右边没有值。 舍去0， n-1
        l = [0 for i in range(n)]
        r = [0 for i in range(n)]
        water = 0
        for i in range(1, n-1):
            l[i] = max(l[i-1], A[i-1]) 
        for i in range(n-2, 0, -1):
            r[i] = max(r[i+1], A[i+1])
        for i in range(1, n-1):
            water +=max(0,  min(l[i], r[i]) - A[i])
        return  water

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