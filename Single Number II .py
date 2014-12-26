'''
http://wp.javayu.me/2014/01/single-number-ii/

 Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, arr):
        ones =  twos = threes = 0
        for x in arr:
            twos |= ones&x        #more than 2 times.   没错。记录了超过了2次的bit 1
            ones ^= x       # one r three times  奇数次数的bit位数
            threes = ones&twos  # three times
            ones &= ~threes
            twos &= ~threes  # remove three times
        return ones