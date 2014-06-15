class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:return 0
        slow = 0
        for fast in range(len(A)):
            if A[slow] == A[fast]:continue
            else:
                slow +=1
                A[slow] = A[fast]
        return slow+1