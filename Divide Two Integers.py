#Divide two integers without using multiplication, division and mod operator.
class Solution:
    # @return an integer
    def divide(self, a, b):  # obvious we can only use plus/minus operation
        sign = 1 if a^b>=0 else -1
        a = abs(a);  b = abs(b)
        ret = 0
        while a >= b:
            k = 1; tmp = b
            while a >= tmp+tmp:
                tmp += tmp
                k+=k
            ret += k
            a -= tmp
        if sign == -1: return 0-ret
        return ret   #dividend剩下的部分就是mod的值