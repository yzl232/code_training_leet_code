'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution:
    # @param A, a list of integers    #7123456     2345671
    # @param target, an integer to be searched
    # @return an boolean
    def search(self, A, target):
        l , h = 0, len(A)-1
        while l<=h:
            m = (l+h)/2
            if A[m] == target: return  m
            elif A[m]>A[l]:
                if A[l]<=target<=A[m]:  h = m-1
                else: l = m+1
            elif A[m]<A[l]:
                if A[m]<=target<=A[h]:   l = m+1
                else:   h = m-1
            else:    l+=1
        return -1   #因为l和m相等，但是m又不是target。这时候，最左边的l没有用了。直接舍掉。l+1