class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        lenA = len(A)
        if lenA == 0 : return  0
        slow = 0
        count = 1
        for fast in range(1, lenA):
            if A[fast] == A[fast-1]:
                count+=1
                if count <=2:
                    slow +=1
                    A[slow] = A[fast]
            else:
                count = 1
                slow +=1
                A[slow] = A[fast]
        return  slow + 1