'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13. 
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum((n/base+8)/10*base + (n/base%10==1)*(n%base+1) for base in (10**i for i in range(len(str(n))+1)))

'''
151222        15*1000+223       n%base+1
152222        16*1000
150222        15*1000
                n/base/10
千位

def countDigitOne(self, n):
    ones = 0
    m = r = 1
    while n > 0:
        ones += (n + 8) / 10 * m + (n % 10 == 1) * r
        r += n % 10 * m
        m *= 10
        n /= 10
    return ones

class Solution(object):  # http://blog.csdn.net/xudli/article/details/46798619
    def countDigitOne(self, n):  # http://www.cnblogs.com/grandyang/p/4629032.html
        ret, base = 0, 1    #从个位到十位到百位。  m不断乘以10
        while base <= n:  # 用(x+8)/10来判断一个数是否大于等于2
            a, b = n/base, n%base
            ret += (a + 8) / 10 * base + (a % 10 == 1) * (b + 1)  #判断某一位的一, 整天看,  一个数量位. 结果为x/10数量级
            base *= 10
        return ret

digit >=2:    (a/10 + 1) * base
digit ==1:    a/10*base + (b+1)
digit ==0:   a/10*base

以算百位上1为例子:   假设百位上是0, 1, 和 >=2 三种情况:

    case 1: n=3141092, a= 31410, b=92. 计算百位上1的个数应该为 3141 *100 次.

    case 2: n=3141192, a= 31411, b=92. 计算百位上1的个数应该为 3141 *100 + (92+1) 次.

    case 3: n=3141592, a= 31415, b=92. 计算百位上1的个数应该为 (3141+1) *100 次.

以上三种情况可以用 一个公式概括:

(a + 8) / 10 * m + (a % 10 == 1) * (b + 1);

'''
