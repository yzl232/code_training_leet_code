# encoding=utf-8

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''

class Solution:
    def helper(self, n):
        nums = list('018') if n%2 else ['']  #如果n为偶数,  [empty string]
        for i in xrange(n/2):    #  i  次数. 每次+2.  有n/2次. 最后一次不能是00.
            nums = [a + x + b for a, b in '00 11 88 69 96'.split()[i==n/2-1:] for x in nums]
        return nums

    def strobogrammaticInRange(self, low, high):
        return sum(1 for i in xrange(len(low), len(high)+1) for x in self.helper(i) if not ((len(x) == len(low) and x<low) or (len(x)==len(high) and x>high)) )  
#list comprehension 和正常的顺序是一样的。