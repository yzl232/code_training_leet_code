# encoding=utf-8
'''

Factorial Trailing Zeroes
Total Accepted: 5915 Total Submissions: 21121

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        ret = 0
        while n>0:
            n/=5
            ret+=n
        return ret