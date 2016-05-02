'''
 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''

class Solution(object):
    def singleNumber(self, arr):
        s = 0; x=y=0
        for i in arr:    s ^=i
        right1Bit  = s&(~(s-1))   # s&(-s)
        for i in arr:
            if right1Bit&i:   x^=i
            else: y^=i
        return [x, y]
# -x = ~x+1      x-1 = -(~x)    ~(x-1) = -x