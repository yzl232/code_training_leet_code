'''
 Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<=2: return len(A)
        slow =1; cnt=1
        for fast in range(1, len(A)):
            if A[fast]==A[fast-1] and cnt>=2:  continue
            if A[fast]!=A[fast-1]: cnt=0
            A[slow]=A[fast]
            cnt+=1; slow+=1
        return slow