'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    # @return a float
    def findMedianSortedArrays(self, a, b):  # Just see kitt's explanation
        m = len(a); n = len(b)
        if (m + n)  % 2 ==1: return self.getK(a, b, (m + n)/2+1)   # here k from 1. k Can not be 0. The kth num
        else: return 0.5 * (self.getK(a, b, (m + n)/2) + self.getK(a, b, (m + n)/2 + 1)) # k not 0-based

    def getK(self, a, b, k):
        # return kth smallest number of arrays A and B, assume len(A) <= len(B)
        m = len(a) ; n = len(b)
        if m > n: return self.getK(b, a, k)
        if m == 0: return b[k-1]
        if k == 1:return min(a[0], b[0])
        pa = min(k/2, m); pb = k-pa     ##normal case pa =  k /2 .  Special case:  pa = lenA  # the part that can be cut down
        return self.getK(a[pa:], b, k-pa) if a[pa-1] <= b[pb-1] else self.getK(a, b[pb:], k-pb)# 注意不是if A[k/2-1]<=B[k/2-1] 而是

#需要背下的只有最后两行代码而已
#比如k = 6, 分别看A和B中的第3个数, 已知 A1 < A2 < A3 < A4 < A5... 和 B1 < B2 < B3 < B4 < B5..., 如果A3 <＝ B3, 那么第6小的数肯定不会是A3, 因为最多有四个数小于A3。 最多A3第5小