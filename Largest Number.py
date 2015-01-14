# encoding=utf-8
class Solution:
# @param num, a list of integers
# @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        ret = ''.join(num)
        return ret.lstrip('0') or '0'