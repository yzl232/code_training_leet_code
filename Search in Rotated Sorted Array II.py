class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        n = len(A)
        l = 0; r = n-1
        while l<= r:
            m = (l+r)/2
            if A[m] ==target: return True
            elif A[l] < A[m] :
                if A[l]<=target <=A[m]:
                    r = m-1
                else:
                    l = m+1
            elif A[l] > A[m]:
                if A[m] <= target <=  A[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                l +=1 # A[l] == A[m]
        return False