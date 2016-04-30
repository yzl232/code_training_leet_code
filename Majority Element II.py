'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''

class Solution:
    def majorityElement(self, arr):
        if not arr:   return []
        cnt1, cnt2, x1, x2 = 0, 0, None, None
        for x in arr:
            if x == x1:   cnt1 += 1
            elif x == x2:    cnt2 += 1
            elif cnt1 == 0:   x1, cnt1 = x, 1
            elif cnt2 == 0:   x2, cnt2 = x, 1
            else:    cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        return [x for x in (x1, x2) if arr.count(x) > len(arr) / 3]