#Divide two integers without using multiplication, division and mod operator.
class Solution:
    # @return an integer
    def divide(self, a, b):  # obvious we can only use plus/minus operation
        assert b!=0
        sign = 1 if a^b>=0 else -1
        a = abs(a);  b = abs(b)
        ret = 0
        while a >= b:
            k = 1; t = b
            while a >= t+t:
                t += t
                k+=k
            ret += k
            a -= t
        if sign == -1: return 0-ret
        return max(min(ret, 2147483647 ), -2147483648)  #dividend剩下的部分就是mod的值