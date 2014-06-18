class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        lenA = len(A)
        canReach = 0
        for i in range(lenA):
            if i<= canReach:  # i can be reached
                canReach = max(canReach, A[i]+i)
                if canReach >= lenA-1:return True
            else: break
        return False
        