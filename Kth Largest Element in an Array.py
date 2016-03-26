'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
import random
class Solution(object):
    def findKthLargest(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        assert 1<=k<=len(arr)
        pivot = random.choice(arr)
        s = [i for i in arr if i < pivot]
        m = [i for i in arr if i == pivot]
        b = [i for i in arr if i > pivot]
        if k<=len(b):  return self.findKthLargest(b, k)
        elif k>len(b)+len(m): return self.findKthLargest(s, k-len(b)-len(m))
        else: return pivot