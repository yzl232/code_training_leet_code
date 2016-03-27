'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13. 
'''
class Solution(object):  # http://blog.csdn.net/xudli/article/details/46798619
    def countDigitOne(self, n):  # http://www.cnblogs.com/grandyang/p/4629032.html
        ret, base = 0, 1    #从个位到十位到百位。  m不断乘以10
        while base <= n:  # 用(x+8)/10来判断一个数是否大于等于2
            a, b = n/base, n%base
            ret += (a + 8) / 10 * base + (a % 10 == 1) * (b + 1)  #判断某一位的一, 整天看,  一个数量位. 结果为x/10数量级
            base *= 10
        return ret
