class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones =0 ; twos = 0; threes = 0
        for i in range(len(A)):
            twos |= ones&A[i]   #more than 2 times
            ones ^= A[i]   # one r three times
            threes = ones&twos  # three times
            ones &= ~threes  # remove three times.
            twos &= ~threes  # remove three times
        return ones
        
'''
http://wp.javayu.me/2014/01/single-number-ii/

 Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

'''