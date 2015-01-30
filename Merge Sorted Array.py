'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, a, m, b, n):  #in place    必须从后往前。   A足够长。  后面是空得。    从前面要用的会被覆盖。
        i = m-1; j = n-1; x=m+n-1
        while i>=0 and j>=0:
            if a[i] > b[j]:
                a[x] = a[i]
                i -=1; x-=1
            else:
                a[x] = b[j]
                j -=1; x-=1
        a[:j+1] = b[:j+1]