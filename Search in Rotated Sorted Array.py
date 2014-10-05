class Solution:
    # @param A, a list of integers   #7123456          2345671
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        l = 0; h = len(A) - 1
        while l<=h:
            m = (l+h)/2
            if A[m] == target: return m
            elif A[m]< A[l]:
                if A[m]<=target<=A[h]:
                    l = m + 1
                else:
                    h = m - 1
            elif A[m] > A[l]:
                if A[l] <= target <=A[m]:
                    h = m-1
                else:
                    l = m+1
            else: l+=1
        return -1