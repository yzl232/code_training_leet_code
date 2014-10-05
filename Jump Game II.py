class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        maxCanReach = 0
        jumpNum = 0
        if n<2: return 0
        while True:
            jumpNum+=1
            for i in range(maxCanReach+1):
                maxCanReach = max(maxCanReach, A[i]+i)
                if maxCanReach>=n-1: return jumpNum