'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        while n:
            ret += n & 1
            n >>= 1
        return ret