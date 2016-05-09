'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, arr):
        if len(arr) <= 1: return 0   # 例子 1  4  6.   buckets 1~ 3    4~6
        a = min(arr);  b = max(arr);  w = max(1, int(math.ceil((b-a)/(len(arr)-1.0)))) #ceil( (B - A) / (N - 1) )
        n = ((b - a) / w + 1);    bkt = [None] * n   #桶的数目n= 间隔+1
        for x in arr:
            i = (x - a) / w
            bkt[i] =  (x, x) if not bkt[i] else (min(bkt[i][0], x), max(bkt[i][1], x))
        bkt = [x for x in bkt if x] #极端情况， arr全为1.  bkt长度为[(1, 1)]
        return max([bkt[i][0]-bkt[i-1][1] for i in range(1, len(bkt))] or [0])
# #bucket sort特点。  array里面元素的difference