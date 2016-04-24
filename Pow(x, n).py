# Implement pow(x, n).
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n<0: return 1.0/self.pow(x, -n)
        ret = 1.0
        while n:
            if n&1: ret*=x
            x*=x
            n>>=1
        return ret'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def myPow(self, x, n):
        if n == 0: return 1
        elif n==1: return x
        elif n<0:  return 1.0 / self.myPow(x, -n)
        half = self.myPow(x, n / 2)
        return half *half if n%2==0 else half *half*x