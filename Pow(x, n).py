class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0: return 1
        elif n==1: return x
        elif n > 1:
            half = self.pow(x, n/2)
            if n%2==0: return half * half
            elif n%2 == 1: return half * half * x
        else:
            return 1.0 / self.pow(x, -n)