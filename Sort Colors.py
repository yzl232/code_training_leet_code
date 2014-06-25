class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []:return
        l = len(A)
        p1=0; p2 = l -1  # p1 points to first 1, p2 points to the one before first 2.  0 is before p1,  2 is after p2.
        i = 0
        while i <= p2:
            if A[i] == 2:
                A[p2], A[i] = A[i], A[p2]
                p2 -= 1
            elif A[i] == 0:
                A[p1], A[i] = A[i], A[p1]    # A[i] always get 1, since 0 is before p0,  2 is after p2.
                i+=1
                p1+=1
            else:
                i+=1