class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        lenA = len(A); maxCanReach = 0; jumpNum = 0
        if lenA <= 1:return 0
        while True:
            jumpNum +=1
            for i in range(maxCanReach +1):
                maxCanReach = max(maxCanReach, i+A[i])
                if maxCanReach >= lenA -1:return jumpNum