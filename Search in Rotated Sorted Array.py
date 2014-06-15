class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        l = 0; r = n-1
        while l<=r:
            m = (l+r)/2
            if A[m] == target: return m
            elif A[m] >= A[l]:
                if A[l] <=target <= A[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if A[m] <= target <= A[r]:
                    l = m+1
                else:
                    r = m-1
        return -1