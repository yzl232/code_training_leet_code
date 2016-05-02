'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

    The array is only modifiable by the update function.
    You may assume the number of calls to update and sumRange function is distributed evenly.

'''

#https://www.hrwhisper.me/binary-indexed-tree-fenwick-tree/
class NumArray(object):
    def __init__(self, arr):
        self.bits, self.arr = [0] * (len(arr) + 1), [0] * len(arr)
        for i in xrange(len(arr)):  self.update(i, arr[i])

    def getSum(self, i):   #记忆: 求和的时候, i最大的. 变小, 所以是 减法
        ret = 0;  i+=1
        while i > 0:    #从底下一直加到root
            ret += self.bits[i];  i -= (i & ~(i - 1)) # i&=i-1  # #    (i & -i)  结论:  i&(i-1) 和i - i & (-i)功能相同
        return ret

    def update(self, x, val):    #从root一直往下加, 加到底.
        diff, self.arr[x], i = val - self.arr[x], val, x + 1     #有先后关系.
        while i < len(self.bits):
            self.bits[i] += diff;   i += (i & ~(i - 1)) # (i&-i)

    def sumRange(self, i, j):
        return self.getSum(j) - self.getSum(i-1)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)