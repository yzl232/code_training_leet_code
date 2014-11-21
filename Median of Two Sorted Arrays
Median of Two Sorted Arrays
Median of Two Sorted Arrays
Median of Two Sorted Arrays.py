'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):  # Just see kitt's explanation
        lenA = len(A); lenB = len(B)
        if (lenA + lenB)  % 2 ==1: return self.getMedian(A, B, (lenA + lenB)/2+1)   # here k from 1. k Can not be 0. The kth num
        else: return 0.5 * (self.getMedian(A, B, (lenA + lenB)/2) + self.getMedian(A, B, (lenA + lenB)/2 + 1)) # k not 0-based
    def getMedian(self, A, B, k):
        # return kth smallest number of arrays A and B, assume len(A) <= len(B)
        lenA = len(A) ; lenB = len(B)
        if lenA > lenB: return self.getMedian(B, A, k)
        if lenA == 0: return B[k-1]
        if k == 1:return min(A[0], B[0])   
        pa = min(k/2, lenA); pb = k-pa     ##normal case pa =  k /2 .  Special case:  pa = lenA  # the part that can be cut down
        return self.getMedian(A[pa:], B, k-pa) if A[pa-1] <= B[pb-1] else self.getMedian(A, B[pb:], k-pb)# 注意不是if A[k/2-1]<=B[k/2-1] 而是 