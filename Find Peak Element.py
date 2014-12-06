# encoding=utf-8
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, arr):
        l=0; h = len(arr)-1
        while l<h:  #当l==h的时候，找到了
            m = (l+h)/2
            if arr[m]<arr[m+1]:  l=m+1  #在右边。 l取更大的。 m+1
            else: h=m  #在左边。 h取更小的。 m
        return l