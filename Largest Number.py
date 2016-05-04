'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
'''
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):   #  sort(cmp, reverse, key)
        num = [str(x) for x in num]
        num.sort(cmp = lambda x, y: cmp(y+x, x+y))   #大的在前面, 所以就是(y+x, x+y)
        return ''.join(num).lstrip('0') or '0'
# merge interval用到了key= lambda x: x.start.  
#这是cmp = lambda x,y : cmp(y+x, x+y)

# 与https://leetcode.com/problems/create-maximum-number/区别。  这个是一个array。 那个是2个array。 那个的array都是digits.这边不一定。