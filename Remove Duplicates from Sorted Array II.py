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
        if len(A) == 0: return 0
        slow = 0; count = 1
        for fast in range(1, len(A)):
            if A[fast] == A[fast-1]:
                if count >=2: continue
                else: 
                    count+=1
                    slow+=1
                    A[slow] = A[fast]
            else:
                count = 1
                slow +=1
                A[slow] = A[fast]
        return slow+1