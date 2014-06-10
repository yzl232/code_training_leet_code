class Solution:
    # @return a string
    def getPermutation(self, n, k):
        total = self.factorial(n)
        if k> total: return
        digits = range(1, n+1)
        k -= 1  # quite necessary
        seq = ''
        while n>0:
            total = total/n
            i, k = divmod(k, total)
            seq += chr(digits[i]+ord('0'))
            digits.pop(i)
            n-=1
        return seq

    def factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result*=i
        return result