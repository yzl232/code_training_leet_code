'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13. 
'''
class Solution(object):  # http://blog.csdn.net/xudli/article/details/46798619
    def countDigitOne(self, n):  # http://www.cnblogs.com/grandyang/p/4629032.html
        ret, base = 0, 1
        while base<=n:
            a, b = a/base, a%base
            ret += (a+8)/10*base + (a%10==1)*(b+1)
            base *=10
        return ret
'''

xxx0xx
xxx1xx
xxx2xx
digit >=2:    (a/10 + 1) * base
digit ==1:    a/10*base + (b+1)         #这里b+1<base
digit ==0:   a/10*base


xxx0
xxx1
xxx2
base = 1

'''
